# Remaining Decks: 07 Lighting · 02 Aspect Ratios · 08a/08b Continuity · 04 Script to Storyboard · 03 Fundamentals of the Shot · 06 Perspective
*Slide-level outlines. Each entry: slide title · on-slide content · what you say.*
*Companion to `decks-revised-01-05-12.md` and `decks-new-09-10-11.md`. Same format, same conventions.*

---

## How to read this file

The other two spec files describe decks that were either already rebuilt (01, 05, 12) or built from nothing (09, 10, 11). This one describes **surgery on six existing decks** that are sitting in the parent `Storyboarding/` folder. Every slide referenced by number below is a slide that exists today, and I have read all 260 of them.

**Order of work is by value, per PROJECT.md:** 07 → 02 → 08 → 04 → 03 → 06.

**Output convention:** edit the original `.pptx` in place, save to `NewLectures/` as `NN_Name_REVISED.pptx`. This is how 05 and 12 were made: the source deck's theme, media, and layouts are preserved and slides are deleted, inserted, or rewritten around them. Deck 12 went 40→41 slides with the scanning block (source 22–32) cut and the prep pipeline inserted; every surviving slide kept its images. Do the same here. Do not generate decks from scratch: the media in these files is largely film stills the instructor sourced, and regenerating loses them.

**Theme note.** Decks 04, 06, 07, 08 already carry "Game Design Theme" (Garamond; accents `D9B247` / `CC702D` / `B53A31`), matching 05 and 12. Decks 02 and 03 carry "Organic" with Century Gothic. Deck 01 was rebuilt *without* converting its theme, so precedent says leave 02 and 03 on Organic rather than restyle: a theme conversion re-flows every text box in a 47- and a 53-slide deck and buys nothing pedagogically. Flagged, not recommended.

**Diagrams** are native vector shapes on the theme palette (see `05_Composition_REVISED.pptx` slides 17–19 for the pattern). **Copyrighted stills** stay as `[ADD IMAGE:...]` markers in speaker notes. **Speaker notes** are prose in spoken register.

---

## ⚠️ Before you delete anything: progressive builds

Several slide pairs and triples in these decks have **identical on-slide text but different speaker notes**. Those are almost always animated progressive builds, the same slide revealed in stages, not accidental duplicates. Deleting them strips a reveal.

**Verify before deleting** (open the file, check for animation and for differing shape visibility):

| Deck | Slides | Assessment |
|---|---|---|
| 06 | 35, 36, 37 "In Conclusion" | Three different notes pages. **Almost certainly a build.** Keep the slide, merge the notes. |
| 06 | 13, 14 "Three Point perspective" | Different notes, continuous prose across the pair. **Build.** Merge. |
| 03 | 30, 31 "Canted Shot" | **Identical notes.** Genuine duplicate: safe to delete one. |
| 03 | 47, 48 "zolly" | **Identical notes.** Genuine duplicate, and both carry the wrong title (see Deck 03 below). |
| 04 | 3, 4 "Getting Started" | Different notes (Scorsese vs. Fincher). **Build.** Merge into one slide with both examples. |
| 04 | 7, 8 "The Shooting Script" | Different notes. **Build.** Merge. |
| 07 | 30, 31 "Color" | Different notes, but both are inside the color block being cut to 4 slides anyway. Moot. |
| 08 | 12, 13 "The Line of Action" | Different notes. **Build.** Merge. |
| 08 | 26, 27 "Shot/Reverse Shot" | Different notes. **Build.** Merge. |
| 02 | 43–47 "In Summary" | Five slides, five different notes. **Build**: a summary revealed point by point. Compress to 2. |

---

## The four cross-deck obligations

Content left a rebuilt deck and currently lands nowhere. These are not optional.

1. **Screenplay format → Deck 04.** `decks-revised-01-05-12.md` line 13: slug lines, two-column format, and screenplay conventions were "moved out entirely to Deck 04." Deck 04 currently opens on the shooting script at slide 6 with no format primer at all. Deck 04 gains a new front section.
2. **Color → Deck 07, capped at ~4 slides.** Deck 05's spec drops color ("minus color, which moves to the lighting deck"); PROJECT.md §9 caps Deck 07's color theory at ~4 slides. Deck 07 currently spends 13 (slides 30–42). Nine come out.
3. **Deck 04's overhead diagram is load-bearing for Deck 10.** `decks-new-09-10-11.md` slide 9 calls back to it by name: *"remember the floor plan I said was underused?"* Deck 04 slides 19–21 must survive **and must actually say "underused" out loud**, or the callback lands on nothing.
4. **Deck 02's *Snow White* wall is load-bearing for Deck 11.** Deck 11 slide 3 is a direct callback to Webb Smith pinning sketches to a wall. Deck 02 slides 15–16 carry it. Keep, and sharpen into the pitch precedent. That wall *is* the origin of the pitch format.

---
---

# DECK 07: STORYTELLING THROUGH LIGHTING
**42 slides → target ~30 · Session 11 · Paired with EX6**

> **⚠️ Revised.** This deck was previously skipped and is now back in scope. Beyond the repairs below, it must carry the framing that the redesigned **EX6 Lighting Study** depends on. Three additions are load-bearing and are marked **[EX6]** in the outline:
>
> 1. **Identification before production.** EX6 Part 1 is eight stills read for five attributes, worth 12 points, with no making at all. That's how a student who can't draw earns marks on the actual objective. The lecture has to mirror that ordering: teach reading a lit frame *before* teaching making one.
> 2. **The three-value reduction, demoed live on three media.** Posterizing a photograph, a render and a drawing side by side is what makes EX6 gradeable across media, and seeing it is far more convincing than being told it.
> 3. **The medium list said out loud.** Drawing, phone photo with a desk lamp, 3D render, value study. All equal credit. This must be offered before anyone asks, not granted when they do.
>
> Also strengthen the **two dials** material (slide 11): high key vs. low contrast is the single most costly confusion in the assignment.

## What changed
- **Color: 13 slides → 4.** The entire color-theory block (30–42: color wheel, complementary, analogous, triadic, split-complementary, tetradic, square, warm, cool, meanings-of-color) is general design theory, not lighting, and not shot lighting. Four slides survive.
- **A defect PROJECT.md §10 doesn't list: the speaker notes desynchronize from slide 25 onward.** Each notes page from 25 to 39 belongs to the slide **three positions later**. Slide 25 "Backlighting" carries notes about realistic vs. dramatic lighting; slide 27 "Understanding Lighting" carries notes about color palettes; slide 30 "Color" carries notes about secondary colors. The trailing slide numbers left in the notes text (`30`, `31`, `32`…) confirm the offset. **Every notes page from 25 on must be re-matched to its slide before anything else is done to this deck.** This is why 07 is first: it's the cheapest deck to fix and the most broken.
- Slides 40–42 have **no speaker notes at all** (39 notes pages for 42 slides).
- Title-slide notes: `Sdg sdf adsf awer q4j`: delete.
- Slides 4 and 5 are a near-duplicate pair on 3D lighting. Merge.
- **The reframe:** this deck currently teaches lighting as a *cinematography* subject. It should teach lighting as a *drawing* subject. Every setup answers "and what do I actually put on the panel." Source slide 20 is the only slide that does this today. It becomes the spine.

---

### PART 1 WHY LIGHT (1–4)

**1 · Title**: Storytelling through Lighting
*(Delete the placeholder notes.)*

**2 · Nothing in the frame is an accident**
*(Source slide 2, kept.)* Light is one of the few elements you control completely, even in a rough board.
*Say: you've spent a week on where the camera goes. This is about what the camera sees when it gets there.*

**3 · Light became expressive by accident**
*(Source slide 3, kept and tightened.)* Early film needed light for exposure. Film noir turned a technical necessity into a language.
*Say: the entire vocabulary you're about to learn was invented by people solving a problem, not by people theorizing. That's usually how it goes.*

**4 · Live action vs. animation vs. 3D**
*(Source slides 4 + 5 merged.)* Physical instruments vs. virtual lights. Same principles, different labor.
*Say: and in both cases it starts at the board. You're the first person on the project who decides where the light comes from.*

---

### PART 1B: READ IT BEFORE YOU MAKE IT (4a–4c) ← **new [EX6]**
> Placed first on purpose. The assignment is ordered this way and the lecture has to match, or the ordering reads as an afterthought instead of an argument.

