# CLAUDE.md: working with Claude on this repo

> Read this alongside two other files.
> `Storyboarding/PROJECT.md` is the source of truth for course content and pedagogy.
> `VOICE_ANALYSIS.md` is the source of truth for how the writing should sound.
> This file is about *how* to build things and how I like to work.

---

## 1. Who I am, what I'm doing

I teach design, games and animation courses at a private university that runs on a
block schedule, so a full course gets crammed into about a month, four days a week.
I'm rebuilding my lecture decks to be more current, more visual, and better paced
for that compressed format. Students are mixed-skill. Some are very eager, some are
checked out. A number are ADA/learning-disability accommodated. The school is
for-profit, which shapes some of the constraints I'm working against (not something
to fix, just context for why retention and pacing are hard).

Outside teaching I work as a technical artist and character TD, mostly in Maya, and
that background matters here more than it looks like it should: a lot of the way I
build assignments is really rigging thinking applied to people. Don't ask the
animator to be careful, build the control so the wrong thing can't happen.

I have a mixed view on AI in the classroom. It's a real augmenting tool for people
who already know what they're doing, and a real risk to critical thinking if
students lean on it instead of building judgment. Many of my better students are
AI-averse and see it as cheating. Build content that acknowledges this honestly.
Don't oversell AI, don't dismiss it either.

---

## 2. Voice

**This is the section I have corrected on most. Read `VOICE_ANALYSIS.md` before
writing any prose that goes out under my name.** That file is a study of my actual
professional and academic writing (dissertation chapter, letters, teaching
philosophy, talk outlines, lecture decks, email). Its Master Prompt Profile section
at the bottom is the short version if you only read one part.

Note that `VOICE_ANALYSIS.md` is a *description* of the voice, not a sample of it.
Its own punctuation is not a model. The rules below win.

### 2a. Two hard bans

**No em dashes. Ever.** Not in slides, not in handouts, not in speaker notes, not in
build scripts, not in notes to me in chat, not in this file. They are the clearest
tell of AI-generated writing and I will notice. Use a comma, a colon, parentheses,
or two sentences.

One exception worth naming precisely, because it is a real habit of mine and not the
same character: the **spaced en dash in a bullet gloss** is fine.
`**Willingness to learn** – This is especially important here.` That is an en dash
(–), not an em dash (—). Bolded term, spaced en dash, then the gloss.

**No LinkedIn or Instagram brain.** No "unlock," no "elevate," no "game changer," no
manufactured drama, no forced inspirational beats, no tidy thesis-and-three-supports
structure. If a sentence could be a LinkedIn post, rewrite it. When in doubt,
plainer and flatter beats punchier and hollow.

### 2b. What the voice actually does

Pulled out of `VOICE_ANALYSIS.md` so you don't have to go get it every time.

- **Anecdote first, principle second.** Arrive at the idea through a specific thing
  that happened (a project, a student, a tool, a moment where something broke)
  rather than declaring the principle and then illustrating it.
- **Every abstraction gets a physical, mechanical object.** Pumps, valves, strings,
  puppets, wheels, tables, libraries, photographs, shapes. Don't explain the
  metaphor after it lands.
- **Hedge my competence downward.** *Somewhat*, *quite*, *more or less*, *enough*,
  *at least some*. Never stack superlatives about me. State a credential flatly and
  move on. (See §2c, this one has a cost.)
- **Hedge dates and quantities.** *Or so*, *around*, *close to*, *roughly*. Never a
  flat year if the year is from memory. "Back in 2004 or so."
- **Open lists with "Some of these include..."** and keep them explicitly partial.
- **Scare quotes on borrowed vocabulary.** Any term that is jargon, imprecise, or
  not quite mine gets quarantined in quotes: "digital puppets," "technical
  animator," "dailies," "artificial intelligence." Occasionally say why the word is
  wrong.
- **Concede the counterargument before anyone raises it.** *Nevertheless*, *It is
  possible however, to argue that...*, *Not all agree*. Prefer a reframing over a
  verdict.
