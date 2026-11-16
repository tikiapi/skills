---
name: tikiapi-generate
description: >-
  Generate images and videos with TikiAPI (Seedance, Gemini Omni, Nano Banana, GPT Image, Seedream) through its MCP
  server or REST API: pick a model from the live list, price the order, make it, wait for it and hand back the links.
  Use whenever someone asks to generate, make, render or draw a picture, photo, frame, clip or video with TikiAPI, to
  upload a file for a generation, or to check a TikiAPI price, order or balance. The other tikiapi-* skills build on it.
license: MIT
---

# TikiAPI: generate

One order = one prompt in, one picture or clip out. This skill is the base the other `tikiapi-*` skills stand on: how
to reach the API, how to spend safely, and how to hand back results.

## 1. Connect

Use the first that works:

1. **MCP tools.** If tools such as `list_models`, `estimate_cost` and `generate` from the `tikiapi` server are
   available, use them. Server: `https://mcp.tikiapi.com/mcp`, header `Authorization: Bearer <key>`.
2. **REST.** `https://api.tikiapi.com/v1`, with `Authorization: Bearer $TIKIAPI_KEY`. The helper
   `scripts/tikiapi.mjs` (Node 18+, no dependencies) wraps every call; see [mcp-and-rest](references/mcp-and-rest.md).

**The key** lives in the `TIKIAPI_KEY` environment variable.
- Never print, echo, log or write it to a file, and never paste it into the chat. Refer to it as `$TIKIAPI_KEY` in
  commands; don't run `env`, `printenv` or `set -x` where it could show.
- If it is missing, tell the person to create a key at https://tikiapi.com/dashboard/keys and set `TIKIAPI_KEY` in
  their environment (then restart the agent). Never ask them to send it in the chat.
- `tk_test_…` keys are free and return sample results: good for trying a flow. `tk_live_…` keys spend the balance.

## 2. The order of work

1. **List.** `list_models` (`GET /v1/models`). Use only models it lists, within its limits (durations, resolutions,
   aspect ratios, reference counts, image modes). Prices come from here only, never from memory.
2. **Price.** `estimate_cost` (`POST /v1/generations/estimate`) before every video, and before any batch. Tell the
   person the price; check `enough_balance`.
3. **Ask** before spending on video, unless the person asked for exactly that clip. Videos one at a time; show each
   result before the next. Several pictures the person asked for may go together: `generate` with `wait: false` for
   each, then one `wait_for_generations` with their ids (up to 12).
4. **Make.** `generate` (`POST /v1/generations`). The MCP tool waits about a minute and reports its progress; REST
   answers at once unless you send `Prefer: wait=60`.
5. **Wait, never re-order.** While `status` is `queued` or `running`, check the same id with `get_generation`
   (`GET /v1/generations/{id}`) after `poll_after_seconds`. A slow order is not a failed one. Placing it again pays twice.
6. **Look, then hand back links.** The MCP answer shows a small preview of each result (a picture at 1024 px; a clip as
   4 frames: its first, two from the middle, its last); check it before you send it on. Give `outputs[].url` (the
   original), with what it cost (`charged`). Send videos as links, not files. Results are kept for 30 days
   (`expires_at`); download what must be kept.

## 3. Inputs

- A local file goes in with `upload_media` or `POST /v1/uploads` (REST: the raw file). Images up to 20 MB, video 50 MB,
  audio 15 MB; kept 48 hours. `upload_media` takes it three ways: `mode: "prepare"` with the file's `bytes` gives a
  signed link and a ready `curl` command to send the file yourself (best whenever you have a shell: no base64 in the
  chat); `url` fetches a public link; `data` takes base64 (up to 20 MB). The answer's `id` (`up-…` or `put-…`) or its
  `url` goes into an order, a character or an edit.
- MCP fields are `image_urls`, `video_urls`, `audio_urls`; REST fields are `images`, `videos`, `audios`.
- Video `image_mode`: `reference` (default: things to bring in, several images), `first_frame` (the clip opens on the
  one image), `first_last_frame` (opens on the first, ends on the second). Frames and references don't mix.
- In a Seedance prompt, name the references by kind and order: "image 1", "image 2", "video 1", "audio 1", and say
  what each one controls.
- `audio: false` asks for a silent clip where the model allows it (`audio_optional` in the model list).

## 4. Which model

Models, limits and prices change often. Check `list_models` first: its `capabilities` (`max_seconds`,
`max_reference_images`, `max_reference_videos`, `max_reference_video_seconds`, `max_reference_audios`, `resolutions`,
`aspect_ratios`, `image_modes`) are the only limits to trust, and its `pricing` the only prices. These are today's
usual picks, as examples; if one is gone, take the closest of its kind from `list_models`:

| Job | Model id |
|---|---|
| Video with sound and the longest clips, from text, references, a reference video or a first frame | `seedance-2.5` |
| Cheaper or shorter video drafts | `seedance-2.0-fast`, `seedance-2.0` |
| A picture with people or products kept from references | `nano-banana-pro` (at most 2 references) |
| A picture with readable words in it | `gpt-image-2.6-sunburst` |
| Fast drafts, boards, many variants | `nano-banana-2`, `seedream-5.0-flash` |
| Large, detailed stills and storyboards | `seedream-5.0-pro` |
| A song or an instrumental music bed (`lyrics`, `style`, `instrumental`; two takes an order) | `suno-v6` |
| A sound effect from a description | `elevenlabs-sfx-v3` |
| A voice-over with `speak` (a voice direction, emotion cues in brackets) | `fish-audio-drama-3` |

## 5. Spending rules

- Never top up the balance. On `insufficient_balance`, give the person the `top_up_url` from the error (or from
  `get_account`).
- `input_refused` (the model refused a reference): retry once with `run_again` (REST: a new idempotency key). If it is
  refused again, report it and change the reference.
- A failed or refused order costs nothing. Don't retry `content_refused` with the same prompt.
- No photos of real, recognisable people as references (actors, celebrities, strangers), and no brands or logos that
  aren't the person's own.

Errors and fixes: [troubleshooting](references/troubleshooting.md).

## Related skills

- `tikiapi-character`: the same person across every picture and clip.
- `tikiapi-location`: the same place across every angle and first frame.
- `tikiapi-director`: a scene into a shot breakdown and a block-by-block Seedance prompt.
- `tikiapi-motion-transfer`: a reference video's movement or camera on your character.
- `tikiapi-story-bible`: a whole world kept consistent across a series.
- `tikiapi-ad-video`: a whole ad, script to final cut. `tikiapi-launch-video`: a project or website as a launch video.
- `tikiapi-look`: a colour look measured and matched.
