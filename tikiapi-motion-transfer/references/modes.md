# The three modes

Fill the square brackets. The mouth line comes from SKILL.md, step 3. With a saved `character_id`, the server puts
the person's photos first and names them: call them by their saved name and your other images by their role
("the location image").

## Body: copy the movement and the camera

Files: `video 1` the source, `image 1` the character (face close-up), `image 2` the full body or the place.

```text
Video 1 is a motion reference only: copy the performer's whole-body movement, timing and the camera exactly, beat for
beat. Do not copy the performer's face, hair, body shape, skin, clothes, the room, the props or the colours.
Image 1 is the character who performs it: her face, hair and build. Image 2 is her outfit [or: the place].
Exactly one person appears: the character from image 1, performing the movement of video 1 [in the place].
[MOUTH LINE]
Light: [direction, quality, colour temperature]. [The look words]. No text, no subtitles.
```

## Camera only: copy the camera path

Files: `video 1` the source, then the people and the place.

```text
Video 1 is a camera reference only: copy its camera path, speed, framing changes and handheld shake exactly. Do not
copy anything in front of the camera: no people, actions, objects, places or colours from video 1.
The scene: [the action in timed windows, as in the director skill]. Image 1 is [the character]; image 2 is [the place].
[MOUTH LINE]
Light: [...]. [The look words]. No text, no subtitles.
```

Good sources: a drone reveal, a dolly-zoom, an orbit, a running handheld follow. The new action should fit the path:
a camera that circles needs a subject that stays near the centre.

## Body + new camera: the movement, a different camera

Files: `video 1` the source, `image 1` the character, `image 2` the outfit or the place.

```text
Video 1 is a motion reference for the body only: copy the performer's whole-body movement and timing exactly. Ignore
video 1's camera, framing and angle, and do not copy the performer's face, hair, body shape, clothes, the place or
the colours.
Camera: [one new move, its speed and where it ends: a slow orbit to the right from a three-quarter front view to a
profile / a low angle, locked off].
Image 1 is the character who performs it; image 2 is [the outfit / the place]. Exactly one person appears.
[MOUTH LINE]
Light: [...]. [The look words]. No text, no subtitles.
```

Keep the new camera simple. A camera that moves a lot while the body also moves a lot is where limbs smear.

## Two characters

A source with two performers works in body mode when both stay in frame and apart. Bind them by position:
"the performer on the left in video 1 becomes the character in image 1; the one on the right becomes the character
in image 2". Two people need two sets of pictures: check `max_reference_images` first.

## Fixes

| Symptom | Fix |
|---|---|
| The source performer's face or clothes appear | Strengthen "do not copy the performer's face, hair, body shape, clothes"; put the character's face close-up as image 1 |
| The character talks when they shouldn't | The closed-mouth line, plus "No speech, no voices, no singing" at the very end |
| Lips miss the new line | Send the line as audio from `speak` and bind it: "her lips match audio 1 exactly" |
| Limbs smear or multiply | A source with the whole body in frame and no fast spins; a simpler camera; a shorter clip |
| The motion drifts from the source | Trim the source to one clean movement; say "beat for beat, the same timing" |
| The room from the source leaks in | Add a place image and "do not copy the room"; describe the new place in one clause |
| The camera copies when it shouldn't | "Ignore video 1's camera" and describe the new camera's single move |
| `input_refused` | Retry once with `run_again`; if refused again, change the reference (often a too-real face) |
