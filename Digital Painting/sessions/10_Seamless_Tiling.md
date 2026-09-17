# Class 10: Seamless Tiling

**Digital Painting · session 10 of 19**

> **The argument of the day:** the seam is easy to remove. The repeat is the hard
> part, and it is what the eye actually catches.

---

## The clock

| Time | Block | Minutes |
|---|---|--:|
| 0:00 | Recall: the four behaviors, EX5 collected | 10 |
| 0:10 | Lecture: offset, repair, frequency | 25 |
| 0:35 | Demo: one tile, start to finish | 25 |
| 1:00 | Where the machine fits: generated tiles and the seam | 10 |
| 1:10 | Studio: build a tile | 65 |
| 2:15 | Exit ticket and EX6 handout | 15 |

Total 2:30. Short lecture, heavy demo, heavy studio. This is a technique day.

---

## Recall

Five minutes. Name the four behaviors from class 9 and give an example of each from
the room rather than from the slide. Collect EX5 and put the student-photographed
seventh swatches up while people settle.

---

## Lecture beats

### Beat 1: Why anything tiles at all

**Slide:** *One square. A thousand square feet.*

Start with the economics, briefly, because it explains every constraint that follows.

A game needs a warehouse floor. Painting a thousand square feet of concrete at a
usable resolution is not possible and would not fit in memory if it were. So one
square of concrete gets painted, perhaps two feet across, and it gets repeated across
the whole floor.

Everything difficult about tiling comes from that repetition. The square has to meet
itself on all four sides without a visible join, and it has to survive being seen
forty times at once without announcing that it is the same square forty times.

### Beat 2: The offset trick

**Slide:** *Move the seam into the middle. Fix it there.*

The technique is old, simple, and takes about ninety seconds to explain.

The problem with a seam is that it sits at the edge of the canvas where you cannot
paint across it. So move it: offset the image by half its width and half its height,
which wraps the edges into the center of the frame and puts the join somewhere you
can reach. Paint it out with the clone stamp, the healing brush, or a patch from
elsewhere in the image. Offset back. The edges now match.

A physical object for it, since students remember it better this way: it is the same
move as rotating a tablecloth to get the stain off the corner and onto the middle of
the table, where you can work on it.

### Beat 3: The seam is not the problem

**Slide:** *Nobody sees the seam. Everybody sees the repeat.*

The beat that actually matters, and the one most tutorials skip.

Offsetting removes the join in about four minutes. What it does not remove is the
thing the eye is genuinely good at catching, which is pattern. Repeat a square forty
times and any distinctive feature in it becomes a grid: one dark blotch, one bright
stone, one crack, and suddenly the floor has polka dots.

The eye finds repeating features almost involuntarily, faster than it finds edges, so
this is where the work goes.

### Beat 4: Killing the repeat

**Slide:** *No hero features. Even value. Break the grid.*

Three fixes, ranked by how much they buy.

**Remove hero features.** Anything unusually dark, bright, or distinctive has to go
or be reduced, because that is what becomes the polka dot. This feels like removing
the interesting parts, and it more or less is, and it is correct.

**Even out the large value structure.** A tile that is darker in one corner will
produce visible banding across a floor. Flatten the low-frequency variation until the
tile is roughly uniform at a squint, keeping all the detail. That is what frequency
separation is for, and it is Beat 5.

**Break the grid downstream.** Rotate, flip, overlay a large-scale variation pass, or
blend two tiles. Worth naming and worth being honest that most of this happens in the
engine or the shader rather than in Photoshop, which is somebody else's job.

### Beat 5: Frequency separation, in plain language

**Slide:** *Big shapes. Small details. Separately.*

The technique students have heard of and cannot explain.

An image contains large slow changes, meaning the overall lightness across the
surface, and small fast changes, meaning grain, pores, cracks, fibers. Frequency
separation puts those on two layers so they can be edited independently.

The practical use here is exactly one thing: flatten the large slow changes so the
tile does not band, without touching the small fast detail that makes it look like
concrete. A blur on the low layer, nothing on the high layer, and the tile stops
producing shadows across the floor that are not there.

Say plainly that this is also the retouching technique from every skin tutorial on
the internet, doing the same job for a different reason.

### Beat 6: The cold reversal

**Slide:** *Which of these tiles, and which one will you see?*

Four tiles on screen, each shown twice: once alone, once repeated in a four by four
grid. Show the single versions first and ask which will hold.

