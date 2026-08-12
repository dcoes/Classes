# Image Ledger

Every image dropped from a rebuilt deck, with the source slide it came from, so any of them can be restored. The originals in `Storyboarding/` are untouched and remain the recovery source.

**Method note.** Decks are rebuilt by unzipping the source `.pptx`, editing the slide XML, and rezipping. Surviving images are never decoded or re-encoded — they are copied through as bytes. This is verified per deck by comparing SHA-256 of every carried-over media part against the source.

---

## 02 — Aspect Ratios

`2_AspectRatios.pptx` (47 slides) → `02_AspectRatios_REVISED.pptx` (35 slides)

**Media: 37 in source · 33 carried over · 33/33 byte-identical · 4 dropped**

### Dropped

| Media | Source slide | What was on it | Why |
|---|---|---|---|
| `image6.jpeg` | 2 | Opening image on "Storyboarding and Aspect Ratios" | The slide was a generic opener; its content folded into the new slide 2. No unique teaching value. |
| `image13.jpeg` | 12 | Disney influenced by Fleischer and McCay; Chaplin and Keaton | The Disney run compressed 4 slides → 2. The surviving slides carry the story department and Webb Smith's wall, which are the load-bearing beats. |
| `image27.jpeg` | 28 | Cinerama feature titles — *How the West Was Won*, *South Seas Adventure*, *Seven Wonders of the World* | Cinerama compressed 2 slides → 1. The surviving slide already carries six images. |
| `image28.jpeg` | 28 | As above | As above. |

### Rescued

Seven images lived only on slides that were cut. Rather than lose them, they were re-related to a surviving slide before cleanup — no copy, no re-encode, just a new relationship from a different slide.

| Media | Was on source slide | Now on | Placement |
|---|---|---|---|
| `image7.jpeg` | 3 (Lumière) | 2 — *Before There Was a Plan* | Beside Méliès, matched size — both are natively 1.778, so they read as a pair |
| `image14.png` | 13 (*Plane Crazy* story sketches) | 6 — *Webb Smith Pins It to a Wall* | Beside the wall photo: the sketches, then the wall |
| `image17.jpeg` | 18 (Hitchcock) | 7 — *Live Action Takes Notice* | Beside *Citizen Kane* |
| `image18.jpeg` | 19 (Bond) | 8 — *Why the Industry Actually Adopted It* | Beside *Star Wars* / *Raiders* |
| `image31.jpeg` | 30 (*20,000 Leagues*) | 18 — *CinemaScope (1953)* | With the CinemaScope screen diagram; both films are named on the slide |
| `image32.jpeg` | 30 (*Lady and the Tramp*) | 18 — *CinemaScope (1953)* | As above |
| `image35.jpeg` | 33 (2.35:1 example) | 20 — *The Two Ratios You'll Actually Use* | Stacked under the 1.85:1 example at equal width, so the two shapes compare directly |

**Net effect:** of the 11 images that the slide cuts would have orphaned, 7 were kept and 4 were dropped.
