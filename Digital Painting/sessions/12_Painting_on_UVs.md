# Class 12: Painting on UVs, and Maya as the Mirror

**Digital Painting · session 12 of 19 · P2 albedo pass due**

> **The argument of the day:** the map is not the deliverable. The surface is. Go
> look at it.

---

## The clock

| Time | Block | Minutes |
|---|---|--:|
| 0:00 | Recall: the three questions, albedo passes collected | 10 |
| 0:10 | Lecture: what a UV is, and painting into a flattened world | 30 |
| 0:40 | Demo: the round trip, live | 25 |
| 1:05 | Where the machine fits: generated maps in the viewport | 10 |
| 1:15 | Studio: load, look, fix, repeat | 60 |
| 2:15 | Exit ticket | 15 |

Total 2:30.

---

## Recall

Five minutes. Three questions, three maps, from the room. Collect the albedo passes.

---

## Lecture beats

### Beat 1: What Maya is doing in this course

**Slide:** *Maya is a mirror. Nothing else.*

Say the boundary first, because half the room is nervous and the other half wants to
model something.

Nobody models anything. Nobody unwraps anything. The prop exists, the UV layout
exists, the shader is already wired, the lights are already placed. The entire Maya
component of this course is: save your maps into the right folder, reload, look, and
go back to Photoshop.

That is not a simplification for a classroom. It is close to how a texture painter
actually spends a day, which is mostly in the painting application with a viewport
open next to it.

### Beat 2: A UV is the object, unwrapped

**Slide:** *Cut it. Flatten it. Paint the flat thing.*

The physical object, and it does the whole job: a UV layout is the pattern for a
sewn garment, or the flattened cardboard a cereal box was cut from before it was
folded.

Take an object, cut along some seams, unfold it until it lies flat, and lay it on a
square sheet. That flat arrangement is the UV layout. Painting on the sheet paints
the object, because every point on the sheet corresponds to a point on the surface.

Two things follow immediately and both matter. The cuts are called seams, and paint
has to continue across them or a line appears on the object. And the flattening
distorts, so a shape painted on the sheet is not exactly the shape that lands on the
object, especially anywhere the surface curves hard.

### Beat 3: Reading a UV layout

**Slide:** *Shells. Seams. Padding. Scale.*

Four things to point at on the provided template.

**Shells** are the separate islands, each one a piece of the object. **Seams** are
where the cuts happened, and they are where paint has to match on both sides.
**Padding** is the bleed of a few pixels past the edge of every shell, which exists
because the renderer samples slightly outside the boundary and an unpadded shell
gets a dark fringe. **Scale** is how much sheet each shell was given, which tells
you how much resolution that part of the object will have.

That last one is worth a moment. A shell taking up a quarter of the sheet will be
four times sharper on the object than one taking up a sixteenth, which means detail
painted at the same size in Photoshop will land at different sizes on the surface.

### Beat 4: Painting across a seam

**Slide:** *Paint both sides. Check the object.*

The practical problem, and the honest answer.

There is no clever trick available in Photoshop alone. Paint up to the seam on one
shell, paint the matching thing on the other side, load the map, and look at the
object. It will be slightly wrong. Fix it. Look again.

That loop is the actual craft, and it is why the next beat matters more than
anything else today.

### Beat 5: The loop is the method

**Slide:** *Paint. Load. Look. Fix.*

The thing to say plainly, because students will try to avoid it.

A texture painter does not paint a map and then check it. They paint for ten minutes,
look at the object, paint for ten minutes, look at the object, all day. The flat map
lies constantly: it looks even and lands blotchy, it looks detailed and lands
invisible, it looks correct and lands upside down on one shell.

A student who paints for three hours and looks once at the end will produce something
that needed the three hours spent differently. This is also, more or less, the same
argument as the blockout in class 5 and the four by four test in class 10, arriving a
third time.

### Beat 6: What the viewport will tell you that the map did not

**Slide:** *Too even. Too small. Too dark. Wrong way up.*

Prepare them for the specific disappointments, because knowing the list in advance
turns disappointment into diagnosis.

**Too even.** Wear that looked placed on the flat map reads as uniform noise on the
object, because the object curves away and compresses it. **Too small.** Detail
painted at a comfortable zoom level disappears entirely at viewing distance.
**Too dark, or too light.** A map that looks right on a bright monitor in Photoshop
sits differently under a light rig, every time. **Wrong way up.** Something painted
on a shell that turns out to be the underside, or rotated ninety degrees.

None of these are failures. They are the information the mirror exists to provide.

### Beat 7: The cold reversal

**Slide:** *Which map produced which render?*

Three renders and three maps, shuffled, no answers. Match them.

