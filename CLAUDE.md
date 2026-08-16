# CLAUDE.md: working with Claude on this repo

> Read this alongside the relevant course's `PROJECT.md` (course content, pedagogy,
> and production plan) and `CURRICULUM.md` (how the courses relate to each other
> across the program). Those say *what* to build. This file is about *how* to build
> it and how I like to work.

---

## 1. Who I am, what I'm doing

I teach design/games/animation courses at a private university with a block
schedule (a full course crammed into ~1 month, 4 days/week). I'm rebuilding my
lecture decks to be more current, more visual, and better paced for that
compressed format. Students are mixed-skill, some very eager, some checked
out. A number are ADA/learning-disability accommodated. The school is
for-profit, which shapes some of the constraints I'm working against (not
something to fix, just context for why retention and pacing are hard).

I have a mixed view on AI in the classroom: it's a real augmenting tool for
people who already know what they're doing, and a real risk for critical
thinking if students lean on it instead of building judgment. Many of my
better students are AI-averse and see it as cheating. Build content that
acknowledges this honestly. Don't oversell AI, don't dismiss it either.

## 2. Voice, the one I've corrected on most

- **No em dashes.** Ever, in any user-facing content (slides, docs, notes to
  me in chat). They read as the clearest tell of AI-generated writing. Use a
  comma, a colon, parentheses, or a full stop. Note that swapping every em
  dash for a hyphen is its own tell: rewrite the sentence instead.
- **No LinkedIn/Instagram-brain phrasing.** No "unlock," "elevate," "game
  changer," manufactured drama, forced inspirational beats. If a sentence
  could be a LinkedIn post, rewrite it.
- I want the material to sound like **me**, not like AI trying to sound
  human. When in doubt, plainer and flatter beats punchier and hollow.
- This applies to slide text, speaker notes, and any prose deliverable
  (handouts, rubrics, syllabus language).

## 3. Teach problem solvers, not button pushers

Systems thinking, and the ability to recognize a pattern and then exploit it,
is the through-line of every course here. It matters more than any specific
technique. The technique a student learns this week will change. The habit of
noticing they have seen this shape before will not.

So: **every technique is taught as an instance of a pattern the student has
already met, and the connection gets named out loud.** In CA 140 three tools
carry most of that weight, and they should be pointed at by name every time
they resurface:

- **The floor plan.** It appears in scripting, in staging, in the lighting
  study, and again in games, where the camera moves through a space instead
  of being placed in it.
- **The three-value reduction.** It appears in composition, in lighting, and
  in every readability check.
- **The silhouette test.** Week one, and every week after: figures, staging,
  and game character design.

**Software is never the subject.** Where a tool gets taught (Photoshop, After
Effects, anything), the lesson ends on what the student had to *decide* to
make the tool work, never on which menu the command lives in. The closing
question of a software session is a design question.

The corollary shows up in grading: what gets assessed is the **decision**, not
the artifact. A crude panel that stages the beat beats a polished one that
doesn't, and that has to be true on the rubric, not just in the encouragement.

## 4. Student-facing material carries no instructions to me

Slides, briefs, rubrics, handouts, and syllabus language get read start to
finish by a student, with nothing in them addressed past the student.

Speaker notes are a special case, because **the notes page is already the
verbatim script I deliver.** A meta-instruction there is redundant: the note
*is* the instruction. Write what gets said, not a description of what to say.

- Good: *"Fill it in solid black. If a stranger can't name the action, the
  pose failed."*
- Bad: *"Explain the silhouette test here and tell them it applies all
  semester."*

**Stage directions still belong in the notes** (see §5), but bracket them so
they're visually skippable when I'm reading aloud:

```
[LIVE: ten figures in 90 seconds]
[Let them answer wrong first]
```

Anything longer than a clause moves out of the notes entirely.

**Instructor-only content lives in `<Course>/INSTRUCTOR.md`**, one file per
course, one section per class. That's the home for timing, demo setup, forward
connections worth planting early, and known failure modes.

**One narrow exception.** A note that has to fire at a *specific slide* can sit
in that slide's notes, prefixed exactly `Note for instructor:`. Use it
sparingly. If it isn't tied to a slide, it goes in `INSTRUCTOR.md`. If it
restates something already obvious from the material, cut it.

## 5. Deck build workflow, hard-won lessons

**Theme inheritance, not approximation.** When rebuilding a deck, load an
already-finished deck (e.g. `07_Storytelling_through_Lighting_REVISED.pptx`)
as the base file and clear only its slides. Never rebuild the theme from
scratch by eyeballing colors. This preserves the actual masters, layouts, and
theme XML. Clear slides by removing them from `<p:sldIdLst>` **and** dropping
the relationship (`prs.part.drop_rel(rId)`); removing from the ID list alone
leaves orphaned parts and throws duplicate-name warnings.

**Bullets on slide, prose in notes, never mixed.** This was the single
biggest miss in an early draft: full paragraphs ended up in the slide body,
visible to students. The rule going forward:
- Slide body: 2-4 short bullets, 3-8 words each. What a student reads at a
  glance.
