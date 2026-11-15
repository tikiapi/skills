# Look DNA: the numbers and the words

CIELAB splits a pixel into lightness L (0 black to 100 white) and two colour axes, a (green ↔ red) and b
(blue ↔ yellow). The hue angle is the direction of (a, b), the chroma its length: how colourful.

## The numbers

| Number | Reads as | Typical values |
|---|---|---|
| Median L | How dark the frame is overall | Low-key crime film 15–30; daylight comedy 45–60 |
| Highlights share (L ≥ 60) | How much of the frame is bright | Low-key under 0.2 |
| Black point (L 1st percentile) | How deep the blacks are | Under 4: true blacks. Over 12: lifted, milky |
| Peak white (L 99th) | How hot the highlights are | Under 92: rolled off. Over 97: clipped |
| Hue angle | Which colour a zone leans to | 20–45 red and brick, 45–70 orange and cognac, 70–100 amber and gold, 100–135 olive, 135–200 green, 200–250 teal, 250–300 blue |
| Chroma | How colourful a zone is | Under 4 neutral, 4–12 slightly, 12–25 clearly, over 25 rich |

Measure shadows (L < 20), mids and highlights (L ≥ 60) apart: a look is often neutral shadows, warm mids and golden
highlights, and a single average hides that.

## From numbers to words

Write what a video model can follow, in this order: key, blacks, each zone's colour, highlights, texture.

```text
low-key, two-thirds of the frame in deep shadow; deep, true blacks, neutral, never green; mids warm cognac and brick
orange; highlights soft golden amber, rolled off; small pools of tungsten light, hard and from the side; fine 35mm grain
```

Name what must not happen when the model tends to drift: "never green or olive in the shadows", "never clipped".

## Comparing our frame

| Gap | Fix in the prompt | Fix in the edit |
|---|---|---|
| Our black point 3+ higher | "rich black shadows" | Contrast up, blacks crushed |
| Median L 6+ higher | "two-thirds of the frame in deep shadow", fewer lamps | Exposure down |
| A zone's hue 20°+ off | Name the zone's colour and what it must never be | A hue shift on that zone |
| A zone too grey | "saturated burgundy, cognac and gold" | Saturation up |

A clip that misses only on the black point or a white fade-in is fixed in the edit; one that misses the world (wrong
set, daylight instead of lamps) needs a new frame.