The interesting pairing is the map that looks best flat and produced the worst render.
Let the room argue. Do not settle it, because the studio hour settles it for everyone
individually in about twenty minutes.

---

## The demo

Twenty-five minutes, live, one full round trip. The point is the loop, so run it
three times rather than once.

1. Open the P2 Maya scene. Show the shader, the three file nodes, and where the maps
   are read from. Ten seconds each, no more.
2. Save a deliberately unfinished albedo into the folder. Reload the texture. Look.
3. Name three things wrong, out loud, using Beat 6's list.
4. Back to Photoshop. Fix one of the three. Save. Reload. Look again.
5. Repeat once more.
6. **The deliberate mistake:** paint a piece of detail at a comfortable zoom, be
   pleased with it, load it, and discover it is invisible at viewing distance. Go
   back and paint it at roughly three times the size. Narrate the correction as a
   rule: anything meant to read has to be painted bigger than feels right.
7. Rotate the light. Show that the albedo holds up because there is no lighting baked
   into it, then swap in the baked version from class 11 for five seconds to show the
   contrast one last time.

---

## Where the machine fits

Ten minutes.

**The beat.** Generated material enters here the same way it entered everywhere else,
and this session gives it the harshest test available, which is that the result is
being judged on an object under a light rig rather than as a thumbnail.

Put a generated texture in as an albedo and look at it in the viewport. Two things
will usually be true. It will be somewhat convincing at a glance, and it will have
lighting baked into it, because a generator asked for "rusted metal" produces a
photograph of rusted metal under some particular light rather than a flat sample of
the material. So the object arrives with a shadow that does not move, which is class
11's Beat 2 failure, and the room has now seen it three times.

Then show the useful version, because there is one and pretending otherwise would be
dishonest. Generate a plate, strip the lighting out of it by hand using frequency
separation from class 10, use it as a starting layer, and paint on top. That is a
source being integrated, which is the same thing the course has said in every one of
these segments.

Say the rule for the last time in this unit: generated material is a source, sources
get integrated, and the integration is what is graded.

**The non-generative equivalent.** A photograph from EX5 or a stock texture goes
through the identical treatment and produces the identical lesson. Nothing in P2
requires a generator at any tier.

---

## Studio

Sixty minutes.

**1:15 The loop (45 minutes).** Load the albedo pass. Look. Write down three things
the viewport revealed. Fix them. Load again. Minimum three full round trips in the
block, and the count is checked.

Circulate constantly. The only question at every desk today: what did the viewport
tell you, and what did you change because of it.

**2:00 CHECKPOINT.** Before and after renders on the projector, six or seven of them.
Not the maps. The renders. The room says what changed.

---

## Tiers for today's work

| Tier | The loop |
|---|---|
| **Baseline** | Three observations written down about the albedo, from the viewport if the machine cooperates, or from a paired classmate's screen if it does not. The looking is the requirement rather than the software, and the fixes do not have to land today. |
| **Target** | Three full round trips, with a before and after render showing a real change and a written note on what the viewport revealed. |
| **Extension** | Start the roughness map today and loop on that instead, since it is where most of the believability lives and it benefits most from the mirror. |

---

## Exit ticket

One viewport render, plus one sentence: the thing you changed because of what you saw.
Not a list. One thing.

---

## What breaks

**Maya will not open, or the paths are wrong.** Budget for it. Have the scene tested
from a student machine rather than yours, have a second machine ready, and have a
pairing plan so a student who is locked out works alongside somebody who is not.
Baseline does not require Maya for a reason, and today is the day that reason gets
used.

**Somebody tries to model something.** Usually a student who has had a 3D course and
is bored. Redirect once, plainly: this session is the mirror, and the painting is the
assignment.

**The loop gets run once.** Students will paint for forty minutes and load at the
end, because switching applications feels like an interruption. The three round trip
minimum is checked at the desk, not on the honor system.

**The first render is demoralizing.** It nearly always is. Beat 6 exists so the room
knows the list in advance, and it is worth saying again at the checkpoint: the
viewport is not a verdict, it is a note, and a note is data.

**Detail painted too small.** Universal. The demo's deliberate mistake preloads it and
the fix at the desk is the same sentence: paint it about three times bigger than
feels right.

---

## Prep

- The Maya scene, opened and tested from a student machine, with relative paths
  confirmed.
- A second machine, or a plan for pairing.
- The baked-lighting albedo from class 11, for the five-second contrast.
- A generated texture for the machine beat, plus the stripped version already prepared
  so the useful path can be shown rather than described.
- Three maps and three renders, shuffled, for the cold reversal.
- Albedo passes collected at the start.
