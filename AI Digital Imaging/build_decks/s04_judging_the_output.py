#!/usr/bin/env python3
"""Session 4. Judging the output.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/04_Judging_the_Output.pptx"

SPEC = [
("title", "Judging the Output", "AI Digital Imaging  |  Session 4",
"""**Running time, about 50 minutes.** Spot it and recall (6). Why a checklist (4). The six checks, one at a time (18). Beyond the checklist: the brief and the value check (7). How to mark up, and the find-them-all exercise (9). Project 1 introduced (5). Options (1).

**Prep before class.** One "find them all" image with at least six errors across the checklist (mix them: one anatomy, one light, one perspective, one lettering, one repeated texture, plus general sheen). Four marked-up practice images for Option A, and six outputs for one short brief for Option B (include one that's technically clean but misses the brief, and one with a visible error that fits the brief well). The Project 1 packet: three flawed images, a short written brief for each.

Slot images: one of your generated hands with an anatomy problem, and one glossy over-smoothed generated portrait for the "sheen.\""""),

warmup("a generated image whose main error is light direction, not anatomy",
       "Pick one where the obvious-looking problem is not the biggest one. It sets up the order of today's checklist."),

("bullets", "Last time",
["The selection is the instruction.",
 "Remove, replace, extend.",
 "GEN_, FIX_, REF_, CALLOUT."],
"""Thirty seconds. [Cold call.] What were the three tells we checked after a fill? [Shadow or reflection left behind, a seam at the edge, a patch that doesn't match the grain.]

Those three are a small checklist already. Today we make the full one, and it's the most practical session in the course, because everything after this uses it. Project 1 is built on it, and so is every critique."""),

("quote", "Today's idea", "Looking is a skill.",
"And it's the one that gets paid.",
"""I believe this is the most valuable thing you'll learn this month, and I want to say why before we start.

Generating an image is now cheap and fast, and getting cheaper. **Seeing what's wrong with it** is not. A client, a lead, an art director, a hiring manager, they can all generate images. What they need is someone who looks at one and says "the light is coming from two directions and the horizon is tilted on the left," and then fixes it.

That's an eye, and an eye gets trained like anything else, by looking carefully, many times, with words for what you're seeing."""),

("bullets", "Why a checklist",
["Your eye gets used to the mistake.",
 "A list doesn't.",
 "Pilots use them. So do surgeons."],
"""Why a checklist rather than just "look carefully"?

Because the longer you look at an image, the more your eye forgives it. You stare at a generated picture for five minutes and the sixth finger stops looking strange. It becomes part of the picture. Anyone who has painted for a few hours and then looked at their work the next morning knows this feeling.

A list doesn't get used to anything. That's why pilots and surgeons use them, and they're not less skilled for it. They know that a skilled person looking at something familiar is exactly the person who misses the obvious.

So: you go down the list, every time, in order."""),

("checklist", "The six checks",
["1. Anatomy and hands", "2. Perspective", "3. Light direction",
 "4. Lettering", "5. Repeated texture", "6. The \"sheen\""],
"""Here are the six. Take a photo of this slide, it's the checklist for the rest of the course and it's on Canvas too.

Anatomy and hands. Perspective. Light direction. Lettering. Repeated texture. And the general "AI sheen," which is the hardest one to define and we'll get to it last.

Notice what we said in the first session: the generator is good at surface and bad at rules. Five of these six are **rules**. The sixth is a surface problem, the surface being too good, which is its own kind of tell."""),

("bimage", "1. Anatomy and hands",
["Count the fingers. Actually count.",
 "Joints bend one way.",
 "Ears, eyes, teeth: do they match?"],
"slot:one of your generated hands with an anatomy problem",
"""One, anatomy. Hands are the famous one, and you should still actually count the fingers, out loud if you have to, because your eye will tell you there are five.

Newer models are much better at hands than they were two or three years ago, which means the errors have moved somewhere subtler. Some of the places they hide now include: hands holding objects (where fingers merge into the handle), two people's hands touching, earrings that don't match left to right, pupils that point in slightly different directions, teeth that turn into one long tooth, and limbs that join the body in a place no skeleton would allow.

If you're an animation student, this is where your anatomy and figure drawing pays off directly. You know how an arm works. The generator only knows what arms usually look like."""),