- Speaker notes: the actual teaching script, second person, spoken register,
  contractions fine, with bracketed stage directions per §4.
- The slide is for the students to look at and discuss. The notes are for me.

**Images are the visual anchor, not decoration.** Slides with source material
available should be built around the image, not have an image squeezed in
next to a wall of text. Use full source resolution; don't compress images
during the build unless there's a real file-size constraint, and say so if
there is one.

**Positioning consistency.** Extract real EMU coordinates from the source
deck's actual placeholder XML rather than guessing (content-left column,
full-width content, single right-side image, and two-up side-by-side images
all have fixed coordinate sets pulled from Deck 07's real layout). Reuse those
constants across every new deck rather than re-deriving them per slide.

**Diagrams are native vector shapes** on the deck's theme palette: editable,
not embedded images.

**Copyrighted film stills stay as `[ADD IMAGE: ...]` markers** in the notes and
get sourced by me. Never generate, substitute, or approximate a copyrighted
character or frame.

**QA pipeline before delivery, every time:**
1. `python-pptx` / validation script for OOXML schema errors
2. Convert to PDF via LibreOffice, render to JPEG, visually inspect every
   slide for overflow, misalignment, text-on-image contrast
3. Content check: no em dashes, no LinkedIn phrasing, no leftover placeholder
   text, no duplicate slides carried over from source

## 6. Rubrics

**Every rubric totals 100% for its own assignment**, unless the assignment
says otherwise. Course-level weighting is a separate layer and lives in the
syllabus.

**Each criterion carries pre-populated bands I can click in Canvas**, each with
a short justification for that band. This is the part that has to be fast with
forty submissions open:

```
Silhouette readability, 20% of this assignment
  Exemplary   20%  Every pose reads filled solid black.
  Good        17%  Reads throughout, one or two ambiguous poses.
  Average     14%  Reads about half the time; limbs lost in the torso.
  Developing  10%  Most poses don't read; action inferred from the caption.
  Missing      0%  Not submitted.
```

A longer prose explanation of the criterion belongs underneath, for the
student. The clickable bands are for me.

**Rubrics map to course objectives directly**, never to program-level SLO
numbers, which are unverified. See `Storyboarding/PROJECT.md` §2.

## 7. Pedagogy decisions already locked in

These live in full in `Storyboarding/PROJECT.md` §9 ("Decisions already made,
do not revisit"). Highlights relevant to deck rebuilds:
- Storyboard/aspect-ratio history sections are **kept**, not compressed.
  They're actively taught material (Fleischer to dailies, Disney innovation,
  McCay vaudeville precedent), not filler.
- Formula/technique slides get **one worked example, then a cold reversal
  with no answer shown**: "teach them to fish," not a solved answer key.
  Don't pre-solve problems I want students to work through live.
- Silhouette readability, milestone grading, and the forward-looking AI/craft
  framing are recurring threads. See PROJECT.md §3 and §7 for exact language.

## 8. Repo / workflow mechanics

**Work on `master`. Don't create feature branches.** I don't want to track
work across branches. If a session starts on one, fast-forward `master` to it
and continue there.

**File organization:**
- `CURRICULUM.md`: cross-course boundaries, what each course owns and what it
  may not re-teach
- `INSTRUCTOR_PROFILE.md`: accumulating professional profile, across all
  courses and outside projects
- `<Course>/PROJECT.md`: that course's content and pedagogy source of truth
- `<Course>/INSTRUCTOR.md`: instructor-only notes, one section per class
- `Storyboarding/NewLectures/`: rebuilt decks, named `NN_Title_REVISED.pptx`
- `Storyboarding/NewLectures/deck-NN-outline*.md`: full outline and speaker
  note drafts, built *before* the deck itself
- `Storyboarding/source_images/`: extracted source images reused across
  rebuilds, numbered `imageN.ext`
- `Storyboarding/build_deck_NN*.py`: the build script per deck, kept in-repo
  so a deck can be regenerated later without rebuilding the approach
- `Storyboarding/assignments/` and `Storyboarding/rubrics/`: 1:1, sharing a
  basename, cross-linked both ways. `EX*` for single-stage skill exercises,
  `PR*` for milestone-graded projects.

**Update the status table in `PROJECT.md` §11 as work lands.**

## 9. Status snapshot (as of this writing)

See `Storyboarding/PROJECT.md` §11 for the live table. As of now:
- Rebuilt: 01 Intro, 02 Aspect Ratios, 03 Fundamentals of the Shot,
  04 Script to Storyboard, 05 Composition, 06 Perspective, 07 Lighting,
  08 Continuity (split into 08a/08b), 12 Animatics
- Not yet built from scratch: 09 Staging & Acting, 10 Boarding for Games,
  11 The Pitch, 13 After Effects for Boards
- Specced but not built: four swap-in modules in `Storyboarding/modules/`
  (New Media, AI in the Pipeline, Previs, VR)
- Produced: handouts H1-H8, twelve assignment briefs, twelve rubrics,
  syllabus language, `SESSION_MAP.md`, `INSTRUCTOR.md`
