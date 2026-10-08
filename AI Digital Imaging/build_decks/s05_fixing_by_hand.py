#!/usr/bin/env python3
"""Session 5. Fixing by hand.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/05_Fixing_by_Hand.pptx"

SPEC = [
("title", "Fixing by Hand", "AI Digital Imaging  |  Session 5",
"""**Running time, about 50 minutes.** Spot it and recall (6). Why by hand (5). The kit: paint-over, clone and heal, Liquify, photo patch (16). Worked example and cold reversal (8). Matching so the fix disappears (8). Order of operations and when to stop (5). Options (2).

**Prep before class.** A generated image with a hand error for the worked example, and a second one, unfixed, for the cold reversal. The Option A image with two marked errors, on Canvas. Rehearse the demo's deliberate mistake: regenerate the hand five or six times on screen, let it get worse rather than better, then stop and fix it by hand in about two minutes.

Remind students to bring a phone. The best reference for a generated hand is the student's own hand.

Boundary note: this course assumes Photoshop basics and doesn't re-teach painting. If the room is weak on clipping masks or adjustment layers, show them in the demo rather than adding lecture time."""),

warmup("a generated image with a hand or face problem that's fixable in a few minutes"),

("bullets", "Last time",
["Six checks, in order.",
 "Brief first, errors second.",
 "CALLOUT layer, numbered."],
"""[Cold call, thirty seconds.] Give me the six checks. [Anatomy, perspective, light, lettering, repeated texture, sheen.] And which one did the room miss the most in the find-them-all exercise? [Almost always light.]

And from Option B: was the cleanest image your top pick? [Ask a few people. Some will have ranked a clean but off-brief image first. That's the lesson landing.]

Last session was about seeing. Today is about doing something about it."""),

("quote", "Today's idea", "The generator gets you somewhere.",
"The hand work gets you to the brief.",
"""Here's the shape of the whole workflow, and it's been true of every image-making tool I've used.

The generator gets you somewhere. Often somewhere quite good, quite fast. The hand work is what gets you from "somewhere" to "what the brief actually asked for." That last stretch is usually the smaller part of the time and the larger part of the value.

Most people who are unhappy with generated images are stuck at "somewhere," trying to get the rest of the way by asking the machine again."""),

("bullets", "Why not just regenerate?",
["Rerolling is a slot machine.",
 "Each pull can break something new.",
 "A fix by hand stays fixed."],
"""Which brings us to the most common habit, and the most expensive one: rerolling. The hand is wrong, so you select it and generate again. Still wrong. Again. Now it's wrong differently. Twenty minutes later you have forty hands and none of them are right.

That's a **slot machine.** Each pull is random, and each pull can break something that was fine before. It feels like work because you're busy, but you aren't making any decisions.

A fix by hand is different: you decide what's wrong, you change exactly that, and it stays changed. It's often faster, too, once you're used to it. That's what the demo will show, including me making the rerolling mistake on purpose so you can watch it fail."""),

("boxes", "The kit",
["Paint-over|new layer, sampled color", "Clone and Heal|copy what's already there",
 "Liquify|push shapes into place", "Photo patch|your own reference"],
"""Four tools, and you know most of them already from earlier Photoshop work.

**Paint-over**: painting on a new layer above the image. **Clone Stamp and Healing**: copying parts of the image that are already right over the parts that are wrong. **Liquify**: pushing shapes, like a finger that's too long or a jaw that drifted. **Photo patch**: bringing in a real photograph, often one you take yourself, and blending it in.

Most real fixes use two or three of these together."""),

("bullets", "Paint-over",
["A new layer, above, named FIX_.",
 "Sample color from the image.",
 "Value first, then color."],
"""Paint-over. Always on a new layer above the image, never on the image itself, named FIX_ for what it fixes.

Sample your colors from the image with the eyedropper (hold Alt with the brush), so you're painting in the image's own palette, not one you invented.

And do it in the order painters do: get the **value** right first, the lights and darks, then worry about color. If the value is right, a slightly off color usually passes. If the value is wrong, a perfect color still sticks out. This is the same idea from the gray check last session.

I'm not going to teach painting here, there's a whole course for that. You don't need to be a strong painter to fix a shadow or simplify a background. You need to be careful and to check your work in gray."""),

("bullets", "Clone and Heal",
["Clone: copies exactly.",
 "Heal: copies texture, matches tone.",
 'Empty layer, sample "Current & Below."'],
"""Clone Stamp and the Healing Brush. The difference matters.

**Clone Stamp** copies pixels exactly from one place to another. Good for edges, straight lines, and anything where you need the exact structure. **Healing Brush** copies the texture from one place but blends the tone and color with where you paint. Good for skin, sky, walls, anything soft. The Spot Healing Brush and the Remove tool guess the source for you, which is quick but less controlled.

The habit that keeps this non-destructive: make an empty layer, set the tool's Sample option to **Current & Below**, and paint there. Your fixes live on their own layer and the original stays clean underneath.

And remember the repeated-texture check from last session. Clone carelessly and you create exactly the error you were removing."""),

