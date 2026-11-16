# Wording per model

Check `list_models` for what is on sale now: the names below are examples, and a model's `description` there says
what it is good at. Whatever the model, the order of the prompt stays: what each reference is for, the framing, the
subject, the place, the light, the look, the constraints.

| Model family (examples) | Write | Avoid |
|---|---|---|
| Nano Banana (Pro, 2) | Plain, full sentences, like briefing a photographer. The role of each reference first ("The location image is the set: keep it exactly"). Edits as "Change only … Keep everything else identical." | Keyword lists; describing a face that a reference already carries |
| Seedream (5.0 Pro, 5.0 Flash) | Compact, ordered sentences: subject, place, light, look. It handles large, detailed plates and storyboards well, so spell out the floor plan and the anchors | Long stories about the scene's mood with no visible content |
| GPT Image | Exact words in quotes for any sign or label, with where it sits and its style. A precise layout ("a 3x2 grid, thin dark dividers") | Text you don't want readable: it will render it |

## Settings

- **Aspect ratio:** the plate in the shape of its main use (9:16 for vertical clips, 16:9 for wide). A plate made at
  one ratio and cropped to another loses its anchors.
- **Resolution:** drafts at the lowest the list offers, the final plate at the highest you need (often 2K; 4K for
  big prints or heavy crops). Higher costs more: check `estimate_cost`.
- **References:** as few as the job needs. The plate alone for an angle or an edit; the plate and one person for a
  character frame; never above `max_reference_images`. A character's saved photos count among them.

## Check-list for a plate or an angle

- Every anchor the view faces is there, on its wall, the right size.
- The light comes from the side the sheet and the camera position say.
- The colour temperatures read right: warm sources warm, daylight neutral, shade cool.
- No people, figures or faces in an empty plate, and no stray readable text.
- The materials match the sheet (a brick wall stays brick).

A failed check is fixed in the prompt's block it belongs to (the floor plan, the light, the constraints), not by
adding adjectives elsewhere.
