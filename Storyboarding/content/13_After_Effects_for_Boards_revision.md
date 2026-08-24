# Lesson: After Effects for Boards

**CA 140 Storyboarding · Class notes**

> Handout H8 covers the file discipline for this material. Software is never the subject in this course, and that still holds here: this is the small corner of After Effects that lets boards move, because an animatic needs a way to time something. Five operations, and one question at the end that's the actual point.

---

## What this is, and isn't

Five operations, chosen because they're exactly what an animatic needs and nothing more. This is not a motion graphics course; if the graph editor, expressions, and effects are the goal, that's a different class. This lesson teaches the corner of After Effects that makes boards move, and stops there.

## Why an animatic needs any of this

A board holds blocking, camera, and action. It cannot hold duration: no panel says whether a moment lasts half a second or four, and how long something lasts is most of what makes a sequence feel like anything. Everything below exists to get that fourth dimension onto work already made.

## The five operations

**1. Import with the layers intact.** File, Import, File, and pick the source PSD. The import dialog offers a choice that matters more than it looks. "Footage" collapses every layer into one flat image, nothing separable. "Composition" keeps layers but resizes them to fill the comp, putting every anchor point in a useless place. "Composition, Retain Layer Sizes" keeps layers at their own dimensions with anchor points in a useful place, this is the one to pick. Get it wrong and nothing else below is possible, and there's no error message. It just quietly doesn't work.

**2. The anchor point is the joint.** Press Y for the Pan Behind tool, drag a layer's anchor point to where its joint actually is (the shoulder, for an arm), then press V to return to the selection tool. Rotate the layer now, and it pivots from the shoulder. Skip this step, and the same rotation spins the layer around its own middle like a propeller. Every rotation in the program happens around the anchor point, and so does every scale; when a layer scales in an unexpected direction, the anchor is why. It's not technical trivia, it's the joint, and once it's understood that way, a whole category of problems stops being mysterious.

**3. Parenting.** In the timeline, the Parent and Link column holds a pick-whip (a small spiral icon); drag it from a child layer to its parent to link them. A parented layer inherits its parent's position, rotation, and scale, on top of its own. Move the body, and an arm parented to it moves too, without the arm itself being touched. Build the chain outward from the root: body, then upper arm, then forearm, then hand, each parented to the thing closer to the middle. That's a rig.

One thing surprises everyone exactly once: a parented layer's position values become relative to its parent, not to the composition. Move the body across the screen, and the arm follows, but the arm's own position number never changes, because it's now measuring from the body, and relative to the body, nothing moved. That's correct, not broken.

**4. Keyframes, minimally.** Click the stopwatch icon next to a property to start recording, move the playhead to a later point in time, change the value, and After Effects creates a keyframe. That's the entire mechanism. No easing, no graph editor, no velocity curves, none of that is needed to make a board move clearly, and straight interpolation does the job for this purpose.

**5. Masks.** Grab the Pen tool with G, select a layer, and draw a closed shape on it. Everything outside that shape disappears, not deleted, just not drawn, and it stays adjustable. Give the mask a feather of one to two pixels; it softens the edge enough to hide small imprecision in the shape, at no cost.

## Making something to hide behind

A character has to walk into a house, but the background is one flat layer with no separate doorway object to put them behind. The fix: duplicate the background layer, mask the copy down to just the doorway (or wall, or whatever needs to sit in front), then drag that masked copy above the character in the layer stack. The character now passes behind something that was never a separate object, a foreground manufactured out of the background.

This isn't a broken file. Boards, matte paintings, and reference art all arrive flat as a matter of course; somebody hands over a single image and asks for a character to walk behind a pillar that has no pillar layer, just a picture with a pillar in it. Anything that has to pass behind anything else in a flat image gets a mask. That's a permanent condition of the work, not a one-time inconvenience.

## Settings worth getting right at the start

**Frame rate**: pick 24 or 30 and never change it mid-project. Changing it later silently shifts every keyframe already set, with no clean undo.

**Comp size**: match the delivery aspect ratio used all term. 16:9 is 1920×1080. 1.85:1 is 1920×1038. 2.39:1 is 1920×803. These are the same arithmetic from the aspect ratio lesson in week two, in different units.

**Numbered sequences**: name exported panels in sequence (`SEQ01_SH010.png`, `SH020`, `SH030`), incrementing by ten, and tick "PNG Sequence" on import to bring them in as one item, one frame each. Incrementing by ten means a shot added later between two others just becomes 015, without renaming everything downstream.

**Export**: File, Export, Add to Adobe Media Encoder, then H.264, Match Source, High Bitrate, producing an mp4 that plays anywhere. Do not accept the render queue's default of AVI Lossless, which produces a multi-gigabyte file nobody can play and that Canvas will refuse. That default is the single most common way to lose an evening on this assignment.

## The question this class is about

Everything awkward in this process traces back to a decision made, or not made, while drawing. A doorway drawn as its own layer turns the masking step into thirty seconds instead of ten minutes. An arm drawn clear of the torso makes the anchor point obvious. A background drawn wider than the frame lets a character enter from off-frame instead of appearing at the edge. A pan needs artwork past the frame edge; a push needs artwork bigger than the frame. Detail that was never drawn can't be invented later.

The move wanted determines the artwork needed, and knowing that before drawing is the difference between a two-hour animatic and a two-day one. This is the same shape as the floor plan, which costs four minutes and prevents a crossed line, or a beat sheet, which costs an afternoon and prevents a restructure: the cheap decision made early replaces the expensive one made late. That's most of what this course is about, and today it happened to look like software.
