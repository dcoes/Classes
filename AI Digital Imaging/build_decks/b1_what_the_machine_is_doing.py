#!/usr/bin/env python3
"""Bridge lecture 1 for Digital Imaging and Painting: what the machine is doing.

A stand-alone lecture that introduces generative imaging to a painting class in its
current form. Students generate nothing; every image is instructor-made. Uses the
painting course's own vocabulary (value, form and light, edges, perspective).
Run from the repo root.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/bridge_for_Digital_Imaging_and_Painting/B1_What_the_Machine_Is_Doing.pptx"

SPEC = [
("title", "What the Machine Is Doing", "Digital Imaging and Painting  |  A painter's look at generated images",
"""**What this is.** A stand-alone lecture, about 50 minutes, that introduces generative imaging to the painting course without changing its shape. Students don't generate anything. It assumes they've had the value and form-and-light sessions, so it fits best anywhere after session 3; the strongest spot is shortly before the paint-over in session 12, either as an extra meeting or in place of a lecture on a lighter day, keeping that day's own options.

**Running time.** The room and a little history (8). How it works (12). Why it fails where it fails, in painting terms (14). The job market and ownership, briefly (8). Spot it together (5). Options (3).

**Prep.** Two or three of your own generated images with typical errors, for the Spot it exercise and for Option A. Slot images: a daguerreotype (public domain), a darkroom print in a tray.

**Boundary.** This course owns painting fundamentals; the AI course owns generative workflows. This lecture names how the tools work and why a painter can see their mistakes. It doesn't teach prompting or Generative Fill."""),

("quote", "Let's start with the room", "Some of you think this is cheating.",
"That's allowed here.",
"""A topic I'd rather raise than avoid: image generators. Some of you think they're cheating. Some of you think they're worse than that. Some of you use them every day.

All of those are allowed in this room. Nothing today asks you to use these tools, and nothing in this course will require it. What I'd like is for you to understand what they're actually doing, because it turns out that a painter is unusually well equipped to see what they get wrong."""),

("bullets", "Hands up",
["Used an image generator?",
 "Avoid them on purpose?",
 "Haven't decided?"],
"""Quick show of hands, nobody gets graded. [Ask the three. Count aloud.]

The room is always split. That's fine. By the end of today, everyone, including the people who'll never touch one, should be able to look at a generated image and say, in painting words, what's wrong with it."""),

("bimage", "1839 or so",
["Photography arrives.",
 '"From today, painting is dead."',
 "Painters used photos anyway."],
"slot:a daguerreotype, e.g. Daguerre's Boulevard du Temple (public domain)",
"""A bit of history. Around 1839 or so, photography arrives, and a painter named Paul Delaroche supposedly says "from today, painting is dead." Historians aren't sure he said it.

Painting didn't die. Portrait painters lost a lot of work, quite quickly. And painting changed: the Impressionists went after exactly what the cameras of the time couldn't do, and painters used photographs as reference almost from the start, some of them secretly.

You're doing that in this course, in session 8: photo and paint, integrated. Bringing a new kind of image source into a painting isn't new. The question of what the painter's part is gets asked every time."""),

("section", "How it works", "No magic, a lot of arithmetic",
"""So, how does a generator make a picture? I'll keep it mechanical."""),

("bullets", "It isn't a collage machine",
["No stored pictures inside.",
 'It "learned" what things look like.',
 "It builds new pictures out of noise."],
"""The common belief is that a generator keeps a library of pictures and cuts them together. It doesn't. There are no stored images inside it. There's a very large set of numbers, adjusted during training until the system got good at one job.

It "learned" what pictures with certain captions tend to look like. I put "learned" in quotes because it doesn't know what a cat is, or what light is. It knows what pictures captioned "cat" or "sunset" usually look like.

That difference, knowing how things look versus knowing how they work, explains every mistake we'll look at today."""),

("image", "An image developed out of noise", "diffusion_strip.png",
"It removes a little noise at a time, steered by the words.",
"""This is the mechanism, called "diffusion." It starts from pure noise, like static, and removes a little of it, step by step, often thirty to fifty times, each step nudged by the words in the prompt toward something that matches.

To be honest about the slide: I made this strip by adding noise to an old NASA photograph and showing it backwards. A real generator starts from static with no picture underneath at all.

[Point at the early steps.] Notice what arrives first: the big value masses, the overall color, the composition. Detail comes last."""),

