# DECK 13: AFTER EFFECTS FOR BOARDS
**19 slides + live build-along · Class 11 · Paired with EX7 · BUILT**

## Why this deck exists

The After Effects exercise has been running every term with **no deck, no brief, no rubric and no handout.** It was walked through live and existed nowhere in writing. For a meaningful number of these students it is also the only structured AE exposure they get before they need it, and PR3 is due shortly after.

It is the cheapest deck in the set to build: screenshots, not licensed film stills. Nothing here needs `[ADD IMAGE:...]` sourcing.

**The design risk is that this becomes a tutorial**, which `CLAUDE.md` §3 forbids: software is never the subject. The guard is structural: the deck teaches exactly five operations, and closes on a design question rather than a technique. If it grows past five operations, or if easing and effects appear, it has crossed into Motion Graphics' territory (`CURRICULUM.md`) and should be cut back.

Format: build along live, everyone's screen up, one operation at a time. The slides are the reference, not the delivery.

---

### PART 1 WHY YOU'RE HERE (1-3)

> Built as 19 slides: a section divider was added before the five operations, since the class is a live build-along and the break is useful.

**1 · Title**: After Effects for Boards

**2 · What this is and isn't**
This is five operations, chosen because they're what an animatic needs. It is not a motion graphics course. That one exists and it isn't this.
*You will not learn After Effects today. You'll learn the corner of it that makes your boards move.*

**3 · Why an animatic needs any of this at all**
Boards handle blocking, camera and action. They can't hold duration. Everything in this session exists to get the fourth dimension onto work you've already made.
*Forward: PR3 is due shortly and PR4 needs it too.*

---

### PART 2 THE FIVE OPERATIONS (4–13)
> Build along. One at a time. Everyone's screen visible.

**4 · Operation 1: Import with layers intact**
`File → Import → File`, then **Import As: Composition: Retain Layer Sizes.**
Three-way comparison: *Footage* gives one flat image · *Composition* gives layers resized to the comp · *Retain Layer Sizes* gives layers at their own dimensions with usable anchor points.
*Get this wrong and nothing else in the session is possible. It's also invisible until you try to move something.*

**5 · Why "Retain Layer Sizes" and not just "Composition"**
Diagram: the same arm layer under both settings, with the anchor point marked.

**6 · Operation 2: The anchor point is the joint**
**Y** for Pan Behind, drag the anchor to the shoulder, **V** to get back.
Side by side: an arm rotating around its own middle vs. around the shoulder.
*One is a propeller. One is an arm. That's a single drag.*

**7 · Anchor points, generalized**
Every rotation and scale in this program happens around the anchor. Once you see it as *the joint*, it stops being a technicality.

**8 · Operation 3: Parenting**
The Parent & Link column, the pick-whip, the child inheriting position, rotation and scale while keeping its own on top.
Build the chain outward from the root: body → upper arm → forearm → hand.

**9 · The thing that surprises everyone once**
A parented layer's values are now **relative to the parent.** Move the body, the arm follows and its own position number doesn't change.
*This surprises everyone exactly once, and then never again.*

**10 · Operation 4: Keyframes, minimally**
Stopwatch on, move the playhead, change the value. That's it.
*No easing. No graph editor. Not today, and not on the rubric.*

**11 · Operation 5: Masks**
Pen tool **(G)**, closed shape, everything outside disappears. Mask Feather at 1–2px hides a great deal.

**12 · The move that matters: making something to hide behind**
Step diagram: duplicate the background → mask the copy down to the doorway → drag it **above** the character.
*The character now walks behind a thing that was never a separate object.*

**13 · Why the file is like that**
It isn't broken. **Boards, matte paintings and reference art arrive flat.** Anything that has to pass behind anything else in a flat image gets a mask. There is no version of this job where that stops being true.

---

### PART 3 GETTING IT OUT (14–16)

**14 · Frame rate and comp size**
Pick 24 or 30 **at the start** and never change it: changing it later shifts every keyframe you've set. Comp size matches your delivery ratio: 1920x1038 for 1.85, 1920x803 for 2.39.

**15 · Numbered sequences**
`SEQ01_SH010.png`, incrementing by ten, imported as a PNG Sequence.
*By ten so you can insert SH015 later without renaming everything downstream. You will need to.*

**16 · Export**
`File → Export → Add to Adobe Media Encoder`, H.264, Match Source – High Bitrate.
*The render queue's default is AVI Lossless, which produces a file in the gigabytes that nobody can play. It's the most common way to lose an evening.*

---

### PART 4 THE POINT (17–18)

**17 · The question this session is actually about**
> **What would you have had to plan in the drawing to make this move possible?**

The doorway as its own layer. The arm drawn clear of the torso. The background drawn wider so the character could enter from off-frame. A pan needs artwork past the frame edge; a push needs artwork bigger than the frame.
*You find this out either by planning it, or by discovering it at 2am.*

**18 · Which is the whole lesson**
The tool is not the subject. **The move you want determines the artwork you need**, and knowing that before you draw is the difference between a two-hour animatic and a two-day one.
*That's the same argument as the floor plan, the beat sheet, and every milestone in this course: the cheap decision made early replaces the expensive one made late.*

---

## Assignment pairing

**EX7: AE Rig & Move**, 3% of the course grade. Brief and rubric exist. Graded on the five operations independently, plus the planning paragraph, which is why a student whose mask fails still scores most of the points and can be fixed in two minutes at the desk.

## Handout pairing

**H8: After Effects & File Discipline.** Written. Carries the five operations, the settings that break things, and the naming/versioning/audio-sourcing material that PR3 grades and no session teaches.

## Boundary

CA 140 owns AE **as an animatic tool**: these five operations. Motion Graphics owns it as a craft. See `CURRICULUM.md`, which flags this as the one row where two courses touch the same software rather than the same idea, and worth confirming with that instructor-of-record.
