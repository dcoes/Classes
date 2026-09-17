# PROJECT.md: Digital Painting

*Course source of truth. Content and pedagogy decisions live here. The spine lives in
[`SESSION_MAP.md`](SESSION_MAP.md). Voice and build mechanics live in the repo-root
`CLAUDE.md`. Cross-course boundaries live in the repo-root `CURRICULUM.md`.*

---

## 1. What the course is

On paper it is a digital painting class with an emphasis on Photoshop, and the
description was never specified past that point. That ambiguity is worth treating as
an opening rather than a problem, because it means the course can be built around
what a student will actually be asked to do for money rather than around a survey of
menus.

The working definition used throughout this repository:

> **Digital Painting is a course about applying Photoshop to the jobs that real
> production actually hands to a painter: extending a set, building a surface, and
> directing an image that somebody else has to use downstream.**

Photoshop is the visible spine from the first session to the last. Maya appears for
one short run, and only as a mirror. After Effects appears for one and a half
sessions, and only on the top tier. Neither one is a unit, and neither one is
allowed to grow into one.

---

## 2. The room

The block schedule compresses a full semester into roughly a month, four days a
week, two and a half hours a day. That shape drives almost every decision below. A
subject that needs a week to settle does not get one, so the course carries fewer
ideas and returns to them more often.

The students are a mixed group. Some arrive eager and somewhat advanced and want the
thing they signed up for. Some are checked out. A number are ADA accommodated. All
three of those groups are in the same room at the same time, and the course has to
work for all of them without being run twice.

Retention of prior software skill is weaker than the catalog assumes. Students who
have already taken a Photoshop course routinely arrive without reliable recall of
masks, blend modes, or non-destructive structure. The first unit is built on that
assumption rather than on the transcript.

---

## 3. The tier system

Every deliverable in the course states three levels on one brief. One assignment,
one critique, one rubric, three lines at the top telling each student where the bar
sits for them.

| Tier | Who it is for | What it means |
|---|---|---|
| **Baseline** | The student who is not going to be moved | The floor that passes. Written precisely enough that missing it is a choice rather than a misunderstanding. |
| **Target** | The actual assignment | What the rubric is built around and what the critique discusses. |
| **Extension** | The passionate and the advanced | The harder problem. After Effects lives here. So does the awkward material, the second lighting condition, and the surface that has to sit next to another surface. |

This is a rigging decision more than a grading one. Rather than asking a mixed room
to self-regulate, the brief itself carries the controls, so a student cannot
accidentally aim at the wrong thing and a student who wants more does not have to
ask permission for it.

Two rules that keep the system honest:

- **Nothing on a Baseline tier, anywhere in the course, requires Maya, After
  Effects, a generative tool, or a drawing tablet.** Every floor is reachable on a
  lab machine with a mouse.
- **Extension work is never graded against Target work.** A student who reaches and
  lands badly is assessed on the Target underneath it. Reaching has to be free or
  nobody reaches.

---

## 4. The AI position

Neglecting this would be silly, and overselling it would be worse. The position the
course takes, stated plainly in session 1 and returned to throughout:

> **Generative tools extend digital imaging. They do not replace the judgment that
> tells you whether the image is any good, and that judgment is the thing being
> graded here.**

So AI is woven through the course rather than blocked at the end. A recurring
segment, roughly ten minutes, appears in most sessions under the heading **Where the
machine fits**, always attached to the technique being taught that day. Generative
fill follows the masking session because a bad generative edge is a masking problem.
Generated plates follow the photobashing session because their failures are
color-match and light-logic failures the students were just taught to see.

Two rules the segment obeys everywhere:

1. **It extends the imaging idea of the day.** It is never a tool tour.
2. **It always names its non-generative equivalent.** Some of the better students in
   this program are AI-averse and read it as cheating. The course does not argue
   them out of that. It gives them a reason to be able to see the failure modes
   anyway, which is the durable half of the skill and the half that is on the
   rubric.

Tooling is limited to what is already installed: Photoshop's own generative fill and
Firefly, plus browser tools. Nothing here requires an install, a local model, or
anything IT has to be talked into.

The humanist line stays audible whenever this comes up, and it stays short. The tool
is a means of expression and the person using it is not an operator.

---

## 5. What each unit owns

**Unit 1, The Working File (sessions 1 to 3).** Non-destructive structure, selection
and masking, blend modes, value and light logic for a single image. This unit exists
because the rest of the course assumes a student can build a file that survives
being revised. Most cannot when they arrive.

**Unit 2, Digital Imaging and Matte Painting (4 to 8).** Reading professional
breakdowns, photobashing, plate integration, perspective over a photograph, detail
hierarchy, knowing when to stop. Project 1 lives here. This is the largest unit and
the one closest to a real job.

**Unit 3, Materials and Surfaces (9 to 13).** How different material types behave,
seamless tiling, map sets in plain language, painting against a UV layout with Maya
as the mirror. Project 2 lives here.

