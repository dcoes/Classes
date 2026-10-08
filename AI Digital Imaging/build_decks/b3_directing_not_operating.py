#!/usr/bin/env python3
"""Bridge lecture 3 for Digital Imaging and Painting: directing, not operating.

The thinking behind AI workflows (brief, reference, structure input, integration),
taught through the painting course's own tools: thumbnails, value, light and photo
integration. Students generate nothing; the instructor runs one student-style
thumbnail through a workflow at home. Run from the repo root.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, vocab

OUT = "AI Digital Imaging/bridge_for_Digital_Imaging_and_Painting/B3_Directing_Not_Operating.pptx"

SPEC = [
("title", "Directing, Not Operating", "Digital Imaging and Painting  |  The thinking behind AI workflows",
"""**What this is.** A stand-alone lecture, about 50 minutes, on how people who use generators well actually work: a brief, references, a drawing as input, and integration by hand. It suits the week the frame extension thumbnails are due (session 10), because the thumbnail is the hero of the argument. Run it as an extra meeting, or in place of a lighter lecture day, keeping that day's own options if you prefer them to the ones here.

**Running time.** A prompt is a brief (10). The describe-and-sketch exercise (8). The ladder of control (12). Integration is photo-and-paint again (8). Does drawing matter more now (6). Options (4) and close.

**Prep, at home.** Take one rough three-value thumbnail (yours, or an anonymous one from a past class, with permission) and run it through a structure-guided workflow, so you have the thumbnail and four or five outputs side by side. Make a set of six generated images for one short brief, for Option A. One film still, hidden, for the describe-and-sketch exercise.

**Boundary.** This names how direction works so painters can see where their skills fit. It doesn't teach prompting or Generative Fill; that's the AI Digital Imaging course."""),

("bullets", "A question to start",
["Who decides what's in a picture?",
 "The tool, or the person?",
 "It depends on what you hand over."],
"""A question to start, and I'd like a few answers. When someone makes an image with a generator, who decides what's in it?

[Let them answer. Usually it splits between "the AI does" and "the person does, with the prompt."]

The honest answer is: it depends on how much of the decision the person hands over. Someone who types four words and takes the first result has handed over almost everything. Someone who arrives with a brief, a reference and a drawing has handed over very little.

Today is about the second kind of person, because that's how the people who use these tools well actually work, and because nearly all of it is stuff this course already teaches."""),

("quote", "Today's idea", "A prompt is a brief.",
"Art directors have been writing these for a century.",
"""Start here. A prompt is a **brief**, the same document art directors have handed illustrators and photographers for about a century: what the image is, how it should look, what must be true, and a picture of what they mean.

The only new thing is the reader. A person can ask you questions. A generator can't, so it fills every gap with the most average possible answer."""),

("boxes", "Five parts of a brief",
["Subject|who, doing what", "Composition|shot and angle", "Lens|wide or long",
 "Light|source, time, softness", "Style|medium and finish"],
"""For image-making, a brief has five parts, borrowed from film and photography.

Subject, composition, lens, light, style. Every part you leave out is a decision you've handed to the average.

Notice which two parts you've spent the most time on in this course: light and composition. That's not a coincidence. They're the hardest parts to describe and the ones that matter most."""),

("image", "Light words are painter's words", "light_spheres.png",
"Overhead, golden hour, overcast, rim, practical.",
"""The vocabulary that works for light in a brief is the vocabulary from session 6: warm light, cool shadow, golden hour, overcast, rim light, a "practical" (a visible light source like a lamp).

"Dramatic lighting" tells anyone, person or machine, nothing. "A single warm light low from the left, cool shadows, the background falling to near black" is a decision. You've been making those decisions with a brush for three weeks. The same words, written down, are the most useful part of any brief."""),

("bullets", "Vague words get the average",
['"Dramatic" is not a direction.',
 "The average of everything is nothing much.",
 "Specific words make decisions."],
"""Why vagueness is the enemy. A vague request gets an average answer, because the average is the only honest answer to a vague request. "Epic," "beautiful," "dramatic," "high quality": all of them push toward the same glossy middle.

The same is true when you're the one being briefed, by the way. When a client says "make it pop," your job is to ask the questions that turn it into a decision: pop how, where, compared to what?"""),

("section", "Words are lossy", "An exercise",
"""An exercise, about eight minutes."""),

("bullets", "Describe and sketch",
["One person sees the image.",
 "Sixty seconds to describe it.",
 "Everyone else thumbnails it."],
"""[Show a hidden film still to one volunteer only.] Our volunteer has sixty seconds to describe the image, no pointing. Everyone else makes a quick three-value thumbnail of what they hear, two minutes.

[Run it. Hold up several thumbnails, then reveal the still.]

What got through? Usually the subject. What got lost? Placement, scale, and the pattern of lights and darks: the value structure, the thing you've been told is the most important part of an image.

That's exactly what happens when someone describes a picture to a generator. Words carry "what" quite well and "where" very badly."""),

("section", "The ladder of control", "",
"""So if words can't carry "where," what can?"""),

