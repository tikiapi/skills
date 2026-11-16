# Creative laws, tones and sound

> Adapted from brag-slim by Shunit Haviv Hakimi (https://github.com/latent-spaces/brag), MIT License,
> Copyright (c) 2026 Shunit Haviv Hakimi. Rewritten for TikiAPI; the notes on generated shots are ours. See NOTICE.

## The laws

- **Short.** 15–25 seconds; 18–22 is the sweet spot.
- **Clear to a stranger.** After one viewing, someone who has never heard of it knows what it does, who it is for and
  how to get it. Lead with that, not with how it is built.
- **The hook decides everything.** The first two seconds decide whether anyone keeps watching. Plan the hook first.
- **Show the thing.** Reuse the real product from the source: its UI, components, copy, images, videos and
  animations. Rebuild only what can't be reused. The working app doing its job beats a landing page describing it.
  Small illustrative text inside the UI is fine (a file name, a "Saved" toast); invented claims, numbers or
  testimonials are not. No abstract filler.
- **Placeholder people.** If the product shows data about people (messages, contacts, customers, health or money
  records), show the real interface with obviously made-up records, never rows from a database or an export. The
  video is made to be shared, and those people never agreed to be in it.
- **Specific.** It must feel made for this exact project: its own words and claims. Generic SaaS phrases ("streamline
  your workflow") are banned.
- **Readable.** Pace comes from motion and cuts, not from pulling text away early. A line meant to be read stays
  fully on screen and settled for about 0.3 s per word, counted from when the whole line is visible. Text that is
  only texture needn't be read.
- **Alive.** Things that appear one by one, simulated clicks, swipes and typing beat static slides.
- **Funny earns its place.** Humour comes from the project's own absurdity, not from trying.
- **Every frame postable.** Any frozen frame is worth sharing.
- **Clear of the platform's own buttons.** Reels, TikTok and Shorts draw the user name, caption, audio line and
  buttons over a vertical video. In `vertical`, keep everything meant to be read between about 13% and 80% of the
  height (y 250–1536 at 1080×1920) and out of the right 140 px of the lower half. Check one still with those bands
  drawn on it before the full render.

## Generated shots (our addition)

- A generated shot must do something the real UI can't: open on the world the product lives in, make the problem
  physical, or deliver a visual punchline. If it could be cut without losing meaning, cut it and save the money.
- Never generate the product's interface, logo or screenshots: models invent buttons and misspell names. Put the real
  UI on top of a generated shot in the edit (a phone or a laptop screen composited in) when the two must meet.
- No words inside generated pictures; all text is set in the edit, in the product's own fonts.
- Invented people only, never real, recognisable ones. The `tikiapi-character` skill keeps a person the same across
  shots.
- Match the product's palette in the generated shot's prompt (its exact colours in words), or the cut will jump.

## Tones

Presets are defaults; free-form direction ("a fake 2016 Series A launch") refines or replaces them.

| Tone | Feel | Pacing and transitions |
|---|---|---|
| `default` | Punchy, playful, clean | 4–5 scenes; soft transitions |
| `polished` | Serious, elegant, restrained | 3–4 scenes, long holds; soft fades |
| `yc-parody` | A deadpan startup launch, played straight | 4–5 scenes, one claim each; hard cuts |
| `chaotic` | Fast, loud, all caps | 6–8 scenes, some under 2 s; flash and zoom cuts |
| `deadpan` | Calm and dry; nothing is a joke | 3–4 scenes, big empty space; slow fades |
| `cinematic` | Trailer scale, epic claims | 4–5 scenes, big type; dramatic wipes |
| `app-store` | Clean feature cards | 4–6 scenes; smooth slides |

On the generated path, `cinematic` and `chaotic` gain most from a generated hook shot; `polished`, `deadpan` and
`app-store` usually need none.

## Sound

Write the music and the effects as one piece: effects in the music's key and space, blended in rather than laid on
top. Mix it like a real track: effects sit softly under the music, nothing harsh or spiky, repeated small sounds stay
in the background. Every part (drums, bass, melody, the effects on cuts) plays on one beat grid counted from the first
frame, so nothing drifts or flams.

A voice line, when there is one, sits on top: the music dips under it and comes back. One line is usually enough: the
reveal or the punchline, said the way people say it.
