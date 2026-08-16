#!/usr/bin/env python3
"""Deck 13: After Effects for Boards. Class 11, paired with EX7.

Spec: NewLectures/deck-new-13-after-effects.md
Run from the repo root:  python3 Storyboarding/build_decks/build_deck_13_after_effects.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import *  # noqa: F401,F403

OUT = "Storyboarding/NewLectures/13_After_Effects_for_Boards.pptx"
prs = new_deck(OUT)

# ============================================== PART 1: WHY YOU'RE HERE (1-3)
title_slide(prs, "After Effects for Boards",
    "Five operations, and one design question  |  CA 140 Storyboarding",
    """Today is the one class in this course that happens inside a piece of software, and I want to be honest about that up front because it sits oddly against everything else I've told you.

The rule in here has been that software is never the subject. That still holds. What we're doing today is learning the small corner of After Effects that lets your boards move, because your animatic is due shortly and you cannot hand in a timed sequence if you have no way to time anything.

Five operations. That's the whole session. Then one question at the end that is the actual point.""")

bullets(prs, "What this is, and what it isn't",
    ["Five operations. Nothing else.",
     "Chosen because an animatic needs them.",
     "Not a motion graphics course."],
    """Five operations, chosen because they are exactly what an animatic needs and nothing more.

This is not a motion graphics course. That course exists, it is taught by someone who knows the program far better than I do, and it is not this. If you want expressions and effects and the graph editor, take it.

You will not learn After Effects today. You will learn the corner of it that makes your boards move, and then you will stop.""")

bullets(prs, "Why an animatic needs any of this",
    ["Boards hold blocking, camera, action.",
     "Boards cannot hold duration.",
     "This is how you add the fourth dimension."],
    """Think about what a board can and can't tell you.

It holds blocking. It holds the camera. It holds the action. Hand a board to somebody and they know what happens and roughly how it's framed.

What it cannot tell you is how long. Not one panel of yours says whether that moment lasts half a second or four. And how long is most of what makes a sequence feel like anything.

Everything in this session exists to get that fourth dimension onto work you have already made.

[Say the due dates out loud so nobody is surprised: PR3 lands shortly after this, and the final needs it too.]""")

# ============================================== PART 2: THE FIVE OPERATIONS (4-13)
section(prs, "The five operations",
    "Build along. One at a time.",
    """Screens up, everybody. We do these one at a time and nobody moves on until the person next to them has it working.

If you fall behind, say so. There is no version of this where you catch up later from notes.""")

bullets(prs, "1. Import with the layers intact",
    ["File, Import, File",
     "Import As: Composition, Retain Layer Sizes",
     "Get this wrong and nothing else works."],
    """Operation one. File, Import, File. Pick the PSD.

Then the dialog gives you a choice, and this is the only part of today you can get catastrophically wrong.

Footage gives you one flat image. Every layer collapsed. Nothing separable.

Composition gives you layers, but resized to fill the comp, which puts every anchor point in a useless place.

Composition, Retain Layer Sizes gives you layers at their own dimensions with anchor points you can actually work with. That is the one you want.

Here's why it matters more than it looks: get this wrong and nothing else in the session is possible, and you will not find out until you try to move something. There is no error message. It just quietly doesn't work.""")

s = title_only(prs, "The same arm, two ways",
    """Here's the same arm layer imported both ways, with the anchor point marked on each.

On the left, plain Composition. The layer has been stretched to the size of the whole comp, so the anchor sits somewhere out in empty space. Rotate that and the arm swings around a point that has nothing to do with the character.

On the right, Retain Layer Sizes. The layer is the size of the arm. The anchor is on the arm. Now you can put it where the joint is.

That's the entire difference, and it is one dropdown.""")
box(s, Inches(1.3), Inches(2.3), Inches(4.2), Inches(2.8), "COMPOSITION\n\nlayer stretched to comp size",
    size=13, bold=True)
box(s, Inches(3.1), Inches(3.3), Inches(0.7), Inches(1.4), "", fill=PAPER)
o = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(3.25), Inches(3.55), Inches(0.22), Inches(0.22))
o.fill.solid(); o.fill.fore_color.rgb = ACCENT; o.line.fill.background(); o.shadow.inherit = False
label(s, Inches(1.3), Inches(5.2), Inches(4.2), "anchor lands in empty space", size=12, italic=True)

box(s, Inches(7.5), Inches(2.3), Inches(4.2), Inches(2.8), "RETAIN LAYER SIZES\n\nlayer is the size of the arm",
    size=13, bold=True, line=ACCENT)
box(s, Inches(9.3), Inches(3.3), Inches(0.7), Inches(1.4), "", fill=PAPER, line=ACCENT)
o = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.53), Inches(3.35), Inches(0.22), Inches(0.22))
o.fill.solid(); o.fill.fore_color.rgb = ACCENT; o.line.fill.background(); o.shadow.inherit = False
label(s, Inches(7.5), Inches(5.2), Inches(4.2), "anchor is on the arm, movable to the joint", size=12, italic=True)

