# Voice and captions

## Lines by ear

Before any voice is made, read the lines as a listener who sees nothing:
- Name the thing in every line. "This is her subscription", not "This is it".
- Introduce people by role: "This creator", "Her friend".
- Say numbers the way people say them: "forty-nine dollars a month", "two dollars fifty".
- Say the category once early ("makes AI videos"), and explain a product name once ("Seedance AI").
- Spell names for the voice only, never in the captions: "Seed-dance", "Tiki A-P-I dot com".

## The take

`speak` with:
- **text** (MCP `speak`; `input` in REST `POST /v1/audio/speech`): the lines, in order;
- **a voice direction:** who speaks, then one emotion cue per line, for example
  `[a young British woman with a low, husky, confident voice, cinematic like a movie trailer narrator]
  [slow, intriguing] This creator makes AI videos. [dark, tense] This is her subscription. [building tension] She feeds
  it forty-nine dollars a month! … [bold, final] Tiki A-P-I dot com.`;
- **reference_audio_url** only for a voice the person owns or has the rights to.

Natural pace. If the take runs longer than the cut, cut words or give the cut more time; never speed the voice up.
Make one take, send the link, and wait for a yes before captions.

## Captions

`transcribe` the approved take for word timestamps, then:
- one sentence on screen at a time, at most two lines; it appears with its first word and stays until the next;
- names spelled right (fix "Seed dance" → "Seedance");
- large (about 72 px on a 1080×1920 frame), white with a dark outline, uppercase reads well;
- above the bottom fifth of the frame, where the app's buttons and caption sit;
- **one text layer at a time:** a caption steps aside while a name card or a stamp is on screen.

An SRT is enough for `edit_video` and for most editors:

```text
1
00:00:00,500 --> 00:00:02,300
THIS CREATOR MAKES AI VIDEOS.
```

## Timing the cut to the voice

Put the voice in first (start it about 0.5 s in), then place every cut and stamp on its word: the stamp "$49 / MONTH"
lands on "forty-nine", the coin lands on our price as the voice says it. A beat is as long as its line plus a breath, 2.5–3.5 s.
