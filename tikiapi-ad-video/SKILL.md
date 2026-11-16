---
name: tikiapi-ad-video
description: >-
  Make a vertical video ad end to end with TikiAPI: script and audience test, cast, storyboard frames, Seedance clips,
  narrator voice, word-timed captions and the assembled cut at -14 LUFS, with a stop for the person's go before any
  video is paid for. Use whenever someone wants a finished ad, promo, Reels or TikTok video, commercial or explainer
  made from an idea, a product or an approved script, or wants to continue such an ad from frames, clips or voice.
license: MIT
---

# TikiAPI: ad video, end to end

This is the pipeline that produced a 36-second ad in one day, with the mistakes it took to get there written in as
rules. Every step ends with something shown to the person and their yes. Money is spent on pictures from step 3, and
on video only after their go at step 5.

| Step | Output | Gate |
|---|---|---|
| 1. Script | Beat table, one idea | Audience room passes |
| 2. Approval | The table, four verdicts, a rough cost | **Yes to this exact script** |
| 3. Cast | A face close-up and a full body per character | Yes |
| 4. Frames | One first frame per beat, shown as a board | Yes (redo only the flagged ones) |
| 5. Cost | `estimate_cost` for every clip, one total | **Go for video spend** |
| 6. Clips | 4-second Seedance clips, one at a time | Each shown |
| 7. Voice and captions | Narrator take, word timestamps | Yes to the take |
| 8. Edit | The assembled cut | Audience room on the cut |
| 9. Delivery | Links | |

Calls follow the `tikiapi-generate` skill: the key from `TIKIAPI_KEY`, never printed; `list_models` before choosing;
results as links.

## 1–2. Script and approval

Use the `tikiapi-ad-script` skill, then the `tikiapi-audience` skill. The rules that matter most later:
- One idea per ad. Characters by role, not by name. Every narrator line makes sense by ear.
- One beat = one picture = one idea, 2.5–3.5 s. Never speed the voice up to fit; cut words.
- Show the maths on screen; every prop physically logical and countable.
- No words inside the generated pictures: all text goes on in the edit, so one picture track serves any language.

Stop and wait for a yes to this exact script before any picture is made.

## 3. Cast

Use the `tikiapi-character` skill: a face close-up and a full body per person, the identity block in every prompt,
never the hair in your own words, at most 2 references on `nano-banana-pro`, a cast photo for two people in one frame,
saved with `create_character`. Non-human characters (a monster, a mascot) get one clean front view on a plain
background first, then are used as a reference like a person.

## 4. Frames

One first frame per beat, 9:16, 2K. Rules and a prompt pattern: [frames](references/frames.md).
- Framing first, the room in one short clause; the look words at the end of every prompt.
- A beat that freezes in the edit needs open eyes in its frame.
- Stamps will sit at the top or bottom of the frame: keep faces out of those zones.
- Show all frames as one board. Redo only what the person flags.

## 5. Cost, then stop

`estimate_cost` for every clip (today `seedance-2.5`, `duration` 4, `resolution` 720p, `image_mode` `first_frame`,
one frame each; check `list_models` for the current model, its limits and its prices). Add the voice if `list_models`
prices it. Give the total in one line and **wait for the go**. No clip,
not even a test, before it.

## 6. Clips

One at a time, each shown before the next. The full method, adapted from the Seedance 2.5 Skill (CC BY 4.0):
[seedance-clips](references/seedance-clips.md).
- `seedance-2.5`, `image_mode` `first_frame` with the approved frame, `duration` 4, `resolution` 720p.
- The prompt: one action, one camera move, the sound effects in `<angle brackets>`, then the lock: "Start exactly from
  image 1 and keep everything in it unchanged… No speech, no dialogue, no voices, no music: only the sound effects
  described. No subtitles, no captions, no new text."
- `input_refused`: retry once (`run_again`); refused again, remake the frame.
- Still running is not failed: poll the same id, never order it again.
- Seedance can lift the blacks to grey and fade in from white in the first 0.3 s: fix in the edit, not with a redo.

## 7. Voice and captions

[voice-and-captions](references/voice-and-captions.md). `speak` with the narrator lines and a voice direction (who
speaks, one emotion cue per line), at natural pace; spell names for the voice only. Then `transcribe` the approved
take for word timestamps; the captions are built from them, one sentence at a time.

## 8. Edit

[edit](references/edit.md). `edit_video`, operation `assemble`: the clips in order, each trimmed past its first 0.3 s
with the blacks brought back down where they came out grey, the voice as the audio track, the subtitles burned in,
loudness -14 LUFS. `reframe` turns a 16:9 clip into 9:16. Cards, stamps and freeze frames, if the tool can't place
them, go to a local editor (Remotion or ffmpeg recipes in the reference) or to a list for a human editor.
- One text layer at a time: subtitles step aside under a card or a stamp. Stamps never cover faces.
- Freeze frames only on open eyes.

Run the audience room on the cut: the muted viewer gets the shot list with the on-screen text, the listener only the
transcript. Fix and re-run once if needed.

## 9. Delivery

Send links, never files: the cut, and the clips and voice if asked. Say what it cost in total (sum of `charged`).
