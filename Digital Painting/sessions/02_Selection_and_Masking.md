# Class 2: Selection, Masking, Blend Modes

**Digital Painting · session 2 of 19**

> **The argument of the day:** almost every composite that fails, fails at the edge.

---

## The clock

| Time | Block | Minutes |
|---|---|--:|
| 0:00 | Recall: the working file test, and EX1 collected | 10 |
| 0:10 | Lecture: selection, the edge, blend modes | 30 |
| 0:40 | Demo: one hard edge, three ways | 20 |
| 1:00 | Where the machine fits: generative fill and the edge | 10 |
| 1:10 | Studio: the edge set | 70 |
| 2:20 | Exit ticket | 10 |

Total 2:30.

---

## Recall

Five minutes, out loud. Ask the question from class 1 and make somebody answer it:
**could a stranger open your file and change the sky?** Collect EX1. Do not grade it
in front of them.

---

## Lecture beats

### Beat 1: Nobody gets hired for their selections

**Slide:** *The selection is never the point.*

Open by lowering the stakes on the technique and raising them on the outcome. There
are perhaps eight ways to make a selection in Photoshop and the room will meet most
of them today, but none of that is the skill. The skill is knowing what kind of edge
the thing you are cutting out actually has, and then producing that edge.

A brick wall, a chrome bumper, a glass of water, and a dog all need different edges,
and the tool matters much less than the decision.

### Beat 2: Four kinds of edge

**Slide:** *Hard. Soft. Feathered. Fuzzy.*

Physical objects for each, and do not explain the metaphor after it lands.

A **hard** edge is a cut sheet of metal. It is sharp because the object is sharp and
the camera was focused on it. A **soft** edge is anything out of focus, and it is
soft because the lens was looking somewhere else. A **feathered** edge is a shadow
falling across a floor, where the transition is gradual because the light source has
size. A **fuzzy** edge is hair, fur, a pine tree at distance, smoke: the edge is not
an edge at all, it is thousands of small objects, and any attempt to draw a line
through them produces a helmet.

Most student composites fail because everything in them has the same edge, usually a
slightly feathered hard edge, which is the default the software hands you.

### Beat 3: The selection tools, ranked by how often they are right

**Slide:** *Subject. Color range. Pen. Brush on a mask.*

Go quickly. The tools are not the lesson.

Select Subject and Object Selection get you eighty percent of the way in two
seconds, and the remaining twenty percent is the part that matters. Color Range is
the right answer more often than students expect, particularly for skies and for
anything shot against a consistent background. The Pen tool is the right answer for
anything manufactured, because manufactured things have the kind of edge a path
describes. And painting directly on a mask with a brush is the right answer more
often than any of them, especially for fuzzy edges, and it is the one students skip
because it feels like it is not a real technique.

### Beat 4: The mask is the edit

**Slide:** *Black hides. White reveals. Gray is halfway.*

Three sentences and a physical object: a mask is a stencil, and the thing about a
stencil is that cutting it wrong does not ruin the paint.

Repeat the day-one move: a mistake on a mask costs nothing, because the pixels are
still there. This is why every removal in this course happens on a mask, all term,
without exception.

### Beat 5: Blend modes, the three that matter

**Slide:** *Multiply darkens. Screen lightens. Overlay does both.*

Twenty-seven blend modes exist. Three of them do most of the work, and knowing why
is more useful than memorizing the list.

Multiply darkens, and it is how shadows, dirt, ink, and stains behave, because all
of those are things that subtract light. Screen lightens, and it is how glows, fog,
haze, and lens flare behave, because those add light. Overlay does one on the dark
half and the other on the light half, which is why it is the one people use for
texture and the one that goes wrong most often.

The underlying idea, said once and then referred back to: a blend mode is arithmetic
on light. Multiply is light being blocked. Screen is light being added. Everything
else is a variation on those two, and knowing which one a real-world thing is
usually tells you which mode to reach for.

### Beat 6: The cold reversal

**Slide:** *Which mode, and why?*

Four images on screen: a shadow across pavement, a neon sign reflected in a wet
street, a coffee stain on paper, and the beam of a flashlight in dust.

Ask the room which blend mode each one wants, and make them say why in terms of
light being added or blocked. Do not show the answers. Do not resolve it before the
studio block. The students who work it out during the studio will remember it, and
the ones who are told will not.

---

## The demo

Twenty minutes, live.

One image, one hard subject to cut out, and the same cut made three ways so the
difference is visible rather than described.

1. **Select Subject, straight out of the box.** Show it on the projector against a
   contrasting background so the halo is obvious. Name what is wrong: a uniform edge
   on a non-uniform object.
