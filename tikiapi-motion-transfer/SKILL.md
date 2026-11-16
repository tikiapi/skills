---
name: tikiapi-motion-transfer
description: >-
  Move the motion of a reference video onto new characters with Seedance 2.x reference video on TikiAPI, in three
  modes: copy the body (a dance, a fight, a gesture, a walk), copy only the camera move, or copy the body under a new
  camera, with the mouth decided first (closed, exact new lines, or as in the source). Use whenever someone wants
  their character to "do what this video does", to recreate a dance or a trend with their own character, to reuse a
  choreography, a stunt or an acting take, to copy a camera move from a clip, or to get motion capture without a suit.
license: MIT
---

# TikiAPI: motion transfer

Seedance 2.x takes a reference video and can lift its motion (a body's movement, the camera's path, or both) while the
people, the place and the look come from your images and words. The whole craft is saying exactly which part of
`video 1` to copy and which to ignore. Calls follow the `tikiapi-generate` skill: the key from `TIKIAPI_KEY`, never
printed; the price before the order; one paid clip at a time; links back.

## 1. Check the model can

Call `list_models` with `kind` `video` (REST `GET /v1/models`). Use a model whose `max_reference_videos` is at least 1;
today that is the Seedance 2.x family (for example Seedance 2.5 or Seedance 2.0), but check the list. Note:

- `max_reference_video_seconds`: the longest source clip it takes;
- `max_reference_images`: the character pictures count here, a saved character's photos included;
- `max_reference_audios` and `reference_audio_alone`, for a voice track;
- `min_seconds` / `max_seconds`, `resolutions`, `aspect_ratios`;
- `pricing`: `with_video_usd` is charged per second over the clip's seconds plus the reference video's seconds.

A reference video can't go with an opening frame (`first_frame`, `first_last_frame`): the character comes in as a
reference image, and the model builds the first frame itself.

## 2. Prepare the source clip

- **Rights:** the person's own clip, or one they may use. The performer's face and body never carry over; the prompt
  says so.
- **Trim** it to just the motion wanted, within `max_reference_video_seconds`. Shorter is cheaper, since its seconds
  are billed. Trimming locally is free:
  `ffmpeg -ss 2.0 -i source.mp4 -t 5 -c:v libx264 -crf 18 -an motion.mp4` (keep the sound, without `-an`, only when
  the mouth follows the source).
- **Body modes:** one performer, the whole body in frame the whole time (cut-off limbs get invented), no cuts inside
  the trimmed part, steady light.
- **Shape:** the source in the aspect ratio of the result, or close to it.
- **Upload** with `upload_media` (`mode: "prepare"` for a big file) and use the id or link it returns.

## 3. Decide the mouth first

Mouths break first, and a model that isn't told will often invent talking. Ask before anything else:

| Mouth | When | In the prompt |
|---|---|---|
| **Closed** | Dance, action, a music video with its own track | "Mouths stay closed the whole time; nobody speaks or sings. No speech, no voices." |
| **Exact lines** | The character says new words | The words in quotes with their time window; or a take from `speak` sent as `audio 1`: "her lips match audio 1 exactly" |
| **As in the source** | Lip-sync to the source's speech or singing | Keep the source's sound in `video 1`: "her mouth follows the speech in video 1 exactly" |

## 4. Pick the mode

| Mode | Copy from video 1 | From your images and words |
|---|---|---|
| **Body** | The performer's movement and timing, and the camera | The character, the place, the light, the look |
| **Camera only** | The camera's path, speed and shake | The action, the people, the place |
| **Body + new camera** | The performer's movement and timing | A camera you describe (one move) |

Prompts for each, the binding lines and the fixes: [modes](references/modes.md).

## 5. Bind every reference

One line per file: what it controls and what not to take from it. "Video 1 is a motion reference only: copy the
dancer's body movement and timing exactly; do not copy the dancer's face, hair, body shape, clothes, the room or the
colours." "Image 1 is the character: her face, hair, build and outfit." "Image 2 is the place." Say the head count:
"exactly one person appears".

## 6. Price, ask, make

1. `estimate_cost` with the real fields: the model, `duration` (the trimmed source's length, rounded to a whole
   second within the model's range), `resolution`, `aspect_ratio`, `image_urls`, `video_urls`, `audio_urls`. Pricing
   reference videos needs a signed-in key. Tell the person the price and wait for the go.
2. One clip. Check it in this order: the mouth, identity, the motion against the source, the camera, the place.
3. `queued` or `running` is not failed: check the same id; never place it again. A redo changes one thing at a time.

## Related skills

`tikiapi-character` for the people, `tikiapi-location` for the place, `tikiapi-director` for the full scene prompt
around the motion.
