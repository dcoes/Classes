# Class 11: Map Sets, in Plain Language

**Digital Painting · session 11 of 19**

> **The argument of the day:** three maps are three different questions about the
> same square inch, and the renderer is asking all three at once.

---

## The clock

| Time | Block | Minutes |
|---|---|--:|
| 0:00 | Recall: the four by four test, EX6 collected | 10 |
| 0:10 | Lecture: what each map is actually telling the renderer | 40 |
| 0:50 | Demo: one surface, three maps, and what each one changes | 25 |
| 1:15 | Studio: the sort, then the P2 albedo | 60 |
| 2:15 | Exit ticket | 15 |

Total 2:30.

---

## Recall

Five minutes. Put two tiles from EX6 up at four by four and let the room find the
repeat, fast. Collect EX6.

---

## Lecture beats

This is the session that carries the whole justification for the materials unit, so
it ends by naming exactly where this gets picked up later in the program.

### Beat 1: The renderer is asking questions

**Slide:** *Every pixel. Three questions.*

Frame the whole thing as an interrogation rather than as a file format, because the
file format changes and the questions do not.

When light hits a point on a surface, a renderer needs to know three things about
that point. What color is it. How scattered is the bounce. Which way is it facing.
The three maps are three images, each answering one of those questions for every
point on the object at once.

That is the entire idea. Everything else today is detail on top of it.

### Beat 2: Albedo is the paint with the lamp switched off

**Slide:** *Color. No light. No shadow. No lamp.*

The one students get wrong, every term, without exception.

Albedo answers: what color is this, with all lighting removed. Not what it looked
like in the photograph. Not with the soft shadow under the ledge. Not with the
highlight along the top edge. Just the color.

A physical object for it: it is the color of the paint in the can, not the color of
the wall at four in the afternoon.

Say why it matters in consequences rather than in theory. A shadow painted into an
albedo is a shadow that cannot move. When somebody lights the object from the other
side, the painted shadow stays exactly where it was, and now there are two shadows
disagreeing, and the object reads as a sticker. It is the same error as class 3's
contradictory light directions, arriving from a different door.

The honest part: a stripped albedo looks flat and boring in Photoshop, and students
will believe they have made it worse. They have not. That flatness is correct.

### Beat 3: Roughness is the sharpness dial

**Slide:** *Black is a mirror. White is chalk.*

Class 9's first question, made into an image.

Roughness answers: how scattered is the reflection at this point. Dark values mean
organized reflection, meaning polish, wet, glass, chrome. Light values mean scattered
reflection, meaning chalk, unfinished wood, dry concrete.

The key teaching point is that this map is where believability actually lives, and it
is the one students spend four minutes on. Nothing in the world has uniform
roughness. Fingerprints, wear on the edges, dust in the recesses, a wet patch, the
polished place where a hand grips. A roughness map is a map of what has happened to
the object, and a flat gray one says nothing has ever happened to it.

Worth saying directly: **a mediocre albedo with a great roughness map beats a great
albedo with a flat one.** Most students do not believe that until class 12.

### Beat 4: Normal is faked geometry

**Slide:** *Which way is this facing?*

The one that looks the strangest and is the simplest.

A normal map answers: which direction is the surface pointing at this point. It does
this by storing a direction in the red, green and blue channels, which is why a
normal map looks like violent purple. The purple is not a color, it is three numbers
wearing a color's clothing.

The consequence is that small bumps catch light as though they were modeled, while
the geometry underneath stays flat. Grout lines between tiles, wood grain, rivets,
fabric weave. None of it exists, all of it lights correctly.

The limit, stated honestly: it is faked, so it fails at the silhouette. A brick wall
with a normal map has a perfectly straight edge when you look along it, and at a
grazing angle the illusion falls apart. This is why the technique is invisible most
of the time and obvious occasionally.

In practice it is generated from a height map, meaning a grayscale image where white
is high and black is low, rather than painted directly. Painting a height map is
something a person can actually think about. Painting a normal map is not.

### Beat 5: The set, in one table

**Slide:** *Paint. Finish. Feel.*

| Map | The question | The physical object |
|---|---|---|
| Albedo | What color is it | The paint in the can |
| Roughness | How sharp is the reflection | The finish on top of the paint |
| Normal | Which way is it facing | The texture you feel with a fingertip |

Three different questions about the same square inch. Students who hold this table
stop mixing the three up, which is most of the battle.

### Beat 6: The maps you will meet and are not doing here

