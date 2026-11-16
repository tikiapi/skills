# The twelve blocks

Write each block as plain sentences after its label (`COMPOSITION:`, `MAP:` …). Labels keep the blocks apart for the
model and for the person reviewing the prompt. A block that doesn't apply is left out, except Dialogue and
Constraints, which are always written, even as "No speech".

## Wording rules

- **Name files by kind and position:** "image 1", "image 2", "video 1", "audio 1", in the order they are sent.
  With `character_id`, the server puts the person's photos first and names them; call the person by their saved name
  and your own images by their role ("the location image", "the product photo").
- **One name per thing.** "The rider" stays "the rider"; a second word ("the courier") reads as a second person.
- **Observable only.** Write what a camera could record. "She is nervous" gives nothing; "she rubs her thumb along
  the cup's rim and doesn't look up" does.
- **One camera move per shot.** Two moves at once (a push-in while orbiting) make the picture wobble and morph.
- **One main action per time window,** and windows of about two seconds or more. Actions crammed into one second are
  skipped or blurred together.
- **Every time window adds up:** the last one ends exactly at the clip's `duration`.
- **End states are visible:** "the bowl is half full, both look at each other", not "they feel at home".
- **Constraints last and short;** restate the most expensive one (usually identity) as the very last sentence.
- **Cut adjectives, not blocks,** when the prompt is too long (`prompt_too_long`).

## Block by block

**Composition.** The aspect ratio and the frame's thirds: who or what fills which part, how much of the body is in
frame (full, waist up, chest up, face), what sits in the foreground and the background. A face that must hold
identity is large in frame; a wide shot with a small face drifts.

**Map.** The space as a floor plan, from the camera: left, right, near, far, and which way each person faces. Give
distances in plain units ("two metres apart"). Name fixed things that anchor the space (a door, a counter, a window)
and keep their side the same in every clip. Props get an owner: "the cup belongs only to the customer".

**First frame.** A still: who is already in place, in which pose, holding what, where they look. "Nobody is moving
yet." When the clip opens on an image (`first_frame`), this block describes that image and adds "start exactly from
image 1".

**Lens and angle.** A focal-length feel (24mm wide, 35mm natural, 50mm, 85mm portrait compression), the camera height
(eye level, low from the waist, high from above), the angle (frontal, three-quarter, over the shoulder, profile).

**Camera.** One move with its speed and its end: "a slow push-in over the whole clip, ending in a medium two-shot";
"locked off, no movement"; "handheld, gentle breathing sway, no shake". Several shots in one clip: one move per shot.

**Light.** Each source on its own line: where it comes from (frame left, behind, above), its quality (hard with crisp
shadows, soft with gradual ones), its colour temperature (warm tungsten about 3200K, daylight about 5600K, cool shade
or blue hour about 7000K and up), and what makes it in the world (a window, a neon sign, a lamp). Say which side of
the faces is in shadow.

**Timed actions.** `0–2 s: …` windows, the subject named in each, the verb concrete. A hard cut inside a clip is its
own line: `4.0 s: hard cut to …`. The last window carries the end state.

**Physics.** What has weight and how it moves: wet cloth hangs heavy, hair settles after a turn, steam rises and
drifts with the air, liquid sloshes and doesn't defy the cup. Name what must stay rigid (a helmet, a phone, a car
body), because rigid things are the ones that melt.

**Acting.** The gaze (to whom, when it moves), the micro-expressions (a half smile, a slow blink, a jaw tightening),
and the tempo of reactions ("reacts half a second late"). Small and specific beats big and general.

**Dialogue or lip-sync.** The speaker, the exact words in quotes, the time window, the language and the delivery
("low and tired"). Keep a line within the window: about two and a half words a second. Others: "does not speak". With
a voice track sent as `audio 1`: "the rider's lips match audio 1 exactly; nobody else speaks". Silent clips: "No
speech, no voices, no singing", because a model left alone may add talking.

