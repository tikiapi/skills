# Changelog

## 0.2.0 (2026-11-16)

New skills:
- `tikiapi-director`: a scene into a short brief, a reference list, a shot breakdown with timings and a Seedance
  prompt in twelve fixed blocks; long scenes split into clips that cut together.
- `tikiapi-location`: one consistent place for image models: an empty plate, characters placed into it as a video's
  first frame, an angle set that keeps the geometry and light, and one-detail edits; light by direction, quality and
  colour temperature; wording per model.
- `tikiapi-motion-transfer`: a reference video's motion onto new characters with Seedance 2.x reference video: copy
  the body, only the camera, or the body under a new camera, with the mouth decided first.
- `tikiapi-story-bible`: interviews the person about their world and writes a project skill they install, so every
  later prompt keeps the characters, places, rules, look, sound and timeline.
- `tikiapi-launch-video`: a project or a website as a short launch video, adapted from brag-slim (MIT): free motion
  graphics, or upgraded with generated shots, a music bed, a sound effect and a voice line, priced before spending.

Changed:
- `tikiapi-character`: built in four stages (face, details, outfit, sheet) on neutral light-grey references; detail
  pictures saved as extra images; the sheet is for people, never a model reference.
- `tikiapi-generate`: limits and prices only from the live model list; music, sound-effect and speech models in the
  usual picks; references named by kind ("video 1", "audio 1").
- Every skill reads current limits from `list_models` and prices paid steps with `estimate_cost`; model names are
  examples, never fixed limits or prices.

## 0.1.0 (2026-11-15)

First release: `tikiapi-generate`, `tikiapi-character`, `tikiapi-ad-video`, `tikiapi-ad-script`, `tikiapi-audience`,
`tikiapi-look`, with plugin manifests for Claude Code, Codex and Cursor.
