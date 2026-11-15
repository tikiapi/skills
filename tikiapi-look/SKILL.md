---
name: tikiapi-look
description: >-
  Match the colour look of a reference (a film still, a director's style, a moodboard) in TikiAPI pictures and Seedance
  clips: measure the look in CIELAB numbers, turn the numbers into prompt words, build a colour board without faces, give
  every image a role in the prompt, and check the result against the numbers. Use when someone wants a shot "in the
  style of" a film or director, a cinematic grade, a consistent look across an ad, or says a generated look is wrong.
license: MIT
---

# TikiAPI: match a look

A look is a world, not a filter. A warm grade on a daylight kitchen is not a crime film: the film's look comes from
its sets, its materials and its light sources, and only then from its colour. So build the world in the frame, and
use the reference for colour only.

## 1. Measure the look's DNA

Run `scripts/look_dna.py` (Python with numpy and Pillow):

```bash
python scripts/look_dna.py measure reference.jpg [our_frame.jpg]
```

It reports, in CIELAB: median lightness, the share of highlights (L ≥ 60), the black point (L at the 1st percentile)
and peak white (99th), and for shadows (L < 20), mids and highlights the hue angle and chroma, plus prompt words. With
our frame as well, it lists what must change. Without code, estimate the same by eye. What the numbers mean and how
they become words: [look-dna](references/look-dna.md).

Then add the world: the set, the materials, the light sources ("emerald walls, brass lamps, burgundy leather, small
pools of tungsten light, hard and from the side"). The numbers say what colour; the world says why.

## 2. Colour board

Crop the reference where there are no faces and no readable text (lamps, fabric, walls, floor) and tile the crops:

```bash
python scripts/look_dna.py board board.jpg reference.jpg:0.05,0.6,0.3,0.3 reference.jpg:0.6,0.1,0.3,0.3 …
```

Upload it (`upload_media` or `POST /v1/uploads`). Never send a still with real actors' faces to a model: it may be
refused, and it isn't ours to use.

## 3. The prompt: a role for every image

```text
Image 1 is the shot: same people, set and composition. Image 2 is a colour reference only: use only its colour grade,
contrast and light; do not use the objects, people or layout in it.
[The one action]. Camera: [one move]. [The look words from step 1, last.]
```

## 4. Pick the route

An order takes either one opening frame or references, not both:
- **first_frame** (`image_mode` `first_frame`, one image): the clip opens exactly on our frame, so the look must already
  be in it. Remake the frame first with `nano-banana-pro`: our frame and the colour board as the 2 references, the look
  words at the end.
- **reference** (default, several images): our frame and the board as references; the model rebuilds the shot rather
  than opening on it. Composition can shift.

Say which one you chose and why.

## 5. Test, then check

`estimate_cost`, then one 4-second clip (`duration` 4). Take its first and middle frames and measure them:

```bash
ffmpeg -ss 0.1 -i clip.mp4 -frames:v 1 first.png
ffmpeg -ss 2 -i clip.mp4 -frames:v 1 middle.png
python scripts/look_dna.py measure reference.jpg middle.png
```

Seedance can lift the black point to grey and fade in from white in the first 0.3 s. Fix both in the edit (contrast,
trim), not with a paid redo. Show the clip with the look numbers next to it.
