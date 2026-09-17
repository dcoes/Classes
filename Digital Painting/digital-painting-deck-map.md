# Digital Painting: Deck Map

*Superseded as a planning document. The course now lives in
[`SESSION_MAP.md`](SESSION_MAP.md) and [`sessions/`](sessions/).*

---

## What changed, and why

The earlier version of this file planned twelve decks across a fifteen-week semester.
The course does not run that way. It runs as a block: roughly a month, four days a
week, two and a half hours a day, nineteen sessions.

That mismatch was most of why the earlier plan read as vague. It described deck
subjects rather than classes, and a subject is not a class when the class is a single
sitting with a light lecture at the front and a long supervised studio behind it. A
line like "values, atmospheric perspective, light direction consistency" is a topic
list. It does not say what happens at 1:40 on a Tuesday, what the room is doing with
their hands, or what gets posted before anybody leaves.

So the planning artifact moved. Each of the nineteen sessions now has its own document
containing the clock, the lecture beats, the live demo, the studio block with its
checkpoint, the tiers, the exit ticket, the predictable failure of that day, and the
prep list.

---

## Where to look now

| For | Go to |
|---|---|
| Pedagogy, tiers, the AI position, decisions already made | [`PROJECT.md`](PROJECT.md) |
| The nineteen-session spine, milestones, exercises, software boundaries | [`SESSION_MAP.md`](SESSION_MAP.md) |
| Any individual class | [`sessions/`](sessions/) |
| The three project briefs and their rubrics | [`assignments/`](assignments/) |
| The material behind session 17 | [`Artist_in_the_Age_of_AGI.md`](Artist_in_the_Age_of_AGI.md) |

---

## Decks, when they get built

No deck has been built yet, and the session documents are written so that none of
them starts from nothing. Every lecture beat in every session file is already a slide
line plus the spoken version underneath it, which is the outline stage the repo
convention asks for before a build begins. See the root `CLAUDE.md` §3 for theme
inheritance and the QA pipeline.

Build order when that starts: **01, 09, 17, then the matte painting run 04 to 07,
then 10 to 15, then the rest.**

Session 01 goes first because it sets the tone the whole course argues toward. Session
09 goes second because the materials unit is the newest material and the one most
likely to need revision after it has been taught once. Session 17 goes third because
it is the largest argument in the course and it will date fastest.

Sessions 08, 13, 18 and 19 get no deck at all. Two are critique, one is a scheduled
work session, one is the final. Building slides for a critique day produces filler and
the room reads it as filler.

---

## What the earlier plan got right and kept

Several things survived the restructure more or less intact and are worth naming so
they do not get relitigated:

- Matte painting as the spine of the largest unit, taught by reverse-engineering
  professional work before anybody builds anything. Now session 04.
- The broken-file recovery exercise, which needed a deliberately mangled PSD authored
  as a separate deliverable. Now session 07, and the PSD is still the main prep item
  in the course.
- Seamless tiling and map sets carrying the justification for the 3D-adjacent unit.
  Now sessions 10 through 12, with Maya reduced to a mirror.
- The recurring threads: art direction over tool operation, a home equivalent named
  for every technique, judgment as the thing being graded, and the humanist line
  whenever automation comes up.

---

## What the earlier plan got wrong

**It blocked the AI material into one large deck near the end.** That deck would have
had to carry the entire argument alone, and it would have read as a special topic
bolted onto a painting course. The material is now woven: eight ten-minute segments
attached to whatever technique is being taught that day, consolidated at session 16,
and argued at session 17. The generative fill segment follows the masking session
because a bad generative edge is a masking problem, which is a better teaching order
and a more honest claim.

**It had no tier system**, which meant no answer to a mixed room beyond hoping. See
`PROJECT.md` §3.

**It assumed a fifteen-week cadence** in its milestone spacing, which does not survive
a block schedule at all.
