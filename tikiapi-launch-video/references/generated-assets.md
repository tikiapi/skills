# Generated pieces (the generated path)

Every piece goes through the `tikiapi-generate` skill's rules: the key from `TIKIAPI_KEY`, never printed; models,
limits and prices from `list_models` only; the person's go on the total before the first order; one piece at a time;
a slow order is waited for, never placed twice. Model names below are examples of what is on sale today: check the
list and use what it offers.

## The usual set

| Piece | What for | Example model | Typical fields |
|---|---|---|---|
| Music bed | The whole video's music; its beat sets the cut | Suno V6 | `instrumental: true`, `style`, `duration` |
| Hook or world shot | The first two seconds, or the world the product lives in | Seedance 2.5, opening on a frame | `image_mode: "first_frame"`, `duration`, `resolution`, `aspect_ratio` |
| Still frame | A shot that needs no motion, or the first frame for a clip | Nano Banana Pro | `aspect_ratio`, `resolution` |
| Signature effect | One hit on the reveal or the logo | ElevenLabs Sound Effects v3 | `duration` |
| Voice line | The reveal or the punchline, said aloud | Fish Audio Drama 3 (with `speak`) | `text`, `voice` |

Most launch videos need the music and at most one or two of the others. Each piece must pass the test in the
creative laws: if it could be cut without losing meaning, cut it.

## Music first

1. `estimate_cost`, then `generate` with a music model: `instrumental: true`; `style` in words: the genre, a tempo
   in BPM, the instruments, the mood ("bright synth-pop, 120 BPM, punchy kick, plucky arps, confident"); `duration`
   the video's length in whole seconds, within the model's `min_seconds` and `max_seconds`.
2. Suno gives two takes an order (`outputs_per_order` in the list): send both, the person picks one.
3. Find the take's real beat before cutting: the asked tempo is a request, not a promise. Measure it (for example
   `aubio tempo music.mp3` or `librosa.beat.beat_track`, if installed; otherwise count the beats over a few bars),
   then re-time the storyboard so every cut lands on a beat of this take.
4. Trim or fade the take to the video's length in the mix (an `afade` out over the last second).

## A hook or world shot

1. A frame first, on an image model (Nano Banana Pro, or what the list offers): the video's aspect ratio, the
   product's palette in words, no text, invented people only. Show it; wait for a yes.
2. The clip, opening on that frame: `image_mode: "first_frame"`, the shortest `duration` the shot needs within the
   model's limits, the `resolution` the list sells. The prompt: one action, one camera move, the effects in
   `<angle brackets>`, then: "Start exactly from image 1 and keep everything in it unchanged. No speech, no voices,
   no music: only the sound effects described. No subtitles, no captions, no new text." For a fuller scene, the
   `tikiapi-director` skill writes the prompt.
3. Check it; trim the first 0.3 s in the edit and bring the blacks down if they came out grey.

## A signature effect

One order per effect with a sound-effect model: the sound described plainly ("a deep, soft whoosh ending in a bright
glassy chime"), `duration` just the effect's length within the model's range. Place it on a beat, under the music.

## A voice line

`speak` with a speech model from `list_models` (`model`; the first one when left out): `text` with one emotion cue in
brackets (`[confident, warm] Your repo, as a video, in one command.`), and `voice` as a free-text direction ("a young,
upbeat narrator with a light British accent"). Natural pace: if it's long, cut words. Clone a voice with
`reference_audio_url` only when the person owns it. Send the link; wait for a yes.

## Putting it together

**Locally (free), when ffmpeg is at hand.** Render the motion video with the generated clips and frames as layers,
then mix the sound: the music dips under the voice, the effect lands on its beat, the whole at -14 LUFS.

```bash
# work/silent.mp4: the silent render. Voice at 6.2 s, effect at 2.0 s, a 20-second video.
ffmpeg -i work/silent.mp4 -i music.mp3 -i voice.mp3 -i hit.mp3 -filter_complex \
  "[1:a]volume=0.6,afade=t=out:st=19:d=1[m];\
   [2:a]adelay=6200|6200,asplit=2[v][vkey];\
   [m][vkey]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=300[mduck];\
   [3:a]adelay=2000|2000,volume=0.7[h];\
   [mduck][v][h]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest work/render.mp4
```

Then bake the poster in as frame 0 (see build-and-deliver), which writes `launch.mp4`.

**With `edit_video` (paid per second of output), when there is no local editor.** `operation` `assemble` takes the
clips in order (each with `start` and `end` trims), one audio track (`audio_url`, `audio_volume`), the clips' own sound
(`clip_volume`), captions from `transcribe` and loudness at -14 LUFS. One audio track per pass, so with music and a
voice, assemble twice: first the clips with the music at a low `audio_volume`, then that cut with the voice as the
track. Effects that must land at exact moments are easier in the local mix. Check the tool's schema for the current
fields and limits.

## Cost line

Before the go, one line per piece and the total, for example: "music 1 order, hook clip 1 × N s, 1 effect, voice ~60
characters, no edit_video (local mix): $X in total". Every number from `estimate_cost` or `list_models`, never from
memory. After delivery, report the sum of `charged`.
