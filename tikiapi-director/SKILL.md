---
name: tikiapi-director
description: >-
  Direct a Seedance video like a film director: ask a short brief (references, scene, camera, lines, sound, duration),
  then hand back a reference list, a shot breakdown with timings and a full prompt in fixed blocks (composition, a map
  of the space, the first frame, lens and angle, camera, light, timed actions, physics, acting, dialogue or lip-sync,
  sound, constraints), split into several clips when the scene is longer than the model allows. Use whenever someone
  wants a Seedance or AI video prompt, a cinematic shot or scene, a dialogue scene, a music-video moment, "turn this
  scene into a video", a shot list for a clip, or says their video prompts give wobbly, random or off-script results.
license: MIT
---

# TikiAPI: Seedance director

A video model does exactly what the prompt pins down and improvises everything else. A director leaves nothing that
matters to improvisation: where everyone stands, what the lens sees at 0.0 s, what happens second by second, and what
must never happen. This skill turns a scene into that, then into orders. Calls follow the `tikiapi-generate` skill:
the key from `TIKIAPI_KEY`, never printed; the price before the order; one paid clip at a time; links back.

## 1. Read the live limits

Models, limits and prices change often, so nothing in this skill is a number to trust. Before planning, call
`list_models` (REST `GET /v1/models`) and note for the target model:

- `min_seconds` and `max_seconds`: the shortest and longest single clip;
- `max_reference_images`, `max_reference_videos` with `max_reference_video_seconds`, `max_reference_audios` and
  `reference_audio_alone`;
- `image_modes`: whether a clip can open on a frame (`first_frame`) or land on one (`first_last_frame`);
- `resolutions`, `aspect_ratios`, `audio_optional`, and `pricing` (`with_video_usd` when reference videos are billed).

Current examples, to check against the list: Seedance 2.5 for long clips with many references, Seedance 2.0 and 2.0
Fast for cheaper drafts.

## 2. The brief

Ask in one message, at most six questions, skipping what the person already said. Offer a default for each, so a
plain "yes" is an answer:

1. **References:** which people, places, products, looks, motion clips or voices they have as files.
2. **Scene:** what happens, from the first moment to the last, in two or three sentences.
3. **Camera:** a feel (handheld, locked-off, a slow dolly, a drone, a whip pan) or "you choose".
4. **Lines:** who says what, in which language, or no speech at all.
5. **Sound:** ambience, effects, music, or silence for a voice-over added later.
6. **Duration and format:** total seconds; 9:16, 16:9 or another ratio from the list.

People come from the `tikiapi-character` skill and places from `tikiapi-location`; if the person has neither, offer
to make them first, because a clip built on a written face drifts.

## 3. Hand back three things

1. **The reference list:** every file as `image N`, `video N` or `audio N` in the order it will be sent, with what it
   controls and what not to take from it.
2. **The shot breakdown:** clip, shot, start and end time, framing and camera, action, line, sound. The times add up
   to the clip's `duration`.
3. **The prompt**, in these twelve blocks and this order:

| Block | Holds |
|---|---|
| Composition | The frame: aspect, who fills which part, foreground and background |
| Map | Where each person and object is in the space, which way each faces, distances |
| First frame | Exactly what is visible at 0.0 s, and that nothing moves yet |
| Lens and angle | Focal length feel, camera height, angle to the subject |
| Camera | One move, its speed, and where it ends |
| Light | Each source: direction, quality (hard or soft), colour temperature |
| Timed actions | `0–2 s: …`, `2–5 s: …`, one main action per window, the end state last |
| Physics | Weight, cloth, hair, liquid, smoke; what stays rigid |
| Acting | Gaze, micro-expressions, the tempo of reactions |
| Dialogue or lip-sync | Who says the exact words in quotes, when, how; or "No speech" |
| Sound | Ambience, effects at their moments, music or none |
| Constraints | The locks: identity, head count, no text, no cuts, nothing new enters |

How to write each block, the wording rules and a full example: [prompt-blocks](references/prompt-blocks.md).

## 4. Long scenes become clips

When the scene is longer than `max_seconds`, or holds more angles than one clip carries cleanly, split it. Each clip
gets its own full prompt; the light, look and constraint blocks are copied word for word, so the clips cut together.
How to split, carry the action across a cut and keep the sound continuous:
[shot-breakdown](references/shot-breakdown.md).

## 5. Price, ask, make

1. `estimate_cost` for every clip with its real fields: `duration`, `resolution`, `aspect_ratio`, the images, the
   reference videos (their seconds are billed too, and pricing them needs a signed-in key). Give the total in one line
   and wait for the go.
2. One clip at a time. Show each and check it against the breakdown in this order: identity, constraints, timing,
   camera, sound. Stop at the first failure; polish can't save a wrong face.
3. `queued` or `running` is not failed: check the same id; never place it again.
4. Fix one block at a time on a redo, so you learn what the model listened to.

## Related skills

- `tikiapi-character`: the people. `tikiapi-location`: the places and the first frames.
- `tikiapi-motion-transfer`: copy a movement or a camera path from a clip.
- `tikiapi-story-bible`: keep a whole series consistent. `tikiapi-look`: the colour.