**Slide:** *Metalness. AO. Height. Opacity.*

Ninety seconds, named and set aside, so nobody is surprised later.

Metalness, which is a nearly black-and-white map saying whether a point is metal or
not, and which matters because metal behaves fundamentally differently from
everything else. Ambient occlusion, which darkens crevices. Height, which the normal
was generated from. Opacity, for anything transmitting.

They are real and they are not in P2, because three maps in four class days is
already enough and the idea transfers.

### Beat 7: Where this goes next

**Slide:** *You will be handed this again.*

End on the handoff, because the students who wonder why a painting class is doing
this deserve an answer.

Name the specific course in this program that picks this up and what it will assume
you already know walking in. This is the only slide in the session that is about the
curriculum rather than the craft, and it should be one sentence and true.

### Beat 8: The cold reversal

**Slide:** *Eight maps. Three piles.*

Eight map images on screen with no labels: three albedos, three roughness maps, two
normals. One of the albedos has lighting baked into it and one of the roughness maps
is a flat gray.

Sort them. Do not give the answers. It becomes the studio block.

---

## The demo

Twenty-five minutes, live, one surface built into a set.

Use a flat plane in the Maya scene rather than the prop, so the maps are the only
variable.

1. Load an albedo alone. Flat, lit by the rig, unconvincing. Say so.
2. Add roughness. Something happens immediately and the room will react. Point out
   that nothing about the color changed.
3. Add the normal. The surface acquires texture that is not in the geometry. Rotate
   the view to show it working, then rotate to a grazing angle to show it failing.
4. **The comparison that makes the session:** swap in a second albedo that has
   lighting baked into it. Same roughness, same normal. Rotate the light. Let the
   painted shadow sit there stubbornly while the real one moves. Nobody forgets this.
5. **The deliberate mistake:** set roughness to a flat gray. Watch the surface turn
   to plastic. Restore the varied map. Say the line from Beat 3 again, now that it is
   visible.
6. Show the height map the normal came from, and generate the normal live so it stops
   being magic.

---

## Studio

Sixty minutes.

**1:15 The sort (15 minutes).** The eight unlabeled maps from Beat 8, sorted into
three piles, plus a written answer to two questions: which albedo has light baked in,
and how do you know.

Fast, and it is the diagnostic that tells you who understood Beat 2.

**1:30 CHECKPOINT.** Take the sort from the room. Settle it now rather than leaving
it open, because unlike the other cold reversals this one has a right answer and the
next forty-five minutes depend on it.

**1:45 P2 albedo (30 minutes).** Start the real albedo for the prop, painted against
the UV template, with the seams visible as a layer. No lighting, no shadows, no
highlights.

Circulate with one question: is there any light in that map.

---

## Tiers for today's work

| Tier | The albedo start |
|---|---|
| **Baseline** | Base color laid in across the whole UV shell, no baked lighting, material nameable. |
| **Target** | The above plus wear placed where use would put it, and a stated real-world scale for the surface. |
| **Extension** | Paint the height map alongside the albedo and generate the normal from it, rather than leaving the normal to the last day. |

---

## Exit ticket

The eight maps sorted into three piles, submitted as a list, plus one sentence naming
the albedo with light baked into it and how you spotted it.

---

## What breaks

**Shadows go into the albedo.** Every term, by everyone, including the students who
just watched the demo prove why not. Ask the one question at every desk. Catching it
today is thirty seconds. Catching it at class 13 is a repaint.

**The normal map is treated as magic.** The purple is alarming and students stop
thinking. Generating one live from a height map in front of them fixes it, which is
why step 6 of the demo is not optional.

**Roughness gets four minutes.** It will get four minutes unless Beat 3 is repeated
at the desks. Use the plastic demo as the reference point by name.

**Somebody asks why this is in a painting class.** Fair question, deserves a real
answer rather than a defensive one. Beat 7, plus the honest version: painting a
surface that behaves correctly under light somebody else chose is a harder painting
problem than painting one where you picked the light, and it is the one that pays.

---

## Prep

- The Maya scene with a flat plane variant, plus a second albedo with lighting
  deliberately baked into it for step 4.
- Eight unlabeled maps for the sort, including one baked albedo and one flat gray
  roughness.
- A height map and the tools to generate a normal from it live.
- The name of the specific downstream course for Beat 7, confirmed, plus its current
  entry assumptions if the instructor of record can be asked.
- EX6 collected.
