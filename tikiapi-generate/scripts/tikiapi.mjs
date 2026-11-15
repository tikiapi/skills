#!/usr/bin/env node
// tikiapi.mjs: a small client for the TikiAPI REST API. Node 18+, no dependencies.
// The key comes from the TIKIAPI_KEY environment variable and is never printed.
//
//   node tikiapi.mjs models                       models, limits and prices
//   node tikiapi.mjs account                      balance and the top-up link
//   node tikiapi.mjs estimate '<json>'            the price of an order; nothing is made
//   node tikiapi.mjs generate '<json>' [--wait] [--again]
//   node tikiapi.mjs get <id> [--wait]
//   node tikiapi.mjs list [limit]
//   node tikiapi.mjs upload <file>                a local file -> a link for images / videos / audios (48 hours)
//   node tikiapi.mjs download <id> <dir>          saves an order's outputs into dir
//
// '<json>' is the request body, or @file.json. Results go to stdout as JSON; progress and errors go to stderr.
// generate is idempotent: the same body within 10 minutes returns the same order. --again places a new one.

import { createHash, randomUUID } from "node:crypto";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { basename, extname, join } from "node:path";

const BASE = (process.env.TIKIAPI_BASE_URL ?? "https://api.tikiapi.com/v1").replace(/\/+$/, "");
const FINAL = new Set(["succeeded", "failed", "canceled"]);
const POLL_SECONDS = 10;
const WAIT_MINUTES = 20;

const [command, ...rest] = process.argv.slice(2);
const flags = new Set(rest.filter((a) => a.startsWith("--")));
const args = rest.filter((a) => !a.startsWith("--"));

function die(message, code = 1) {
  process.stderr.write(`${message}\n`);
  process.exit(code);
}

function key() {
  const k = process.env.TIKIAPI_KEY?.trim();
  if (!k) die("TIKIAPI_KEY is not set. Create a key at https://tikiapi.com/dashboard/keys and put it in the environment (never in the chat).");
  return k;
}

async function call(method, path, { body, headers = {} } = {}) {
  const res = await fetch(`${BASE}${path}`, {
    method,
    headers: { authorization: `Bearer ${key()}`, ...headers },
    body,
    signal: AbortSignal.timeout(120_000),
  });
  const text = await res.text();
  let data;
  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    data = { raw: text.slice(0, 500) };
  }
  if (!res.ok) die(JSON.stringify({ status: res.status, ...(data.error ? { error: data.error } : data) }));
  return data;
}

async function jsonArg(value) {
  if (!value) die("Give the request body as JSON, or @file.json.");
  const raw = value.startsWith("@") ? await readFile(value.slice(1), "utf8") : value;
  try {
    return JSON.parse(raw);
  } catch {
    die("The request body isn't valid JSON.");
  }
}

const json = (body) => ({ body: JSON.stringify(body), headers: { "content-type": "application/json" } });
const print = (data) => process.stdout.write(`${JSON.stringify(data, null, 2)}\n`);
const sleep = (s) => new Promise((r) => setTimeout(r, s * 1000));

/** Polls the same order until it is final: never places it again. */
async function wait(gen) {
  const until = Date.now() + WAIT_MINUTES * 60_000;
  while (!FINAL.has(gen.status)) {
    if (Date.now() > until) {
      process.stderr.write(`Still ${gen.status} after ${WAIT_MINUTES} min. Check later with: get ${gen.id}\n`);
      return gen;
    }
    process.stderr.write(`${gen.id}: ${gen.status}\n`);
    await sleep(POLL_SECONDS);
    gen = await call("GET", `/generations/${encodeURIComponent(gen.id)}`);
  }
  return gen;
}

const TYPES = { ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".mp4": "video/mp4", ".mov": "video/quicktime", ".mp3": "audio/mpeg", ".wav": "audio/wav" };

switch (command) {
  case "models":
    print(await call("GET", "/models"));
    break;
  case "account":
    print(await call("GET", "/account"));
    break;
  case "estimate":
    print(await call("POST", "/generations/estimate", json(await jsonArg(args[0]))));
    break;
  case "generate": {
    const body = await jsonArg(args[0]);
    // The same body in the same 10-minute window is one order, so a retry after a dropped connection never pays twice.
    const window = Math.floor(Date.now() / 600_000);
    const idem = flags.has("--again") ? randomUUID() : `cli-${createHash("sha256").update(JSON.stringify([body, window])).digest("hex").slice(0, 40)}`;
    const req = json(body);
    let gen = await call("POST", "/generations", { ...req, headers: { ...req.headers, "idempotency-key": idem, ...(flags.has("--wait") && { prefer: "wait=60" }) } });
    if (flags.has("--wait")) gen = await wait(gen);
    print(gen);
    if (gen.status === "failed") process.exitCode = 2;
    break;
  }
  case "get": {
    if (!args[0]) die("Give the order id.");
    let gen = await call("GET", `/generations/${encodeURIComponent(args[0])}`);
    if (flags.has("--wait")) gen = await wait(gen);
    print(gen);
    break;
  }
  case "list":
    print(await call("GET", `/generations?limit=${Number(args[0] ?? 20)}`));
    break;
  case "upload": {
    if (!args[0]) die("Give the file to upload.");
    const bytes = await readFile(args[0]);
    print(await call("POST", "/uploads", { body: bytes, headers: { "content-type": TYPES[extname(args[0]).toLowerCase()] ?? "application/octet-stream" } }));
    break;
  }
  case "download": {
    if (!args[0] || !args[1]) die("Give the order id and a folder.");
    const gen = await call("GET", `/generations/${encodeURIComponent(args[0])}`);
    if (gen.status !== "succeeded") die(`The order is ${gen.status}, nothing to download.`);
    await mkdir(args[1], { recursive: true });
    const saved = [];
    for (const [i, o] of gen.outputs.entries()) {
      const res = await fetch(o.url, { signal: AbortSignal.timeout(300_000) });
      if (!res.ok) die(`Download failed: HTTP ${res.status}`);
      const name = `${gen.id}-${i + 1}${extname(basename(new URL(o.url).pathname)) || ""}`;
      await writeFile(join(args[1], name), Buffer.from(await res.arrayBuffer()));
      saved.push(join(args[1], name));
    }
    print({ saved });
    break;
  }
  default:
    die("Commands: models, account, estimate, generate, get, list, upload, download. See the top of this file.", command ? 1 : 0);
}