bullets(prs, "2. The anchor point is the joint",
    ["Y for the Pan Behind tool",
     "Drag the anchor to the shoulder",
     "V to get back",
     "One is a propeller. One is an arm."],
    """Operation two, and this is the one that carries an idea rather than a keystroke.

Press Y. That's the Pan Behind tool. Drag the anchor point of the arm layer up to where the shoulder is. Press V to get back to the selection tool.

Now rotate the arm. It pivots from the shoulder.

Undo the anchor move and rotate it again. It spins around its own middle like a propeller.

Same layer, same rotation, one drag of difference. The anchor point is where the joint is. That is the whole concept, and once you have it you have it for every piece of software you will ever touch that rotates anything.""")

bullets(prs, "Anchor points, generally",
    ["Every rotation happens around it.",
     "Every scale happens around it.",
     "It is the joint, not a technicality."],
    """Worth generalising for a second, because this is bigger than one arm.

Every rotation in this program happens around the anchor point. So does every scale. When you scale a layer and it grows in a direction you didn't expect, the anchor is why.

Students file this under technical trivia. It isn't. It's the joint. The moment you think of it that way, a whole category of problems stops being mysterious.""")

s = title_only(prs, "3. Parenting",
    """Operation three. In the timeline there's a column called Parent and Link. Take the pick-whip, that little spiral, drag it from the arm to the body.

The arm is now a child of the body. It inherits the body's position, rotation and scale, and it keeps its own on top of that.

Move the body. The arm goes with it, and you didn't touch the arm.

You build the chain outward from the root. Body, then upper arm, then forearm, then hand. Each one parented to the thing closer to the middle. That's a rig, and you just made one.""")
chain = ["BODY", "UPPER ARM", "FOREARM", "HAND"]
for i, name in enumerate(chain):
    x = Inches(0.9 + i * 3.05)
    box(s, x, Inches(3.2), Inches(2.4), Inches(0.95), name, size=14, bold=True,
        line=ACCENT if i == 0 else INK)
    if i < 3:
        arrow(s, x + Inches(2.5), Inches(3.52), Inches(0.45), Inches(0.3))
label(s, Inches(0.9), Inches(4.4), Inches(2.4), "root", size=12, italic=True, color=ACCENT)
label(s, Inches(2.5), Inches(5.1), Inches(9.0),
      "each one parented to the thing closer to the middle", size=14, italic=True)

bullets(prs, "The thing that surprises everyone once",
    ["A child's values are now relative to its parent.",
     "Move the body, the arm follows.",
     "The arm's own position number never changed."],
    """One thing will confuse you, exactly once.

Once a layer is parented, its position values are relative to its parent, not to the composition. Move the body across the screen and the arm goes with it, but if you look at the arm's own position number, it hasn't changed at all.

That is correct. It's measuring from the body now, and the body is where it always was as far as the arm is concerned.

Everybody hits this once and thinks something is broken. Then they never think about it again.""")

bullets(prs, "4. Keyframes, minimally",
    ["Stopwatch on.",
     "Move the playhead.",
     "Change the value.",
     "That's the whole thing."],
    """Operation four, and it's the shortest.

Click the stopwatch next to a property. That starts recording. Move the playhead to a later point in time. Change the value. After Effects makes a keyframe.

That's it. That is the entire mechanism.

No easing today. No graph editor. No velocity curves. None of that is on the rubric and none of it makes a board move any more clearly than a straight interpolation does. When you get to the point where linear motion is the thing holding your work back, come and find me, and it will not be this term.""")

bullets(prs, "5. Masks",
    ["Pen tool, G.",
     "Draw a closed shape on a layer.",
     "Everything outside it disappears.",
     "Feather 1 to 2 pixels hides a lot."],
    """Operation five. Grab the pen tool with G, make sure you have a layer selected, and draw a closed shape on it.

Everything outside that shape is gone. Not deleted, just not drawn. You can adjust it forever.

One practical thing: give the mask a feather of a pixel or two. It softens the edge just enough that small imprecision in your shape stops being visible, and it costs you nothing.""")

s = title_only(prs, "Making something to hide behind",
    """This is the move that matters, and it's the one you'll actually need in a minute.

Your character has to walk into the house. But the background is one flat layer. The doorway isn't a separate object, so there's nothing to put the character behind.

So you make one. Three steps.

Duplicate the background layer. Control D, or Command D.

Mask that copy down to just the doorway, or just the wall, or whatever needs to be in front.

Then drag that masked copy above the character in the layer stack.

Now the character walks behind a thing that was never a separate object. You manufactured the foreground out of the background.""")
steps = [("1. DUPLICATE\nthe background", INK), ("2. MASK\ndown to the doorway", INK),
         ("3. MOVE IT\nabove the character", ACCENT)]
