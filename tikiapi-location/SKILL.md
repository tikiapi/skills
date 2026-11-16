---
name: tikiapi-location
description: >-
  Build one consistent location with TikiAPI image models (Nano Banana, Seedream, GPT Image): an empty environment
  plate with no people, characters placed into it as a ready first frame for a video, a set of angles of the same
  place that keeps its geometry and light, and an edit that changes one detail and nothing else. Use whenever someone
  needs a set, a background, an environment, a room, a street or a landscape for a story, an ad or a series; a first
  frame for a Seedance clip; "the same place from another angle"; or wants to change one thing in a generated picture
  without the rest drifting.
license: MIT
---

# TikiAPI: location builder

A place drifts the way a face does: the window jumps to another wall, the light swaps sides, the room grows. Fix it
twice, once in words (the location sheet) and once in a picture (the master plate), and reuse both every time. Calls
follow the `tikiapi-generate` skill: the key from `TIKIAPI_KEY`, never printed; the price before the order; links back.

## 1. Read the live limits

Call `list_models` with `kind` `image` (REST `GET /v1/models`) and note, per model: `max_reference_images`,
`resolutions`, `aspect_ratios` and the price. Never assume them; they change. Current examples, to check against the
list: Nano Banana Pro for keeping a reference exactly, Seedream 5.0 Pro for large detailed plates, a GPT Image model
when a sign must be readable, Nano Banana 2 or Seedream 5.0 Flash for cheap drafts. `estimate_cost` before every
batch; tell the person the price.

## 2. The location sheet

Write it before the first picture and show it to the person: the name, the type of place, the time of day and
weather, a floor plan in words (entrances, windows, fixed furniture, seen from the master camera position), three to
five anchors that make the place recognisable, the materials and palette, the light rig, and what is never there.
Template: [location-sheet](references/location-sheet.md).

## 3. Light in three parts

Every source is described by its **direction** (from frame left, behind, above, through the window on the north
wall), its **quality** (hard with crisp shadows, or soft with gradual ones) and its **colour temperature** (warm
tungsten about 3200K, daylight about 5600K, cool shade or blue hour about 7000K and up), plus what makes it in the
world. Directions are tied to the place, not the frame: when the camera turns, the window stays on its wall, so the
light's side in the frame changes. Write the new side for every angle.

## 4. The four jobs

| Job | Inputs | Output |
|---|---|---|
| Empty plate | The sheet | The master wide shot, no people |
| Characters in the scene | The plate + each person's references | A picture that can open a video clip |
| Angle set | The plate + the sheet | Other views of the same place, same geometry and light |
| One-detail edit | One finished picture | The same picture with one change |

Prompts for each: [location-sheet](references/location-sheet.md).

1. **Empty plate.** A wide, eye-level view that shows every anchor. "No people, no figures, no silhouettes, no
   reflections of people." No readable text unless the sheet asks for it. Draft a few on a cheap model, let the
   person pick, then make the final at the resolution the job needs (often 2K). This plate is the reference for
   everything after.
2. **Characters in the scene.** The plate plus the person (`character_id`, or their face close-up and full body from
   the `tikiapi-character` skill). Framing first, then where they stand on the floor plan and which way they face,
   then how the sheet's light falls on them. For a video's first frame: the clip's exact aspect ratio, the pose the
   first action starts from, eyes open, no motion blur, and room for the camera move (frame wider if it pushes in).
3. **Angle set.** One picture per view, each from the plate: name the camera's position on the floor plan, the lens,
   which anchors are visible and where, and the light's side as seen from there. Check every angle: anchors on the
   right walls, the light from the right side, the same materials.
4. **One-detail edit.** The picture as the only reference. "Change only this: …. Keep everything else identical."
   One change per order; chain orders for more. Compare before and after side by side; if anything else moved, redo
   with a tighter lock.

## 5. Wording per model

Each model reads prompts a little differently: plain sentences for Nano Banana, compact and ordered for Seedream,
exact quoted words for GPT Image. The adaptations and a check-list: [model-wording](references/model-wording.md).
Whatever the model, keep this order: what each reference is for, the framing, the subject, the place, the light, the
look, the constraints.

## 6. Hand over

Give the plate's link, each angle's link, and the sheet. Results are kept for 30 days: tell the person to download
the plate and the sheet into their project. For a series, the `tikiapi-story-bible` skill stores both; for a clip, the
`tikiapi-director` skill uses the plate as a reference and a character frame as the first frame.
