# Image Ledger

Every image dropped from a rebuilt deck, with the source slide it came from, so any of them can be restored. The originals in `Storyboarding/` are untouched and remain the recovery source.

**Method note.** Decks are rebuilt by unzipping the source `.pptx`, editing the slide XML, and rezipping. Surviving images are never decoded or re-encoded. They are copied through as bytes. This is verified per deck by comparing SHA-256 of every carried-over media part against the source.

---

## 02: Aspect Ratios

`2_AspectRatios.pptx` (47 slides) → `02_AspectRatios_REVISED.pptx` (35 slides)

**Media: 37 in source · 33 carried over · 33/33 byte-identical · 4 dropped**

### Dropped

| Media | Source slide | What was on it | Why |
|---|---|---|---|
| `image6.jpeg` | 2 | Opening image on "Storyboarding and Aspect Ratios" | The slide was a generic opener; its content folded into the new slide 2. No unique teaching value. |
| `image13.jpeg` | 12 | Disney influenced by Fleischer and McCay; Chaplin and Keaton | The Disney run compressed 4 slides → 2. The surviving slides carry the story department and Webb Smith's wall, which are the load-bearing beats. |
| `image27.jpeg` | 28 | Cinerama feature titles: *How the West Was Won*, *South Seas Adventure*, *Seven Wonders of the World* | Cinerama compressed 2 slides → 1. The surviving slide already carries six images. |
| `image28.jpeg` | 28 | As above | As above. |

### Rescued

Seven images lived only on slides that were cut. Rather than lose them, they were re-related to a surviving slide before cleanup: no copy, no re-encode, just a new relationship from a different slide.

| Media | Was on source slide | Now on | Placement |
|---|---|---|---|
| `image7.jpeg` | 3 (Lumière) | 2 (*Before There Was a Plan* | Beside Méliès, matched size) both are natively 1.778, so they read as a pair |
| `image14.png` | 13 (*Plane Crazy* story sketches) | 6: *Webb Smith Pins It to a Wall* | Beside the wall photo: the sketches, then the wall |
| `image17.jpeg` | 18 (Hitchcock) | 7: *Live Action Takes Notice* | Beside *Citizen Kane* |
| `image18.jpeg` | 19 (Bond) | 8: *Why the Industry Actually Adopted It* | Beside *Star Wars* / *Raiders* |
| `image31.jpeg` | 30 (*20,000 Leagues*) | 18: *CinemaScope (1953)* | With the CinemaScope screen diagram; both films are named on the slide |
| `image32.jpeg` | 30 (*Lady and the Tramp*) | 18: *CinemaScope (1953)* | As above |
| `image35.jpeg` | 33 (2.35:1 example) | 20: *The Two Ratios You'll Actually Use* | Stacked under the 1.85:1 example at equal width, so the two shapes compare directly |

**Net effect:** of the 11 images that the slide cuts would have orphaned, 7 were kept and 4 were dropped.

---

## 03: Fundamentals of the Shot

`3_Fundamentals_of_Shot.pptx` (53) → `03_Fundamentals_of_Shot_REVISED.pptx` (46)

**Media: 57 in source · 57 carried over · 57/57 byte-identical · 0 dropped**

Two images lived only on merged-away slides and were rescued:

| Media | Was on | Now on | Placement |
|---|---|---|---|
| `image49.gif` | 40 (crane in 3D) | 35: *Crane* | Beneath the live-action crane photo: the same move, free in 3D |
| `image51.jpeg` | 42 (pan across a landscape) | 36: *Pan* | Beneath the pan diagram |

## 04: From Script to Storyboard

`4_Script_to_StoryBoard.pptx` (36) → `04_Script_to_StoryBoard_REVISED.pptx` (36)

**Media: 28 in source · 28 carried over · 28/28 byte-identical · 0 dropped**

| Media | Was on | Now on | Placement |
|---|---|---|---|
| `image7.jpeg` | 5 (Fincher's *Fight Club* boards) | 7: *Break It Into Components* | Beside the Scorsese example, since the slide names both |
| `image10.png` | 8 (shooting script page) | 9: *What Gets Added* | Beside the existing still |

Slide 23 (*Expanding a Panel Into a Succession*) was **kept as its own slide** rather than merged into 22 as the spec proposed. It carries two unique images and distinct content.

## 06: Drawing in Perspective

`6_perspective.pptx` (37) → `06_Perspective_REVISED.pptx` (30)

**Media: 29 in source · 29 carried over · 29/29 byte-identical · 0 dropped**

| Media | Was on | Now on | Placement |
|---|---|---|---|
| `image5.jpeg` | 3 | 2: *Flat Surface, Dimensional World* | Right of the narrowed body column |
| `image15.png` | 16 (Dead Marshes) | 7: *Atmospheric Perspective* | Under the body text, with the two existing stills at left |
| `image22.jpeg` | 23 | 17: *Circles in Perspective* | Under the body text |
| `image17.jpeg` | 18–19 | 18: *Foreshortening* | Beside the pipe example |
| `image26.jpeg` | 30 (lens comparison) | 23: *Lenses Tell the Story* | Beside the *Orient Express* still |

## 08: Continuity, split into 08a and 08b

`8_Continuity.pptx` (45) → `08a_Continuity_The_Rules.pptx` (24) + `08b_Continuity_The_Cut.pptx` (22)

**Media: 29 in source · 29 carried across the two files · 29/29 byte-identical · 0 dropped**

The split means each half carries only the media its own content needs: 20 parts in 08a, 14 in 08b, overlapping on the shared ones. **Verified as a union:** every source image appears in at least one of the two files.

| Media | Was on | Now on | Placement |
|---|---|---|---|
| `image6.png` | 6 (compressing a baseball game) | 08a slide 4: *Film Time Is Not Real Time* | Right of the body text |
| `image12.jpeg` | 18 (third person enters) | 08a slide 12: *Crossing It Legally: Move a Character* | Beside the existing still |
| `image7.jpeg` | 8 (2001 bone-to-spacecraft) | **08b** slide 18: *The Graphic Match* | Also retained on 08a slide 5, since both halves reference the cut |

---

## Totals

| Deck | Slides | Media carried | Byte-identical | Dropped |
|---|---|---|---|---|
| 02 Aspect Ratios | 47 → 35 | 33 / 37 | 33/33 | 4 |
| 03 Fundamentals | 53 → 46 | 57 / 57 | 57/57 | 0 |
| 04 Script to Storyboard | 36 → 36 | 28 / 28 | 28/28 | 0 |
| 06 Perspective | 37 → 30 | 29 / 29 | 29/29 | 0 |
| 08a + 08b Continuity | 45 → 24 + 22 | 29 / 29 | 29/29 | 0 |

**Four images dropped in total, all from Deck 02, all listed above.** Every other source image survives, byte-for-byte. Every output slide carries a speaker-notes page.
