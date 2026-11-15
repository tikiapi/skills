# Seedance clips

> Adapted from "Seedance 2.5 Skill" by AtlasCloudAI (SKILL.md, references/multi-reference.md,
> references/troubleshooting.md), https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills, licensed under
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Shortened, rewritten for TikiAPI's tools and merged with
> our own production notes. This file stays under CC BY 4.0; see NOTICE.

## Choose the route first

| Need | Route | TikiAPI order |
|---|---|---|
| A beat that must open on an approved frame | First frame | `image_mode` `first_frame`, one image |
| A shot with an exact start and end | First and last frame | `image_mode` `first_last_frame`, two images |
| A clip built from people, product and set pictures | References | `image_mode` `reference` (default), one line binding each image |
| A short multi-shot sequence from one storyboard image | Storyboard reference | The whole board as one reference; "Shot 1, Shot 2…" in order |
| One simple scene | Text only | No images |

For an ad cut to a narrator, **first frame, 4 seconds a clip** is the route that worked: each beat is approved as a
still, the clip can't drift from it, and a 4-second clip is cheap to redo. A clip opening on a frame doesn't inherit
the previous clip's tail; cuts between beats are hard cuts made in the edit.

## Write the prompt

Sort instructions by what they govern, or they stop applying:

| Scope | Holds | Where |
|---|---|---|
| Global | The style, the premise, the camera principle | Once, at the top or bottom |
| Locks | Identity, reference roles, sound, no text | Stated once, the costliest restated at the very end |
| Time | One beat's action and its end state | In the beat |

The blocks, using only those that matter:

```text
[one observable action] + [where things are] + [one camera move] + [sound effects in <angle brackets>]
+ [end state, if the clip must land somewhere] + [the lock]
```

- **One action, one camera move.** Competing moves cause wobble and morphing.
- **End states are visible:** "the reel stops next to the other three", not "she feels relieved".
- **Bind every reference** with what it controls and what not to use: "Image 2 is a colour reference only: use only
  its colour grade; do not use the objects, people or layout in it."
- **The lock** for a first-frame clip under a narrator:

```text
Start exactly from image 1 and keep everything in it unchanged: faces, hair, clothes, the set and the light. No speech,
no dialogue, no voices, no music: only the sound effects described. No subtitles, no captions, no new text.
Photoreal, cinematic.
```

"No speech" matters: without it Seedance may add speech or music of its own, which fights the narrator.

## Example clips (4 s each)

```text
The hand pushes the wad of dollar bills deeper into the monster's mouth; the mouth snaps shut on it, the cheeks bulge,
one loose bill flutters down. Camera: a quick snap push-in. <a wet chomp> <a cash register 'ka-ching'> LOCK

Overhead, nothing moves on the table except a faint drift of dust in the lamp light; the camera slowly pushes down
towards the four reels. <a quiet projector whirr> LOCK
```

## Ordering and waiting

1. `estimate_cost` for every clip before the first; the person's go for the total.
2. One clip at a time. Record the order id as soon as it exists.
3. `queued` and `running` are active: check the same id every 10–15 s. A slow answer, a dropped connection or a
   timeout in your tool is **not** a failure. Never order it again; "continue" means resume the same id.
4. `succeeded`: download or keep the link, look at it, then the next clip.
5. `failed`: nothing was charged. `input_refused` (a face judged too real): retry once with `run_again`; refused again,
   remake the frame. Any other failure: report it and ask before a new order.

## Review a clip, in this order

Identity → the lock (no speech, no text) → the end state → composition → motion → sound. Stop at the first failure:
later polish can't save a wrong face.

## Known Seedance habits

| Habit | Fix |
|---|---|
| Fades in from white over the first ~0.3 s | Trim 0.3 s in the edit |
| Lifts the blacks to grey | Contrast up in the edit (for example `contrast(1.5) saturate(1.15)` in CSS, or an ffmpeg `eq`) |
| Adds speech or music | "No speech, no dialogue, no voices, no music" in the lock |
| Writes captions into the picture | "No subtitles, no captions, no new text" |
| Refuses a realistic face (`input_refused`) | Retry once; then a more stylised frame |
| Duplicates a person from a character sheet | One person per reference image, and the count stated |
| Props move between people | "belongs only to …" |
| Face warps in a close-up turn | Wider framing, gentler move, or a cut |