("bullets", "Liquify",
["Push, don't paint.",
 "Small brush, small moves.",
 "Fix proportion, not detail."],
"""Liquify, under the Filter menu. It doesn't add anything, it moves what's there, like pushing wet paint around with a finger.

It's the right tool for proportion problems: a finger that's too long, a neck that's slightly too thin, an eye that's a bit higher than the other, a jaw that drifted, a building that leans. It's the wrong tool for missing parts or wrong details.

Two habits. Convert the layer to a Smart Object first, so the Liquify stays editable. And use a small brush and small moves. Big Liquify pushes are how you get the stretched, melted look, which is ironically very close to the generator's own mistakes."""),

("bimage", "Photo patch",
["Shoot your own reference.",
 "Your hand, your phone, same pose.",
 "Mask it in, then match it."],
"slot:a phone photo of a hand in the pose of the generated one",
"""Photo patch, and this is the one I'd push hardest.

When a generated hand is wrong, the best reference in the world is at the end of your arm. Put your hand in the same pose, light it roughly the same way (a window or your phone's light from the same side as the image), and take a picture.

Then bring it in as a REF_ layer, scale and rotate it into place, mask away everything but the part you need, and match it to the image (which we're about to talk about). Sometimes you'll paint over it rather than use it directly. Either way, now you know exactly what the hand should look like.

Artists have used mirrors and their own hands as reference for centuries. This is that, with a phone."""),

("boxes", "Worked example: one bad hand",
["Callout|number the error", "Reference|shoot your hand", "Block|paint the silhouette",
 "Patch|mask in, or paint over", "Match|value, grain, color"],
"""Here's the worked example, one bad hand, and I'll do it live in the demo.

**Callout**: circle it, number it, write what's wrong ("six fingers, thumb on the wrong side"). **Reference**: shoot your own hand in the pose. **Block**: on a FIX_ layer, paint the correct silhouette of the hand over the wrong one, flat color, just the shape. If the silhouette reads, the hand will read. **Patch**: either mask your photo in or paint the forms over your block-in. **Match**: value, grain, color, until it disappears.

Five steps. Notice that the silhouette comes before any detail. Same as in drawing."""),

("image", "Now you: plan this fix", "slot:a second generated image with a hand or limb error, unfixed",
None,
"""Cold reversal. Here's a different problem, unfixed.

In pairs, two minutes: what's wrong, which tools would you use, and in what order? Don't do it, plan it. Write it as steps.

[Take two or three plans. Compare them. Don't pick a winner. Point out where plans differ: someone wants to regenerate, someone wants Liquify, someone wants a photo patch. Ask each one what could go wrong with their plan.]

There's rarely one correct fix. There are fixes you can explain and fixes you can't."""),

("section", "Making the fix disappear", "",
"""Now the part that separates a fix from a patch. A good fix is invisible."""),

("checklist", "Match these four",
["Value: squint, check in gray", "Edge softness", "Noise and grain", "Color temperature"],
"""Four things to match, and the order matters.

**Value**: does your fix have the same lights and darks as the area around it? Check with the gray layer. **Edge softness**: the image has soft edges in some places and sharp ones in others, and your fix needs to match its neighborhood. A razor-sharp hand on a softly focused figure looks pasted on. **Noise and grain**: next slide. **Color temperature**: is your patch slightly cooler or warmer than the area around it? Phone photos usually are.

A funny thing happens here. Sometimes your fix is better drawn than the rest of the image, sharper and more detailed, and that makes it stick out just as much as an error would. The fix has to match the image, not be better than it."""),

("image", "Grain is part of the image", "composite_zoom.png",
"Add noise to the patch until it matches. Match softness, too.",
"""Zoomed way in. On the left, a clean, hard edge with no grain, the way a painted fix or a generated patch often comes out. On the right, grain matched and the edge softened to match the image.

At normal size you might not see the difference consciously, but you feel it: the left one looks stuck on.

The fix: on your FIX_ layer, or a layer clipped to it, add noise (Filter, Noise, Add Noise, monochromatic, a small amount) until it matches the area around it at 100% zoom. And if the image is slightly soft, blur your fix slightly to match. We'll go deeper on this when we composite in session 8."""),

