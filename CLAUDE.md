# CLAUDE.md — how material in this repository is written

This file governs **how** course material is written, not what it says.

Before changing anything: read `CURRICULUM.md` for cross-course boundaries, and the
relevant course's `PROJECT.md` for decisions that are already settled. If a change
would contradict either, don't make it — flag it.

---

## 1. Teach problem solvers, not button pushers

Systems thinking and pattern recognition are the through-line of every course in
this repository. The specific technique a student learns this week matters less
than whether they can recognize it again, in a different medium, wearing a
different name.

So: **every technique is taught as an instance of a pattern the student has
already met, and the connection is named out loud.**

Three patterns carry most of the weight in CA 140, and they should be pointed at
by name every time they reappear:

- **The floor plan** is one tool. It appears in scripting, in staging, in the
  lighting study, and again in games — where the camera moves through a space
  instead of being placed in it.
- **The three-value reduction** is one discipline. It appears in composition, in
  lighting, and in every readability check.
- **The silhouette test** is one standard. It appears in week one and every week
  after, in figures, in staging, and in game character design.

When a new technique is introduced, say which existing tool it is.

**Software is never the subject.** Where a tool is taught — Photoshop, After
Effects, anything — the lesson ends on what the student had to *decide* to make
the tool work, never on which menu the command is under. The closing question of
a software session is a design question, not a procedural one.

The corollary, which shows up in grading: the assessed object is the **decision**,
not the artifact. A crude panel that stages the beat outscores a polished one that
doesn't, and that has to be true on the rubric, not just in the encouragement.

---

## 2. Student-facing material carries no instructions to the instructor

Decks, assignment briefs, rubrics, handouts and syllabus language are written to
be read start to finish by a student, with nothing in them addressed past them.

**PowerPoint speaker notes are the verbatim script the instructor delivers.** A
meta-instruction there is redundant — the note *is* the instruction. Write what
is said, not a description of what to say:

- ✅ *"Fill it in solid black. If a stranger can't name the action, the pose
  failed."*
- ❌ *"Explain the silhouette test here and tell them it applies all semester."*

Stage directions that genuinely have to survive into the notes get **bracketed**,
so they're visually skippable when reading aloud:

```
[LIVE: ten figures in 90 seconds]
[Let them answer wrong first]
```

Anything longer than a clause moves out of the notes entirely.

**Genuine instructor-only content lives in `<Course>/INSTRUCTOR.md`** — one file
per course, one section per session. That is the home for timing, demo setup,
forward connections worth planting early, and known failure modes.

**One narrow exception.** A note that must fire at a *specific slide* may sit in
that slide's speaker notes, prefixed exactly:

```
Note for instructor: this is the shot vocabulary the midterm is graded against —
name the midterm here so it isn't a surprise in four sessions.
```

Use it sparingly. If it isn't tied to a specific slide, it belongs in
`INSTRUCTOR.md`. If it restates something already obvious from the material, cut
it.

---

## 3. Repository conventions

**Assignments and rubrics.** Every brief has a rubric; every rubric has a brief.
They share a basename across `assignments/` and `rubrics/` and cross-link both
ways. Band prefixes: `EX*` for single-stage skill exercises, `PR*` for
milestone-graded projects.

**Rubrics map to course objectives (CO1–CO5) directly**, never to program-level
SLO numbers, which are unverified. See `Storyboarding/PROJECT.md` §2.

**Decks are edited, not regenerated.** Open the original `.pptx`, edit in place,
save to `NewLectures/` as `NN_Name_REVISED.pptx`. The embedded media is
instructor-sourced film stills and it must survive — check `image-ledger.md`.
Never rebuild a deck from scratch.

**Copyrighted film stills stay as `[ADD IMAGE: ...]` markers** in the speaker
notes, sourced by the instructor. Never generate, substitute, or approximate a
copyrighted character or frame.

**Diagrams are native vector shapes** on the deck's theme palette — editable, not
embedded images.

**Voice.** Second person, direct, contractions fine. Briefs open with why the
assignment exists and close with what is *not* graded. Say the uncomfortable
thing plainly rather than reassuringly — the students can tell.
