"""look_dna.py: measure a colour look in numbers, and make a colour board from crops. Needs numpy and Pillow.

  python look_dna.py measure REFERENCE.jpg [OURS.jpg]
      The look's DNA in CIELAB: median lightness, the share of highlights, the black point and peak white, and the hue
      and chroma of the shadows, mids and highlights, with words a video model follows. With a second image, also what
      must change in it to match the first.

  python look_dna.py board OUT.jpg IMAGE:x,y,w,h [IMAGE:x,y,w,h ...]
      Tiles crops (x, y, width, height as fractions of the image, 0-1) into one board. Pick crops with no faces and no
      readable text: lamps, fabric, walls, floor. The model then takes colour, not content.

To measure a clip, take frames first: ffmpeg -ss 0.1 -i clip.mp4 -frames:v 1 first.png (and one from the middle).
"""
import json
import math
import sys

import numpy as np
from PIL import Image


def lab(path, size=512):
    """sRGB (D65) to CIELAB, on a copy scaled down to `size` on the long side."""
    img = Image.open(path).convert("RGB")
    img.thumbnail((size, size))
    rgb = np.asarray(img, dtype=np.float64) / 255.0
    lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    m = np.array([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]])
    xyz = lin.reshape(-1, 3) @ m.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > (6 / 29) ** 3, np.cbrt(xyz), xyz / (3 * (6 / 29) ** 2) + 4 / 29)
    return np.stack([116 * f[:, 1] - 16, 500 * (f[:, 0] - f[:, 1]), 200 * (f[:, 1] - f[:, 2])], axis=1)


HUES = [(20, "magenta-red"), (45, "red and brick"), (70, "orange and cognac"), (100, "amber and gold"), (135, "olive"),
        (200, "green"), (250, "teal and cyan"), (300, "blue"), (340, "violet"), (361, "magenta-red")]


def hue_words(hue, chroma):
    if chroma < 4:
        return "neutral"
    name = next(n for limit, n in HUES if hue < limit)
    return ("slightly " if chroma < 12 else "rich " if chroma > 25 else "") + name


def zone(px, mask):
    if mask.sum() < 50:
        return None
    a, b = np.median(px[mask, 1]), np.median(px[mask, 2])
    hue = math.degrees(math.atan2(b, a)) % 360
    chroma = math.hypot(a, b)
    return {"share": round(float(mask.mean()), 3), "hue_deg": round(hue), "chroma": round(chroma, 1), "words": hue_words(hue, chroma)}


def measure(path):
    px = lab(path)
    L = px[:, 0]
    p1, p50, p99 = (float(np.percentile(L, q)) for q in (1, 50, 99))
    dna = {
        "image": path,
        "median_L": round(p50, 1),
        "highlights_share": round(float((L >= 60).mean()), 3),
        "black_point_L": round(p1, 1),
        "peak_white_L": round(p99, 1),
        "shadows": zone(px, L < 20),
        "mids": zone(px, (L >= 20) & (L < 60)),
        "highlights": zone(px, L >= 60),
    }
    key = "low-key" if p50 < 35 else "high-key" if p50 > 65 else "mid-key"
    words = [f"{key}, {round(float((L < 35).mean()) * 100)}% of the frame in deep shadow" if key == "low-key" else key]
    words.append("deep, true blacks" if p1 < 4 else "lifted, milky blacks" if p1 > 12 else "soft blacks")
    for name in ("shadows", "mids", "highlights"):
        z = dna[name]
        if z:
            words.append(f"{name} {z['words']}")
    words.append("highlights rolled off, never clipped" if p99 < 92 else "bright, crisp highlights")
    dna["prompt_words"] = "; ".join(words)
    return dna


def compare(ref, ours):
    notes = []
    if ours["black_point_L"] - ref["black_point_L"] > 3:
        notes.append(f"blacks are lifted (L {ours['black_point_L']} vs {ref['black_point_L']}): add contrast, crush the blacks")
    elif ref["black_point_L"] - ours["black_point_L"] > 3:
        notes.append(f"blacks are deeper than the look (L {ours['black_point_L']} vs {ref['black_point_L']}): lift them a little")
    if abs(ours["median_L"] - ref["median_L"]) > 6:
        notes.append(f"overall {'too bright' if ours['median_L'] > ref['median_L'] else 'too dark'} (median L {ours['median_L']} vs {ref['median_L']})")
    if ours["peak_white_L"] - ref["peak_white_L"] > 5:
        notes.append("highlights hotter than the look: roll them off")
    for name in ("shadows", "mids", "highlights"):
        r, o = ref[name], ours[name]
        if r and o:
            gap = (o["hue_deg"] - r["hue_deg"] + 180) % 360 - 180
            if r["chroma"] >= 4 and abs(gap) > 20:
                notes.append(f"{name} hue off by {round(gap)} degrees ({o['words']} vs {r['words']})")
            if abs(o["chroma"] - r["chroma"]) > 6:
                notes.append(f"{name} {'too colourful' if o['chroma'] > r['chroma'] else 'too grey'} (chroma {o['chroma']} vs {r['chroma']})")
    return notes or ["close to the look"]


def board(out, specs, cell=512, cols=3):
    tiles = []
    for spec in specs:
        path, box = spec.rsplit(":", 1)
        x, y, w, h = (float(v) for v in box.split(","))
        img = Image.open(path).convert("RGB")
        W, H = img.size
        crop = img.crop((round(x * W), round(y * H), round((x + w) * W), round((y + h) * H)))
        side = min(crop.size)
        crop = crop.crop(((crop.width - side) // 2, (crop.height - side) // 2, (crop.width + side) // 2, (crop.height + side) // 2))
        tiles.append(crop.resize((cell, cell), Image.LANCZOS))
    rows = math.ceil(len(tiles) / cols)
    sheet = Image.new("RGB", (cell * min(cols, len(tiles)), cell * rows), (0, 0, 0))
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % cols) * cell, (i // cols) * cell))
    sheet.save(out, quality=92)
    return {"board": out, "tiles": len(tiles)}


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "measure":
        ref = measure(sys.argv[2])
        result = {"look": ref}
        if len(sys.argv) > 3:
            ours = measure(sys.argv[3])
            result.update({"ours": ours, "to_change": compare(ref, ours)})
        print(json.dumps(result, indent=1))
    elif len(sys.argv) >= 4 and sys.argv[1] == "board":
        print(json.dumps(board(sys.argv[2], sys.argv[3:])))
    else:
        print(__doc__)
        sys.exit(1)
