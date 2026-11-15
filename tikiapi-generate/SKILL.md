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
3. **Ask** before spending on video, unless the person asked for exactly that clip. One paid item at a time; show each
   result before the next.
4. **Make.** `generate` (`POST /v1/generations`). The MCP tool waits about a minute; REST answers at once unless you
   send `Prefer: wait=60`.
5. **Wait, never re-order.** While `status` is `queued` or `running`, check the same id with `get_generation`
   (`GET /v1/generations/{id}`) every 10–15 s. A slow order is not a failed one. Placing it again pays twice.
6. **Hand back links.** `outputs[].url`, with what it cost (`charged`). Send videos as links, not files. Results are
   kept for 30 days (`expires_at`); download what must be kept.

## 3. Inputs

- A local file becomes a link with `upload_media` (MCP: base64, up to 20 MB) or `POST /v1/uploads` (REST: the raw
  file; images 20 MB, video 50 MB, audio 15 MB). The link works for 48 hours.
- MCP fields are `image_urls`, `video_urls`, `audio_urls`; REST fields are `images`, `videos`, `audios`.
- Video `image_mode`: `reference` (default: things to bring in, several images), `first_frame` (the clip opens on the
  one image), `first_last_frame` (opens on the first, ends on the second). Frames and references don't mix.
- In a Seedance prompt, name the references in order: "image 1", "image 2", and say what each one controls.
- `audio: false` asks for a silent clip where the model allows it (`audio_optional` in the model list).

## 4. Which model

Check `list_models` first; these are the usual picks.

| Job | Model id |
|---|---|
| Video with sound, up to 30 s, from text, references or a first frame | `seedance-2.5` |
| Cheaper or shorter video drafts | `seedance-2.0-fast`, `seedance-2.0` |
| A picture with people or products kept from references | `nano-banana-pro` (at most 2 references) |
| A picture with readable words in it | `gpt-image-2.6-sunburst` |
| Fast drafts, boards, many variants | `nano-banana-2`, `seedream-5.0-flash` |
| Large, detailed stills and storyboards | `seedream-5.0-pro` |

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
- `tikiapi-ad-video`: a whole ad, script to final cut.
- `tikiapi-look`: a colour look measured and matched.