("bimage", "2. Perspective",
["Find the horizon.",
 "Do all the lines agree?",
 "Is everything the right size?"],
"error_perspective.png",
"""Two, perspective. Find the horizon line first, then check whether the receding lines of buildings, tables, floors and roads all head toward vanishing points on that horizon.

In this diagram, the box on the left agrees with the floor. The red box on the right has its own private horizon somewhere up in the sky. Generated images do this constantly, especially in rooms and streets, because each object was "painted" to look right on its own, without any shared rule.

Then scale. Are the people in the background the right size for where they're standing? A quick check: in a photo taken from standing height, the heads of standing people on flat ground all sit roughly on the horizon line, whatever their distance. Generators get this wrong all the time."""),

("bimage", "3. Light direction",
["Where is the sun?",
 "Every shadow has to agree.",
 "Highlights and reflections too."],
"error_light.png",
"""Three, light, and if I could only keep one check, it would be this one, because untrained eyes almost never catch it and trained eyes always do.

Ask: **where is the light coming from?** Point at it. Then check that every shadow in the image falls away from that point, and that every highlight faces toward it.

Here, two spheres in the same scene, lit from opposite sides. Your eye accepts it at first, because each sphere is lit correctly on its own. That's exactly the generator's mistake: every object locally convincing, the scene as a whole impossible.

Painting students, this is the form and light material from your other course: light side, core shadow, cast shadow. The same thinking, used as a test."""),

("bimage", "4. Lettering",
["Letter-shaped, not letters.",
 "Signs, labels, book spines.",
 "Usually: replace by hand."],
"error_lettering.png",
"""Four, lettering. Text in generated images has historically come out as marks that look like letters from across the room and fall apart up close: backwards letters, letters that don't exist, words that are almost words.

Some newer models are quite a lot better at this, and a few are good at short headlines. So check every letter anyway, especially small text in the background: signs, labels, book spines, screens, license plates, T-shirts.

The professional fix is usually not to regenerate. It's to remove the fake text and set real type by hand, which is what we'll do in session 13. Real type is sharp, spelled right, and you chose the font."""),

("bimage", "5. Repeated texture",
["The same clump twice.",
 "Crowds of twins.",
 "Bricks, leaves, windows, clouds."],
"error_repeat.png",
"""Five, repeated texture. Look for the same thing appearing twice. Here, the same clump in the grass shows up five times, which is easy to see once it's circled and easy to miss when it isn't.

It happens in grass, leaves, gravel, brick, windows on a building, clouds, waves, and in crowds, where the same face or the same jacket appears in several places.

This is also, for what it's worth, the oldest Clone Stamp mistake there is. People have been leaving repeating clone patterns in retouched photos since the tool existed. The fix is the same as it always was: break the repetition by hand."""),

("bimage", '6. The "sheen"',
["Too smooth, too glossy.",
 "Everything in focus, everything lit.",
 "Perfect, and about nothing."],
"slot:a glossy, over-smoothed generated portrait (yours)",
"""Six, the "sheen." I put it in quotes because it isn't a technical term and I'm not sure there is one.

Some of what people mean by it includes: skin like plastic, no pores, no blemishes; everything at the same level of detail; a glossy rim light on everything; very saturated, very "cinematic" orange and teal color; perfect symmetry; and a general feeling of an advertisement for nothing in particular.

I'll be honest that this one is closer to taste than to a rule, and that it moves as the tools change. But clients and audiences have learned to spot it, and many react badly to it, so it's worth being able to name it. Usually the fix is to take some of the polish back out: grain, texture, imperfection, less saturation, a real focal point."""),

