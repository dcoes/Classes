# Rubric — EX7: AE Rig & Move
**20 points · Band EX · Assessed against CO1**
**Brief:** [`assignments/EX7_AE_Rig_and_Move.md`](../assignments/EX7_AE_Rig_and_Move.md)

> CO1 — *Draw storyboards as a planning tool for their visual narratives.*

A tool-fluency exercise. Its CO claim is deliberately thin and it is priced accordingly — see `PROJECT.md` §4. Near-free if attempted, zero if not.

---

| Component | Pts | Full credit |
|---|--:|---|
| **1 · PSD imported as a composition, layers intact** | 3 | *Import As: Composition — Retain Layer Sizes.* Body, arm and background are separate layers in the timeline. |
| **2 · Anchor point moved to the shoulder, arm parented to body** | 3 | Both halves. The arm rotates from the joint, not from its own center, and it is a child of the body. |
| **3 · Body animated toward camera** | 3 | Position and/or scale keyframed. The arm follows without separate keyframes on its position. |
| **4 · Wave — rotation keys on the parented arm** | 3 | Three or more rotation keyframes on the arm layer. |
| **5 · Exit into the house via a background mask** | 3 | A masked copy of the background sits in front of the character, so the character passes behind the doorway. |
| **The planning paragraph** | 3 | Answers *what would you have had to plan in the drawing to make this easier* with something specific and correct. |
| **Delivery** | 2 | Rendered `.mp4`/`.mov`, 5–8 seconds, plays cleanly, plus the `.aep`. |

**Total: 20**

---

## Grading notes

**Grade the steps, not the result.** Each of the five is independently visible in the project file, and each scores on its own. A student whose mask is visibly wrong still earns 12 of the 15 technical points, because four steps are present and the fifth is diagnosable — which is the whole reason the `.aep` is a required deliverable.

**Step 2 is the one worth checking properly.** Parenting without moving the anchor point produces an arm rotating around its own middle. It often still *reads* as a wave in the render, so it has to be caught in the project file. It is also the conceptual core: an anchor point is a joint, and that idea carries into every rig any of these students touch afterward.

**Step 5 is the designed obstacle.** The background is deliberately one flat layer, so the doorway must be manufactured. Students read this as a broken file; it is the normal condition of the job. Boards, matte paintings and reference art arrive flat, and anything passing behind anything else in a flat image requires a mask.

**The planning paragraph is the only part that isn't button-pushing**, which is why it's worth as much as a technical step. Acceptable answers name something concrete: the doorway should have been its own layer, the arm should have been drawn clear of the torso, the background should have been drawn wider so the character could enter from off-frame. *"I would plan better"* scores zero.

---

## Common failures

| Failure | Cost |
|---|--:|
| Imported as footage — one flat layer | 3, and steps 2–5 become impossible |
| Parented without moving the anchor point | 3 |
| Arm keyframed separately in position instead of following the parent | 3 |
| Character walks in front of the doorway instead of behind it | 3 |
| No `.aep` submitted — steps 1–5 unverifiable | Up to 15 |
| Planning paragraph is generic | 3 |

---

## What is not graded

**Animation quality.** The walk may be a slide, the wave a metronome. No easing, arc, or timing requirement.

**Drawing.** All artwork is supplied.

**Polish.** No transitions, effects, or sound. It's a rig test.

---

## Milestone note

Single-stage, no cap. Due Session 14, but **PR3 is due Session 15** and is substantially harder for anyone who skipped this. The sequencing is the argument for attempting it — worth saying plainly when the assignment is issued, since the failure mode here is not poor work but no work.

Boundary: CA 140 owns After Effects **as an animatic tool**. Motion Graphics owns it as a craft. See `CURRICULUM.md`.
