# P2: The Material Set

**Digital Painting · briefed class 9 · final due at the start of class 13**

---

## Where the tiers sit

| Tier | What you deliver |
|---|---|
| **Baseline** | One seamless albedo map for the provided prop, painted against the provided UV layout. The material has to be nameable by a stranger: someone should look at it and say "that's oak," or "that's cast iron," without being told. Photoshop only. No Maya required. |
| **Target** | Albedo, roughness and normal, checked in the Maya viewport and revised after what the viewport showed you. The revision is the assignment. |
| **Extension** | Two materials on the same prop that have to meet. A metal band around a wooden handle, a painted panel with the paint worn off at the edges. The transition between them is the whole problem. |

Baseline requires nothing but Photoshop and a mouse. Maya only enters at Target, and
if the lab machine you are on will not open it, come find me rather than dropping a
tier.

---

## The job

Somebody models a prop. Somebody else lights it. Between those two people there is a
painter deciding what the surface is actually made of, and that painter's work has
to survive being lit by a person who was not in the room when it was painted.

This is the difference that makes the project hard. In P1 you controlled the light.
Here you do not. A surface that looks convincing as a flat image in Photoshop can
turn to plastic the moment a real light hits it, and the reason is almost always
that the painting described how the object looked under one specific light rather
than what the object is made of.

So the question is not "does this look like wood." It is "will this still look like
wood when I do not get to choose the lamp."

---

## What you are given

- **The prop.** A simple object, already modeled. You will not model anything.
- **The UV layout**, exported as a template image with the seams marked. You will
  not unwrap anything.
- **A Maya scene** with the prop, a shader already connected to three file nodes,
  and a light rig. Your job in Maya is to save your maps into the right folder,
  reload, and look. That is the entire Maya component of this course.

Substance Painter is not used here, and that is a deliberate decision rather than an
oversight. The transferable idea is how materials behave. Which application authored
the map is a detail that changes every few years.

---

## Deliverables

One folder named `Lastname_P2`.

1. **`Lastname_P2_albedo.png`**, 2048 square, seamless where the UV shell wraps.
2. **Target and up:** `Lastname_P2_roughness.png` and `Lastname_P2_normal.png`, same
   resolution.
3. **`Lastname_P2_working.psd`**, layered and named.
4. **Target and up:** `Lastname_P2_viewport_before.jpg` and
   `Lastname_P2_viewport_after.jpg`, two renders from the provided Maya scene,
   showing the state before your revision and after it.
5. **`Lastname_P2_notes.md`**, three to six sentences: what the viewport showed you
   that the flat map did not, and what you changed because of it. This is graded and
   it is the part most people skip.
6. **Extension only:** the second material, and one close-up render of the meeting
   between the two.

---

## Milestone

| Due | What |
|---|---|
| Class 12 | Albedo pass, loaded in the viewport, looked at. Not finished. Looked at. |
| Class 13 | Final, in critique. |

Class 12 is the mirror day. Bring something to put in front of the mirror or the day
is wasted.

---

## The three maps, in one line each

The long version is class 11. The short version, for the brief:

- **Albedo** – what color the surface is, with the light taken out of it. No
  shadows, no highlights, no lamp. This is the hardest habit to break, because
  painting shadows into an albedo map is exactly what every instinct tells you to do.
- **Roughness** – how scattered the reflection is. Black is a mirror, white is
  chalk. Almost every convincing surface has variation here, and almost every
  unconvincing one is a flat gray.
- **Normal** – which way the surface is facing, faked, so small bumps catch light
  without any geometry existing. Generated from a height pass rather than painted
  directly, most of the time.

A useful way to think about the set: the albedo is the paint, the roughness is the
finish, and the normal is the texture you would feel with a fingertip. Three
different questions about the same square inch of an object.

---

## Rubric

Totals 100% of this assignment.

| | Weight | What earns it |
|---|--:|---|
| **Material read** | 30% | A stranger can name the material. It behaves like that material rather than merely resembling a photograph of it. |
| **Albedo discipline** | 20% | No baked light. No painted shadows, no painted highlights, no lamp in the map. |
| **Seam and tiling quality** | 15% | No seam visible at the UV border. No obvious repeat. |
| **Response to the viewport** | 20% | The before and after renders show a real change, and the notes explain what the viewport revealed. A student who looked and then changed nothing has not done this part. |
| **File craft** | 15% | Layered, named, correct resolution, correct file names. Somebody else can load these maps without asking you where anything is. |

Baseline students are graded on the first three rows only, reweighted. The response
row cannot be earned without Maya, so it is not held against a Baseline delivery.

---

## What usually goes wrong

**Painting the light into the albedo.** Every single term. A beautifully rendered
wooden surface with soft shadows painted in, loaded onto a prop, lit from the other
side, and now the object has two contradictory light sources and looks like a
sticker. Strip the lighting out. If it looks flat and boring in Photoshop, that is
frequently correct.

**Flat roughness.** A uniform gray roughness map means the surface is uniformly
worn, which nothing real is. Fingerprints, wear at the edges, dust in the recesses,
a wet patch. This map is where most of the believability actually lives and it is
the one students spend four minutes on.

**Too much detail, too evenly.** A surface covered edge to edge in scratches reads
as noise. Wear happens where hands and feet and weather go. Put the damage where a
person would have put it.

**Never looking at it on the object.** The map is not the deliverable. The surface
is. Load it, look at it, go back.

---

## A note on the Extension tier

Two materials meeting is the problem that separates people who can paint a texture
from people who can build a prop. The interesting part is never the metal or the
wood. It is the eighth of an inch where they touch: the dirt that collects at the
joint, the way the paint chips at the edge and not in the middle, the slight
darkening in the gap where light does not reach.

If you take it on, finish the single material first.