("bullets", "Generating inside your fix",
["Allowed: small fills inside your work.",
 "Paint rough, then fill over it.",
 "Named GEN_, decided by you."],
"""Can you use Generative Fill inside your own fixes? Yes, and honestly it can be a good workflow, as long as it stays your decision.

The one that works best is the one from session 3: **paint rough, then fill.** Paint the corrected shape, badly, in the right colors. Select over it and generate. The generator uses your painting as a guide, and you get something that follows your decision rather than inventing its own.

The rules are the same as always. It's on its own layer, named GEN_. You picked it from the variations for a reason you can say. And you check it with the six checks, because a fill inside a fix can bring its own new errors with it."""),

("checklist", "The order of fixes",
["1. Structure: anatomy, perspective", "2. Light: direction and shadows",
 "3. Surface: texture, repeats, text", "4. Edges and grain, last"],
"""Order of operations, and it's the same order a painter works in.

**Structure** first: anatomy, perspective, proportion. If the hand has six fingers, there's no point fixing its shadow. **Light** second: shadows and highlights that agree with one source. **Surface** third: textures, repeated patterns, lettering. **Edges and grain** last, because every fix you made above changes them.

Doing it in the wrong order means doing some of it twice."""),

("bullets", "When to stop",
["Fixed to the brief, not perfect.",
 "Stop when the callout list is empty.",
 "Ten minutes fixing beats an hour rerolling."],
"""And when to stop, which is the hardest part for some of you and too easy for others.

You stop when the **callout list is empty** and the image does what the brief asks. Not when it's perfect, because it never will be, and not when you're tired of it.

If you find yourself adding new problems to the list as you go, that's fine, that's your eye getting better. Add them, fix them, and then stop."""),

("bullets", 'Is a fixed image "yours"?',
["You fixed it by hand.",
 "You didn't make the rest.",
 "So what is it?"],
"""A quick question to end on, four minutes, no answer from me today.

If you generate an image and then spend an hour fixing it by hand, is it yours? Partly yours? What would you call it?

[Let a few people answer. Push gently on easy answers in either direction.]

We're going to spend a whole session on this in week three, including where copyright law currently stands, which is more interesting than most people expect. For now, the practical answer is the one we already have: you say what was generated and what you made, and your layers prove it.

[Into the demo, including the rerolling mistake.]"""),

("bimage", "The industry has always done this",
 ["Concept artists paint over.",
  "Over photos, 3D blockouts, each other.",
  "The paint-over is the job."],
 "slot:a concept art paint-over breakdown: 3D blockout or photobash, then the painted final",
"""[About four minutes.] Something worth knowing: the workflow we're learning today isn't new to the industry, it just has a new source.

Concept artists and matte painters have worked like this for a long time. Some of these include painting over a rough 3D blockout, over a "photobash" made of chopped-up stock photos, over a frame from a previous film, or over another artist's sketch. The source gets you composition and perspective fast. The paint-over is where the decisions happen: the light, the focal point, the story.

[Show a breakdown, blockout or photobash on one side, painted final on the other. Ask: what changed between the two? Make them list it.]

Usually what changed is exactly our order: structure fixed, light unified, surfaces simplified, edges controlled. The generator is one more kind of blockout. The paint-over is still the job."""),

("bullets", "Fix or start over?",
 ["Fix: the idea is right.",
  "Start over: the idea is wrong.",
  "Decide before you spend the hour."],
"""One more judgment call, because it saves a lot of time.

Before you start fixing, ask: is the **idea** right? If the composition, the pose and the light basically work and the problems are hands and textures, fix it. That's an hour well spent.

If the composition is wrong, or the light comes from the wrong place for the whole scene, or the image misses the brief, don't fix it. Start over, with a better brief or a rough sketch underneath. No amount of perfect hand work rescues the wrong picture.

[Ask the room: who has ever spent ages fixing something that should have been started over? Hands up. Mine's up too.] This is the same lesson every painter learns about a bad drawing underneath a nice rendering."""),

vocab([("Paint-over", "painting on a new layer above the image"),
       ("Clone Stamp", "copies pixels exactly"),
       ("Healing Brush", "copies texture, matches tone"),
       ("Current & Below", "sample setting for fixing on an empty layer"),
       ("Liquify", "pushes shapes, adds nothing"),
       ("Grain", "noise that belongs to the image; match it")]),

("options",
["Fix two marked errors", "on a provided image.", "Before and after on named layers."],
["Fix one of your own", "generated images.", "List what you changed, and why."],
"""Tonight, due next class.

**Option A**: the image on Canvas has two errors marked. Fix both by hand, on FIX_ layers, so I can toggle before and after.

**Option B**: take one of your own generated images, from Option A in session 1 or 2 if you like, run the six checks, call out what you find, fix it, and list what you changed and why.

Project 1 is due in two classes. Option A tonight is good practice for it."""),

("quote", "One line to take home", "Stop rerolling. Start painting.",
"A fix you decided stays fixed.",
"""Stop rerolling. Start painting. A fix you decided on stays fixed. [Demo.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