**Unit 4, The Extended Image (14 to 15).** Building a painting that is layered well
enough to move, and the five After Effects operations that move it. Project 3 is
briefed here.

**Unit 5, Direction, Ownership and What Happens Next (16 to 18).** Prompting treated
as art direction, the economics of being an artist while production gets cheaper,
and a scheduled studio day on the final.

---

## 6. Projects

| Code | Title | Briefed | Due | The question it asks |
|---|---|--:|--:|---|
| **P1** | The Set Extension | 4 | 8 | Can you make separate photographic sources agree that they were shot at the same moment? |
| **P2** | The Material Set | 9 | 13 | Can you paint a surface that still reads as that material once somebody else lights it? |
| **P3** | The Extended Image | 14 | 19 | Can you build a file that somebody downstream can actually use? |

Briefs live in [`assignments/`](assignments/). Each carries its own three tiers and
its own rubric totaling 100% of that assignment.

Exercises are small, each assigned one session and due at the start of the next:
EX1 diagnostic, EX2 the working file, EX3 value study, EX4 shoot your own plates,
EX5 swatch set, EX6 one tile, EX7 the five operations, EX8 prompt and provenance log.

---

## 7. Recurring threads

Threads rather than topics, meaning they surface in several sessions rather than
getting taught once and dropped.

- **Art direction over tool operation.** The software is never the subject. A
  student who can name every panel in Photoshop and cannot tell whether an image is
  working has learned the wrong half.
- **The home equivalent.** Every technique shown in the lab gets named with whatever
  the student can reach at home, whether that is Photopea in a browser, a phone
  camera, or a mouse instead of a tablet. The skills live in the head rather than in
  Adobe's license.
- **Judgment is what is graded.** Said out loud, repeatedly, and reflected in every
  rubric.
- **Value and silhouette**, in language identical to the Storyboarding course, so
  the concept compounds across the program rather than fragmenting. See
  `CURRICULUM.md`.
- **The humanist line** whenever automation comes up. One clause, never a paragraph.

---

## 8. Teaching shape of a session

Two and a half hours, the same shape every day, so the room knows where it is.

| Clock | Block |
|---|---|
| 0:00 | Recall. Five minutes on the session before, out loud or on screen. |
| 0:10 | Lecture. Thirty to thirty-five minutes. Light, and mostly an explanation of the thing they are about to do. |
| 0:45 | Demo. Twenty minutes, live, including one deliberate mistake recovered in front of them. |
| 1:05 | Studio. Seventy-five minutes with desk crits, and a stated checkpoint partway so drift gets caught on the clock rather than at the end. |
| 2:20 | Exit ticket. One artifact posted before anyone leaves. |

The lecture is deliberately the smallest block. Most of the learning in this course
happens in the studio hour with the instructor circulating, which is also the only
reliable way to reach the students who will not ask.

The stated checkpoint inside the studio block is the accommodation mechanism as much
as the pacing mechanism. It gives every student a fixed moment where somebody looks
at their screen without them having to raise a hand.

---

## 9. Decisions already made, do not revisit

- **Nineteen sessions.** Eighteen taught, one final critique. Sessions 8, 13, 18 and
  19 carry no lecture on purpose.
- **Photoshop is the course.** Maya and After Effects are guests.
- **Maya is a mirror only.** Provided prop, provided UV layout. No modeling, no
  unwrapping, no Substance Painter. Substance was considered and set aside as too
  much tool for the time available, and because the transferable idea is how
  materials behave rather than which application authored them.
- **After Effects is five operations, one and a half sessions, Extension tier only.**
  The same containment device that keeps the Storyboarding After Effects material in
  its lane. See `CURRICULUM.md`, which assigns After Effects as a craft to Motion
  Graphics.
- **No ComfyUI and no local model installs.** Neither the students nor IT has any
  appetite for it, and the course does not need it.
- **AI is woven, not blocked.** See §4.
- **One worked example, then a cold reversal with no answer shown**, on every
  technique session. Do not pre-solve a problem the students should work through
  live, and do not hand out a table of solved examples to memorize.
- **Three tiers on every deliverable.** See §3.

---

## 10. Status

| Artifact | State |
|---|---|
| `PROJECT.md` | Written |
| `SESSION_MAP.md` | Written |
| Session documents 01 to 19 | In progress |
| `assignments/P1`, `P2`, `P3` | In progress |
| Rubrics | Not yet written, currently carried inside each brief |
| Handouts | Not yet written |
| Decks | Not yet built. Session documents are written deck-ready so an outline already exists when the build starts. |
| Syllabus language | Not yet written |
| `CURRICULUM.md` Digital Painting row | Provisional, needs filling |

Needed from the instructor before several sessions can be finished: the plate set for
the P1 demo, the Maya prop and its UV layout, the deliberately mangled PSD for
session 7, and which breakdown material to use in session 4.
