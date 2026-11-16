# Prompt templates

`IDENTITY` is the identity block from SKILL.md. Square brackets are yours to fill. Today's usual model is
`nano-banana-pro` at 2K with at most 2 references; check `list_models` for what is on sale and its limits. The order
of the stages: face → details → outfit → sheet.

## 1. Face close-up (invented person)

References: none. Aspect 3:4.

```text
Photoreal portrait, head and shoulders, of [age, origin, face shape; eyes; skin with natural texture and fine pores;
hair colour, length and style], wearing [top]. Calm expression, eyes open, looking into the lens. Plain neutral
light-grey studio background, no colour cast, no gradient, soft even light. No text, no props, one person.
```

This is the only prompt that describes the face and hair.

## 1. Face close-up (from a photo)

References: [the person's photo]. Aspect 3:4.

```text
IDENTITY Head and shoulders, plain neutral light-grey studio background, no colour cast, soft even light, calm
expression, eyes open, looking into the lens. One person, no text.
```

## 2. Detail close-up

References: [face close-up]. Aspect 1:1 or 3:4. One detail per picture.

```text
IDENTITY A close-up of [their left hand resting on a table, the silver ring with a green stone on the ring finger /
the thin scar through the right eyebrow / their round tortoiseshell glasses, worn]. [What exactly the detail looks
like: material, colour, size, which side]. Plain neutral light-grey background, soft even light, sharp focus on the
detail. One person, no text.
```

Write which side the detail is on (left hand, right eyebrow) and keep that side in every later prompt that shows it.

## 3. Full body (one per outfit)

References: [face close-up]. Aspect 3:4 or 9:16.

```text
IDENTITY They wear [outfit, colours, materials, shoes]. Full body, head to toe, standing, arms relaxed, facing the
camera, plain neutral light-grey studio background, no colour cast, soft even light. One person, no text.
```

## 4. Character sheet (local, free)

Not an order: tile the approved files, so the person sees the whole character at once. Never a model reference.

```bash
# Face, full body and up to two details, all scaled to one height, side by side on grey
ffmpeg -i face.png -i body.png -i detail1.png -i detail2.png -filter_complex \
  "[0]scale=-2:1200[a];[1]scale=-2:1200[b];[2]scale=-2:1200[c];[3]scale=-2:1200[d];[a][b][c][d]hstack=inputs=4,pad=iw+64:ih+64:32:32:color=0x9a9a9a" \
  -frames:v 1 sheet.png
```

Fewer files: drop the inputs and set `hstack=inputs=` to the count. Add the name, the outfits and the notes in a
caption or next to the sheet in the story bible.

## Cast photo (two people)

References: [A full body], [B full body]. Aspect 3:4.

```text
Reference photo of two people standing side by side, full body, facing the camera, plain neutral light-grey studio
background, soft even light. Left: exactly the person from image 1, same face, hair and outfit. Right: exactly the
person from image 2, same face, hair and outfit. Both deadpan. No text.
```

## Scene frame

References: [face close-up] (+ [full body] or one prop). Aspect 9:16.

```text
IDENTITY They wear the outfit from image 2. [Framing: medium close-up from the chest up, the face large in frame].
[One action, one expression]. [The set in one clause]. [The look words, if any]. No text.
```

## Video, opening on the frame

`seedance-2.5`, `image_mode` `first_frame`, the approved frame as the only image.

```text
[One action]. Camera: [one move]. Start exactly from image 1 and keep everything in it unchanged: faces, hair,
clothes, the set and the light.
```
