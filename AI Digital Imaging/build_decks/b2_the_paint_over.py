#!/usr/bin/env python3
"""Bridge lecture 2 for Digital Imaging and Painting: the paint-over.

Written as the lecture for the painting course's session 12 (the one AI exercise),
so it fits the course in its current form with no schedule change. Options match
the outline's session 12 options exactly. Run from the repo root.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/bridge_for_Digital_Imaging_and_Painting/B2_The_Paint_Over.pptx"

SPEC = [
("title", "The Paint-Over", "Digital Imaging and Painting  |  Judging what the machine made",
"""**What this is.** The lecture for session 12, the paint-over, which is the one generative exercise in this course. It fits the course as it stands: same session, same options. Milestone 2 (the value block-in for the frame extension) is collected at the start, as scheduled.

**Running time, about 50 minutes.** Milestone check and Spot it (6). Why this is a painting exercise (4). The painter's checklist, in painting order (18). The callout layer and the fix (10). Worked example and cold reversal (6). Your extension versus a generated one (4). Options (2).

**Prep.** The instructor-generated image set with typical errors (hands, light direction, perspective, mush), one per student plus spares, on Canvas, plus the second image for Option A. One image of your own, already called out and fixed, for the worked example, and one unfixed for the cold reversal. Slot images: a generated hand with errors, a generated image with even, everywhere detail, and the Pope puffer jacket image (2023 or so), shown in class.

If you also ran "What the Machine Is Doing" earlier in the course, skip the recap slide."""),

warmup("one of the instructor-generated images from today's set",
       "Use one of the images the students are about to work on. They get a head start, and you see what they catch on their own."),

("bullets", "Milestone 2 is in",
["Value block-in, collected.",
 "Today: someone else's image.",
 "Back to your extension tomorrow."],
"""Milestone 2, your value block-in, is in. [Collect.]

Today is the one session in this course where we work on generated images. I made them at home, so nobody's generating anything. You'll be correcting them by painting, using everything from the first three weeks.

Tomorrow it's back to your own frame extension, and I think you'll find today useful for it, for a reason I'll get to at the end."""),

("bullets", "If you missed it: what these are",
["Built out of noise, steered by words.",
 "Good at surfaces, bad at rules.",
 "No decisions about light or focus."],
"""[Skip if you ran the earlier bridge lecture.]

A generator builds a picture out of noise, a little at a time, steered by words, using patterns absorbed from millions of captioned images. It's very good at surfaces: textures, materials, general mood. It's unreliable at things with rules: where the light comes from, one horizon, anatomy. And it makes no decisions about what should read first.

Which means its mistakes are painting mistakes."""),

("quote", "Today's idea", "The generator produced something.",
"The painter decides what's wrong with it.",
"""Here's the point of today, and it's the only reason this exercise is in a painting course.

The generator produced something. Your job is to decide what's wrong with it, and fix it with paint. That's judgment, and judgment is what this course has been training since the first squint test."""),

("bullets", "Why this is a painting exercise",
["Every error here is a painting error.",
 "Value, light, form, edges, perspective.",
 "You already have the words."],
"""Every error in today's images is one you already have a word for: a value structure that doesn't hold, a light that comes from two places, a cast shadow that falls the wrong way, edges that are all equally sharp, a horizon that doesn't agree with itself.

None of these are "AI problems." They're imaging problems, and the tool happens to produce a lot of them. Which means you don't need to learn anything new today. You need to look with what you already know."""),

("checklist", "The painter's checklist",
["1. Value structure (squint)", "2. Light direction", "3. Form: core and cast shadows",
 "4. Edges and material", "5. Perspective and scale", "6. Anatomy and hands"],
"""Here's the checklist for today, in painting order. Photograph it.

Value structure first, because if that's wrong, nothing else matters. Then light direction. Then form: are the core and cast shadows where the light says they should be? Then edges and material. Then perspective and scale. Then anatomy and hands.

Notice that hands are last. Everyone sees the hands first, because they're loud. A painter checks the big structure first, because that's where the image actually lives or dies."""),