("section", "Beyond the checklist", "Does it do the job?",
"""The checklist catches errors. But an image can pass all six checks and still be the wrong image."""),

("bullets", "A clean image can still fail",
["Check the brief first.",
 "Then the errors.",
 "Rank against the brief, not your taste."],
"""This is where people go wrong in critique, and it's what Option B tonight practices.

A technically perfect image of the wrong thing is a failed image. If the brief says "a quiet, rainy evening" and you bring a perfect sunny afternoon, it doesn't matter how good the hands are.

And an image with one fixable error that nails the brief is a better starting point than a clean one that misses it. You can fix a hand. You can't easily fix the wrong idea.

So: **brief first, errors second.** And when you rank images, rank them against the brief, not against what you personally like. That's the same rule we'll use in every critique this month."""),

("image", "Check it in gray", "value_check.png",
"Desaturate it. Squint. Does anything read first?",
"""One more check, and it's a painter's check. Put a black and white adjustment layer on top, or just desaturate a copy, and squint.

Does the image have a structure in gray: a clear light area, a clear dark area, something your eye goes to first? Or is everything a medium gray fighting with every other medium gray?

Generated images very often fail this. They're full of detail and full of color, and when you take the color away, there's nothing underneath, just mush. That's the "detail everywhere, focus nowhere" problem, and no amount of extra prompting fixes it. Paint fixes it, by darkening the parts that don't matter and keeping the light where the eye should go."""),

("section", "How to mark it up", "",
"""Now how to put all this on the file, because looking isn't enough. You have to show what you saw."""),

("boxes", "The callout layer",
["Duplicate|keep the original", "New layer|named CALLOUT", "Circle and number|each error",
 "List|number, check, fix"],
"""Four steps.

**Duplicate** the original image layer and lock the original, so it's never touched. Make a **new layer** above it called CALLOUT. On that layer, **circle and number** each error in a bright color. Then, in a text layer or in your submission, **list** them: the number, which of the six checks it fails, and what you'd do to fix it.

"3. Light: shadow under the cup falls left, sun is on the left. Fix: repaint shadow to the right." That's one line, and it's worth more than a page of "the image has some issues.\""""),

("image", "What that looks like", "heal_demo.png",
"Generated, marked up, then fixed on its own layer.",
"""Here's the whole sequence on a simple example. As generated, the saucer's rim and the spoon melt into the table. The callout layer circles it and numbers it. Then the fix is on its own FIX_ layer, so you can switch it off and see the before and after.

That's exactly what Project 1 asks for, three times. And it's exactly what you'll practice tonight."""),

("image", "Find them all", "slot:your 'find them all' image, six or more errors, unmarked",
None,
"""[About six minutes.] Here's an image with several errors in it. In pairs, go down the checklist and find as many as you can. Write them down as numbered callouts, the way we just described: number, which check, where. Four minutes.

[Then go around the room, one error per pair, until nobody has anything new. Keep a count on the board.]

I'm not going to put an answer key up. You'll notice the room found the hands and the lettering first, because they're loud, and found the light and the perspective late, if at all. That's normal for week one, and it's why we do Spot it every single class."""),

("section", "Project 1: The Fix-It Set", "Due session 7",
"""Now, Project 1."""),

("bullets", "Project 1: The Fix-It Set",
["Three flawed images, from me.",
 "A short written brief for each.",
 "Find, call out, fix by hand.",
 "Every fix on a named layer."],
"""Project 1, the Fix-It Set, due at the start of session 7.

I'm giving you three generated images, and each one comes with a short written brief, a few sentences describing what the image is supposed to be. Each image has problems, some that the checklist catches and some that are about the brief.

For each image: a CALLOUT layer with every significant error numbered. Then fix them by hand, which is what session 5 is all about, with every fix on its own named FIX_ layer, so the before and after can be compared.

You can use small generative fills inside your own fixes if you want, as long as they're named GEN_ and the result is yours to defend. But the fixes are hand work, and that's what's being graded."""),