for i, (txt, col) in enumerate(steps):
    x = Inches(0.9 + i * 4.05)
    box(s, x, Inches(2.9), Inches(3.4), Inches(1.5), txt, size=14, bold=True, line=col)
    if i < 2:
        arrow(s, x + Inches(3.5), Inches(3.5), Inches(0.45), Inches(0.3))
label(s, Inches(2.0), Inches(5.0), Inches(9.3),
      "the character now passes behind something that was never a separate object",
      size=14, italic=True)

bullets(prs, "Why the file is like that",
    ["It isn't broken.",
     "Boards and reference art arrive flat.",
     "Anything passing behind anything else gets a mask."],
    """A few of you are going to tell me the file I gave you is broken, or that I forgot to separate the layers.

I didn't. It's like that on purpose, because that is the normal condition of this job.

Boards arrive flat. Matte paintings arrive flat. Reference art arrives flat. Somebody hands you a single image and says make the character walk behind that pillar, and there is no pillar layer, there is just a picture with a pillar in it.

Anything that has to pass behind anything else in a flat image gets a mask. There is no version of this work where that stops being true, so you may as well learn it on a file where the stakes are twenty minutes.""")

# ============================================== PART 3: GETTING IT OUT (14-16)
bullets(prs, "Frame rate and comp size",
    ["Pick 24 or 30 at the start. Never change it.",
     "1.85 : 1 is 1920 by 1038",
     "2.39 : 1 is 1920 by 803"],
    """Two settings to get right at the start, because both are painful later.

Frame rate. Pick 24 or 30 and never change it. Changing frame rate mid-project shifts every keyframe you have already set, and it does it silently. There is no undo that feels like an undo.

Comp size. Match your delivery ratio, which means the ratio of the template you have been drawing on all term. Sixteen by nine is nineteen twenty by ten eighty. One eight five is nineteen twenty by ten thirty eight. Two thirty nine is nineteen twenty by eight oh three.

If those numbers look familiar it's because you calculated them yourself in week one. Same arithmetic, different units.""")

bullets(prs, "Numbered sequences",
    ["SEQ01_SH010.png, SH020, SH030",
     "Increment by ten.",
     "Tick PNG Sequence on import."],
    """Name your exported panels in a numbered sequence and After Effects will bring them in as one item, one frame each.

Select the first file, tick PNG Sequence in the import dialog, done.

The thing worth doing is incrementing by ten. Ten, twenty, thirty. Not one, two, three.

Because at some point a shot gets added between two others, and if you numbered by one you rename everything downstream. If you numbered by ten, the new shot is fifteen and you carry on with your day.

You will need this. Everybody needs this.""")

bullets(prs, "Export",
    ["File, Export, Add to Adobe Media Encoder",
     "H.264, Match Source, High Bitrate",
     "Not the render queue default."],
    """Last technical thing. Getting it out.

File, Export, Add to Adobe Media Encoder. Then H.264, Match Source, High Bitrate. That gives you an mp4 that plays anywhere.

What you must not do is hit the render queue and accept its default, which is AVI Lossless. That produces a file in the gigabytes that nobody can play, that Canvas will refuse, and that takes twenty minutes to discover.

It is the single most common way to lose an evening on this assignment, and it happens because the default is wrong rather than because anybody did anything careless.""")

# ============================================== PART 4: THE POINT (17-18)
quote(prs, "The question this class is actually about",
    "What would you have had to plan in the drawing to make this move possible?",
    "Answer it in your submission.",
    """Right. Software off for a second.

Everything that was awkward today traces back to a decision somebody made, or didn't make, while drawing.

The doorway should have been its own layer, and then step five would have taken thirty seconds instead of ten minutes. The arm should have been drawn clear of the torso, and then the anchor point would have been obvious. The background should have been drawn wider, so the character could enter from off frame instead of appearing at the edge.

A pan needs artwork past the frame edge. A push needs artwork bigger than the frame. You cannot invent detail you didn't draw.

You find this out one of two ways. You plan it, or you discover it at two in the morning with the thing due.""")

bullets(prs, "Which is the whole lesson",
    ["The move you want determines the artwork you need.",
     "The cheap decision made early",
     "replaces the expensive one made late."],
    """So here's the thing to take out of today, and it isn't a keyboard shortcut.

The move you want determines the artwork you need. Knowing that before you draw is the difference between a two hour animatic and a two day one.

And you have heard this argument before, in a different costume. It's the floor plan, which costs four minutes and prevents a crossed line. It's the beat sheet, which costs an afternoon and prevents a restructure. It's every milestone on the final.

Same shape every time. The cheap decision made early replaces the expensive one made late. That's most of what this course is, and today it just happened to look like software.""")

n = finish(prs, OUT, expected=19)
print(f"OK  {OUT}  {n} slides")
