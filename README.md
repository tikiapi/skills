# TikiAPI skills

Agent skills for making images, video and sound with [TikiAPI](https://tikiapi.com): Seedance, Gemini Omni, Nano
Banana, GPT Image, Seedream, Suno and more at live prices, plus the playbooks around them: a director for Seedance
scenes, consistent characters and locations, motion transfer, story bibles for a series, launch videos, and a whole
ad from the script to the finished cut. They work in Claude Code, Codex, Cursor and other agents that load Markdown
skills, and call the TikiAPI MCP server or the REST API.

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
| [`tikiapi-character`](./tikiapi-character) | One person who looks the same in every picture and clip: built face → details → outfit → sheet on neutral grey, the identity block, a saved character reused by id |
| [`tikiapi-location`](./tikiapi-location) | One place that stays the same: an empty plate, characters placed into it as a video's first frame, an angle set with the same geometry and light, one-detail edits |
| [`tikiapi-director`](./tikiapi-director) | A scene into a director's brief, a reference list, a shot breakdown with timings and a twelve-block Seedance prompt; long scenes split into clips |
| [`tikiapi-motion-transfer`](./tikiapi-motion-transfer) | A reference video's movement onto your character with Seedance: copy the body, only the camera, or the body under a new camera; the mouth decided first |
| [`tikiapi-story-bible`](./tikiapi-story-bible) | Interviews you about your world and writes a project skill you install, so every later prompt keeps the characters, places, look and timeline |
| [`tikiapi-ad-video`](./tikiapi-ad-video) | A vertical ad end to end: script, audience test, cast, frames, 4-second Seedance clips, narrator voice, word-timed captions, the cut at -14 LUFS. Stops for your go before any video is paid for |
| [`tikiapi-ad-script`](./tikiapi-ad-script) | A short, funny ad script with one idea that a child gets, as a beat table with honest numbers |
| [`tikiapi-audience`](./tikiapi-audience) | Four cold viewers test a script or a cut: a kid of 8, a muted viewer, an audio-only listener and a skeptic |
| [`tikiapi-look`](./tikiapi-look) | A colour look measured in CIELAB numbers, turned into prompt words and a colour board, then checked on the clip |
| [`tikiapi-launch-video`](./tikiapi-launch-video) | A project or a website as a 20-second launch video: free motion graphics, or with generated shots, music, an effect and a voice line, priced first |

They chain:
- **An ad:** `tikiapi-ad-script` → `tikiapi-audience` → your yes → `tikiapi-character` → `tikiapi-ad-video` (frames,
  clips, voice, edit).
- **A series or a film scene:** `tikiapi-story-bible` → `tikiapi-character` and `tikiapi-location` →
  `tikiapi-director` (with `tikiapi-motion-transfer` when a movement comes from a clip).
- **A launch:** `tikiapi-launch-video`, with or without generation.

`tikiapi-look` sets the colour, and `tikiapi-generate` sits underneath every call.

## How they spend

- Models, limits and prices change often, so no skill trusts a number from memory: each reads them from
  `list_models` (`GET /v1/models`). The model names in the skills are examples.
- Every video and every paid batch is priced with `estimate_cost` first, and the agent tells you the price.
- One paid item at a time, each shown before the next. The ad flow stops for your go before any clip.
- A failed or refused order costs nothing. A slow one is waited for, never placed twice.
- The agent never tops up your balance; it gives you the top-up link.

## MCP scenarios

Several of the playbooks also ship as prompts on the MCP server (`ad-video`, `ad-script`, `audience-room`,
`consistent-character`, `voiceover-captions`, `ugc-ad`, `look-match`, `product-photo`, `thumbnail`). In Claude Code
they appear as `/mcp__tikiapi__ad-video` and so on.

## Changes

See [CHANGELOG.md](./CHANGELOG.md).

## License

MIT, see [LICENSE](./LICENSE). Two reference files are adapted from the Seedance 2.5 Skill by AtlasCloudAI and stay
under CC BY 4.0. `tikiapi-launch-video` is adapted from brag-slim in [brag](https://github.com/latent-spaces/brag)
(MIT, Copyright (c) 2026 Shunit Haviv Hakimi). Both notices are in [NOTICE](./NOTICE).
