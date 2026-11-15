# Install for agents

You are an AI agent. The person asked you to install the TikiAPI skills. Do this, in order.

## 1. The key

Check that `TIKIAPI_KEY` is set in the environment without printing it:

```bash
[ -n "$TIKIAPI_KEY" ] && echo "TIKIAPI_KEY is set" || echo "TIKIAPI_KEY is missing"
```

If it is missing, ask the person to create a key at https://tikiapi.com/dashboard/keys and set `TIKIAPI_KEY` in their
shell profile or the agent's environment settings, then restart you. Never ask them to paste the key into the chat,
and never print, log or store it.

## 2. The skills

**Claude Code:** run `/plugin marketplace add tikiapi/skills`, then `/plugin install tikiapi@tikiapi`, and ask the
person to restart Claude Code. The plugin brings the MCP server too.

**Other agents:** clone the repo and put each `tikiapi-*` folder where the agent loads skills:

| Agent | Path |
|---|---|
| Codex | `~/.codex/plugins/tikiapi` |
| Cursor | `~/.cursor/plugins/tikiapi` |
| Other | `~/.<agent>/skills/<skill-name>` |

```bash
git clone --depth 1 https://github.com/tikiapi/skills.git <path>
```

For the MCP server in Cursor or Codex, follow https://tikiapi.com/mcp.

## 3. Check

```bash
node <path>/tikiapi-generate/scripts/tikiapi.mjs account
```

It should print the balance. `invalid_api_key` means the key is wrong; ask the person to fix it in the environment.

## 4. Done

Tell the person the skills are installed and offer three starts: "make a 9:16 product photo", "write and test a
30-second ad script", "make a vertical ad for my product, script to final cut". Don't explain the file layout.