("bullets", "Big shapes first, detail last",
["Value masses arrive first.",
 "Then form. Then detail.",
 "Sound familiar?"],
"""Which should sound familiar. It's roughly the order you paint in: block in the big values, then turn the forms, then the detail and the edges. It's why your final project has a block-in milestone before the color pass.

The analogy breaks in one important place, though. When you block in, you **decide** where the light comes from and what reads first. The generator doesn't decide anything. Its block-in is the average of what pictures with those words usually look like, so the big decisions get made by accident.

That's the part a painter can see and fix."""),

("bimage", "A print in a tray",
["It comes up slowly.",
 "Big shapes first.",
 "But there's no negative."],
"slot:a photographic print developing in a darkroom tray",
"""If you've seen a print come up in a darkroom tray, that's close to what it looks like. Dark masses first, detail last.

Except in the darkroom there's a negative: a real photograph of a real moment. Here, **there is no negative.** The picture never existed. It's invented as it develops, steered by words and by everything absorbed in training. That's why the same prompt never gives the same picture twice."""),

("bullets", "Training, in plain words",
["Millions of captioned pictures.",
 "Noise added, then removed, over and over.",
 "Whose pictures? That's the argument."],
"""Where does the steering come from? Training. An enormous number of images with captions, billions for some well-known models, collected largely from the web. The system practices removing noise from them, over and over, and builds connections between words and how things look.

Whose pictures were they? Often, the work of living artists and photographers who were never asked. That's the center of the ethical and legal argument about these tools, and it's a fair argument. Adobe says its model was trained on licensed and public domain images instead; not everyone accepts that at face value.

I'm not going to tell you what to think about that. I'd like you to know that it's the real argument, rather than "robots bad" or "artists just mad.\""""),

("section", "Why it fails where it fails", "In painting terms",
"""Now the part this course is uniquely good at."""),

("bullets", "Surfaces, not rules",
["Good at textures and moods.",
 "Bad at things with rules.",
 "Light has rules. So does perspective."],
"""A generator is very good at **surface**: textures, materials, the general feeling of a light, what a forest or a face usually looks like.

It's much worse at things that follow **rules**. Light comes from somewhere, so every shadow in a scene must agree. A scene has one horizon. A hand has five fingers that bend one way. Averaging millions of pictures gives you convincing surfaces and unreliable rules.

And the rules are exactly what you've been studying in this course: value structure, form and light, edges, perspective."""),

("image", "The four light questions, again", "light_spheres.png",
"Where it comes from, what color it is, how hard it is.",
"""Same object, five lights, the kind of exercise you did with the primitives. Noon overhead, golden hour low and warm, overcast and soft, rim light from behind, night with a warm lamp.

You know how to read these: where's the light side, the core shadow, the cast shadow, the bounce, the highlight. The generator produces images that **look like** these, but it doesn't track where the light actually is. That's next."""),

("bimage", "Two suns",
["Each sphere is lit correctly.",
 "The scene is impossible.",
 "A painter sees it in a second."],
"error_light.png",
"""This is the single most common error a painter can spot in generated images. Each object, on its own, is lit convincingly. Together, they're lit from opposite sides. Two suns.

The generator makes this mistake because each part was "painted" to look right locally, without a single light source for the whole scene. You'd never do this, because you start by deciding where the light is.

Most people, looking at a generated image, see the hands. A painter sees the shadows. That's a real, marketable difference."""),

("image", "Check it in gray", "value_check.png",
"Desaturate and squint. Does anything read first?",
"""The squint test, from session 2. Desaturate, squint, and ask: is there a value structure? A clear light mass, a clear dark mass, something that reads first?

Generated images very often fail this. Lots of color, lots of detail, and underneath, in gray, everything is a medium tone fighting every other medium tone. Detail everywhere, focus nowhere. Some people call it "mush."

No prompt fixes this reliably. Paint does: darken what doesn't matter, keep the light where the eye should go. That's a value decision, and the generator doesn't make value decisions."""),