("image", "1. Value structure", "value_check.png",
"Desaturate. Squint. Is there a light mass, a dark mass, a focal point?",
"""One: value, the squint test from session 2. Desaturate the image, or put a black and white adjustment layer on top, and squint.

Is there a clear light mass and a clear dark mass? Does something read first? Or is it medium against medium everywhere? Generated images are often the latter: plenty of color and detail, and in gray, nothing holds.

If the value structure fails, your first fix isn't a hand. It's a big, soft value pass: darken what doesn't matter, so the focal area can be the lightest or highest-contrast part."""),

("bimage", "2. Light direction",
["Point at the light.",
 "Every shadow agrees?",
 "Highlights face the source?"],
"error_light.png",
"""Two: light direction. Point at where the light is coming from. Literally point. Then check that every cast shadow falls away from that point and every highlight faces it.

Two suns, as here, is the classic generated error: each object lit convincingly on its own, the scene as a whole impossible. In the images today there's at least one of these. Most people never notice it. You will."""),

("image", "3. Form: core and cast", "light_spheres.png",
"Light side, core shadow, cast shadow, bounce, highlight. In the right places?",
"""Three: form. Same as the primitives in session 3. Light side, core shadow, cast shadow, bounce light, highlight. Are they where the light says they should be, on every form?

Generated images often get the light side right and fumble the rest: the core shadow wanders, the cast shadow is missing or too soft, the bounce light is the wrong color for what it's bouncing off. Those are small paint fixes with big effects."""),

("bimage", "4. Edges and material",
["Everything equally sharp?",
 "Hard, soft and lost: where?",
 "Does metal read as metal?"],
"slot:a generated image with even, everywhere detail and uniform edges",
"""Four: edges and material, session 4. Generated images tend to have the same edge quality everywhere: everything equally sharp, equally detailed. There's no edge hierarchy, so there's no focus.

Your fix is to decide: hard edges at the focal point, soft edges where forms turn away, lost edges where things merge into shadow. And check materials: does the metal have a sharp highlight and a dark reflection, does the cloth have soft edges? Often the generator gets the texture of a material right and its edges wrong."""),

("bimage", "5. Perspective and scale",
["Find the horizon.",
 "Lines agree with it?",
 "Figures the right size?"],
"error_perspective.png",
"""Five: perspective, which you've just been doing for your extension in session 11. Find the horizon line, check that receding lines go to vanishing points on it, check that figures are the right size for where they stand.

The fix is often not painting at all, but Transform and Warp on a part of the image, guided by a perspective grid on its own layer. Same as you'd do for your extension."""),

("bimage", "6. Anatomy and hands",
["Count the fingers.",
 "Joints bend one way.",
 "Shoot your own hand as reference."],
"slot:a generated hand with errors (from today's set)",
"""Six: anatomy and hands. Count the fingers, actually count. Check the joints. Check that two hands belong to the same person.

The best fix: put your own hand in the same pose, light it from the same side, take a photo, and use it as reference, or mask it in and paint over it. Painters have used their own hands in a mirror as reference for centuries. This is that, with a phone."""),

("section", "Marking it up, then fixing it", "",
"""Now how the work goes in the file."""),

("boxes", "The callout layer",
["Lock the original|never paint on it", "CALLOUT layer|circle and number", "List|number, check, fix",
 "FIX_ layers|one per fix"],
"""Four steps, and the grade rests on them as much as on the paint.

**Lock the original** image layer and never paint on it. Add a layer called **CALLOUT**, circle and number each error. **List** them: number, which check it fails, what you'll do. Then each fix on its own layer, **named for what it fixes**: FIX_cast_shadow, FIX_left_hand, FIX_value_pass.

So anyone can turn the fixes on and off and see the before and after, which is what Option A asks for."""),

("image", "What it looks like", "heal_demo.png",
"Generated, called out, fixed on its own layer.",
"""A simple example. As generated, the saucer's rim and the spoon melt into the table. The callout circles and numbers it. The fix is on its own layer, painted and cloned from the image's own material, and you can toggle it.

That's the whole session in three frames."""),

