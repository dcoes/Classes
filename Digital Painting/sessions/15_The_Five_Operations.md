# Class 15: The Five Operations

**Digital Painting · session 15 of 19 · P3 layer plan due**

> **The argument of the day:** a camera move is an amplifier. It makes a good file
> better and a bad file worse, and it does nothing on its own.

---

## The clock

| Time | Block | Minutes |
|---|---|--:|
| 0:00 | Recall: the parallax test, layer plans collected | 10 |
| 0:10 | Lecture: what a move is for, and the boundary | 20 |
| 0:30 | Demo: the five operations, live, start to finish | 30 |
| 1:00 | Where the machine fits: generated motion | 10 |
| 1:10 | Studio: the push, or the plan for one | 65 |
| 2:15 | Exit ticket and EX7 handout | 15 |

Total 2:30.

---

## Recall

Five minutes. The parallax test, asked of two objects in an image on screen. Collect
the P3 layer plans.

---

## The boundary, stated first

Two minutes, and it goes before the lecture rather than inside it.

After Effects belongs to the Motion Graphics course, which owns it as a craft:
effects, expressions, motion design, compositing. This session borrows the smallest
usable piece of it and stops there, and it is five operations.

Say that out loud to the room, for two reasons. It tells the students who have taken
Motion Graphics that nothing here is competing with what they already know, and it
tells everybody else that the scope is genuinely small and they are not about to be
graded on an application they met forty minutes ago.

The grade is in the painting. The move is on the Extension tier. Neither of those
facts changes today.

---

## Lecture beats

### Beat 1: Why a still painting gets moved at all

**Slide:** *Parallax is the only depth cue that needs time.*

Open with the mechanism, because it is genuinely interesting and it takes one minute.

Every depth cue used so far works in a still image: overlap, atmosphere, scale,
convergence, focus. There is one that does not, and it is parallax, meaning near
things sliding past far things as the viewpoint changes. It is the cue the human
visual system trusts most and the only one a static painting cannot supply.

That is the entire reason this technique exists. Six seconds of a slow push buys a
depth cue that no amount of rendering can produce, and it costs about twenty minutes
once the file is cut correctly.

### Beat 2: The move is an amplifier

**Slide:** *Good file, better. Bad file, worse.*

The honest warning, delivered before anybody opens the application.

A move does not rescue a painting. It reveals it. Every unpainted hole becomes
visible, every plane that was cut at the wrong depth slides wrong, every soft edge
that was hiding a mistake stops hiding it. A mediocre painting with a slow push is a
mediocre painting that is now moving.

So the sequence is not negotiable: finish the painting, cut it correctly, paint the
holes, and only then move it.

### Beat 3: Slow, short, and one thing

**Slide:** *Six seconds. One move. No cuts.*

Three constraints, and all three exist because students will otherwise build
something that fights the painting.

**Slow.** A fast move destroys a matte painting, because the eye stops reading the
image and starts tracking the motion. **Short.** Six to ten seconds. A longer move
exposes more of the holes and there is no more file to expose. **One thing.** A push,
or a drift, or a slow rise. Not a push that becomes a tilt that becomes a rotation.

Name the reason plainly: the painting is the subject and the move is a way of looking
at it, rather than the other way around.

### Beat 4: Easing, and why a linear move looks wrong

**Slide:** *Nothing real starts at full speed.*

Ninety seconds, one idea, and it is the difference between a move that reads as a
camera and one that reads as a slideshow.

A camera on a dolly has mass. It accelerates, holds, and decelerates. A keyframe with
no easing starts instantly at full speed and stops instantly, which nothing physical
does, and the eye reads it as mechanical even when nobody can say why.

Ease both ends. That is the whole lesson and it is one keyboard shortcut.

### Beat 5: The five operations, listed

**Slide:** *Import. 3D. Camera. Ease. Export.*

Read them once, then do them in the demo. Nobody takes notes on a list.

1. Import a layered PSD as a composition, retaining layer sizes.
2. Set the layers to 3D and push them apart in Z.
3. Add a camera and set two position keyframes.
4. Ease the keyframes.
5. Export.

Say the containment out loud one more time, because it is what keeps this session
honest: no effects, no expressions, no plugins, no motion design. If those are
wanted, Motion Graphics is the course that teaches them properly.

### Beat 6: The scale problem nobody warns you about

**Slide:** *Push it back. Scale it up.*

The single thing that confuses everyone at step 2, worth naming before it happens.

Moving a layer away in Z makes it smaller, because that is what distance does. So a
background pushed back leaves a gap around the edges of the frame. The fix is to
scale it up until it fills the frame again, and the ratio is not something to
calculate, it is something to adjust by eye until the composition looks the way it
did in Photoshop.

Students who do not know this is coming will assume they broke something.

---

## The demo

Thirty minutes, live, the whole round trip on a file the room has already seen.

