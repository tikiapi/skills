# Identity: references and what to write

> Adapted from "Seedance 2.5 Skill" by AtlasCloudAI (references/real-person.md, references/multi-reference.md),
> https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills, licensed under
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Shortened, rewritten for TikiAPI and merged with our own
> notes. This file stays under CC BY 4.0; see NOTICE.

## The references

- **A clean face close-up and a separate full-body picture.** One person per image, plain background, even light.
- **Never a front / side / back composite** (turnaround, character sheet, contact sheet) as the identity input. It is
  read as several people, and duplicates appear.
- **One binding line per person**, saying what the image controls and what not to take from it:
  "Image 1 is the creator: use only her face, hair and build. Image 2 is her outfit: use only the clothes."
  Never "images 1–4 are four characters": that states no mapping at all.
- **Say the count** when several images show one subject: "both images show one woman; exactly one woman appears".
- **Props have an owner**: "the tiki mug belongs only to the friend". Without it, props migrate between people.

## What to write when a reference carries the face

Written details compete with the picture, and the picture usually wins after a fight that shows up as drift.

| Situation | Write | Leave out |
|---|---|---|
| No identity reference (an invented person, first picture) | Age, origin, face shape, skin texture, eyes, hair, outfit, build | — |
| The reference carries the face | The outfit if it changes, build and bearing, what the eyes and hands do | Face, skin, hair (the identity block covers them) |
| The reference carries only the style or the set | Everything about the person | — |

Build, bearing and the gaze stay in the text because a still picture can't show behaviour: "leans back, slow blink,
a tiny smirk" works; "she looks happy" doesn't.

## The identity block

Put it first in every prompt where a person comes from a reference. It comes from production templates where it held
faces across dozens of frames:

```text
The person in image 1 is the person in this photo. Keep their appearance 100%: the same face and facial features, the
same body proportions, skin tone, eye colour, eyebrows, moles, freckles, piercings and tattoos. Their hair stays
exactly as in image 1: the same length, volume, texture, colour and parting, worn the same way. Do not beautify, slim,
age or restyle them.
```

Our own finding on top: a hand-written hair description ("a blonde helmet bob") made the image model put a helmet on
her head. Leave the hair to the picture.

## When it drifts

| Symptom | Fix |
|---|---|
| Two copies of the person | The reference was a sheet or a collage: use one person per image and state the count |
| Face changes between shots | Put the face close-up as image 1 and the identity block first; drop face words |
| Hair changes | Remove every hair word from the prompt |
| Outfit changes | Add the full-body picture as image 2 and name it "the outfit" |
| The face shrinks into a wide room | Framing first, the room in one short clause |
| Face warps in a clip | Wider framing, gentler camera motion, or a cut instead of a turn |