2. **The same cut, refined.** Select and Mask, the edge brush on the hair, decontaminate
   colors. Show the improvement and also show where it still fails.
3. **The same cut, painted on a mask by hand**, for the twenty percent the automatic
   pass could not reach. Slowly, with a soft brush, at low flow.
4. **The deliberate mistake:** paint on the mask with the wrong color and let the
   subject disappear. Say "good, that costs nothing," and paint it back. Every term,
   somebody in the room exhales at this.
5. Drop the cut subject onto a second background and let it look wrong. Ask why.
   Somebody will say the edges. Somebody sharper will say the values. Both are right
   and the second one is class 3.

---

## Where the machine fits

Ten minutes.

**The beat.** Generative fill is a masking tool that also paints. Everything it does
is governed by a selection, which means a bad result is very often a selection
problem rather than a model problem. Demonstrate that directly: run the same fill
twice on the same image, once with a sloppy selection and once with a selection that
includes a little more context around the hole, and let the room see the difference.

**Where it fails, and this is the part that matters.** Look at the edge. Generated
content meets existing content along the selection boundary, and that boundary
frequently carries a faint smear, a shift in grain, or a change in focus that the
eye reads as wrong before it can say why. The fix is the same fix as always: mask
the result, feather it correctly, match the grain.

State the general rule once. A generated element is a source, exactly like a stock
photograph. It has to be integrated, and integration is the graded skill.

**The non-generative equivalent.** Everything shown here is achievable with
content-aware fill, the clone stamp, and a patch from elsewhere in the same
photograph, which is how it was done for twenty-five years and how it is still done
when the client will not permit generated pixels. Students who prefer that route use
it and lose nothing: the studio exercise is scored on the edge, not on how the hole
got filled.

---

## Studio

Seventy minutes.

**1:10 The edge set (60 minutes).** Four source images, each with a different kind
of edge: something manufactured and hard, something out of focus, something with a
cast shadow, and something fuzzy. Cut all four onto one neutral background.

The point is not four good cutouts. The point is four *different* edges in one file,
which makes the difference visible in a way that four separate exercises never do.

**1:50 CHECKPOINT.** Everyone stops. Two files on the projector, zoomed to 200% at
the edges, which is the only honest way to look at this work. Ask the room to find
the halo before the artist points at it.

**2:00 Back to it (20 minutes).** Fix what the checkpoint found. Anybody finished
early moves to the Extension tier below.

---

## Tiers for today's work

| Tier | The edge set |
|---|---|
| **Baseline** | All four subjects cut onto the neutral background, every removal on a mask rather than with the eraser. |
| **Target** | Four visibly different edges, appropriate to each subject, holding up at 200%. |
| **Extension** | Add a fifth: something transparent. Glass, water, smoke, a windshield. Transparency is not a cutout problem at all, it is a blend mode problem, and working that out is the exercise. |

---

## Exit ticket

One mask, posted: the fuzzy-edged subject, cropped tight, at 200%, on the neutral
background. Nothing else. The tight crop is the point, because that is where the
work either holds or does not.

---

## Assigned

**EX2 The Working File**, due at the start of class 3. Take the edge set file and
rebuild it as a delivery: named groups, every mask intact, one flattened JPEG, one
layered PSD, correct folder name. Add a two-sentence note naming which edge was
hardest and why. Under an hour.

---

## What breaks

**The room wants tool tips and will keep asking for them.** Questions will arrive
all session in the form of "what's the shortcut for." Answer briefly and steer back
to the decision: which edge does this object have. The tool answers are on the
internet and the decision is not.

**Everything ends up the same edge.** The default outcome of this exercise is four
cutouts that all look automatic, because the automatic pass got them to eighty
percent and eighty percent looks fine at fit-on-screen. The 200% checkpoint exists
entirely to break that, so do not soften it.

**Generative fill eats the studio block.** If it is on screen at all, some of the
room will spend forty minutes rerolling prompts instead of cutting edges. Keep the
beat to ten minutes, keep it on the projector rather than on their machines, and
tell them plainly that the exercise is scored on the edge.

**Blend modes get memorized instead of understood.** If the answer to "why Multiply"
comes back as "because that's the one for shadows," push once: what is a shadow made
of. The answer is light being blocked, which is what Multiply does, and a student
who gets there once never needs the list again.

---

## Prep

- Four source images with deliberately different edge types, plus one neutral
  background plate.
- The transparency image for the Extension tier.
- The generative fill demo image, with a hole worth filling, and a rehearsed sloppy
  selection to contrast against a good one.
- The four cold-reversal images for Beat 6, on a slide, with no answers on it.
- EX1 collected and skimmed before class 3, since it determines how much review
  class 3 needs.
