# The edit

## With edit_video

- `assemble`: the clips in order (each trimmed past its first 0.3 s), the voice as the audio track, the subtitles
  burned in, loudness -14 LUFS. Check the tool's schema for the exact fields: per-clip trims, a contrast fix, where the
  subtitles sit.
- `reframe`: a 16:9 or 1:1 clip to 9:16 (or back), keeping the subject in frame.

The result comes back as a link. Send that link to the person, not the file.

## Rules for any editor

| Rule | Why |
|---|---|
| One text layer at a time | A caption under a card under a stamp is read as none of them. Subtitles hide while a card or stamp is up |
| Stamps and cards never cover a face | The face is the story; put stamps in the top fifth or above the bottom fifth |
| Freeze frames only on open eyes | A frozen blink looks like a glitch. Pick the freeze moment by eye, not by timecode |
| Trim the first 0.3 s of every clip | Seedance can fade in from white |
| Bring the blacks down | Seedance can lift them to grey; the cut must match the approved frames |
| Show the maths | "$49 ÷ 4 videos =" on a strip, then the "$12 A VIDEO" stamp a beat later |
| Count what the line counts | 1-2-3-4 popping next to the four reels as the voice says "four" |
| The old price struck through on the end card | The viewer sees the comparison without reading a sentence |
| -14 LUFS | The loudness Reels, TikTok and Shorts play at; quieter cuts sound weak next to others |

## Name cards and stamps

What worked in the 36-second ad, as a style ("crime file"):
- **Name card** on a freeze frame: a flash, a small "EXHIBIT A" label, the role in big white letters with a black
  outline ("THE CREATOR"), one line under it on a paper strip ("Makes AI videos."). 2.2 s.
- **Stamp:** the price in heavy letters in a rotated box with a short camera shake as it lands; red for theirs, yellow
  for ours. 1.5–3 s.
- **End card:** the logo, "$12 A VIDEO" struck through, our price per video stamped (from `estimate_cost` on the day,
  never from an old cut), the address as a big button, the promo note in readable text when `list_models` shows a
  `promo_until`, the plan maths in one small line.

## ffmpeg recipes (when no editor is at hand)

```bash
# Trim the white fade-in, bring the contrast back, make every piece 1080x1920 at 30 fps (concat needs them alike)
ffmpeg -ss 0.3 -i c1.mp4 -t 3.7 -vf "eq=contrast=1.15:saturation=1.1,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p" -an -c:v libx264 -crf 18 c1_fix.mp4

# Freeze a frame for 2.2 s (pick a moment with open eyes)
ffmpeg -ss 0.4 -i c2.mp4 -frames:v 1 freeze.png
ffmpeg -loop 1 -i freeze.png -t 2.2 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p" -c:v libx264 -crf 18 freeze.mp4

# Join the pieces (same size and frame rate), add the voice at 0.5 s, burn subtitles, -14 LUFS
ffmpeg -f concat -safe 0 -i list.txt -i voice.wav \
  -filter_complex "[1:a]adelay=500|500,loudnorm=I=-14:TP=-1.5:LRA=11[a];[0:v]subtitles=captions.srt:force_style='Fontsize=18,Outline=2,MarginV=120'[v]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest ad.mp4

# Check the loudness
ffmpeg -i ad.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null - 2>&1 | grep "Input Integrated"
```

`list.txt` lists the pieces in order (`file 'c1_fix.mp4'`). Clips with their own sound effects: mix them under the
voice instead of `-an`.

## Remotion (for cards, stamps and word-timed captions)

A composition at 1080×1920, 30 fps: each clip in a `<Sequence>` from its start, `startFrom` 0.3 s in; a CSS filter for
contrast; captions built from the word timestamps, grouped into sentences, hidden during the card and stamp windows;
the voice as `<Audio>` from 0.5 s. Render, then normalise to -14 LUFS with the ffmpeg line above.