- **Mark beliefs as beliefs.** *I feel that*, *I believe*, *I think there is*. Use
  *it is important that* or *it is fundamental that* to state a value without
  claiming personal authority for it.
- **Praise by describing behavior, not by asserting a quality.** And if I didn't
  witness it, say so and hedge it.
- **Long accreting sentences, held together by commas.** Clauses added rather than
  subordinated. Front-load a participial or adverbial opener before the subject
  arrives: *Being*, *Seeing*, *Without*, *While*, *Working*, *Before*. A run-on that
  sounds like speech can stand.
- **Small fixed set of transitions.** In addition, In other words, In a sense,
  Nevertheless, Actually, Though, Rather than, Much like, Aside from, At the end of
  the day.
- **Rhetorical question, then answer,** used to advance the argument rather than to
  decorate it.
- **Parentheses for qualifications** I want on the record but not emphasized.
- **The humanist line stays audible** whenever tools, automation or AI come up: the
  technology is a means of expression and the person using it is not an operator.
  One clause, never a paragraph, never a lecture.

### 2c. What NOT to imitate

`VOICE_ANALYSIS.md` catalogues some things that are accurately observed but are
artifacts of fast drafting, not style. Do not reproduce:

- **The typos.** *inteligence*, *artifcial*, *loosing*, *posses*, and the rest. I
  write fast and don't proofread hard. That is not a feature.
- **Spaces inside quotation marks.** `" What is autonomy? "` is a mistake.
- **British spellings.** *visualise*, *memorise*. Those came from somewhere else.
- **"often times" as two words.** Pick *oftentimes* and be consistent.
- **The self-deprecation, when it is load-bearing.** Hedging my competence is the
  right register in a lecture or a letter. It is the wrong register in a resume,
  portfolio copy, a rate conversation, or a rubric that has to defend a grade. It
  has already cost me once (a whole job title was argued down on the strength of me
  calling my own Python "basic"). If you are writing something where the claim has
  to hold weight, describe the artifact instead of rating my skill, and if I start
  writing "just" or "basic" about my own technical work, push back by name.

### 2d. Register by destination

The voice is the same everywhere, the sentence shape is not.

| Destination | Register |
|---|---|
| **Slide body** | 2 to 4 short bullets, 3 to 8 words each. Almost telegraphic. This is a pedagogy decision, not a voice decision: students read it at a glance and then we talk. Word *choice* still follows §2b, so the scare quotes and the plain vocabulary stay. |
| **Speaker notes** | Full presentation register. Bullets written as complete spoken sentences. Second person, contractions fine, bold on the key term mid-sentence to mark the beat I'm hitting aloud, stage directions in line ("do this live," "let them answer wrong"). End a section on one compressed line. |
| **Handouts, rubrics, briefs, syllabus language** | Full prose register per §2b. Long-breathed, organized with headings, outward-facing. Thank people, hand the exchange back. |
| **Notes to me in chat** | Same bans apply. Plain, no preamble, no recap of what I just said. |

A note on the corpus, since it touches work in this repo directly: the analysis flags
that the old *Aspect Ratios* deck reads unlike everything else of mine (clipped
verbless fragments, no hedging, British spellings) and may have been heavily revised
or co-written. Don't treat that deck's prose as a voice sample. The *Acting for
Animation* deck is the better model for my unedited lecture voice.

---

## 3. Deck build workflow

Hard-won, mostly by getting it wrong first.

**Theme inheritance, not approximation.** When rebuilding a deck, load an
already-finished deck (`07_Storytelling_through_Lighting_REVISED.pptx` is the
current reference) as the base file and clear only its slides. Never rebuild the
theme from scratch by eyeballing colors. Loading the real file preserves the actual
masters, layouts and theme XML. Clear slides by removing them from `<p:sldIdLst>`
**and** dropping the relationship (`prs.part.drop_rel(rId)`). Removing from the ID
list alone leaves orphaned parts and throws duplicate-name warnings.

**Bullets on slide, prose in notes, never mixed.** This was the single biggest miss
in an early draft: full paragraphs ended up in the slide body where students could
read them. See the register table in §2d. The slide is for the students to look at
and discuss. The notes are for me.