Use the demo painting from class 14, the one they watched get cut, so the file is
familiar and the only new thing is the application.

1. **Import.** File, Import, choose Composition retaining layer sizes. Say why that
   option and not the other one: it keeps each layer at its full size rather than
   cropping to the canvas, which matters the moment anything moves.
2. **3D.** Switch the layers to 3D. Nothing visibly changes. Push the far plane back
   in Z. It shrinks. Scale it up to fill. Repeat for each plane, working back to
   front.
3. **Camera.** Add a camera. Set a keyframe at frame zero, move forward in time, move
   the camera in, set a second keyframe. Play it. There is now parallax and the room
   should see it immediately.
4. **Ease.** Play the unease version first and let it look mechanical. Ease both ends.
   Play again. The difference is larger than anyone expects from one shortcut.
5. **The deliberate mistake:** push the camera far enough that an unpainted hole is
   exposed. Stop. Point at it. Say that this is exactly what class 14 was about, and
   that the fix is in Photoshop rather than here. Pull the move back to where the file
   supports it.
6. **Export.** Render queue or Media Encoder, h264, 1920 by 1080. Name the file
   correctly, out loud, the same way class 1 did.

Total elapsed, narrated at the end: about twenty minutes of work on a file that was
already cut properly. That number is the argument for class 14.

---

## Where the machine fits

Ten minutes.

**The beat.** Generative video tools will take a still image and produce motion from
it, and it is worth looking at honestly rather than dismissing.

Show one. Two things will be visible, and the room now has the vocabulary for both.
The motion is frequently convincing for a second or two, and then consistency starts
to fail: a detail drifts, a straight line bends, a texture crawls, something in the
background quietly becomes a different thing. That is the hard problem in generative
video and it is the same problem as class 12's baked lighting seen from another
angle, which is that the tool is producing an appearance rather than a structure.

The contrast worth drawing, and it is the point of the segment: the parallax push
built in this session is not an appearance. It is a file with known planes at known
depths, and it will be identical on the hundredth render. When a client asks for the
move to be two seconds longer, one of those two approaches can answer and the other
one rerolls and hopes.

Say the honest part too. This will get better, possibly a great deal better, and the
consistency problem is exactly the kind of problem that gets solved. What does not
get solved by a better model is somebody deciding what the shot is for, which is the
paragraph they wrote in class 14.

**The non-generative equivalent.** Everything in this session is the non-generative
path already. Nothing in EX7 or in the P3 Extension tier involves a generator.

---

## Studio

Sixty-five minutes.

**1:10 The push (50 minutes).** Two routes, both legitimate, and the room picks.

Students working toward the Extension tier import their cut file and build a six
second push. Students who are not import the provided demo file and do the same thing
on it, which takes twenty minutes and means everybody has done it once whether or not
it ends up in their final.

Students who would rather spend the time on the painting spend it on the painting.
Say that clearly. The move is the top tier and the painting is the grade.

**1:50 CHECKPOINT.** Four or five moves on the projector, played once each. Two
questions only: is it too fast, and is anything exposed that should not be.

**2:00 Back to it (15 minutes).**

---

## Tiers for today's work

| Tier | The move |
|---|---|
| **Baseline** | No move required. A layer plan for P3 with one sentence per group saying what it is for. |
| **Target** | The five operations completed once on any file, provided or your own, and exported. |
| **Extension** | A six to ten second move on your own P3 file, eased, exposing nothing unpainted, at 1920 by 1080. |

---

## Exit ticket

A six second push, exported, or the written layer plan for one. Either is complete.

---

## Assigned

**EX7 The Five Operations**, due at the start of class 16. The five operations run
once on any layered file, exported as an mp4, plus one sentence on which operation
gave you trouble. Under an hour. Not required by any P3 tier below Extension.

---

## What breaks

**Somebody builds a motion graphics piece.** The student who already knows After
Effects will add a light leak, a lens flare and a text card. It is not a disaster and
it is out of scope. Say so once, kindly, and note that none of it is on the rubric.

**The move is too fast.** Universal on the first attempt. Six seconds feels
interminable while building it and reads as correct on playback. The checkpoint
question catches it.

**Holes get exposed and the student keeps going.** The instinct is to shorten the
move until the hole is hidden, which is a workaround rather than a fix. The fix is in
Photoshop and it takes ten minutes.

**The scale problem causes a panic.** Beat 6 preloads it and somebody will still
believe they broke the file. It is thirty seconds to resolve at the desk.

**Render settings eat the last twenty minutes.** Have the export settings written on
the board before class. This is the least interesting way to lose a studio block.

---

## Prep

- The class 14 demo painting, already cut into planes, saved as a layered PSD.
- A provided cut file for students who are not using their own, tested.
- One generative video example for the machine beat, chosen because the consistency
  failure is visible rather than because it is bad.
- Export settings written on the board.
- After Effects confirmed working on the lab machines, tested from a student login.
- Layer plans collected at the start.
