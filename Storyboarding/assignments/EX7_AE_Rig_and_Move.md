# EX7 AE Rig & Move
**3% of the course grade · Assigned Class 11 · Due Class 12**
**Rubric:** [`rubrics/EX7_AE_Rig_and_Move.md`](../rubrics/EX7_AE_Rig_and_Move.md)
**Handout:** H8 (After Effects & File Discipline)

---

## The assignment

A `.psd` is supplied. It contains three layers: **a character's body, the character's arm, and a background**: one house, one environment, flattened onto a single layer.

Make a short shot in After Effects:

1. The character **walks toward camera**
2. **Waves**
3. **Goes inside the house**

Five to eight seconds. That's it.

**We build this together in Class 11.** You do not need to know After Effects. You need to be in the room, and then you need to do it again yourself.

---

## The five things you have to actually do

Each of these is a specific technical step, and each is worth points on its own. Nothing is hidden.

**1 · Import the `.psd` as a composition, layers intact.**
*Import As: Composition: Retain Layer Sizes.* If you import it as footage you get one flat image and none of the rest of this is possible.

**2 · Move the arm's anchor point to the shoulder, then parent the arm to the body.**
Both halves matter. Parenting without moving the anchor point gives you an arm that rotates around its own middle, which looks like a propeller. The anchor point is *where the joint is.*

**3 · Animate the body toward camera.**
Position and scale, keyframed. The arm should follow without you touching it. That's what parenting is for, and watching it happen is the point of step 2.

**4 · Wave: rotation keyframes on the arm.**
On the *arm* layer, which is parented, so the wave is happening in the body's space. Three or four rotation keys. Badly is fine.

**5 · Exit into the house: mask the background.**
The background is **one flat layer**, so the doorway isn't a separate object you can put the character behind. You have to make one: duplicate the background, mask out everything except the doorway area, and put that copy **in front of** the character.

Step 5 is the only genuinely awkward part, and it's the reason this assignment exists in this form.

---

## Why step 5 is the assignment

You will hit it and think it's a limitation of the file. It isn't. It's the normal condition of the job.

Boards, matte paintings, and reference art arrive flat. Whenever something has to pass **behind** something else in a flat image, somebody makes a mask. There is no version of this work where that stops being true.

Which points at the question this session actually closes on, and the one you should be able to answer:

> **What would you have had to plan in the drawing to make this move easier?**

The answer is real and it will change how you prepare panels for **PR3** and **PR4**. If the doorway had been its own layer, step 5 would have been thirty seconds. If the arm had been drawn away from the body instead of overlapping it, step 2 would have been cleaner. If the background had been drawn wider, the character could have entered from off-frame.

**The move you want determines the artwork you need**, and you find that out either by planning it or by discovering it at 2am. Planning is faster.

---

## What to deliver

1. **A rendered movie**: `.mp4` or `.mov`, 5–8 seconds, plays without anyone intervening
2. **The project file**: `.aep`, so the rig is inspectable
3. **One paragraph** answering the question above

---

## Software

After Effects. This is one of the few times in this program you'll be walked through it, and a fair number of you will need it later: for **PR3**, for **PR4**, and for work after this course.

If your machine can't run it, tell me before Class 11 rather than after Class 12.

---

## What is not graded

**Animation quality.** The walk can be a slide. The wave can be a metronome. There is no easing requirement, no arc requirement, no timing requirement.

**Drawing.** All the artwork is supplied.

**Polish.** No transitions, no effects, no sound. It is a rig test.

---

## The honest version

This is close to a free twenty points if you attempt it, and zero if you don't. There is no middle.

It is here because it's one of the only structured After Effects exposures in your program, and because **PR3 is due one session later** and will be much harder for anyone who skipped this. That is not a threat, it's a schedule.

Attempt it badly rather than not at all. A submission where the mask is visibly wrong still scores most of the points, because four of the five steps are still there and I can see exactly where you got stuck, which means I can fix it in two minutes at the desk.