("bullets", "Fixing by painting",
["Structure, then light, then surface.",
 "Sample color from the image.",
 "Value first, then color."],
"""How to fix, and it's how you've been painting all month.

**Order**: structure first (value masses, perspective, anatomy), then light (shadows and highlights agreeing), then surface (texture, edges). Doing it out of order means doing it twice.

**Sample** your colors from the image itself, so the fix lives in its palette. And **value first**: get the light and dark right, then worry about the hue. A fix with the right value and a slightly wrong color usually disappears. The reverse never does."""),

("image", "Make the fix disappear", "composite_zoom.png",
"Match the grain and the edge softness, at 100%.",
"""Last thing about fixing. Your paint is often cleaner than the image around it: no grain, crisp edges. Zoom to 100% and compare.

If the image has grain, add a little noise to your fix layer (Filter, Noise, Add Noise, monochromatic, a small amount). If the image is soft, soften your edges to match. It's the same matching you did in session 8 with photographs: light, color, grain, edges.

Sometimes your fix is better painted than the rest of the image, and that makes it stick out too. Match the image."""),

("boxes", "Worked example",
["Squint|value fails?", "Point|where's the light?", "Callout|number each error",
 "Fix|structure, light, surface", "Match|grain at 100%"],
"""[Show your own worked example, before, callouts, fixed.] The order I worked in: squint first, and the value structure failed, so a big soft value pass came first. Then I pointed at the light and found the second sun. Then the callouts for everything else. Then fixes in order. Then matching at 100%.

Notice how much of the time was looking rather than painting."""),

("image", "Now you: plan the fixes", "slot:a second generated image from your set, unfixed",
None,
"""Cold reversal. In pairs, two minutes. Go down the checklist on this one and plan the fixes: what's wrong, in what order would you fix it, and with what?

[Take two or three plans. Don't confirm. Ask which pair started with value and which started with the hands, and why.]"""),

("bimage", "In the wild: the white puffer jacket",
["A famous fake, 2023 or so.",
 "Millions believed it.",
 "A painter would have caught it."],
"slot:the generated image of the Pope in a white puffer jacket, 2023 or so",
"""[About three minutes.] You've probably seen this one: a generated image of the Pope in a huge white puffer jacket, which went around the world in 2023 or so, and which a lot of people believed.

[Ask: what gives it away?] The hand doesn't close around the cup. The glasses melt into the cheek. The light on the face is too even for the scene. Every one of those is on our checklist.

Nobody needed special software to catch it. They needed ten seconds of looking the way you've been taught to look in this course."""),

("bullets", "Your extension versus Expand",
["Expand fills the space.",
 "You decide what the space says.",
 "That's the whole final."],
"""One last thing, and it's why today matters for your final.

Photoshop has a feature that extends an image past its edges automatically. It fills the new space with something plausible: more sky, more room, more wallpaper. And mostly that's all it adds.

Your frame extension is graded on something the tool doesn't do: the new space has to **change or add to what the image says**, and you have to name that decision. That's the difference between filling space and composing it. The generator can fill. Only you can decide what the space is for."""),

vocab([("Paint-over", "correcting an image by painting on new layers"),
       ("Callout layer", "numbered errors, on their own layer"),
       ("Two suns", "objects lit from different directions"),
       ("Mush", "detail everywhere, value structure nowhere"),
       ("Edge hierarchy", "hard at the focus, soft and lost elsewhere"),
       ("FIX_ layer", "one correction, named for what it fixes")]),

("options",
["A second paint-over", "on a provided image.", "Each fix on its own named layer."],
["Short written comparison: three things", "the generator got wrong and how you", "fixed each, with layer names."],
"""Before next class, the same options as in the course outline for this session.

**Option A**: a second paint-over on the provided image, each fix on its own named layer, with the callout layer above.

**Option B**: a short written comparison: three things the generator got wrong in your image from today, and how you fixed each one, with the layer names. Write it in painting terms.

Same rubric. Tomorrow, back to your frame extension, color pass coming up."""),

("quote", "One line to take home", "Most people see the hands.",
"A painter sees the shadows.",
"""Most people see the hands. A painter sees the shadows. [Demo: one image, called out and fixed, out loud, starting with the squint.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
