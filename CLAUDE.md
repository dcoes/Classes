# CLAUDE.md — Working with Claude on this repo

> Read this alongside `Storyboarding/PROJECT.md` (course content, pedagogy, and
> production plan — the source of truth for what to build). This file is about
> *how* to build it and how I like to work.

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
acknowledges this honestly — don't oversell AI, don't dismiss it either.

## 2. Voice — this is the one I've corrected on most

- **No em dashes.** Ever, in any user-facing content (slides, docs, notes to
  me in chat). They read as the clearest tell of AI-generated writing.
- **No LinkedIn/Instagram-brain phrasing.** No "unlock," "elevate," "game
  changer," manufactured drama, forced inspirational beats. If a sentence
  could be a LinkedIn post, rewrite it.
- I want the material to sound like **me**, not like AI trying to sound
  human. When in doubt, plainer and flatter beats punchier and hollow.
- This applies to slide text, speaker notes, and any prose deliverable
  (handouts, rubrics, syllabus language).

## 3. Deck build workflow — hard-won lessons

**Theme inheritance, not approximation.** When rebuilding a deck, load an
already-finished deck (e.g. `07_Storytelling_through_Lighting_REVISED.pptx`)
as the base file and clear only its slides — never rebuild the theme from
scratch by eyeballing colors. This preserves the actual masters, layouts, and
theme XML. Clear slides by removing them from `<p:sldIdLst>` **and** dropping
the relationship (`prs.part.drop_rel(rId)`) — removing from the ID list alone
leaves orphaned parts and throws duplicate-name warnings.

**Bullets on slide, prose in notes — never mixed.** This was the single
biggest miss in an early draft: full paragraphs ended up in the slide body,
visible to students. The rule going forward:
- Slide body: 2-4 short bullets, 3-8 words each. What a student reads at a
  glance.
- Speaker notes: the actual teaching script, second person, spoken register,
  contractions fine, including stage directions ("do this live," "let them
  answer wrong").
- The slide is for the students to look at and discuss. The notes are for me.

**Images are the visual anchor, not decoration.** Slides with source material
available should be built around the image, not have an image squeezed in
next to a wall of text. Use full source resolution; don't compress images
during the build unless there's a real file-size constraint, and say so if
there is one.

**Positioning consistency.** Extract real EMU coordinates from the source
deck's actual placeholder XML rather than guessing — e.g. content-left column,
full-width content, single right-side image, and two-up side-by-side images
all have fixed coordinate sets pulled from Deck 07's real layout. Reuse those
constants across every new deck rather than re-deriving them per slide.

**QA pipeline before delivery, every time:**
1. `python-pptx` / validation script for OOXML schema errors
2. Convert to PDF via LibreOffice, render to JPEG, visually inspect every
   slide for overflow, misalignment, text-on-image contrast
3. Content check: no em dashes, no leftover placeholder text, no duplicate
   slides carried over from source

## 4. Pedagogy decisions already locked in

These live in full in `Storyboarding/PROJECT.md` §9 ("Decisions already
made — do not revisit"). Highlights relevant to deck rebuilds:
- Storyboard/aspect-ratio history sections are **kept**, not compressed —
  they're actively taught material (Fleischer→dailies, Disney innovation,
  McCay vaudeville precedent), not filler.
- Formula/technique slides get **one worked example, then a cold reversal
  with no answer shown** — "teach them to fish," not a solved answer key.
  Don't pre-solve problems I want students to work through live.
- Silhouette readability, milestone grading, and the forward-looking AI/craft
  framing are recurring threads — see PROJECT.md §3 and §7 for exact language.

## 5. Repo / workflow mechanics

**The cloud Cowork sandbox cannot push to GitHub directly** — its network
proxy blocks outbound git auth even with a valid token, and this is not
configurable from Cowork settings (there's no "authorized repos" panel to
find, contrary to what I said earlier in this thread — that was wrong).

**What actually works:**
- Claude Code CLI, run locally on my machine, has native access to this git
  repo and my real GitHub credentials — no sandbox proxy in the way. This is
  the path going forward for anything that needs to land in git directly.
- If working in Cowork (web/mobile) instead: build/edit happens in the cloud
  workspace, then files get handed back to me via direct file delivery, and I
  commit/push locally myself.

**File organization:**
- `Storyboarding/NewLectures/` — rebuilt decks, named `NN_Title_REVISED.pptx`
- `Storyboarding/NewLectures/deck-NN-outline*.md` — full outline + speaker
  note drafts, built *before* the deck itself
- `Storyboarding/source_images/` — extracted source images reused across
  rebuilds, numbered `imageN.ext`
- `Storyboarding/build_deck_NN*.py` — the actual build script per deck, kept
  in-repo so a deck can be regenerated or adjusted later without rebuilding
  the whole approach from scratch
- `Storyboarding/PROJECT.md` — course content/pedagogy source of truth,
  update the status table in §11 as decks get rebuilt

## 6. Status snapshot (as of this writing)

See `Storyboarding/PROJECT.md` §11 for the live table. As of now:
- Rebuilt: 01 Intro, 05 Composition, 12 Animatics, 02 Aspect Ratios,
  07 Lighting
- Not yet rebuilt: 03 Fundamentals of the Shot, 04 Script to Storyboard,
  06 Perspective, 08 Continuity (splitting into 08a/08b)
- Not yet built (from scratch): 09 Staging & Acting, 10 Boarding for Games,
  11 The Pitch
- Not yet produced: Handouts H1-H6, rubrics, assignment briefs, syllabus
  language (Phase 1 — doesn't need any uploaded source files, can start
  anytime)
