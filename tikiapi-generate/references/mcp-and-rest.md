# MCP tools and REST endpoints

The MCP server and the REST API run the same code: the same checks, the same prices, the same orders.

| MCP tool | REST | What it does |
|---|---|---|
| `list_models` | `GET /v1/models` | Models, their limits and prices |
| `estimate_cost` | `POST /v1/generations/estimate` | The price of an order; nothing is made or charged |
| `generate` | `POST /v1/generations` | Places an order (MCP waits up to about a minute) |
| `get_generation` | `GET /v1/generations/{id}` | Status and result |
| `list_generations` | `GET /v1/generations?limit=&before=` | Past orders, newest first |
| `upload_media` | `POST /v1/uploads` | A local file as a 48-hour link |
| `get_account` | `GET /v1/account` | Balance and the top-up link |
| `create_character`, `list_characters` | | A saved person, reused by `character_id` in `generate` |
| `speak`, `transcribe` | | Voice-over from text; speech to text with word timestamps |
| `edit_video` | | `reframe` a clip, or `assemble` clips, a sound track and burned subtitles at -14 LUFS |

Check each tool's own fields in its schema: the tools above the line are stable, the ones below are newer.

## The helper script

`scripts/tikiapi.mjs` reads `TIKIAPI_KEY` and never prints it. JSON goes to stdout, progress and errors to stderr.

```bash
node scripts/tikiapi.mjs models
node scripts/tikiapi.mjs estimate '{"model":"seedance-2.5","duration":4,"resolution":"720p","images":["https://…/frame.png"],"image_mode":"first_frame"}'
node scripts/tikiapi.mjs generate @order.json --wait     # waits, polling the same id
node scripts/tikiapi.mjs get <id> --wait
node scripts/tikiapi.mjs upload ./frame.png             # -> {"url": …} for images / videos / audios
node scripts/tikiapi.mjs download <id> ./out
```

`generate` sends an idempotency key made from the body and the current 10-minute window, so running the same command
again after a dropped connection returns the same order instead of paying twice. `--again` places a new one.

## Plain curl

```bash
curl https://api.tikiapi.com/v1/generations \
  -H "Authorization: Bearer $TIKIAPI_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: my-order-001" \
  -d '{"model":"nano-banana-pro","prompt":"…","aspect_ratio":"9:16","resolution":"2K"}'

curl https://api.tikiapi.com/v1/uploads -H "Authorization: Bearer $TIKIAPI_KEY" --data-binary @frame.png
```

## An order's fields

| Field (REST / MCP) | Notes |
|---|---|
| `model` | An id from the model list |
| `prompt` | Up to 4,000 characters; English works best |
| `aspect_ratio` | `9:16`, `16:9`, `1:1`, … (the model list says which) |
| `resolution` | Images `1K` / `2K` / `4K`; video `720p` / `1080p` where sold |
| `duration` | Video seconds; you pay for exactly these |
| `images` / `image_urls` | Public https links or upload links |
| `image_mode` | `reference`, `first_frame`, `first_last_frame` |
| `videos` / `video_urls`, `audios` / `audio_urls` | Reference clips and sounds (video models only) |
| `audio` | `false` for a silent clip where allowed |
| `webhook_url` | REST only: we POST the finished order there |

## Statuses

`queued` → `running` → `succeeded` (charged, `outputs` filled) or `failed` (not charged, `error.code` says why) or
`canceled`. Test keys are never charged.