("boxes", "How it's graded",
["Errors found|25", "Hand corrections|30", "Meets the brief|25", "Process record|20"],
"""The rubric, so there are no surprises. It's on Canvas.

**Errors found**, 25 points: and to get the top level, you have to catch light and perspective, not only anatomy. **Hand corrections**, 30: corrections that sit naturally in the image without creating new errors. **Meets the brief**, 25: each fixed image does what its brief asks. **Process record**, 20: every correction on its own named layer, before and after easy to compare.

Notice that more than half the points are about seeing and deciding. The fixes matter, but a beautiful fix of the wrong problem doesn't get you far.""",
{"sub": "100 points. Rubric on Canvas."}),

("bimage", "In the wild: the chocolate factory",
 ["Generated posters, 2024.",
  '"A pasadise of sweet teats."',
  "Then the real warehouse."],
 "slot:the generated promotional posters for the 2024 Glasgow chocolate 'experience'",
"""[About five minutes, and the room usually enjoys this one.] In early 2024, an event in Glasgow sold tickets to a family "chocolate experience" using generated posters: candy landscapes, giant lollipops, glowing rainbow arches. The posters had lettering like "a pasadise of sweet teats" and "cartchy tuns." Families arrived to find a nearly empty warehouse with a few props, and the police were eventually called.

[Show the posters. Ask: run the checklist. What do you find?] Lettering, obviously. Repeated textures. The sheen. And then the big one, which isn't on the checklist at all: the image promised something nobody could deliver.

That's the brief failure in its purest form. The posters weren't checked against what was actually going to happen. A generated image can be a lie even when nobody meant it to be, simply because nobody looked."""),

("bimage", "In the wild: the white puffer jacket",
 ["A famous fake, 2023 or so.",
  "Millions believed it.",
  "The tells were in the hands and glasses."],
 "slot:the generated image of the Pope in a white puffer jacket, 2023 or so",
"""Another one you've probably seen. In 2023 or so, a generated image of the Pope in a huge white designer puffer jacket went around the world, and a lot of people, including people who work with images, believed it for a while.

[Show it. Thirty seconds. Ask: what gives it away?] The hand holding the cup doesn't quite close around it. The glasses melt into the cheek. The crucifix chain does something no chain does. The light on the face is a bit too perfect.

All checklist items. Nobody needed special software to catch it, just somebody who looked at the hands and the light for ten seconds instead of one. The person who made it said he hadn't meant to fool anyone. That's a disclosure question, and we'll come back to it in week three."""),

vocab([("Callout layer", "numbered errors, marked on their own layer"),
       ("Horizon line", "the eye level of the camera"),
       ("Vanishing point", "where parallel lines meet, on the horizon"),
       ("Cast shadow", "the shadow an object throws away from the light"),
       ('"Sheen"', "too smooth, too glossy, about nothing"),
       ("Value structure", "the pattern of lights and darks, seen in gray")]),

("options",
["Mark up four provided images.", "Callouts on a named layer.", "Number, check, fix for each."],
["Rank six outputs against a brief.", "Justify your top pick", "and your bottom pick."],
"""Tonight, due next class.

**Option A**: four images on Canvas. Mark up every error on a CALLOUT layer, numbered, with the one-line list.

**Option B**: six outputs, all made for one short brief, also on Canvas. Rank them first to sixth against the brief, and write a short justification for your top pick and your bottom pick. Watch out: the cleanest image is not necessarily the best fit.

Same rubric. About an hour either way."""),

("quote", "One line to take home", "Your eye forgives. The checklist doesn't.",
"Go down the list, every time, in order.",
"""Your eye forgives. The checklist doesn't. [Demo: mark up one image live, out loud, going down the list.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
