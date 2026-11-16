---
name: tikiapi-character
description: >-
  Keep one person looking the same across every TikiAPI picture and clip: built in stages (face, details, outfit,
  then a character sheet for people) on neutral grey references, the identity block in every prompt, a saved
  character reused by id, and first-frame clips. Use when someone wants a recurring character, a cast for an ad or a
  series, a character sheet, "the same person in every shot", an avatar or presenter, a creator for a UGC ad, or
  complains that a face, hair or outfit changes between generations.
license: MIT
---

# TikiAPI: consistent character

A person drifts for three reasons: the reference is a sheet the model reads as several people, the prompt describes
the face in words that fight the picture, or too many references compete. Each step below closes one of these. Calls
go through the `tikiapi-generate` skill's rules: price first, one paid item at a time, links back.

## The references

Every person gets two working pictures, each showing one person on a plain **neutral light-grey** background (no
colour cast, no gradient) in soft, even light. Grey tints neither the skin nor the clothes, and nothing from it leaks
into the scenes the references are used in later.

1. **Face close-up**, 3:4: head and shoulders, eyes open, a calm expression.
2. **Full body**, 3:4: head to toe, the outfit they wear in the story.

Never a turnaround, a character sheet or a contact sheet as a reference, and above all not for video: the model reads
it as several people. Details and the reasons: [identity](references/identity.md).

Models and their limits change: read `list_models` for the image models, their resolutions and
`max_reference_images` (today's example: Nano Banana Pro at 2K), and run `estimate_cost` before each stage.

## Make the character, in four stages

Face → details → outfit → sheet. Show each stage to the person and get a yes before the next; each stage takes the
approved pictures before it as references, so a fix stays cheap and nothing drifts.

1. **Face.** From the person's own photo (theirs, or someone who agreed), or invented. An invented person is
   described once, in the close-up's prompt, and never again. No real, recognisable people.
2. **Details.** Only what the story shows up close and the face close-up can't hold: a ring or a tattoo on the hand,
   a scar, glasses, a hairpin, the eyes for an extreme close-up. One close picture each, the face close-up as image 1,
   the same grey background. Skip this stage when there are none.
3. **Outfit.** The full body: the close-up as image 1, the identity block below, then the outfit and the pose. One
   full body per outfit the story needs.
4. **Sheet.** A board for people, not for models: the approved pictures tiled side by side, made locally from the
   files, so it costs nothing. It is for the person's approval, the team and a story bible (`tikiapi-story-bible`).
   Never send it to a model.

Then **save it**: `create_character` with the face close-up, the full body, the detail pictures as extra images, a
name, and the outfit and details in words as notes; `list_characters` shows saved ones. From then on pass
`character_id` to `generate`. Several outfits: save one character per outfit (the same face, that outfit's full
body), so each scene sends only the outfit it shows. Without those tools, keep the links (upload links last 48 hours;
generated results last 30 days) and send them as `image_urls` / `images`.

## Every new picture

Start the prompt with the identity block, then the scene:

> The person in image 1 is the person in this photo. Keep their appearance 100%: the same face and facial features,
> the same body proportions, skin tone, eye colour, eyebrows, moles, freckles, piercings and tattoos. Their hair stays
> exactly as in image 1: the same length, volume, texture, colour and parting, worn the same way. Do not beautify,
> slim, age or restyle them.

- **Never describe the face or the hair in your own words.** Words compete with the picture, and the hair drifts first.
  Describe the outfit, the action, the bearing and what the eyes do.
- **Nano Banana Pro: at most 2 references a picture.** The face close-up plus one more (the full body, a detail, a
  product, a prop, or a location plate from `tikiapi-location`). A detail picture goes in only for a shot that shows
  that detail.
- **Two people in one frame:** first make a cast photo of both standing side by side (their two full-body pictures as
  the 2 references, the identity block for each: "the person on the left is image 1…"), then use that cast photo as
  one reference with one more.
- **Framing first, the room short.** A long room description pulls the shot wide and shrinks the face. Write the
  framing ("medium close-up from the chest up, her face large in frame"), then the set in one clause.
- **Check** every result against the close-up: face, hair, build. Redo a drifted one with the close-up as image 1.

Prompt templates: [prompt-templates](references/prompt-templates.md).

## Into video

- Best: open the clip on an approved frame (a video model from `list_models`, for example `seedance-2.5`, with
  `image_mode` `first_frame`). The frame carries the
  identity; the prompt says "keep everything in image 1 unchanged: faces, hair, clothes".
- With references instead (`image_mode` `reference`): the face close-up and the full body, one line binding each
  ("image 1 is her face, image 2 her outfit; exactly one woman appears"). The model rebuilds the scene from them.
- A clip can come back `input_refused` when a face looks too real to the model: retry once, then remake the frame a
  little more stylised (film still, grain, a less frontal angle).
