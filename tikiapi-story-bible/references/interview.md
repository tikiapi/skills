# The interview

Ask a round in one message, three to five questions, each with a default the person can accept. After each round,
show what you wrote down in the bible's own words and ask "anything wrong or missing?". People answer better when
they correct a draft than when they fill a form.

## 1. The world

- Title, and the premise in one sentence. *Default: you propose one from what they said.*
- Genre and tone: two or three words ("cosy mystery, dry humour"). *Default: from the premise.*
- Who watches or reads, in one moment ("commuters on their phones, sound off").
- Format: vertical 9:16 episodes, wide films, a comic, ads; length of one episode.
- Language of lines and on-screen text.

## 2. Characters (one round per main character)

- Role in the story, in four words or fewer ("the night-kiosk owner").
- Age range and look. If a picture exists, the picture carries the face; the words carry only what a picture can't
  (build, posture, how they move).
- Outfits by situation ("work: green cardigan, red scarf; at home: grey hoodie"). One outfit per scene.
- Voice: who they sound like in words (age, accent, pace, texture) for the speech model's voice direction.
- Habits and tells: two physical habits ("taps the counter twice before answering").
- What they never do or wear.
- Relations to the others, one line each.

## 3. Places (one round per main place)

The `tikiapi-location` sheet: name, type, time and weather, floor plan from the main camera, three to five anchors,
materials and palette, the light rig (each source: direction, quality, colour temperature), what is never there.

## 4. Rules

- How the world works where it differs from ours (technology, magic, money, physics).
- What never happens on screen (violence level, brands, real people, topics).
- Running jokes, recurring objects, catchphrases.
- Brand rules if it is a brand world: colours, the logo's use, words to avoid.

## 5. Look

- Palette: three to five colours, with where they appear (walls, clothes, light).
- Light and time: mostly night, golden hour, flat office light.
- Lens and camera: wide and close, long lens, handheld, locked-off.
- Texture: film grain, clean digital, animation style.
- A reference still or two. Measure them with `tikiapi-look` if the person wants exact colour; never use stills
  with real actors' faces as references.

## 6. Sound

- A voice direction per speaking character (for `speak`), and any voice they own the rights to clone.
- The music's style in words: genre, tempo, instruments, mood (for a music model from `list_models`).
- Two or three signature sounds (a kiosk bell, a tram's brakes).

## 7. Timeline

- The events in order, one line each, with an episode number or date.
- After each event: who is where, what changed in how they look (an injury, a haircut, a new coat), which objects
  changed (a broken sign stays broken), who knows what.
- The current state: where the story stands now.

## Defaults when the person is unsure

Propose, don't ask twice: a palette from the genre, a light rig from the time of day, outfits from the role. Mark
proposed facts with "(proposed)" in the summary, and drop the mark when the person confirms.