("boxes", "From least control to most",
["Words|what it is", "Reference|how it looks", "Rough paint|roughly where",
 "A drawing|exactly where"],
"""A ladder. **Words** say what. A **reference image** says how it looks. **Rough paint** under a generated fill says roughly where. A **drawing** used as structure input says exactly where: the layout, the pose, the depth.

Each rung up, the person supplies more of the decision and the machine makes less of it. The people getting the best results from these tools are almost all near the top of the ladder."""),

("image", "Drawings, as input", "control_inputs.png",
"A sketch, a pose, a depth map, an edge map. Each locks something different.",
"""Four kinds of structure input that generators can follow. A sketch, which locks the layout. A pose skeleton, which locks the gesture. A depth map, near is light and far is dark, which locks the space. And an edge map, traced outlines, which locks nearly everything.

Look at the first and third. A rough layout drawing and a value map of the space. Those are, more or less, a thumbnail and a value block-in. The two things this course asks you to make before you paint anything."""),

("image", "One thumbnail, run through a generator", "slot:a three-value thumbnail beside four or five outputs generated from it as structure input",
"The layout and the value plan hold. Everything else varies.",
"""[Show your thumbnail and the outputs.] Here's a rough three-value thumbnail, and several images generated with it as structure input, on my computer at home.

Notice what held across all of them: the composition, the horizon, where the big lights and darks are. That's the thumbnail's work. What varies is everything the thumbnail didn't decide: textures, details, specific objects.

And notice which output is best. It's the one where the generator got out of the way of the thumbnail. The decisions that make the picture work were made in two minutes, with a pencil, before anything was generated."""),

("quote", "A rigging idea", "Don't ask it to be careful.",
"Build the control so the wrong thing can't happen.",
"""A small confession about my other job. Outside teaching I build rigs, the controls animators use to move characters, and the main lesson of rigging is that you don't ask the animator to be careful with the elbow. You build the control so the elbow can't bend backward.

Structure input is that idea applied to a generator. You don't ask it nicely to put the horizon low and the figure on the left, in a longer and longer prompt. You hand it the drawing where the horizon is low and the figure is on the left. Then it can't do anything else."""),

("section", "Integration is painting", "",
"""The last part of the workflow happens after generating, and you already know it."""),

("image", "Generated material is a source", "composite_demo.png",
"Same element, pasted on, then integrated: light, color, grain, edges.",
"""People who use generators professionally almost never use the output as is. They treat it as a **source**, like a photograph, and integrate it.

This is the same matching you did in session 8 with photographs: the light has to come from the same side, the color has to match the scene, the grain and sharpness have to match, the edges have to sit in the image, with a contact shadow where it touches.

On the left, pasted on. On the right, integrated. The generator can make the sphere. Making it belong is painting."""),

("bullets", "What the workflow really looks like",
["Brief and references first.",
 "A thumbnail as the input.",
 "Generate, choose, integrate, paint."],
"""So, the whole workflow, the way people who are good at this actually work.

A **brief and references** first, decided before anything is generated. A **thumbnail** as input. Then generate, **choose** with a reason, **integrate** with the light-color-grain-edges matching, and **paint** the corrections and the focal area by hand.

Count how many of those steps are things this course teaches. Most of them. The generation is one step in the middle, and in a sense the least skilled one."""),

("bullets", "Saying what you did",
["Keep the layers.",
 "Name what was generated.",
 "Say it before you're asked."],
"""And whatever else you take from this: if a generator was involved, keep the layers and say so. Which parts were generated, which parts you made. It's how professionals handle it, clients increasingly ask, and your layered file is also, as it happens, the evidence of what's yours."""),

("bullets", "Does drawing matter more now, or less?",
["It carries your decisions.",
 "Nobody else has it.",
 "It's the input the machine can't make."],
"""[About five minutes of discussion. Let them argue it.]

My own view, marked as a belief: drawing matters more, but in a different way. It used to matter mostly as a finished picture. Increasingly it matters as **the input**: the place your decisions about composition, value and light live, before anything renders them.

Anyone can type a prompt. A clear thumbnail of exactly what you mean is still yours alone. The tool is a means of expression, and the person using it is not an operator."""),

vocab([("Brief", "subject, composition, lens, light, style"),
       ("Reference", "a picture of what you mean"),
       ("Structure input", "a drawing the generator has to follow"),
       ("Thumbnail", "the cheapest and best structure input there is"),
       ("Integration", "matching light, color, grain and edges"),
       ("Disclosure", "saying what was generated and what you made")]),

("options",
["Rank six provided images", "against a short brief.", "Justify your top and bottom picks."],
["Write a five-part brief", "for your frame extension's", "new space. Then thumbnail it."],
"""Before next class. As with the other bridge lectures, if you run this on a regular session day, you can keep that day's options instead.

**Option A**: six generated images on Canvas, all made for one short brief. Rank them first to sixth against the brief, and justify your top pick and your bottom pick in a few sentences each. Watch out: the cleanest image isn't necessarily the best fit.

**Option B**: write a five-part brief, subject, composition, lens, light, style, for the new space in your frame extension, as if you were handing it to someone else to paint. Then make the three-value thumbnail that goes with it. Nobody generates anything; the brief and the thumbnail are the point."""),

("quote", "One line to take home", "Whoever makes the decisions made the picture.",
"Make them before you start.",
"""Whoever makes the decisions made the picture. Make them before you start, in a brief and a thumbnail, and the tool, any tool, has to follow you."""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