**4a · Five questions describe any lit frame ever made**
Key direction · high key or low key · contrast · hard or soft · motivated or stylized.
*Say: there is no sixth question. Answer these five and you've described the lighting of any shot in any film. Naming is the whole skill: the making is proving the naming was real.*

**4b · Run them live on four stills**
Four frames on screen, class answers all five attributes out loud, wrong answers welcome.
*[LIVE: let them argue about hard vs. soft. That's the one with a genuine grey zone.]*

**4c · You cannot direct light you can't name** ← the thesis slide
*Say: most student panels are flat because the value structure was never decided, and it was never decided because there was no vocabulary to decide it in. That's what today fixes, and it's why the first twelve points of your assignment involve no drawing at all.*

---

### PART 2 THE THREE-POINT SETUP (5–9)
*(Source 6–10, essentially intact. This section is good.)*

**5 · Three-point lighting**: key · fill · back. The minimum for expressive light. Standard since 1930s Hollywood.

**6 · Key light**: main source, defines the subject, usually 45° off camera. Creates the shadows that give texture.

**7 · Fill light**: indirect, softens the key's shadows, lowers contrast.

**8 · Backlight**: behind the subject, rims the edge, separates figure from ground.
*Say, and this is the connection: **backlight is figure/ground separation** from the composition lecture, done with a lamp instead of with value. Same problem. Same fix.*

**9 · Diagram: the setup from above** ← **new, vector**
A simple overhead diagram: subject, camera, and three light positions on the theme palette.
*Say: this is a floor plan, which is the same tool from Deck 04. Everything in this course is the same six tools.*

---

### PART 3 THE TWO DIALS (10–15)

**10 · High key / low key**
*(Source 11–13 compressed from three slides to one.)* High key: overall brightness, minimal shadow, comedy and sitcom and daylight. Low key: uneven, shadow-dominant, noir and thriller and horror.
*Say: this is a mood dial and it costs you nothing to turn. Decide it once for the sequence, before you draw a panel.*

**11 · Contrast is a separate dial** ← **strengthened [EX6]**
*(Source 14–16 compressed.)* High contrast: extremes, drama, thriller. Low contrast: all grays, flat, the viewer takes in the whole.
*Say: high key and high contrast are not the same thing, and students mix them up constantly. Brightness is one dial. The distance between your lightest and darkest is another.*

**11b · The 2×2** ← **new, vector [EX6]**
A four-cell table on the theme palette:

| | Low contrast | High contrast |
|---|---|---|
| **High level** | **High key**: sitcom, comedy, most animation | Noon desert. Interrogation. |
| **Low level** | Fog, dusk, rain (**low contrast, nowhere near high key** | **Low key**) noir, horror, thriller |

*Say: high key does not mean bright and low key does not mean dark. Both describe how much shadow there is. That's why your assignment asks for high key AND low contrast as separate items, if your two look the same, you're working one dial when there are two, and it costs you both.*
*[LIVE: put four frames up unlabelled and have the room place each one in a cell.]*

**12 · Light quality: hard vs. soft**
*(Source 17–19 compressed.)* Sunny day = directional = hard edges. Overcast = omnidirectional = soft, diffuse.

**13 · Representing light in a storyboard panel** ← **promoted, and this is now the spine**
*(Source slide 20, moved forward and expanded.)* Hard light: sharp-edged shadow shapes, a sharp tool. Soft light: gradient, blunt tool, no edge.
*Say: here's the actual takeaway. You are not lighting a set. You are drawing the **shadow shapes** that a light would make. Find the two or three biggest ones and put them down. That's the whole technique.*

**14 · Three values, again** ← **new, callback to Deck 05**
Black, mid-gray, white. That's enough to describe any lighting setup on a board.
*Say: you already know this from composition. Lighting doesn't add a fourth value. It tells you *where* the three go.*

**15 · The squint test on a lit panel** ← **new**
Same test, applied to light: squint at your panel. Is the lit thing the thing that matters?
*Say: if the brightest shape in your frame isn't the subject, you've lit the wrong thing, and no amount of rendering will save it.*

**15b · The three-value reduction, live, on three media** ← **new [EX6] · the demo that carries the assignment**
Posterize a **photograph**, a **3D render** and a **pencil drawing** to black / mid-grey / white, side by side on one slide.
*[LIVE: do this in front of them. Pre-load the three originals; posterize each one on screen.]*
*Say: look at what just happened. Three completely different things to make, and once you reduce them they're the same class of object: three shapes on a page. Which means the question "is the lit shape the subject, and is the light coming from where you said" doesn't care what made the image.*

**15c · So the medium is yours** ← **new [EX6] · say this before anyone raises a hand**
Draw it · photograph one object with a desk lamp · render it in 3D · value-study from your own photos. **All equal credit.**
*Say: this assignment assesses whether you can identify and control light. That is not the same skill as drawing, and grading it as though it were would be measuring the wrong thing. So pick whatever you can actually control a light source in. A phone and a desk lamp is a complete kit.*

**15d · The naming test** ← **new [EX6]**
Cover the labels. Hand the six reductions to a stranger. Can they sort them to the six setup names?
*Say: this is the silhouette test from week one, pointed at light instead of shape. Same test, same logic, same reason it's fair. It's independent of how well you draw. You can run it on yourself before you submit, and you should.*

---

### PART 4 DIRECTION OF LIGHT (16–21)
*(Source 21–26. Keep all six. This is the most directly usable section in the deck. Re-match the notes on 25 and 26, which currently carry the realistic/dramatic text.)*

**16 · Direction changes everything**: side · front · back · below · above. Each casts a different shadow pattern; the pattern is the mood.

**17 · Frontal**: flat, minimal shadow, minimal texture. Good for color relationships, bad for drama.

**18 · Side**: strong contrast, one side lit, one side dark. Reads as three-dimensional. *The half-lit face is the visual cliché for moral conflict and it is a cliché because it works.*

**19 · Backlight**: silhouette, separation, depth. *Callback: this is the silhouette test with a light behind it.*

**20 · Underlight**: bottom-lit, shadows inverted, immediately sinister. Horror and thriller.
*Say: this is the only lighting setup that reads as "wrong" to an audience with no film education at all, which is exactly why it's used.*

**21 · Which one is this shot?** ← **new, a decision slide**
Put up a beat from the City Park brief. Class picks a direction and defends it.
*Say: every concept in this course has to land on a decision. Here's the decision.*

---

### PART 5 REALISM VS. DRAMA (22–23)
*(Source 28–29, kept, with their correct notes restored: those notes are currently attached to slides 25 and 26.)*

**22 · Realistic lighting**: motivated by a visible source: window, candle, fire, streetlamp. Most productions, most of the time.
*Say: "motivated" is the word. If there's light on the face, the audience should be able to point at where it came from, or not care, which is a decision you make.*

**23 · Dramatic / stylized lighting**: German expressionism, *Caligari*, *Metropolis*. Light used for meaning, not plausibility.

---

### PART 6 COLOR, IN FOUR SLIDES (24–26)
> **The cut.** Source slides 30–42 (13 slides of color-wheel theory) collapse to three. PROJECT.md §9 caps this at ~4; three plus the warm/cool content inside them lands at the cap. Everything removed is general design theory available in any first-year design course and not specific to boarding a shot.

**24 · Temperature is the one that matters**
Warm (red/orange/yellow): energy, passion, day, safety, fire. Cool (blue/green/purple): calm, night, distance, isolation.
*(Source 40–41, merged.)*
*Say: on a black-and-white board, you can't use color. You can still **note** it. Write "cold" in the margin and the lighting artist knows what you meant.*

**25 · Complementary contrast is the one trick worth keeping**
*(Source 34, kept.)* Opposites on the wheel. Orange and teal is the industry default because skin is orange and everything else can be teal.
*Say: now that I've told you, you'll see it in every trailer for the rest of your life. Sorry.*

**26 · Color means different things to different rooms**
*(Source 42, compressed from the full list to a caution.)* Color association is cultural and personal, not universal.
*Say: white is death in some cultures and weddings in others. If your whole story beat rests on "red means danger," it rests on an assumption. Know that you're making it.*

**Cut entirely:** color wheel construction, primary/secondary/tertiary, analogous, triadic, split-complementary, tetradic, square schemes, and the full meanings-of-color list (source 30–33, 35–39, and the body of 42). Nine slides.

---

### PART 7 APPLY IT (27–28)

**27 · Exit exercise: light one panel three ways**
One panel, three lighting directions: side, back, under. Nothing else changes.
*Say: same drawing, three different scenes. Post them before you leave.*

**28 · The three tools you just used were one tool** ← **new [EX6]**
The **light plan** is Deck 04's floor plan with lamps on it. The **three-value reduction** is H3's composition discipline. The **naming test** is Session 1's silhouette test.
*Say: I keep telling you this course is six tools wearing different hats, and this is the session where you can see all three at once. When the floor plan turns up again in the games session, that'll be its fifth appearance. Noticing that is most of what I'm actually trying to teach you.*

---

## Assignment pairing

**EX6: Lighting Study**, 40 pts, assigned this session, due Session 13. Brief and rubric written.

- **Part 1 · The Read (12)**: eight stills, five attributes each. No making. Directly mirrors slides 4a–4c.
- **Part 2 · Six Setups (28)**: three-point, side, high key, low key, underlight, low contrast, **in any medium**, with a light plan and a three-value reduction each.

**Handout: H7: Lighting Reference Card.** Written. Open-book for Part 1, the way H2 is for the midterm. Carries the five questions, the 2×2, the six setups, direction, hard/soft, motivated/stylized, and the naming test.

**Eight stills needed before this session runs.** They're the answer key for 12 of the 40 points, so pick unambiguous cases. Listed in `INSTRUCTOR.md`'s pre-term checklist.

---
---

# DECK 02: ASPECT RATIOS (AND WHERE BOARDS CAME FROM)
**47 slides → target ~30 · second in the work order**

## What changed
- **The history block is 18 consecutive slides with the identical title "Early History of the Storyboard"** (source 3–20). The content is good and largely accurate; the presentation is punishing. Compressed to 8, with real titles.
- **"In Summary" ×5** (source 43–47) → 2.
- **Added: the ratios students actually deliver to.** This deck stops at 16:9 televisions. It has nothing on 2.39:1, nothing on vertical 9:16, nothing on 4:5, nothing on safe areas for phones. Students in this class are boarding for platforms this deck doesn't know exist. Three new slides.
- The **industry/consumer economics is kept**: PROJECT.md §9 is explicit that the TV-competition story is a deliberate takeaway, and it's the best material in the deck.
- The ***Snow White* wall is sharpened** into the pitch precedent, for Deck 11.
- **A1 (the template build assignment) is specified from this deck.** Source slides 41–42 are the arithmetic; they become an actual worked exercise instead of a formula on a wall.

### Defects confirmed
- Source slide 4 notes: Lumière → **"loom"** ("In stark contrast to the loom years was George Melies"). Fix.
- Source slide 2 carries the line *"Similar experiments by Edward Muybridge and others tied to photography"*, which is a **copy-paste from slide 3**, where it belongs. Slide 2 is about Disney and storyboards; Muybridge is not relevant to it. Delete from slide 2.
- ⚠️ **The McCay bet attribution is wrong.** Source slides 10 and its notes credit the "bring a dinosaur to life" wager to **Ed McMahon**. Ed McMahon was born in 1923; *Gertie the Dinosaur* is 1914. The bet is conventionally attributed to cartoonist **George McManus** (creator of *Bringing Up Father*), a colleague of McCay's. PROJECT.md §10 already flags this as needing verification: the date arithmetic settles it. Correct to McManus, or drop the name and keep the wager.
- Source slide 30 spells Cinemascope as **"Cinescope"** twice (on-slide and in notes). Also appears in the summary at source 45. Fix all three.

---

### PART 1, WHERE THE FORMAT CAME FROM (1–9)
> Compressed from 18 slides to 8. Every slide gets its own title.

**1 · Title**: Aspect Ratios: The Shape of the Frame

**2 · Before there was a storyboard**
Lumière (1895): recording. Méliès (1902, *A Trip to the Moon*): a magician who used film to *tell* something.
*(Source 3–4, merged. Fix "loom.")*
*Say: the split at the very beginning of cinema is documentation versus fiction, and the guy who invented movie storytelling was a stage magician. Hold that thought. You'll meet it again in the composition lecture.*

**3 · Directors sketching before there was a system**
Eisenstein sketched *Battleship Potemkin* (1925). DeMille used Dan Sayre Groesbeck for *The Ten Commandments* (1923).
*(Source 5–7, merged.)*

**4 · Animation had no scripts at all**
McCay and *Gertie the Dinosaur* (1914): 10,000 drawings, made on a bet, and an experiment in motion rather than a story with a beginning, middle, and end. The Fleischers ran a studio with **no script and no story department**: Dave Fleischer walked the room every morning collecting gags.
*(Source 8–11, merged. **Fix the McMahon/McManus attribution.**)*
*Say: that's the state of the art. A studio producing theatrical films with nothing written down anywhere.*

**5 · Disney watched live action and took notes**
Chaplin and Keaton: camera angle, movement, timing. *Plane Crazy* (1928) was built from story sketches that looked like a comic strip, with written action descriptions on separate pages.
*(Source 12–13, merged.)*

**6 · The story department**
Disney splits gag development from animation. Ted Sears heads the first story department, early 1930s.
*(Source 14.)*
*Say: this is the moment your job is invented. Somebody noticed that deciding what happens and drawing what happens are two different jobs.*

**7 · Webb Smith pins it to a wall** ← **load-bearing for Deck 11**
Too many sketches to hold in your head. Smith pins all of them, in order, beginning to end, and reworks the order until the continuity holds. First cartoon to use the method: *Three Little Pigs* (1933).
*(Source 15, kept and given its own slide.)*
*Say: notice what he actually invented. Not a drawing technique: a **way of seeing a sequence all at once, on a wall, so you can rearrange it.** That's still what a board is for. And when we get to the pitch session, the fact that this thing was invented as a wall you stand next to and talk through is going to matter.*

**8 · *Snow White* and the sequence you can perform** ← **load-bearing for Deck 11**
Thousands of sketches. Boards pinned up and the film acted out for the crew before a frame was animated.
*(Source 16, sharpened.)*
*Say: Disney stood in front of this wall and performed the entire film. That's the origin of the pitch, and you're going to do a version of it in week three.*

**9 · Live action catches on**
*Citizen Kane* (deep focus, complex lighting). Menzies on *Gone With the Wind*. Hitchcock, "storyboards come to life", and Saul Bass on the *Psycho* shower sequence, 75 camera setups. Syd Cain on the Bond films. *Star Wars* and *Raiders* for multi-unit coordination.
*(Source 17–20, merged into one.)*
*Say: the through-line is money. Boards spread because they're cheaper than fixing it later. That's still the argument.*

---

### PART 2 WHAT A RATIO IS (10–12)

**10 · The shape of the screen**
*(Source 21–22, merged.)* Width relative to height. 1.5:1 means 1.5 units of width for every 1 of height.
*Say: "This film has been modified from its original format." You've read that a thousand times. Today you find out what it means and why it's an insult.*

**11 · Diagram: the common ratios, to scale** ← **new, vector**
Nested rectangles on the theme palette: 1.33 · 1.37 · 1.78 · 1.85 · 2.39 · 9:16 vertical.
*Say: this is the only slide in the deck you need to remember. Everything else is why.*

**12 · Why the shape is the first decision**
*(Source 47, promoted from the summary to here.)* Before composition, before staging, before anything: the panel's shape.
*Say: you can't compose inside a frame you haven't drawn yet. This is why your first assignment is a template.*

---

### PART 3 THE ECONOMICS (13–19)
> **Kept deliberately.** PROJECT.md §9: the industry/consumer economics is the takeaway, not the trivia. This is the best-argued section in the original deck and it survives nearly intact.

**13 · 1.33:1**: the 35mm camera ratio, the early standard. *(Source 23.)*

**14 · 1.37:1, the Academy ratio**: widened the gate to fit an optical soundtrack. *Wizard of Oz*, *Gone With the Wind*, *Kane*, *Casablanca*. *(Source 24.)*
*Say: notice the ratio changed because of **sound**. The shape of every movie for twenty years was set by where they put the audio.*

**15 · The peak**: 1930s: ~95 million attending weekly. Families three or four times a week. *(Source 25.)*

**16 · Television takes the same shape**, and gives it away for free, at home. By the mid-50s: 45 million. By 1970: 90% of homes have a set. *(Source 25–26, merged.)*
*Say: this is the whole story. Television didn't compete with movies on content. It competed on **the identical rectangle**, at home, for nothing. Everything that happens to the shape of film for the next twenty years is a response to that.*

**17 · Cinerama (1952), 2.60:1**: three cameras, three projectors, a curved screen, and a roller coaster. Abandoned: too expensive to outfit theaters. *(Source 27–28, merged.)*

**18 · CinemaScope (1953) → Panavision**: anamorphic lens squeezes the image onto standard film and unsqueezes it in projection. 2.66:1 → 2.55:1; Panavision fixes the distortion problems and becomes the standard. **Fix the "Cinescope" misspelling.** *(Source 29–31, merged.)*

**19 · Where it settled**: 1.85:1 (most films: comedy, drama, animation) and 2.35/2.39:1 ("epic": *Gladiator*, *Lord of the Rings*, *Braveheart*). *(Source 32–33, merged.)*
*Say: and both of those numbers exist because of a television set in 1954.*

---

### PART 4 FITTING ONE SHAPE INTO ANOTHER (20–23)

**20 · The mismatch**: a 2.35 image on a 1.33 screen loses 45–50% of the frame. 1.85 loses about 25%. *(Source 34–35, merged.)*

**21 · Pan & Scan**: 20th Century Fox, early 1960s. Find the center of interest, crop to it, pan within the shot to follow the action. *(Source 36–38, merged.)*
*Say: a technician re-framed every shot in the movie. Every composition decision the director made, overridden by someone optimizing for a different rectangle. Directors hated this and they were right.*

**22 · Letterboxing**: preserve the ratio, accept the black bars. *(Source 39–40, merged.)*

**23 · 16:9 (1.78:1)**: the compromise ratio, adopted because it's close enough to 1.85 to lose almost nothing. *(Source 34, split out.)*
*Say: 16:9 is a negotiated settlement between two industries. It's not a natural shape. Nothing about it is natural.*

---

### PART 5 THE RATIOS YOU'LL ACTUALLY DELIVER (24–26) ← **entirely new**
> The deck currently ends at widescreen television. That was the state of the world roughly twenty-five years ago. Students in this room are boarding for phones.

**24 · Vertical**
9:16. Social, mobile, short-form. A real delivery format with real money behind it.
*Say: I'm not going to pretend this is the same craft problem. It isn't. You lose the horizontal, which means you lose almost every two-shot in the shot vocabulary and you gain stacking. Staging in vertical is a genuinely different problem, and someone in this room is going to be paid to solve it.*

**25 · Boarding for more than one ratio at once**
Protect-and-deliver: compose for 2.39, protect a 16:9 center extraction, protect a 1:1 or 4:5 crop for social.
*Say: this is now normal on commercial work. You will be asked to make one board that survives three crops. It's a compositional constraint, and it's exactly the headroom/lookroom slide from the composition deck with higher stakes.*

**26 · Safe areas**
Title-safe and action-safe, and why they still exist. *(Forward-links to Deck 10 slide 21, which reuses this for variable game displays.)*

---

### PART 6 BUILD YOUR TEMPLATE (27–30)
> Source slides 41–42 are the arithmetic for A1. They become the assignment.

**27 · The arithmetic**: pick a frame height, multiply by the ratio. 4″ × 1.85 = 7.4″ wide. Going the other way: width ÷ height = ratio. *(Source 41–42, merged.)*

**28 · Worked live**: do 1.85, 2.39, and 16:9 on the board with the class, at a 4″ height.
*Say: do this with me. Three numbers. If your template is the wrong shape, every panel you draw this month is the wrong shape.*

**29 · What a template needs**: panel at the correct ratio, panel number, shot number, space for action description, space for camera notation. *(Forward-links to Deck 04's final-boards guidelines.)*

**30 · Assignment: A1, Template Build**
Build it in Photoshop (or Photopea). Deliver the `.psd` and an export at the correct ratio.
*Say: fifty points for a rectangle with the right proportions. Take the free points and then never think about it again.*

---
---

# DECK 08: CONTINUITY, SPLIT INTO 08a AND 08b
**45 slides → 08a ~24 + 08b ~22 · third in the work order**

## Why the split
PROJECT.md §9 moves continuity **earlier, to Session 4, before City Park is assigned**, because City Park assesses continuity and staging under constraint, and it's unreasonable to grade students on rules they haven't been taught. But 45 slides is too much to front-load, and only half of it is needed before the assignment.

**08a: The Rules (Session 4, before City Park).** The 180° line, screen direction, shot/reverse, match on action, eyeline. Everything City Park is graded on.
**08b: The Cut (later, near the animatic).** Transitions, cutaways and cross-cutting, montage, and the graphic match. Everything that's about *editing rhythm*, which students can't feel until they've timed something.

The source deck's cutaway/cut-in/cross-cut material (33–35) sits on the boundary. It goes to **08b**: those are structural editing devices, not staging rules, and City Park doesn't need them.

## Defects confirmed
- Source slide 1 notes: `_`: an empty placeholder. Delete.
- Source slide 44 notes: **"Sergi eisenstein ablnd Dziga Vertov"** and **"Einstein's Battleship potemkin."** On-slide text also reads "Einstein's." Fix both to *Eisenstein*. This is PROJECT.md §10's item and it appears in two places, not one.
- Source slide 24 on-slide text reads **"Often called Right or Left and Left to Right movement"**: should be *"Right to Left."* Slide 25 has it correct. Fix 24.
- Source slides 12/13 and 26/27 are builds with differing notes: merge, don't delete blindly.
- Source slide 30 on-slide text: **"maintiaining"** → *maintaining*.

---
---

## DECK 08a CONTINUITY: THE RULES
**Target ~24 slides · Session 4, immediately before City Park is assigned**

### PART 1 THE INVISIBLE CRAFT (1–6)

**1 · Title**: Continuity: Making the Cut Disappear

**2 · What continuity editing is**
*(Source 2–3, merged.)* Splicing shots of different sizes and angles so the audience perceives one continuous action. A dozen cuts a minute, none of them noticed.
*Say: the best work in this entire discipline is work nobody sees. Get comfortable with that now.*

**3 · It's decided at the board, not in the edit**
*(Source 4.)* Pacing and transitions are established shot-by-shot at the planning phase.
*Say: an editor can only cut what you gave them. If your boards break the line, the break is in the film.*

**4 · Film time is not real time**
*(Source 5–6, merged.)* A baseball game is three hours; the scene is ninety seconds. Too fast and they don't follow; too slow and they're bored.

**5 · The most famous leap ever cut**
*(Source 8.)* *2001*: a bone thrown in the air becomes a spacecraft. Four million years in one cut.
*Say: and it works because of a **graphic match**: the shapes rhyme. We'll come back to this in 08b, and your composition lecture already showed you the same cut. Three sessions, same example, on purpose.*

**6 · The tools**
*(Source 10.)* Matching eyelines · matching action · the 180° rule · consistent screen direction.

---

### PART 2 THE LINE (7–13)
*(Source 11–19. This is the strongest section in the original deck. Keep almost all of it; merge the 12/13 build.)*

**7 · The line of action (the 180° rule)**
An imaginary line through the scene. Pick a side. Stay on it.

**8 · Diagram: the half-circle** ← **rebuild as vector**
Two figures, the line between them, the 180° arc of valid camera positions shaded on the theme palette.
*(Source 12–13 merged; replace the raster diagram with native shapes so it's editable.)*

**9 · What breaks when you cross it**
*(Source 14.)* One character ends up looking at the back of the other's head. The audience doesn't know it's a geometry error. They just stop believing the space.
*Say: they won't be able to tell you what's wrong. They'll say it "feels off." That's what a broken line feels like from the audience seat.*

**10 · Distant characters still have a line**
*(Source 15.)* Phone calls, two locations. Establish the imaginary line anyway so they face each other across the cut.

**11 · Crossing it legally: move the camera**
*(Source 16.)* A dolly or crane can cross the line as long as the move is continuous and the audience is carried across.

**12 · Crossing it legally: move a character**
*(Source 17–18, merged.)* A character crosses, or a third character enters and establishes a new sightline. Either way, a new line is established and now that's the line.

**13 · Crossing it on purpose**
*(Source 19.)* Disorientation as a choice: a chase, a search through a crowd.
*Say: the fine line here is between conveying a character's confusion and confusing your audience. You will not get the benefit of the doubt. If you break it deliberately, break it hard enough that nobody thinks it was an accident.*

---

### PART 3 SCREEN DIRECTION (14–18)
*(Source 20–25. Fix the "Right or Left" typo on source 24.)*

**14 · Screen direction is a promise**
*(Source 20.)* Which way a person moves or looks, held consistently across shots.

**15 · Neutral**: toward or away from camera. No left/right information at all, which makes it the safe cut between two contradicting directions.

**16 · Constant**: one direction only. The bus goes left to right for the whole sequence, or the audience thinks it turned around.

**17 · Contrasting**: enter one side, exit the other. Left-to-right on the way out, right-to-left on the way back. *(Source 24–25, merged, typo fixed.)*
*Say: this is how you tell an audience "he's going home" without a word of dialogue. Direction reversed means journey reversed. It's free and it's completely reliable.*

**18 · Two directions colliding**: opposing movement creates tension; the timing tightens and the framing closes as they converge.

---

### PART 4 THE THREE MATCHES (19–22)

**19 · Shot / reverse shot**
*(Source 26–27, merged.)* Establish the space, draw the line, then cut back and forth from one side of it.

**20 · Match on action**
*(Source 28.)* Everything at the end of shot A matches the start of shot B. Change the frame size noticeably and cut on the movement.
*Say: cutting on movement hides the cut. Cutting on stillness advertises it. That's most of the technique.*

**21 · Cut late enough to be understood**
*(Source 29.)* Cut only after the audience has taken in the information. Too fast and they miss it; too long and they're annoyed.
*Say: this is your first taste of timing, and you'll get the actual numbers in the animatic session.*

**22 · Eyeline match**
*(Source 30. Fix "maintiaining.")* Look off-screen and the audience expects to see what you saw. That expectation is a debt you have to pay in the next panel.
*Say: your composition lecture called an eyeline a compositional tool. Here it's a contract. Both are true.*

---

### PART 5 APPLY IT BEFORE YOU'RE GRADED ON IT (23–24)

**23 · The continuity checklist** ← **new; becomes handout H4**
Before you call a sequence done:
- Where is the line, and am I on one side of it?
- Does every character move in a consistent direction?
- Does each look off-screen get answered?
- Does the action at the end of each panel match the start of the next?
- If I crossed the line, did I earn it?

**24 · Exercise + City Park is assigned here**
Two panels that break the line. Fix them without redrawing: reposition the camera only.
*Say: City Park is assigned today, and this checklist is the rubric. There are no surprises in this course.*

---
---

## DECK 08b CONTINUITY: THE CUT
**Target ~22 slides · later in the term, paired with the animatic**

### PART 1 MANIPULATING TIME (1–7)

**1 · Title**: The Cut: Time, Space, and Rhythm

**2 · What you actually control**
*(Source 7 + 9, merged.)* Continuity compresses or stretches time. If it works, nobody sees the manipulation.

**3 · Cutaway**: related to the main action, not part of it. Buys you a time shift and adds context. *(Source 31.)*

**4 · What a cutaway is really for**: minor shifts in time, building tension, working inside the psychological space of an interaction. *(Source 32.)*

**5 · Cut-in**: narrows to a detail *inside* the main action. Dramatic emphasis. The bat meeting the ball. *(Source 33.)*
*Say: cutaway goes outside, cut-in goes closer. One buys time, one buys emphasis. Don't confuse them.*

**6 · Cross-cutting (parallel editing)**: two simultaneous actions intercut. Manipulates time and space at once. *(Source 34.)*

**7 · The Godfather baptism**: six minutes, and it's fast. *(Source 35.)*
*Say: a baptism and five murders. Neither sequence would work alone. The meaning is manufactured entirely by the intercutting, and not one shot had to be redrawn to make it.*

---

### PART 2 TRANSITIONS (8–13)
*(Source 36–41.)*

**8 · A transition is a narrative device**: it links two shots that differ in time, place, or focus, and it sets the pace.

**9 · Cut**: over 90% of all transitions. Unnoticed. Best at compressing time.
*Say: the default is correct almost always. If you're reaching for something else, have a reason.*

**10 · Dissolve**: overlapping images, any length. Time lapse or location change.

**11 · Fade**: passage of time; fade-in to open, fade-out to close. Not for present tense.

**12 · Wipe**: one image pushes another off. Popular in the 30s and 40s, dead after the war, resurrected by *Star Wars*.

**13 · Jump cut**: the deliberate opposite of continuity. Same background, character position jumps; or same framing, camera moved slightly.
*Say: a jump cut is a broken rule used on purpose. The difference between this and a mistake is entirely whether the audience believes you meant it.*

---

### PART 3 MONTAGE (14–17)
*(Source 42–44. **Fix "eisenstein ablnd" and "Einstein's": both instances.**)*

**14 · Juxtaposition creates meaning**: shots unrelated in time and space, placed together, produce a third thing that isn't in either.

**15 · The demonstration**: students languishing over an exam, cut with someone asleep in bed. Neither shot means anything. Together they mean something specific. *(Source 43.)*
*Say: nobody drew that meaning. The audience manufactured it in the gap between two panels. This is the closure slide from your composition lecture, operating across a cut instead of inside a frame.*

**16 · Soviet montage, 1920s**: Eisenstein and Vertov. The Odessa Steps from *Battleship Potemkin*: boots, a mother screaming, a pram. **(Spelling fixed.)**

**17 · Music video montage**: assembled to the song; the rhythm of the cut is the structure of the track. *(Source 42, split out.)*

---

### PART 4 COMPOSING ACROSS THE CUT (18–21) ← **new, and required**
> `decks-revised-01-05-12.md` Deck 05 slide 28 says explicitly: *"your continuity lecture will show you this again."* Today it doesn't. This section pays that debt.

**18 · The graphic match**
A shape in one shot echoed by a shape in the next. *2001*'s bone-to-spacecraft, again: third time this term.
*Say: I've now shown you this cut in three different sessions for three different reasons. Composition, continuity, and montage are the same subject looked at from three sides.*

**19 · Contrast across the cut**
Wide → close. Light → dark. Empty → full. If two consecutive panels have the same composition, the cut is invisible in the bad way.

**20 · Continuity of position**
Where the eye already is when your cut lands. Put the next subject there, or move it deliberately and make them travel.

**21 · Motif and visual echo**
*Callback to the Hero's Journey return slide in Deck 01.* Same frame, changed meaning.

---

### PART 5 CLOSE (22)

**22 · Summary + exercise**
*(Source 45, kept. It's a good closing slide.)* Continuity joins shots into dynamic meaning; done well, the audience sees an uninterrupted whole.
*Exercise: take three panels from your animatic and change only the transition between them. Report what changed.*

---
---

# DECK 04: FROM SCRIPT TO STORYBOARD
**36 slides → target ~34 · fourth in the work order**

## What changed
- **Gains the screenplay-format section moved out of Deck 01** (`decks-revised-01-05-12.md` line 13). Four new slides at the front. Deck 04 currently opens on the *shooting* script at source slide 6 with no format primer, which means students meet a slug line for the first time in an assignment.
- **Title-slide notes:** `Sdg sdf adsf awer q4j`: delete.
- **Builds merged:** source 3/4/5 (three "Getting Started," two with identical text) → 1 slide carrying both the Scorsese and Fincher examples. Source 7/8 → 1.
- **Source slide 26 has no speaker notes.** Write them.
- ⚠️ **Textbook dependencies must be removed.** Source slide 17 notes say *"As discussed in Chapter 3"*; source slide 22 notes say *"As discussed in Chapter 3 of your book."* PROJECT.md §1 is explicit: students do not buy the textbook, and all required content must live in these files. Rewrite both to reference **Deck 03** by name instead.
- **Source 19–21 (the overhead diagram) survive and gain the word "underused"**: Deck 10 slide 9 calls back to it. Also rebuild the floor-plan graphic as native vector shapes.
- **Source 31–32 survive verbatim.** "Fail Faster" and "be the solution, not the problem" are quoted back by Deck 11 slide 20.

---

### PART 1 READING A SCRIPT (1–7) ← **slides 2–5 are new, moved from Deck 01**

**1 · Title**: From Script to Storyboard *(delete placeholder notes)*

**2 · Script is where visual ideas start**
*(Source 2, kept.)* The language of film is visual; the script is the input, not the output.

**3 · Screenplay format: the page** ← **new, from Deck 01**
Courier 12, one page ≈ one minute, scene heading / action / character / dialogue.
*Say: the format looks arbitrary and it isn't. Every convention on this page exists so a producer can estimate a budget by weighing the script.*

**4 · Slug lines** ← **new, from Deck 01**
`INT. WAREHOUSE: NIGHT`. Interior or exterior, where, when.
*Say: three pieces of information, and two of them are yours to solve. "Night" is a lighting problem. "Warehouse" is a staging problem. The slug line is a work order.*

**5 · Action, dialogue, and what's not yours** ← **new, from Deck 01**
The script says what happens and what's said. It does not say what the shot is. That gap is your entire job.
*Say: if the script tells you the shot, you're reading a shooting script, and someone has already done the interesting part.*

**6 · The two-column / AV format** ← **new, from Deck 01**
Video left, audio right. Advertising, corporate, instructional, and a lot of game work.
*Say: you'll meet this the first time you take a commercial job, and it'll be the day of the job. So: here it is now.*

**7 · Break it into components**
*(Source 3 + 4 + 5, merged.)* Analyze the script and break it into pieces. Complexity depends on what the director needs: Scorsese blocks scenes in simple drawings; Fincher's boards for *Fight Club* are exhaustive.
*Say: both of those are correct. Match the document to the person reading it.*

---

### PART 2 THE SHOOTING SCRIPT AND THE SHOT LIST (8–11)

**8 · The shooting script**
*(Source 6.)* The green-lit, locked screenplay. The director breaks it down.

**9 · What gets added**
*(Source 7 + 8, merged.)* Camera angles · framing · lighting notation · character blocking · scene numbers. Nothing specified beyond the resources of the production.
*Say: last part matters. A shot you can't afford is not a shot; it's a note.*

**10 · The shot list**
*(Source 9 + 10, merged.)* Framing (distance to subject) · angle (camera relative to subject) · script description (where this shot sits in the screenplay).

**11 · The shot list is a document you'll be handed**
*Say: on most jobs somebody else writes this and you board from it. On the good jobs you're in the room while it's written. Being useful in that room is the difference.*

---

### PART 3 CHOOSING THE SHOT (12–18)
*(Source 11–18, kept nearly intact. This is the applied half of Deck 03 and it earns its place. **Rewrite the two "Chapter 3" notes references to point at Deck 03.**)*

**12 · Practical, aesthetic, psychological**: the three filters. *Ferris Bueller* talks to camera, so the shot is frontal. *(Source 11.)*

**13 · Over-the-shoulder = point of view** *(Source 12.)*

**14 · Establishing shot = orientation**: required any time the location changes. *(Source 13.)*

**15 · The bomb under the car** *(Source 14–15, merged.)* The same scene opened three ways: wide first, or close on the bomb first, or on the villain first.
*Say: three legitimate choices, three different films. Nothing about the script changed.*

**16 · Withholding is a tool** *(Source 16.)* Open close, and the audience asks where, who, and why. But you still owe them an establishing shot before they get lost.

**17 · Framing carries emotion** *(Source 17. **Fix the "Chapter 3" reference → "Deck 03."**)*

**18 · *Psycho*, the shower** *(Source 18.)* Subjective shots of a woman comfortable and unobserved; the POV is interrupted by the curtain pulling back.
*Say: the horror is structural. He gave you her point of view and then took it away from you at the same moment he took it from her.*

---

### PART 4 THE FLOOR PLAN (19–22) ← **load-bearing for Deck 10**

**19 · The overhead diagram**
*(Source 19.)* Camera placement and character movement, seen from above. Catches crossed lines and mismatched eyelines before you draw anything.
*Say, and say this exact thing, because a later session calls back to it: **this is the most underused tool in the discipline.** Nobody makes you do it. Everybody who does it has fewer problems.*

**20 · Icons** *(Source 20. Rebuild as vector.)* Camera as a "V" with a line through it; characters as circles. It's a map key.

**21 · Numbering** *(Source 21.)* Each camera position drawn and numbered by shot. Multiple cameras get their own labels.

**22 · Movement on the page** *(Source 22 + 23, merged. **Fix "Chapter 3 of your book" → "Deck 03."**)* Directional arrows; and expanding one panel into a connected succession of frames to show a move's start and end.

---

### PART 5 THE PROCESS (23–30)

**23 · The chain** *(Source 24.)* Read script → meet director → research → thumbnails → rough → approval → final.
*Say: this chain is also your grade. Every milestone on it is a graded submission, and skipping one caps the assignment. That's not an administrative preference: the process is what I'm assessing.*

**24 · Read it first** *(Source 25.)* Thumbnails and notes in the margins, before the meeting.

**25 · Do your homework before the meeting** *(Source 26. **Write the missing speaker notes.**)*

**26 · Questions to bring** *(Source 27, kept. It's a strong slide.)* Emotional goal · character personalities · overall mood · mood per scene · dominant colors · how the action unfolds · who's in charge of each scene · how you want the audience to feel.
*Say: that last one is the one that matters, and it's the first line of your final project brief.*

**27 · Thumbnails** *(Source 28.)* Small, rough, fast. A note-taking tool as much as a drawing tool.

**28 · Research** *(Source 29.)* You will be asked to draw things you've never seen. Build a reference collection now.

**29 · Roughs** *(Source 30.)* First full-size sketches. Block action, dialogue, characters; establish continuity. Submitted for approval.

**30 · Fail faster** *(Source 31, verbatim.)* There will be problems. Find them early. There is no such thing as a dumb question, if you've done the homework and still don't understand the vision, ask.

---

### PART 6 PROFESSIONALISM (31–34)

**31 · Be the solution, not the problem** *(Source 32, verbatim: Deck 11 slide 20 quotes this back.)*
Rough sketches don't have to be perfect; they have to be understandable. You were given a problem to solve. Solve it. Ask questions to understand the vision: don't ask for the solution.

**32 · It's their vision** *(Source 33.)* Make sure you understand it. That's who you're trying to satisfy.

**33 · Final board guidelines** *(Source 34 + 35, merged.)* Correct aspect ratio · panel numbered to the screenplay scene · shot number · camera angle and action described beneath · directional arrows wherever there's movement.
*Say: this is the spec for every board you hand me for the rest of the term.*

**34 · Summary** *(Source 36, kept.)* The process requires research. Understand angles, framing, and movement, and how they fit. Understand the story. Ask questions: after you've done the homework. Watch things critically.

---
---

# DECK 03: FUNDAMENTALS OF THE SHOT
**53 slides → target ~40 · fifth in the work order**

## What changed
- **This deck owns the shot taxonomy** (CURRICULUM.md boundary table). It is not allowed to shrink much, and the duplication flagged in Acting for Animation slides 32–41 gets resolved in favor of *this* deck. Handle with care.
- **The titling is the main defect.** Twelve consecutive slides are titled `CAMERA ANGLES` and ten are titled `CAMERA MOVEMENT TYPES`. The actual name of each shot is buried in a text box in the corner ("High Angle Shot," "Crane Shot," "Three Quarter Shot"). **Promote the buried label to the slide title.** This is mechanical, it's the single highest-value change in the deck, and it makes the whole thing navigable and searchable for the midterm.
- **Genuine duplicates:** source 30/31 (Canted) and 47/48 (zolly) have identical text *and* identical notes. Delete one of each.
- ⚠️ **Source 47 and 48 carry the wrong title.** Both are labeled `Steadycam® Shot` while the content and notes are about the **zolly** (dolly + zoom, Hitchcock, the *Jaws* beach shot). The Steadicam is source 46. Retitle to "Zolly / Dolly Zoom."
- ⚠️ **Source 43 says a dolly "Zooms in, to end at Position B."** A dolly does not zoom. That's the distinction source 45 spends a whole slide making. Rewrite to "Camera travels from A to B."
- Source 27 on-slide and in notes: **"one acter is positioned"** → *character*.
- Source slides 1, 16, 19 have **no speaker notes**. Write them.
- **Added:** a shot-selection decision gate, and the abbreviations students actually need for the midterm.

---

### PART 1 THE UNITS (1–7)
*(Source 1–9, largely intact.)*

**1 · Title**: Fundamentals of the Shot

**2 · Shot · scene · sequence** *(Source 2, kept as the roadmap.)*

**3 · Shot**: one continuous view from one perspective. Camera on, camera off. New setup = new shot. *(Source 3.)*

**4 · Scene**: shots that share a location. *(Source 4.)*

**5 · Sequence**: scenes that share a dramatic purpose. *(Source 5.)*

**6 · About 1,200 shots in a feature** *(Source 6.)*
*Say: twelve hundred decisions. You are not going to make each one from scratch. That's what a vocabulary is for. It's a set of pre-solved problems so you can spend your judgment on the ten shots that matter.*

**7 · What the director decides** *(Source 7 + 8 + 9, merged.)* Best viewpoint: the most interesting *and* the most clear. Mood. Central idea. Then: framing, angle, movement.
*Say: "show, don't tell" again. Clarity first. Interest second. When they conflict, clarity wins, and that's the standard I grade against.*

---

### PART 2 WHAT SHAPES THE CHOICE (8–10)

**8 · Style of the project** *(Source 10.)* Drama: slower, closer. Action: wider, more movement.

**9 · Screen size** *(Source 11.)* Commercials, games, and industrial video played small; features played large. Frame closer for the small screen.
*Say: this is the same argument as vertical video from the aspect ratio session. The delivery size changes the shot. It always has.*

**10 · The default progression** *(Source 12 + 13, merged.)* Establish wide → move to medium → close-up for personality → back out to reorient.
*Say: this is a formula, and formulas are fine to start from and embarrassing to stay in. Learn it so you can notice when you're using it.*

---

### PART 3 SHOT SIZE (11–19)
*(Source 14–24. **Retitle each to its actual name.** This is the core of handout H2.)*

**11 · Extreme Long Shot (XLS)**: the vastness. A skyline, a landscape, a castle in the distance with a horse for scale. *(Source 14.)*

**12 · Long Shot / Wide Shot (LS)**, where are we, who's there, what's happening. Head to toe with the environment around them. *(Source 15.)*

**13 · Long shots in games, and the exaggeration problem** *(Source 16. **Write the missing notes.**)* Movement has to be exaggerated to read at this size.

**14 · Full Shot (FS)**: head near the top of frame, feet near the bottom. Don't clip either. *(Source 17.)*

**15 · Medium Shot (MS)**: waist or knees up. The conversation default. *(Source 18.)*

**16 · The two-character medium** *(Source 19. **Write the missing notes.**)* Be deliberate about what moves: the audience looks at motion, so don't put motion where you don't want them looking.
*Say: that's a composition note living in a shot-size slide. They're the same subject.*

**17 · Close-Up (CU)**: shoulders to top of head. Subtlety of expression; small movements. *(Source 20.)*

**18 · Extreme Close-Up (ECU)**: fills the frame with a detail. Tension, mystery, a doorknob. *(Source 21.)*

**19 · Single · Two-shot · Insert** *(Source 22 + 23 + 24, merged.)* How many people are in the frame, and the cut-in detail.

---

### PART 4 CAMERA ANGLE (20–28)
*(Source 25–36. **Every slide retitled from `CAMERA ANGLES` to the actual shot name.** Delete the duplicate Canted slide.)*

**20 · Angle changes how they feel about the character** *(Source 25.)* Also: angle creates depth: a three-quarter view has more depth than a flat front.

**21 · High Angle**: camera above, tilted down. Diminishment, vulnerability. *(Source 26.)*

**22 · Low Angle**: camera below. Dominance, scale, threat. Works best when the character is *also* higher in frame. *(Source 27. **Fix "acter."**)*
*Say: hold onto that last part: the staging session builds on it. Angle and physical height stack, and sometimes you want them to contradict.*

**23 · Eye Level**: neutral. The audience meets the character as an equal. *(Source 28.)*

**24 · Bird's Eye**: directly overhead. The audience sees the whole board, and the character doesn't. *(Source 29.)*

**25 · Canted / Dutch**: tilted, off-balance, unsettling. Unhinged characters, unstable worlds. *(Source 30. **Delete source 31, the exact duplicate.**)*

**26 · Tilt**: fixed camera pivoting on the vertical axis. Reveals scale by withholding it. *(Source 32.)*

**27 · Three-Quarter (45°)**: the strongest general-purpose angle, between frontal and profile, because it gives depth between foreground and background. *(Source 33.)*
*Say: if you don't know what angle to use, use this one. It's the rule of thirds of camera angles.*

**28 · Frontal · Profile · Over-the-Shoulder** *(Source 34 + 35 + 36, merged.)* Flat and intimate; side and observational; and the OTS that puts you in someone's position in the conversation.

---

### PART 5 CAMERA MOVEMENT (29–36)
*(Source 37–48. **Retitled throughout. Fix the dolly/zoom error on source 43 and the mislabeled zolly on 47–48; delete one of the pair.**)*

**29 · Movement is a character** *(Source 37.)* Before adding a move, ask what it adds, and what it costs.
*Say: a moving camera is expensive in every medium including yours. Every move you board is a move somebody has to build.*

**30 · Notating movement on a flat page** *(Source 38.)* Direction arrows for camera and for subject, and they are not the same arrow.
*Say: this is handout H1. Camera arrow and motion arrow look different for a reason: the first time you conflate them, an animator builds the wrong shot.*

**31 · Pan**: fixed camera pivoting horizontally. Directs attention from one part of a location to another. Swish pan = fast, dramatic shift. *(Source 41 + 42, merged.)*

**32 · Tilt**: the vertical equivalent. *(Cross-reference slide 26; don't re-teach.)*

**33 · Dolly / Truck**: the camera itself travels toward, away from, or alongside the subject. *(Source 43 + 44, merged. **Rewrite "Zooms in, to end at Position B" → "Camera travels from A to B."**)*

**34 · Zoom**: camera stationary, focal length changes. Tighter (push) or looser (pull). *(Source 45.)*
*Say: dolly and zoom look nothing alike and students conflate them constantly. A dolly changes your relationship to the space. A zoom just magnifies. One of them is a move; the other is a crop.*

**35 · Crane**: swoops, covers distance, produces angles you can't otherwise get. Free in 3D, expensive in reality. *(Source 39 + 40, merged.)*

**36 · Steadicam, and the zolly** *(Source 46 kept; source 47/48 merged into one and **retitled "Zolly / Dolly Zoom."**)* Steadicam: harness-mounted, follows anywhere, smooth. Zolly: dolly one way, zoom the other: the background changes size while the subject doesn't. *Jaws*, on the beach.
*Say: the zolly is the only camera move that has no real-world equivalent in human vision, which is exactly why it feels like the floor dropping out.*

---

### PART 6 PERSPECTIVE AND CLOSE (37–40)
*(Source 49–53, merged from five build slides to three plus the close.)*

**37 · Objective**: neutral, observed from the sidelines. *(Source 50.)*

**38 · Point of view**: the camera near a specific character's viewpoint. *(Source 51.)*

**39 · Subjective**: the camera *becomes* the character. First-person games live here permanently. *(Source 52.)*
*Say: hold this one. The games session is about a medium where the subjective camera is the default and the audience is holding it.*

**40 · Summary + exercise** *(Source 53, kept.)*
*Exercise: name every shot in a 60-second clip, screened twice. Handout H2 is the reference; the midterm is this exercise with the safety off.*

---
---

# DECK 06: DRAWING IN PERSPECTIVE
**37 slides → target ~28 · last in the work order, lowest value**

## What changed
- **The reframe.** This deck currently teaches perspective as draftsmanship (construction, vanishing points, circles in squares) for a course whose stated pedagogy is that *drawing is notation* and *silhouette readability is the standard because it's independent of skill level* (PROJECT.md §3). Taught as-is, it's the one deck that contradicts the course's own grading philosophy and the one most likely to convince a weak draftsman they can't pass.
  **The fix is the ordering, not the content.** Lead with the depth cues that work *regardless of drawing ability*: overlap, size, atmospheric, texture gradient, and value (Deck 05's "cheapest depth cue you own, and it works even if your perspective is wrong"). Then teach linear perspective as the harder tool for people who want it.
- **Defects:** title-slide placeholder notes; *The Two Towers* → **"Twin Towers"** (source 16 notes); aperture → **"preacher"** (source 27 and 28 notes, **and source 28's on-slide text**, so the dictation error is baked into a visible slide).
- ⚠️ **Source 27 and 28 have identical speaker notes**: both carry the deep-focus/Citizen Kane text. Slide 28 is about aperture and needs its own notes written.
- Source 13/14 and 35/36/37 are builds (identical text, different notes). Merge, don't delete.

---

### PART 1 DEPTH IS AN ILLUSION YOU CONTROL (1–4)

**1 · Title**: Drawing in Perspective *(delete placeholder notes)*

**2 · Flat surface, dimensional world** *(Source 2 + 3, merged.)* The 3D world recorded on a 2D surface reduces depth to an illusion.

**3 · You do not need to be good at this to be good at this** ← **new**
*Say: I'm going to teach you six ways to create depth. Five of them work no matter how well you draw. The sixth one is linear perspective and it's the only one that requires construction. We're doing the five first, on purpose, because most of the depth in most panels comes from them.*

**4 · Perspective changes every time the camera moves** *(Source 4.)* Lens choice and camera-to-subject distance are both perspective decisions.
*Say: which means perspective isn't a drawing topic. It's a **camera** topic that you happen to execute with a pencil.*

---

### PART 2 THE FIVE FREE DEPTH CUES (5–10)
> **Reordered to the front.** These are source slides 15, 20, 21, 24, 25: currently scattered through the back half behind the construction material.

**5 · Overlap** *(Source 20.)* One object in front of another. The single cheapest depth cue in existence and it works at any skill level.
*Say: that's it. That's the whole slide. Put something in front of something. You now have depth.*

**6 · Size / scale** *(Source 24.)* Closer is bigger. Scale also tells the audience how big the *thing* is: the horse next to the castle.

**7 · Atmospheric perspective** *(Source 15 + 16, merged. **Fix "Twin Towers" → "The Two Towers."**)* Distance means haze: less contrast, lighter value, cooler cast.

**8 · Value as depth** ← **new; direct lift from Deck 05 slide 11**
Near = darker and higher contrast. Far = lighter and lower contrast.
*Say, verbatim from the composition lecture: this is the cheapest depth cue you own, and it works even if your perspective is wrong.*

**9 · Texture gradient** *(Source 21.)* Texture coarse up close, fine and smooth at distance.

**10 · Foreground / midground / background** ← **new; callback to Deck 05 slide 23**
Three planes is enough. Most student panels use one.
*Say: if you use nothing else from this session, use three planes and overlap them. That's ninety percent of the depth in a professional board.*

---

### PART 3 LINEAR PERSPECTIVE (11–18)
*(Source 5–14, 22–23. Now positioned as the specialist tool, which is what it is.)*

**11 · Picture plane** *(Source 5.)* The window. Line of sight / eyeline.

**12 · Horizon line = eye level** *(Source 6.)* Always at the viewer's eye level. Where an object sits relative to it tells you whether the shot is high, low, or neutral.
*Say: this is the most useful sentence in the deck. **The horizon line is your camera height.** Move the horizon and you've moved the camera. You just changed the angle without drawing anything.*

**13 · Vanishing point** *(Source 7.)* Where parallels converge. Parallel objects share one; objects at other angles get their own.

**14 · One point** *(Source 8 + 9, merged.)* One VP. Verticals, horizontals, orthogonals. Corridors, roads, receding rooms.

**15 · Two point** *(Source 10 + 11 + 12, merged.)* Two VPs on the horizon. Corners. Opens the frame up so you're not staring down a hallway.

**16 · Three point** *(Source 13 + 14, merged.)* A third VP above or below. Looking up or down. Dramatic.
*Say: three-point is what you reach for when the angle *is* the point: the low angle on the tower, the bird's eye over the street. It's from the angles section of Deck 03, executed.*

**17 · Circles in perspective** *(Source 22 + 23, merged.)* Draw the square in perspective, fit the ellipse inside it. Wheels, plates, lamps, tables.

**18 · Foreshortening** *(Source 17 + 18 + 19, merged from three slides to one.)* Applying perspective to a form so one part reads as closer. Easy on a pipe, hard on an arm.
*Say: this is the genuinely difficult one, and it's the one thing on this list where the Marvel Way material on Canvas is worth your time. Optional. Not graded.*

---

### PART 4 THE LENS (19–25)
*(Source 25–34. This is the strongest section in the deck and it's currently buried at the back.)*

**19 · Relative motion** *(Source 25.)* Near things pass faster than far things; the difference is a depth cue in motion.
*Say: this is a **parallax** note and it's the one depth cue you can only use in the animatic. Board a pan across a landscape and put something close in the foreground. Your animatic will do the rest.*

**20 · Depth of field** *(Source 26.)* How much of the frame is in focus, in front of and behind the subject.

**21 · Deep focus** *(Source 27.)* Foreground, midground, and background all sharp; every plane equally important. Welles and Toland, *Citizen Kane*.

**22 · Aperture** *(Source 28. **Fix "preacher" → "aperture" on the slide and in the notes, and write the notes, which currently duplicate slide 21's.**)* Small aperture, less light, greater depth of field. Wide aperture, more light, shallower.

**23 · Normal lens** *(Source 31.)* Mimics the eye. Relationships look the way you expect.

**24 · Wide angle** *(Source 32 + 33, merged.)* Larger area, exaggerated near/far space, both planes in focus, distortion at the edges. Establishing shots.
*Say: wide angle makes a room feel bigger and a face feel wrong. Both are useful.*

**25 · Telephoto** *(Source 34.)* Shallow depth of field; foreground and background compressed together.
*Say: the classic use is a character running toward camera who never seems to get closer. The compression is doing that, and you can draw it.*

---

### PART 5 CLOSE (26–28)

**26 · Which cue is this shot using?** ← **new, a decision slide**
Put up three film stills. Class names the depth cues in each.
*Say: I want to hear "overlap and value," not "good perspective."*

**27 · Summary** *(Source 35 + 36 + 37 merged from three build slides to one.)* Six cues: overlap · size · atmospheric · value · texture · linear. Plus lens and depth of field.

**28 · Exit exercise**
One panel, drawn twice: once using only the free cues, once with constructed linear perspective. Compare how long each took and how much depth you actually gained.
*Say: I'm not trying to prove perspective is useless. I'm trying to show you what it costs, so you spend it where it counts.*

---
---

## Summary of the work

| Deck | Now | Target | Notes pages to rewrite | Slides to delete outright |
|---|---|---|---|---|
| **07 Lighting** | 42 | ~26 | **15+** (the desync from slide 25 on, plus 3 missing at 40–42, plus the title placeholder) | 9 color slides, 1 dup |
| **02 Aspect Ratios** | 47 | ~30 | ~4 (loom, McManus, Cinescope ×3) | ~17 by merge, 3 by summary compression |
| **08a + 08b** | 45 | ~24 + ~22 | ~4 (title placeholder, Eisenstein ×2, "maintiaining", "Right or Left") | 0 outright; 4 builds merged, 8 new slides added |
| **04 Script to Storyboard** | 36 | ~34 | ~4 (title placeholder, 2 textbook refs, 1 missing at source 26) | 0 outright; 3 builds merged, 4 new slides added |
| **03 Fundamentals** | 53 | ~40 | ~5 (3 missing, "acter", the dolly/zoom error) | 2 genuine dups; ~14 by merge; **22 retitles** |
| **06 Perspective** | 37 | ~28 | ~5 (placeholder, Two Towers, preacher ×2 + slide text, slide 28's duplicated notes) | 0 outright; 6 builds merged, 5 new slides added |

**Total notes pages needing attention: roughly 37.** The overwhelming majority are in Deck 07, which is why it's first.

## Still open

- **The theme question for decks 02 and 03.** They're on Organic/Century Gothic while everything else is on Game Design Theme/Garamond. Precedent (Deck 01) says leave it. Worth a decision before 02 is built, since it's second in the queue.
- **The McCay attribution.** Corrected to George McManus here on date evidence, but the instructor should confirm before it goes in front of a class.
- **Source images.** Every deck retains its existing media. New slides that call for a film still are marked for `[ADD IMAGE:...]` in notes and sourced by the instructor: nothing copyrighted gets generated or substituted.