("bimage", "One horizon",
["Find the horizon.",
 "Do the lines agree?",
 "Is everything the right size?"],
"error_perspective.png",
"""Perspective, which you'll use heavily in the frame extension. Find the horizon, then check whether every receding line agrees with it. The box on the right has its own private horizon somewhere in the sky.

Generated rooms and streets do this constantly: each object plausible, the space impossible. Same root cause as the two suns: no single rule for the whole image."""),

("bullets", "What a painter sees that a prompt can't",
["Where the light comes from.",
 "What should read first.",
 "What the image is for."],
"""So here's the summary, and I'll mark it as a belief.

A painter brings three things the generator doesn't have. A decision about **where the light comes from**, held across the whole image. A decision about **what should read first**, carried by value and edges. And an idea of **what the image is for**, which is what your frame extension is about: what the new space adds or changes.

Generators produce candidates. They don't make those decisions. In my experience these tools are most useful in the hands of people who already know what they're trying to achieve, and least useful to people who don't."""),

("section", "Plainly, about jobs", "",
"""A few minutes on the job market, because you deserve a straight answer."""),

("image", "What working developers think", "gdc_chart.png",
"Same survey, three years. About a third of them use these tools at work anyway.",
"""This is from the Game Developers Conference's annual survey of people working in games, a bit over 2,300 of them in the 2026 report. The share who say generative AI is having a negative impact on the industry went from 18% to 30% to 52% in three years, and it's around 64% among visual and technical artists. About a third use the tools at work anyway.

The honest picture: entry-level image-making work has contracted. I'm not going to tell you the field is fine.

What I believe holds up is the list on the next slide."""),

("bullets", "What still costs money",
["Knowing what you want.",
 "Seeing what's wrong.",
 "Fixing it by hand.",
 "Saying what you made."],
"""Knowing what you want: a brief, a light, a composition, decided before you start. Seeing what's wrong: the two suns, the mush, the private horizon. Fixing it by hand: which is painting. And saying what you made, honestly.

Three of those four are things this course already teaches. The tool is a means of expression, and the person using it is not an operator."""),

("bullets", "Who owns a generated image?",
["US: copyright needs a human author.",
 "A prompt alone usually isn't enough.",
 "Your hand work can be yours."],
"""Briefly, because it surprises people. In the US, as of this term, copyright requires a human author. Purely generated images aren't protected, and the Supreme Court declined to revisit that in early 2026. The Copyright Office's position is that writing a prompt, even a detailed one, usually doesn't make you the author of what comes out.

What can be protected is what a person contributes: selection, arrangement, and changes made by hand. So in a sense, the painting is the part that's yours. [I'm not a lawyer, and this changes; check it before you rely on it.]"""),

("bullets", "Say what was generated",
["What was generated.",
 "What you made.",
 "Plainly, without being asked."],
"""And one professional habit, whatever you think of the tools: if a generator touched something, say so. Which parts were generated, which parts you made. A sentence or two.

It's how professionals handle it now, and clients increasingly ask. In this course it applies to the one paint-over exercise, where the images come from me, and you'll say so in the layer names."""),

warmup("one of your generated images with a light or value problem and a hand problem",
       "Do this one as a whole-room exercise, about five minutes, and insist on painting vocabulary: light side, cast shadow, value mass, edge, horizon."),

vocab([("Diffusion", "an image built up out of noise, step by step"),
       ("Training data", "the captioned pictures it learned from"),
       ("Surface vs rule", "it's good at the first, bad at the second"),
       ("Two suns", "objects lit from different directions"),
       ("Mush", "detail everywhere, value structure nowhere"),
       ("Disclosure", "saying what was generated and what you made")]),

("options",
["Mark up two provided generated images.", "Callouts: light, value, perspective, edges.",
 "One line per error."],
["About 150 words: one thing a painter", "can see that a generator can't,", "with an example."],
"""Before next class. These sit in place of that day's usual options if you run this lecture on a regular session day.

**Option A**: two generated images on Canvas, from me. On a new layer called CALLOUT, circle and number every error you find, and write one line for each in painting terms: "2. Cast shadow falls left, light is on the left."

**Option B**: about 150 words. One thing a painter can see that a generator can't, with a specific example from one of the images we looked at, or from your own observation.

Same session rubric as always. Nobody needs to generate anything."""),

("quote", "One line to take home", "It knows how things look.",
"You know how they work.",
"""It knows how things look. You know how they work, and that's the part that's worth something."""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
