# Troubleshooting

Errors have the same shape everywhere: `{"error": {"code", "message", "hint"?, "path"?}}`. Branch on `code`.

## Before the order

| Code | What to do |
|---|---|
| `invalid_api_key`, `expired_api_key` | The key is missing, wrong or old. Ask the person to set a working key in `TIKIAPI_KEY`; never ask for it in chat |
| `missing_scope` | The key can't do this (for example uploads need `generations:write`). A new key with the right permissions |
| `invalid_parameter` | `path` names the field, `hint` says what fits. Fix it from the model list's limits |
| `variant_not_available` | The model isn't sold with these settings (often the resolution). Pick one from the model list |
| `model_not_found` | Use an id from `list_models` |
| `insufficient_balance` | Stop. Give the person the `top_up_url`; never top up yourself |
| `key_limit_reached` | The key's daily limit is spent. Tell the person; don't switch keys |
| `rate_limited` | Wait the `Retry-After` seconds |
| `payload_too_large` | MCP uploads take 20 MB; send bigger clips with `POST /v1/uploads` (50 MB) |
| `model_unavailable` | Try again in a few minutes, or offer another listed model |

## On a failed order (nothing is charged)

| Code | What to do |
|---|---|
| `input_refused` | The model refused a reference, often a face it judged too real. Retry once with `run_again`; if refused again, change the reference |
| `content_refused` | The prompt or a picture breaks the model's rules. Change the request; don't resend it as is |
| `bad_input_file` | A link isn't public or isn't the right kind of file. Upload the file and use the new link |
| `prompt_too_long` | Shorten the prompt; move fixed rules to the end in one short block |
| `timed_out` | If the result arrives later, it is free. Don't re-order straight away; check `list_generations` first |
| `provider_unavailable` | Try again in a few minutes |

## Still running

The MCP `generate` tool returns after about a minute with `status: running` and `poll_after_seconds`. That is normal
for video. Keep calling `get_generation` with the same id; never place the order again.
