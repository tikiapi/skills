# The location sheet and the prompts

## The sheet

```text
LOCATION: [name], [type of place], [era or style]
TIME AND WEATHER: [time of day], [season], [weather]
FLOOR PLAN (from the master camera at [where it stands], looking [which way]):
  - back wall: [what is on it]
  - left wall: [windows, doors, furniture]
  - right wall: [...]
  - floor and centre: [...]
  - behind the camera: [what a reverse angle will see]
ANCHORS (in every angle that faces them): [3–5 objects with their place on the plan]
MATERIALS AND PALETTE: [surfaces, textures, the main colours, the accent colour]
LIGHT:
  - key: [source] from [direction on the plan], [hard / soft], [about N K, warm / neutral / cool]
  - fill: [...]
  - practicals: [lamps, screens, signs], [colour temperature]
  - ambience: [sky, bounce], [colour temperature]
NEVER: [people in the empty plate, modern objects in a period set, readable brand names, ...]
```

A short example: "LOCATION: Mara's night kiosk, a tiny city newsstand, present day. TIME: 2 a.m., late autumn, light
rain. FLOOR PLAN, from the pavement looking in: back wall shelves of magazines, a small fridge bottom right; left side
a serving hatch with a fold-down counter; right side the door; behind the camera the wet street and a tram stop.
ANCHORS: the red fold-down counter, the round wall clock above the shelves, the hanging bare bulb. LIGHT: key the bare
bulb above the counter, hard, about 2700K; ambience cool street light about 7000K through the hatch, soft; the
fridge's cold white glow bottom right. NEVER: people in the plate, readable logos."

## Prompts

### Empty plate

```text
A wide, eye-level photograph of [the location in one sentence]. [Floor plan, as seen from this camera: what is on
the back, left and right]. [Anchors with their places]. [Materials and palette]. Light: [each source: direction,
quality, colour temperature]. No people, no figures, no silhouettes, no reflections of people. No readable text, no
logos. [The look words, if the project has them.]
```

### Characters in the scene

References: the plate, plus the person (their saved `character_id`, or their face close-up and full body). Name the
plate by its role ("the location image"); with `character_id` the server names the person.

```text
[Framing: medium shot from the waist up, her face large in frame]. [The person] stands [where on the floor plan],
facing [which way], [the pose the first action starts from], eyes open. The place is exactly the location image: the
same walls, objects, materials and light; nothing in it moves or changes. Light on her: [the key's direction as it
falls on her, its quality, its colour temperature], [which side of the face is in shadow]. [The look words]. No text.
```

For a first frame, add: "A sharp still, no motion blur" and keep the clip's aspect ratio.

### Angle set

One order per angle, the plate as the reference:

```text
The same place as the reference image, seen from [the camera's position on the floor plan], looking [direction]:
[the reverse angle / a close view of the counter / high from the corner]. [Lens: 24mm wide / 50mm / 85mm]. Visible
here: [the anchors this view faces, with their places in this frame]. Same walls, materials, objects and palette as
the reference; nothing added or removed. Light: [each source, with its side as seen from this camera]. No people.
No readable text.
```

A useful set: the master wide, the reverse, a close view of the main anchor, a high angle, a low angle from the
floor, and the view through the main window or door. Check each against the plate and the sheet; redo an angle that
moved an anchor to another wall.

### One-detail edit

The picture to change as the only reference:

```text
Change only this: [one concrete change: the clock shows ten past three instead of two / the bulb is switched off and
the kiosk is lit only by the street light]. Keep everything else in the image identical: the composition and camera,
every object and its place, the materials, the colours, the light and any people.
```

When the change alters the light (a lamp switched off), describe the new light fully and still lock everything else.