The room will usually pick the most interesting-looking tile, which is usually the
one that fails worst, because interesting means distinctive and distinctive means
polka dots. Show the grids after the vote. This is the fastest way to make Beat 3
permanent.

---

## The demo

Twenty-five minutes, live, one tile from a photograph to a working tile.

1. Start from a photograph of a flat surface, shot square, in even light. Crop
   square.
2. Look at it honestly and name the two problems: it is brighter in one corner, and
   there is one feature in it that will become a polka dot.
3. **Frequency separation first.** Split into low and high. Blur the low layer until
   the lighting variation is gone. Recombine. The tile now looks flatter and slightly
   boring, which is correct.
4. **Offset.** Half and half. The seam appears in the middle.
5. **Repair.** Clone and heal across the join, working along the structure of the
   material rather than across it.
6. Offset back. Show the edges meeting.
7. **Test by tiling.** Define as a pattern, fill a large canvas, and look at it at
   four by four. This is the only honest test and it should be run three times during
   any tile job.
8. **The deliberate mistake:** skip step 3 the first time through and go straight to
   the offset. The tile will look perfect alone and will band visibly at four by four.
   Go back and do the frequency pass. Narrate that the seam was never the problem.
9. Kill the remaining hero feature. Tile again. Stop.

---

## Where the machine fits

Ten minutes.

**The beat.** Generators will produce a texture readily and most of them will claim
to produce a tiling one. Test it the same way anything else gets tested: define as a
pattern and look at four by four on the projector.

Two things the room will see, and they are the two failures from this session rather
than anything exotic. The edges may or may not join, depending on the tool, and that
is the easy half. The lighting variation almost always survives, because the
generator produced an image of a lit surface rather than a flat sample of a material,
so the tile bands across the grid exactly the way step 3 of the demo banded.

The fix is the same fix: frequency separation, flatten the low, keep the high. The
generated tile enters the workflow at the same stage a photograph does, and it needs
the same treatment.

Say the general point once more, since this is the fourth time it has come up and it
should be starting to feel obvious: generated material is a source. Sources get
integrated. The integration is the job.

**The non-generative equivalent.** A photograph of a real surface from EX5, or a
stock texture, run through the identical steps. Nothing in the studio block or in EX6
requires a generator, and the exercise is scored on the four by four test.

---

## Studio

Sixty-five minutes.

**1:10 Build a tile (45 minutes).** One tile, 2048 square, from a photograph. Own
photography preferred, provided source acceptable. Test at four by four at least
three times during the build and keep screenshots of each test.

**1:55 CHECKPOINT.** Everyone fills a large canvas and puts it on the projector at
four by four. The room finds the polka dot. This takes about forty seconds per tile
and it is merciless in a useful way.

**2:05 Kill what the room found (10 minutes).**

---

## Tiers for today's work

| Tier | The tile |
|---|---|
| **Baseline** | Edges join. No visible seam at four by four. |
| **Target** | The above plus no visible repeat: lighting variation flattened, hero features removed, holds at four by four and at eight by eight. |
| **Extension** | Build a tile that works at two scales, meaning it reads as the correct material both filling the screen and seen small across a large surface. Then write two sentences on what you had to give up to get it. |

---

## Exit ticket

One tile, posted twice: alone, and filled four by four. Two images.

---

## Assigned

**EX6 One Tile**, due at the start of class 11. Finish the tile and add the four by
four test as a second image. Under an hour.

---

## What breaks

**Students stop at the seam.** The offset is satisfying and it feels like completion.
The four by four test is the antidote and it has to be mandatory rather than
suggested, which is why it is in the exit ticket.

**The tile gets beautiful instead of useful.** Somebody will paint a genuinely
lovely piece of stone with a striking crack in it. The crack is the problem. This is
worth handling gently, because it is a real disappointment and it is also exactly the
lesson: a tile is a component rather than a picture.

**Frequency separation turns into a rabbit hole.** The technique has a lot of
internet around it and some students will disappear into three-layer versions of it.
One blur on one layer does everything this session needs.

**Nobody tests at eight by eight.** Four by four hides problems that eight reveals.
Mention it at the checkpoint for the Target tier.

---

## Prep

- Four tiles for the cold reversal, each prepared in both forms, single and four by
  four, with the most distinctive one being the worst performer.
- A demo source photograph with a deliberate lighting gradient and one hero feature
  in it.
- A generated texture for the machine beat, prepared, plus one generated live.
- Provided source photographs for students without their own.
- EX5 collected and the student-photographed swatches queued for recall.
