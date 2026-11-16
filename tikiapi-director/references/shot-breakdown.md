# Shot breakdown and long scenes

## The reference list

One line per file, in the order it is sent, with what it controls and what not to take:

```text
image 1: the rider: face, hair, build and jacket. Use only the person.
image 3: the stall at night, empty. Use the set, the layout and the light; no people from it.
video 1: motion reference: the helmet-off movement only; not the performer, the street or the colours.
audio 1: the rider's line, voiced with speak. The rider's lips match it.
```

Check the counts against `list_models` before writing the prompt: `max_reference_images` (a saved character's photos
count among them), `max_reference_videos` and `max_reference_video_seconds`, `max_reference_audios`. A model that
can't take `audio` alone (`reference_audio_alone: false`) needs an image or a video next to it. An opening frame
(`first_frame`, `first_last_frame`) can't go with reference videos or audio: choose one route per clip.

Fewer references hold better than many. Each extra file is one more thing the model has to place; send what the shot
shows, not everything the project has.

## The table

| Clip | Shot | Time | Framing and camera | Action | Line | Sound |
|---|---|---|---|---|---|---|

- Times are clip-relative (each clip starts at 0) and add up to its `duration`.
- A shot inside a clip ends with a hard cut, written into the prompt as `4.0 s: hard cut to …`.
- Keep a clip to one to three shots. More cuts inside one clip blur into each other.

## When to split

- The scene is longer than the model's `max_seconds`.
- The camera changes position in a way one move can't cover (a reverse angle, another room).
- A new place, a jump in time, or a new person who needs references the clip can't also carry.
- One beat is risky (a stunt, a complex hand action): give it its own short clip, so a redo costs only that clip.

Prefer splitting at a natural cut: a change of angle, the start of a line, a look off screen. Never in the middle of
a fast action, unless the next clip continues from its last frame (below).

## Carrying a scene across clips

| Need | Route |
|---|---|
| A hard cut between angles | Each clip from the same references; the Light, Physics and Constraints blocks copied word for word |
| One continuous action across the cut | Take the last frame of clip N and open clip N+1 on it (`image_mode` `first_frame`); the frame carries identity, the set and the light |
| A clip that must end on an exact picture | `first_last_frame` with both frames approved first |
| A continuation that keeps the motion's momentum | Clip N as `video 1` in the next order ("continue video 1 from its last moment…"), if the model takes reference videos; its seconds are billed on top |

The last frame, for the first-frame route:

```bash
ffmpeg -sseof -0.1 -i clip1.mp4 -frames:v 1 -update 1 last.png
```

Upload it with `upload_media` and use the id or link it returns. Check that the frame is sharp; a motion-blurred last
frame makes a blurred opening, so pick a sharper frame a few tenths earlier and trim the clip there in the edit.

## Sound across clips

- The ambience is the same words in every clip's Sound block.
- Music is not generated per clip: each clip would get its own tune. Make the clips with "no music", then lay one
  music bed over the cut (a music model from `list_models`, for example Suno V6, or the person's own track).
- Dialogue: one line per clip at most, timed inside its window. A voice track made with `speak` and sent as `audio 1`
  keeps the same voice across clips.

## Cost and assembly

- `estimate_cost` for each clip with its real fields, then one total. Reference videos are billed per second on top of
  the clip's own seconds (`with_video_usd` in the list). Short clips cost less to redo.
- Make the riskiest clip first: if it fails, the plan changes before the rest is paid for.
- Join the clips with `edit_video` (`operation` `assemble`: the clips in order with trims, one audio track, burned
  captions, -14 LUFS; its price per second is in the tool's description), or in the person's own editor.
