# TikiAPI skills

Agent skills for making images and video with [TikiAPI](https://tikiapi.com): Seedance, Gemini Omni, Nano Banana,
GPT Image and Seedream at live prices, plus the playbooks for a whole ad, from the script to the finished cut. They
work in Claude Code, Codex, Cursor and other agents that load Markdown skills, and call the TikiAPI MCP server or the
REST API.

## Install

### Claude Code

```
/plugin marketplace add tikiapi/skills
/plugin install tikiapi@tikiapi
```

The plugin also adds the TikiAPI MCP server (`.mcp.json`), which reads your key from `TIKIAPI_KEY`.

### Any agent

```bash
npx skills add tikiapi/skills
```

### By hand

```bash
git clone --depth 1 https://github.com/tikiapi/skills.git
```

Then link or copy each `tikiapi-*` folder into your agent's skills folder (Claude Code: `~/.claude/skills/<name>`;
Codex: `~/.codex/plugins/tikiapi`; Cursor: `~/.cursor/plugins/tikiapi`). An agent can do it for you:
[INSTALL_FOR_AGENTS.md](./INSTALL_FOR_AGENTS.md).

## Your key

1. Create a key at [tikiapi.com/dashboard/keys](https://tikiapi.com/dashboard/keys). A `tk_test_` key is free and
   returns sample results; a `tk_live_` key spends your balance. Give an agent its own key with a daily limit.
2. Put it in your environment, not in a chat: `export TIKIAPI_KEY=tk_live_…` (in your shell profile, or your agent's
   secure environment settings), then restart the agent.

The skills read the key from `TIKIAPI_KEY` and never print it. To use the MCP server without the plugin, see
[tikiapi.com/mcp](https://tikiapi.com/mcp) for Claude Code, Cursor and Codex.

## Skills

| Skill | What it does |
|---|---|
| [`tikiapi-generate`](./tikiapi-generate) | Any model through MCP or REST: the live model list, the price before the order, waiting without re-ordering, links back. A small REST client in `scripts/tikiapi.mjs` |
| [`tikiapi-character`](./tikiapi-character) | One person who looks the same in every picture and clip: a face close-up and a full body, the identity block, a saved character reused by id |
| [`tikiapi-ad-video`](./tikiapi-ad-video) | A vertical ad end to end: script, audience test, cast, frames, 4-second Seedance clips, narrator voice, word-timed captions, the cut at -14 LUFS. Stops for your go before any video is paid for |
| [`tikiapi-ad-script`](./tikiapi-ad-script) | A short, funny ad script with one idea that a child gets, as a beat table with honest numbers |
| [`tikiapi-audience`](./tikiapi-audience) | Four cold viewers test a script or a cut: a kid of 8, a muted viewer, an audio-only listener and a skeptic |
| [`tikiapi-look`](./tikiapi-look) | A colour look measured in CIELAB numbers, turned into prompt words and a colour board, then checked on the clip |

They chain: `tikiapi-ad-script` → `tikiapi-audience` → your yes → `tikiapi-character` → `tikiapi-ad-video` (frames,
clips, voice, edit), with `tikiapi-look` for the colour and `tikiapi-generate` underneath every call.

## How they spend

- Every video is priced with `estimate_cost` first, and the agent tells you the price.
- One paid item at a time, each shown before the next. The ad flow stops for your go before any clip.
- A failed or refused order costs nothing. A slow one is waited for, never placed twice.
- The agent never tops up your balance; it gives you the top-up link.

## MCP scenarios

The same playbooks ship as prompts on the MCP server (`ad-video`, `ad-script`, `audience-room`,
`consistent-character`, `voiceover-captions`, `ugc-ad`, `look-match`, `product-photo`, `thumbnail`). In Claude Code
they appear as `/mcp__tikiapi__ad-video` and so on.

## License

MIT, see [LICENSE](./LICENSE). Two reference files are adapted from the Seedance 2.5 Skill by AtlasCloudAI and stay
under CC BY 4.0: see [NOTICE](./NOTICE).
