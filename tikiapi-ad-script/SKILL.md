---
name: tikiapi-ad-script
description: >-
  Write a short, funny vertical video ad script (Reels, TikTok, Shorts, 15–36 s) with one idea that anyone, even a
  child, gets on first watch, then test it on four simulated viewers before anything is generated. Use whenever someone
  asks for an ad, promo, commercial, UGC skit, hook ideas or a narrator script, wants an existing script punched up, or
  is about to generate frames or clips for an ad that has no approved script yet.
license: MIT
---

# TikiAPI: ad script

Scripts fail in the same few ways: two ideas fighting, a joke that needs explaining, a narrator line that means
nothing without the picture, a number nobody can check, frames paid for before anyone agreed on the story. Each step
below guards against one of them. Nothing here costs money; the gate at the end protects what comes next.

## 1. Brief: one idea

Five lines:
- **Message:** one sentence a child could repeat. "With a subscription one video costs $12; here it costs $2.50."
- **Proof:** every number with its source and date. Never invent one: leave a marked gap and ask.
- **Viewer:** one person in one moment, not a demographic.
- **Action:** the one thing they should do.
- **Must-haves:** length, format, language, cast, look, what is forbidden (real brands, real people, rivals' names).

If the message would still work pasted onto a rival's ad, sharpen it.

## 2. Premises

8–12 one-line jokes across the engines in [comedy-engines](references/comedy-engines.md). Keep the 2–3 that pass:
- **The child test:** a 7-year-old can say what happened and why it's funny.
- **The mute test:** it works with the sound off.
- **The product is the punchline**, not a pitch bolted on after a joke.
- **Producible:** 2–3 characters, few places, no fiddly hands or crowds, no words inside the generated pictures.

A character with feelings beats a comparison: a money-eating monster that sulks off with a suitcase won every test
viewer; two people comparing prices bored them.

## 3. The beat table

| # | Time | Picture | Narrator line | On-screen text |
|---|---|---|---|---|

The rules, each learnt on a real ad ([beat-table](references/beat-table.md) has the reasons and an example):
- **One idea per beat, 2.5–3.5 s each.** About 2.5 spoken words a second. Too long? Cut words; never speed up the voice.
- **The hook is action in the first second**, from the first frame. Two still frames in a row lose the scroller.
- **Characters by role, not by name:** "this creator", "her subscription", "her friend". A name is one more thing to
  remember and tells the viewer nothing.
- **Every line makes sense by ear:** name things; never "this" or "it" without its noun. Say "AI video" once at the
  start if the product is technical; spell numbers the way people say them.
- **Show the maths:** "$49 ÷ 4 videos =" then the stamp "$12 A VIDEO". The viewer believes the sum they can see.
- **Props are physically logical:** what a line counts, the picture shows, countable, each tagged ("30 s" on each reel).
- **One text layer per moment:** a caption, a name card or a stamp, never two at once.
- **The price once in speech;** the end card carries the rest. The old price struck through next to the new one.
- **Honest numbers:** compare like with like; a launch price says so in readable text, not small print.

Add one line on what makes it funny and one on the riskiest beat to produce.

## 4. Audience room

Run the `tikiapi-audience` skill on the table: a kid of 8, a muted viewer, an audio-only listener and a skeptic, each
given only what that viewer gets. Fix the cause they name, at most two rounds; if a premise still fails, take the next.

## 5. Show and stop

Show the table, one line per viewer, the sources for every number and a rough cost (frames × price, clips × price,
from `list_models`). Then stop and wait for a clear yes to this exact text. No frames, no "one test clip". After the
yes, the `tikiapi-ad-video` skill takes it from storyboard to cut.
