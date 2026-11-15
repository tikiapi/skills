# Prompt templates

`IDENTITY` is the identity block from SKILL.md. Square brackets are yours to fill. All on `nano-banana-pro`, 2K,
at most 2 references.

## Face close-up (invented person)

References: none. Aspect 3:4.

```text
Photoreal portrait, head and shoulders, of [age, origin, face shape; eyes; skin with natural texture and fine pores;
hair colour, length and style], wearing [top]. Calm expression, eyes open, looking into the lens. Plain warm
light-grey studio background, soft even light. No text, no props, one person.
```

This is the only prompt that describes the face and hair.

## Face close-up (from a photo)

References: [the person's photo]. Aspect 3:4.

```text
IDENTITY Head and shoulders, plain warm light-grey studio background, soft even light, calm expression, eyes open,
looking into the lens. One person, no text.
```

## Full body

References: [face close-up]. Aspect 3:4 or 9:16.

```text
IDENTITY They wear [outfit, colours, materials, shoes]. Full body, head to toe, standing, arms relaxed, facing the
camera, plain warm light-grey studio background, soft even light. One person, no text.
```

## Cast photo (two people)

References: [A full body], [B full body]. Aspect 3:4.

```text
Reference photo of two people standing side by side, full body, facing the camera, plain warm light-grey studio
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