**Sound.** The ambience (rain on an awning, a room tone), the effects at their times ("the strap clicks at 2 s"), and
music or "no music". When the cut gets a narrator or a score later: "only the sound effects described".

**Constraints.** The head count ("exactly two people"), identity ("the rider keeps the face, hair and jacket of image
1"), continuity ("one continuous shot, no cuts" or the cuts listed above), no text ("no subtitles, no captions, no
readable signs"), and "nothing else enters the frame".

## A full example

Brief: 12 s, 9:16, a delivery rider at a noodle stall at night, one line, rain, no music. References: the rider and
the cook as saved pictures, the stall as an empty location plate.

Reference list:

```text
image 1: the rider: face, hair, build and rain jacket. Use only the person.
image 2: the cook: face, build and apron. Use only the person.
image 3: the noodle stall at night, empty. Use the set, its layout and its light; no people from it.
```

Shot breakdown:

| Clip | Shot | Time | Framing and camera | Action | Line | Sound |
|---|---|---|---|---|---|---|
| 1 | 1 | 0–12 s | Over the rider's shoulder, 35mm, slow push-in to a two-shot | Visor up, helmet off, the line, the cook ladles | "Same as yesterday. Extra chilli." | Rain, pot, strap click |

Prompt:

```text
COMPOSITION: Vertical 9:16. The rider fills the left third from the waist up, seen from behind the right shoulder;
the stall's counter and the cook fill the right two-thirds in the middle distance. Rain streaks across the foreground.
MAP: The street runs left to right. The rider (image 1) stands on the pavement at frame left, facing right towards the
counter, two metres from it. The cook (image 2) stands behind the counter at frame right, facing the rider. A steaming
pot sits on the counter, nearer the cook. The stall is image 3, exactly as it is there.
FIRST FRAME: The rider already stands still, helmet on, visor down, hands at the chin strap. The cook stirs the pot,
eyes down. Nobody else is in the street.
LENS AND ANGLE: 35mm, eye level, a three-quarter angle from behind the rider's right shoulder.
CAMERA: A slow push-in over the whole clip, ending in a medium two-shot of both faces. No other move.
LIGHT: Warm tungsten about 3200K from the stall's bulbs above the counter, hard, lighting the cook's face and the
rider's right cheek. Cool blue street light about 7000K from frame left and behind, soft, rimming the rider's helmet
and shoulders. The rider's left side stays in shadow.
TIMED ACTIONS:
0–2 s: the rider lifts the visor with the left hand.
2–5 s: the rider takes the helmet off with both hands and tucks it under the left arm; wet hair falls onto the forehead.
5–7 s: the cook looks up and stops stirring.
7–10 s: the rider says the line below and nods once towards the pot.
10–12 s: the cook smiles and ladles noodles into a bowl. End state: the bowl half full, the two looking at each other.
PHYSICS: Rain falls straight down, brighter in the bulb light; drops bead and run down the helmet shell. Steam rises
from the pot and drifts right. The helmet stays rigid. The wet jacket hangs heavy and does not flutter.
ACTING: The rider is tired and warm: a short exhale before speaking, eyes half closed. The cook reacts half a second
late with a slow, knowing smile. No big gestures.
DIALOGUE: Only the rider speaks, once, from 7 to 10 s, in English, low and tired: "Same as yesterday. Extra chilli."
The lips move only during the line. The cook does not speak.
SOUND: Steady rain on the pavement and the stall's awning, the pot bubbling, distant traffic hiss; the chin strap
clicks at 2 s. No music.
CONSTRAINTS: Exactly two people. One continuous shot, no cuts. No subtitles, no captions, no readable signs or
letters anywhere. Nothing else enters the frame. The rider keeps the face, hair and jacket of image 1 and the cook
keeps image 2, unchanged.
```

The person reviews the reference list and the breakdown first: changing a line there is free, changing it after the
clip is not.
