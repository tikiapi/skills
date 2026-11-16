---
name: tikiapi-launch-video
description: >-
  Turn a project folder or a website into a short, shareable launch video (15–25 s) with a hook, the real product in
  use, music and share copy: pure motion graphics built on this machine at no cost, or upgraded with TikiAPI
  generation (Seedance clips or Nano Banana frames for a few shots, a Suno music bed, an ElevenLabs sound effect, a
  voice-over line, edit_video assembly), each priced with estimate_cost before anything is spent. Use whenever someone
  says "make a launch video", "brag about this", "a promo for my app, site or repo", "a Product Hunt video", "a demo
  reel", "show off what I built", or wants a video of a website or a project.
license: MIT
---

# TikiAPI: launch video

> Adapted from brag-slim by Shunit Haviv Hakimi (https://github.com/latent-spaces/brag), MIT License,
> Copyright (c) 2026 Shunit Haviv Hakimi. Rewritten for TikiAPI and extended with its generation tools; see NOTICE.

You built it; now show it off in about twenty seconds that a stranger understands on first watch. It should feel like
a modern, polished launch video whatever the tone: nothing on screen or in the sound that doesn't earn its place.

## Two paths

| Path | What is made | Cost |
|---|---|---|
| **Motion** (default) | Everything built and rendered on this machine: the product's real UI, type and motion; music and effects synthesised in code, or a track the person owns | Nothing on TikiAPI |
| **Generated** | The same motion video plus a few generated pieces where they add value: a Seedance clip or a Nano Banana frame for the hook or the product's world, a music bed, a signature sound effect, a voice line, joined locally or with `edit_video` | Each piece priced with `estimate_cost`, the total shown before anything is spent |

Options, as flags or plain words: tone (inferred, else `default`); format `landscape` 1920×1080 (default), `vertical`
1080×1920 or `square` 1080×1080, at 30 fps; duration about 20 s; path `motion` or `generated`. Write the results to
`launch-video/` (a timestamped folder if it exists) and every intermediate file to `launch-video/work/`.

## 1. Inspect

Decide what the input is: a **project** (no input, and the current folder is a project) or a **website** (a URL or a
bare domain). Anything else: ask what to make the video about. Then gather the material: the product in use (entry →
key action → result), its exact colours and fonts, its own copy. What to read, what never to read (secrets, keys,
personal data), and how to capture a website: [build-and-deliver](references/build-and-deliver.md).

Before planning, answer: what it is in one sentence; who it is for and what it does for them; what sets it apart; the
most impressive or funniest true claim; the visual hook; the real UI or flow to show; the tone; the one-line share
caption.

## 2. Plan

Write `launch-plan.md`: the angle, the hook, two or three highlights, the punchline, the tone, the visual identity,
and a scene-by-scene storyboard whose durations add up to the target, with the music's tempo chosen now and every cut
on a beat. If the person points at one part (a new version, one feature), the video is about that.

**Shape:** hook (2–3 s) → reveal (2–4 s) → two or three sharp highlights → punchline and outro (2–4 s). A starting
shape, not a template. The creative laws, the tones and the sound: [creative-laws](references/creative-laws.md).

On the generated path, the plan also lists every paid piece: what it is for, the model, its fields. Show the plan and
wait for a yes; planning costs nothing.

## 3. Price, then stop (generated path)

1. Read `list_models` for the current models, limits and prices; never use remembered ones.
2. `estimate_cost` for each order: frames, clips, the music, the effect.
3. Speech isn't an order: its price is the characters read (the voice direction too) times the speech model's price
   per million characters in `list_models`.
4. `edit_video`, if used: its price per second of output is in the tool's description.
5. One line with the total, then wait for the go. Nothing generated before it.

## 4. Generate (generated path)

One paid piece at a time, each checked before the next; the music first, because its beat sets the cut. The real
product UI is never generated: a model invents buttons and features. Generated shots carry the world around the
product, the problem it solves, a metaphor, or the hook. How to order each piece and mix them:
[generated-assets](references/generated-assets.md).

## 5. Build, check, render

Build with the tools already on the machine; ask before installing anything. Check stills from every scene and from
mid-transition before the full render, then check the rendered file itself. The rules:
[build-and-deliver](references/build-and-deliver.md).

## 6. Deliver

- `poster.jpg`: the strongest settled frame, also baked in as frame 0 of `launch.mp4`.
- `share-copy.txt`: one to three sentences, postable as is, specific, in the video's tone. No "excited to share".
- Tell the person where both are, the creative angle in one sentence, and what was spent (the sum of `charged`, or
  nothing on the motion path). Offer to redo one scene or try another tone.
