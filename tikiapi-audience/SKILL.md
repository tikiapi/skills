---
name: tikiapi-audience
description: >-
  Test an ad script, a storyboard or a finished cut on four simulated cold viewers before money is spent on it: a kid
  of 8 who retells every shot and why, a muted viewer, an audio-only listener and a skeptic. Use whenever a script or
  cut needs checking, someone asks "will people get it?", "is it clear?", "test it on an audience", or before frames,
  clips or a final render of any ad or explainer.
license: MIT
---

# TikiAPI: audience room

You wrote the script, so you can't judge it cold. Four viewers can, if each gets only what that viewer would get and
never the brief, the intent or your explanation. Real viewers get no brief either.

## The four viewers

| Viewer | Gets | Must say |
|---|---|---|
| **Kid (8)** | The pictures and the lines, shot by shot | The story back, shot by shot, and *why* each thing happens; what's funny; any word or picture they didn't get |
| **Muted viewer** | The pictures and the on-screen text, with timings; no sound | The story and the offer; the second they would swipe away, and why |
| **Audio-only listener** | Only the narrator's lines (or the transcript of the cut) | The story and the price; every "this", "it" or name they can't place |
| **Skeptic** | Everything | The offer and price in one sentence; which claim smells fake or vague; what the catch is |

The prompts for each are in [personas](references/personas.md).

## Run it

1. Build each viewer's material from the beat table (or, for a cut, from its shot list with timings, the on-screen
   text, and the voice's transcript from `transcribe`).
2. Start one sub-agent per viewer, in parallel, if you can; otherwise answer as each in turn, starting fresh each
   time. Several scripts at once: label them A/B/C, one viewer judges all, then "which one would you send a friend?".
3. Collect a table: viewer | the story as they told it | where they got lost or would swipe | passed?

## It passes when

- the kid retells the story and the offer correctly, with the right cause for each shot;
- the muted viewer and the listener each get the offer **on their own**;
- the skeptic can state the offer and finds no false or vague claim.

For a cut, also check by eye: no moment with two text layers, no stamp or card over a face, no freeze frame on
closed eyes.

## Reading the verdicts

| Verdict | Fix |
|---|---|
| The kid gets the story wrong | The premise is too clever: simplify the picture, not the words |
| The kid can't say why something happens | A prop or an action isn't physically logical: show the cause |
| The muted viewer swipes in the first 3 s | The opening picture is weak or still: start on an action |
| The muted viewer misses the offer | The on-screen text doesn't carry it: one stamp with the price, the maths visible |
| The listener can't place "this" or "it" | Name the thing in the line |
| The listener misses the price or the name | Say it the way people say it; spell the brand for the voice |
| The skeptic can't state the offer | The end card or the payoff line is unclear |
| The skeptic smells a fake claim | Check it against the source; fix the claim or add the caveat in readable text |

Fix the cause, not the wording around it, and run the room again: at most two rounds. A premise that still fails is
dropped. Keep one line per viewer for the person you report to.