**Images are the visual anchor, not decoration.** A slide that has source material
available should be built around the image, not have an image squeezed in next to a
wall of text. Use full source resolution. Don't compress during the build unless
there is a real file-size constraint, and if there is one, say so out loud instead
of quietly degrading the images.

**Positioning consistency.** Extract real EMU coordinates from the source deck's
actual placeholder XML rather than guessing. Content-left column, full-width
content, single right-side image, and two-up side-by-side images all have fixed
coordinate sets pulled from Deck 07's real layout. Reuse those constants across
every new deck rather than re-deriving them per slide.

**QA pipeline before delivery, every time:**

1. `python-pptx` or a validation script for OOXML schema errors.
2. Convert to PDF via LibreOffice, render to JPEG, and visually inspect every slide
   for overflow, misalignment, and text-on-image contrast.
3. Content check: no em dashes, no leftover placeholder text, no duplicate slides
   carried over from the source.

---

## 4. Pedagogy decisions already locked in

These live in full in `Storyboarding/PROJECT.md` §9, "Decisions already made, do not
revisit." The ones that come up most during deck rebuilds:

- Storyboard and aspect-ratio history sections are **kept**, not compressed. The
  Fleischer-to-dailies line, Disney's animation-led innovation, and the McCay
  vaudeville precedent are actively taught material, not filler.
- Formula and technique slides get **one worked example, then a cold reversal with
  no answer shown.** Teach them to fish. Don't pre-solve a problem I want students
  to work through live, and don't hand them a table of solved examples they can
  memorize instead of learning the operation.
- Silhouette readability, milestone grading, and the forward-looking AI-versus-craft
  framing are recurring threads. `PROJECT.md` §3 and §7 have the exact language.

---

## 5. Repo and workflow mechanics

**The cloud Cowork sandbox cannot push to GitHub.** Its network proxy refuses
outbound git auth even with a valid fine-grained token, and this is not something I
can turn on from Cowork settings. There is no "authorized repos" panel to go find.
(I said there was, earlier in a thread. That was wrong, and it cost an hour.)

**What actually works:**

- **Claude Code CLI, run locally.** It has native access to this git repo and my
  real credentials, with no sandbox proxy in the way. This is the path for anything
  that needs to land in git directly, and it is the reason this file exists.
- **Cowork on web or mobile:** build and edit happen in the cloud workspace, files
  come back to me by direct delivery, and I commit and push locally myself. Fine for
  drafting, bad for anything iterative.

**File organization:**

- `Storyboarding/NewLectures/` : rebuilt decks, named `NN_Title_REVISED.pptx`
- `Storyboarding/NewLectures/deck-NN-outline*.md` : full outline and speaker-note
  drafts, written *before* the deck itself
- `Storyboarding/source_images/` : extracted source images reused across rebuilds,
  numbered `imageN.ext`
- `Storyboarding/build_deck_NN*.py` : the build script per deck, kept in-repo so a
  deck can be regenerated or adjusted later without rebuilding the approach from
  scratch
- `Storyboarding/PROJECT.md` : course content and pedagogy source of truth. Update
  the status table in §11 as decks get rebuilt.
- `CURRICULUM.md` : cross-course boundary document. What each course owns, may
  reference, and may not re-teach. Check it before adding material that another
  course owns.
- `VOICE_ANALYSIS.md` : the writing style study. See §2.

---

## 6. Status snapshot

`Storyboarding/PROJECT.md` §11 has the live table. As of this writing:

- **Rebuilt:** 01 Intro, 05 Composition, 12 Animatics, 02 Aspect Ratios, 07 Lighting
- **Not yet rebuilt:** 03 Fundamentals of the Shot, 04 Script to Storyboard,
  06 Perspective, 08 Continuity (splitting into 08a and 08b)
- **Not yet built from scratch:** 09 Staging & Acting, 10 Boarding for Games,
  11 The Pitch
- **Not yet produced:** Handouts H1 to H6, rubrics, assignment briefs, syllabus
  language. This is Phase 1 and it needs no uploaded source files, so it can start
  any time.
