---
name: tikiapi-story-bible
description: >-
  Build a story bible for a series, a brand world, a comic or a recurring cast: interview the person about their world
  (characters, places, rules, look, sound, timeline), make and save reference pictures for it with TikiAPI, and write a
  project-specific skill (a SKILL.md with reference files) they install, so every later prompt in any agent keeps the
  world consistent. Use whenever someone has a recurring world, a series, episodes or a mascot universe, says their
  characters or places keep changing between videos, or asks for a story bible, series bible, world bible, lore
  document or a style guide for AI pictures and video.
license: MIT
---

# TikiAPI: story bible

A series stays consistent when nobody rewrites the same facts twice. A story bible fixes them once, as exact words
and exact pictures, and a project skill makes every agent load them before it writes a prompt. This skill interviews
the person, makes the pictures (with their go) and writes that project skill.

## 1. Interview

Seven short rounds. In each, ask three to five questions in one message, offer a default for each, and show the
running summary before moving on. Skip what is already known; stop a round when the person says "enough".

1. **The world:** title, premise in one sentence, genre and tone, audience, format (vertical episodes, a comic, ads).
2. **Characters:** for each, role, age range, look, outfits by situation, voice, habits, what they never do.
3. **Places:** for each, a location sheet as in the `tikiapi-location` skill: floor plan, anchors, light rig.
4. **Rules:** how the world works (technology, magic, physics, money), what never happens in it, brand rules.
5. **Look:** palette, light, lens, grain, era; a reference still can be measured with the `tikiapi-look` skill.
6. **Sound:** a voice direction for each speaking character, the music's style, signature sounds.
7. **Timeline:** the events in order, and for each, who is where and what has changed (a scar, a new coat, a broken
   sign).

The questions and the defaults: [interview](references/interview.md).

## 2. Pictures (paid, with a go)

For each main character, the `tikiapi-character` skill's stages, ending in `create_character`: the bible keeps the
`character_id`. For each main place, the `tikiapi-location` skill's empty master plate. Read `list_models` for the
current models and limits, `estimate_cost` for the whole set, tell the person the total and wait for the go. Results
are kept for 30 days and uploads for 48 hours, so download every picture into the bible's `assets/` folder; a saved
character stays until it is deleted.

## 3. Write the project skill

A folder named after the world, for example `harbour-nights-bible/`:

```text
harbour-nights-bible/
  SKILL.md                      the rules and the check-list, short
  references/characters.md      one block per character, pasted word for word into prompts
  references/places.md          one sheet per place
  references/look-and-sound.md  the look words, the voice directions, the music style
  references/timeline.md        the events and the current state of everyone and everything
  assets/                       the downloaded pictures
```

The template, with the frontmatter and the rules every bible carries: [bible-template](references/bible-template.md).
Write the description so it triggers on the world's title, its characters' and places' names and "episode",
"scene", "shot". Copy the person's exact words into the blocks; never paraphrase a block later.

## 4. Install

Show the files, then put the folder where the person's agent loads skills. Claude Code: `.claude/skills/<name>/` in
the project (this project only) or `~/.claude/skills/<name>/` (every project). Codex, Cursor and others: the
project's `.agents/skills/<name>/` or the agent's own skills folder. Then ask for a test: "write the prompt for a
shot of [a character] in [a place]"; the agent should paste the blocks without being told.

## 5. Keep it current

After every episode, update `timeline.md` (who changed, what broke, what was learnt) and the date at the top of
`SKILL.md`. New characters and places go through the same interview round and get their own blocks. A fact changed
in one place is changed everywhere it appears.
