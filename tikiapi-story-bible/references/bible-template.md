# The project skill template

Fill the square brackets from the interview. Keep the generated `SKILL.md` short (the rules and the check-list); the
blocks live in the reference files. Paths in the generated files are plain text, relative to the bible's folder.

## SKILL.md

```markdown
---
name: [world-slug]-bible
description: >-
  The story bible of [Title]: [premise in one sentence]. Use for every picture, clip, voice line, script, episode or
  prompt about [Title], [Character A], [Character B], [Place 1] or [Place 2], or any "scene", "shot", "episode" or
  "frame" in this project, even when the request doesn't mention the bible. It keeps faces, places, the look, the
  sound and the timeline consistent.
license: [the person's choice]
---

# [Title]: story bible

Updated [date]. Current state: [where the story stands, one line].

## Before every prompt

1. Find who and what is in the shot. Paste each character's block from `references/characters.md` and the place's
   sheet from `references/places.md` word for word. Never rewrite a block, never describe a face or hair in other
   words: with a saved `character_id`, the pictures carry the face.
2. Check `references/timeline.md` for the scene's moment: outfits, injuries, broken or new objects, who knows what.
3. End the prompt with the look words from `references/look-and-sound.md`.
4. For voice lines, use the character's voice direction from `references/look-and-sound.md`.
5. Read the current limits with `list_models` and price with `estimate_cost` before anything paid.

## Never

- [The world's "never" list, one line each.]
- New facts about a character or place without asking; if a scene needs one, propose it and add it here once agreed.

## Files

- `references/characters.md`, `references/places.md`, `references/look-and-sound.md`, `references/timeline.md`
- `assets/`: the reference pictures, named `<character-or-place>-<view>.png`
```

## references/characters.md

```markdown
## [Name]: [role in four words]

- character_id: [id from create_character, if saved]
- Pictures: `assets/[name]-face.png` (face close-up), `assets/[name]-body.png` (full body), [details]
- Build and bearing: [what a picture can't show: posture, how they move]
- Outfits: work: [...]; home: [...]
- Habits: [two physical tells]
- Never: [...]
- Voice direction: [for speak]
- Prompt block (paste as is): "[Name], [role]: [build and bearing], wearing [the scene's outfit]. [Their habit, if
  the scene shows it]."
```

## references/places.md

One `tikiapi-location` sheet per place, with the plate's file name (`assets/[place]-master.png`) and its angle set.

## references/look-and-sound.md

```markdown
## Look words (end of every prompt)
"[palette, light, lens, texture in one or two sentences]"

## Voices
- [Name]: "[voice direction]"

## Music
[genre, tempo, instruments, mood]

## Signature sounds
[...]
```

## references/timeline.md

```markdown
| # | Episode / date | Event | Changes after it |
|---|---|---|---|
| 1 | [...] | [...] | [who looks different, what broke, who knows what] |

Current state: [...]
```
