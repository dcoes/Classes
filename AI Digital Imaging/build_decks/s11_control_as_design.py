#!/usr/bin/env python3
"""Session 11. Control as a design problem.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/11_Control_as_a_Design_Problem.pptx"

SPEC = [
("title", "Control as a Design Problem", "AI Digital Imaging  |  Session 11",
"""**Running time, about 50 minutes.** Spot it and recall (5). The ladder of control (5). Four kinds of structure input (12). What a node workflow is, and why it isn't in the lab (8). Too much control (3). The version you can do in the lab (4). Worked example and cold reversal (6). Does drawing matter more now (5). Options (2).

**Prep before class, at home.** This session depends on work you do on your own machine. Run one simple scene through a node-based workflow (ComfyUI or similar) with each structure input: a rough sketch, a pose skeleton, a depth map and an edge map, same prompt each time. Save the inputs and outputs side by side. Screenshot the node graph. Make the Option A set: several outputs from one pose and one depth input, so students can pick and composite.

Tell students tonight that Option B sketches need to be submitted by a set time (say 8 p.m.) so you can run them before the next class. Keep that promise; it's the whole option.

The demo today is you showing the workflow running, live if your laptop can do it, or a screen recording if it can't."""),

warmup("a generated figure whose pose is wrong for the brief, though nothing is anatomically broken",
       "The point of today's image: nothing is 'wrong' on the checklist, it's just not the pose anyone asked for. That's a control problem, not an error."),

("bullets", "Last time",
["The brief is the first image.",
 "A board carries what words can't.",
 "Musts and must-nots."],
"""Recall. [Cold call.] What are the five parts of the brief? What did the swap exercise tell you about yours?

Today's Spot it image had no errors on our checklist. The anatomy was fine, the light was fine. It just wasn't the pose the brief asked for. And no amount of rewording fixed it, because words, as we found in session 2, are bad at "where."

Today is about the inputs that are good at "where.\""""),

("quote", "Today's idea", "More control comes from better input.",
"And the best input is still a drawing.",
"""Here's today's argument, and it's the one I'd most like you to take out of this course.

When people want more control over a generator, they usually write longer prompts. That mostly doesn't work. What works is **better input**: giving the machine more of the decision before it starts.

And the best input there is, still, is a drawing. Not a good drawing. A clear one."""),

("boxes", "The ladder of control",
["Words|what it is", "Reference image|how it looks", "Your rough paint|roughly where",
 "Structure input|exactly where"],
"""A ladder, from least control to most.

**Words** tell it what. **A reference image** tells it how it looks. **Your rough paint** under a fill, from sessions 3 and 5, tells it roughly where. And **structure input**, today's topic, tells it exactly where: the pose, the layout, the depth of the scene.

Each step up, you supply more of the decision, and less of it gets made for you. That's the same sentence I've been saying since week one, and today it gets its most literal form."""),

("image", "Four kinds of structure input", "control_inputs.png",
"Each one locks something different. None of them is a finished picture.",
"""Four kinds of structure input. All of these were made on a computer for this slide, the last one from an old NASA photo.

A **sketch**: your layout and shapes, in lines. A **pose**: a stick-figure skeleton, the colored lines are a convention these tools use to tell the left arm from the right. A **depth map**: a gray image where near things are light and far things are dark. An **edge map**: the outlines of a photo or drawing, traced automatically.

The tool that reads these is often called a "ControlNet," a name from a research paper in 2023 or so. I put it in quotes because you'll see the word online, and it's really just "structure guidance." Each input locks something different, and each one leaves the rest to the generator."""),

("bullets", "A sketch",
["Your layout and shapes.",
 "The cheapest control there is.",
 "A bad drawing with a clear layout is fine."],
"""A sketch locks the layout: where the horizon is, where the figure stands, the big shapes. It's the cheapest kind of control in the world. You need a pencil and two minutes.

And it doesn't need to be good. A wobbly drawing with a **clear layout** works better than a beautiful drawing with a confused one. The generator reads the big shapes, not your line quality.

This is the thumbnail from storyboarding and from painting, in a new job. Same drawing, new reader."""),

("bullets", "A pose",
["A skeleton locks the pose.",
 "Not the body, not the costume.",
 "Hands still drift."],
"""A pose input locks the gesture: where the head is, the angle of the spine, where the arms and legs go. It doesn't lock body type, costume, or face. That's still words and references.

You can get a pose skeleton by drawing it, by posing a 3D mannequin, or by having the tool extract it from a photo, including a photo of you acting out the pose. Animation students, you've done this: shoot your own reference.

Hands still drift, by the way. The skeleton has a dot for the wrist and maybe a few for fingers, and the generator fills in the rest, so the checklist still applies."""),

("bullets", "Depth and edges",
["Depth locks the space.",
 "Edges lock the outlines.",
 "Both are good for keeping a place the same."],
"""Depth and edges, together, because they're both mostly about places.

A **depth map** locks the space: what's near, what's far, how the room or landscape recedes. It's very good at keeping a place consistent across a series, which is session 6's problem.

An **edge map** locks the outlines of everything. It's the strongest of the four, and the most dangerous, which is two slides from now.

3D students: a depth map is the same thing as the depth pass you'd render out of Maya. You can block a scene with primitives in 3D, render the depth, and use it as input. That's a very powerful pairing, and it's where a lot of studios are actually using this."""),

("section", "What a node workflow is", "",
"""Now, what's actually running on my machine at home."""),

("bimage", "Nodes: a visible recipe",
["Each box does one step.",
 "Wires carry the image along.",
 "You can see, and change, every step."],
"slot:a screenshot of your node graph (ComfyUI or similar)",
"""[Show your node graph.]

This is a node-based workflow. Each box does one step: load the model, read the prompt, load the pose, apply the structure guidance, run the denoising steps, decode the image, save it. The wires carry the data from one box to the next, like pipes in a plumbing diagram.

3D students, this will look familiar: it's the same idea as the node editor in Maya, or a shading network. And it's the opposite of Photoshop's generative features, which hide every step behind one button. Here, every step is visible and every setting can be changed.

That's both its strength and why we're not doing it in the lab."""),

("bullets", "Why it isn't in the lab",
["A strong graphics card.",
 "Installs, model files, updates.",
 "An afternoon of setup, at least."],
"""I said in session 1 that we wouldn't install anything, and here's the specific reason.

Running these workflows needs a strong graphics card, several gigabytes of model files, a set of installs that break when something updates, and at least an afternoon of setup before you make a single image. On lab machines, under IT restrictions, with fifteen people, that's a week of the course gone, and the lesson would become software troubleshooting.

So I run it, you get the output. The decisions about what goes in, the sketch, the pose, the choice of output, stay with you, and those are the parts worth learning."""),

("quote", "A rigging idea", "Don't ask it to be careful.",
"Build the control so the wrong thing can't happen.",
"""This is where my other job shows up a bit. Outside teaching, I build rigs, the controls that animators use to move characters. And the main lesson of rigging is this one: you don't ask the animator to be careful not to bend the elbow backward. You build the control so the elbow can't bend backward.

Structure input is that idea applied to the generator. You don't ask it nicely to put the figure on the left in a crouch, in a longer prompt. You hand it a pose where the figure is on the left in a crouch, and now it can't do anything else.

In a sense, the whole course has been moving toward this: less asking, more building the conditions."""),

("bullets", "Too much control",
["Edge maps copy everything.",
 "Including the mistakes.",
 "Lock what matters. Leave the rest."],
"""A warning, because control has a cost.

An edge map traced from a photo copies **everything**: the shapes, the clutter, the mistakes, the bad crop. Lock too much and the generator can't help you with anything; you've just made an expensive filter.

These tools usually have a strength setting, a dial for how strictly to follow the input. Lower strength gives the generator room. Higher strength locks it down.

The design question is: **what must be locked, and what can be left open?** It's the must and must-not list again. Lock the musts. Leave the rest for the generator to try things."""),

("bullets", "The lab version",
["Rough paint, then fill.",
 "A reference image for the look.",
 "Structure reference, where available."],
"""So what can you do in the lab, without nodes? More than people think.

**Rough paint, then fill**: paint your layout and big shapes in flat color, then generate over it with a fill. That's structure input, the low-tech version, and you've been doing it since session 3. A **reference image** for the look. And where the tools offer it (Firefly has had a structure reference option, check what's there this term), you can hand it a sketch or a photo for layout directly.

Between those, you can get most of the way there. The node workflow is more precise, and it's what a lot of studios use. The thinking is identical."""),

("boxes", "Worked example: from thumbnail to image",
["Thumbnail|values only", "Clean layout|horizon, shapes", "Input|sketch or pose",
 "Generate|several, same input", "Pick and fix|by hand"],
"""The worked example, which I'll show from my machine in the demo.

A **thumbnail**, values only, three tones, the same exercise as in painting. A **clean layout** from it: horizon, figure placement, big shapes. Turn that into an **input**, a sketch or a pose. **Generate** several outputs from the same input, so the layout holds and everything else varies. Then **pick and fix**, the session 4 and 5 work, by hand.

Notice where the decisions happen: almost all of them are in the first two steps, on paper."""),

("image", "Now you: which input would you use?", "slot:a target image for one of the three brief types, no input shown",
None,
"""Cold reversal. Here's a target image. If you wanted to make something with this exact layout, which input would you use: a sketch, a pose, a depth map, an edge map? And what would you lock and what would you leave open? In pairs, two minutes.

[Take answers. Don't resolve. Different answers can all be defensible. Ask each pair what their choice would fail to control.]"""),

("bullets", "Does drawing matter more now, or less?",
["It carries your decisions.",
 "Nobody else has it.",
 "It's the input the machine can't make."],
"""Last question, five minutes of discussion. Does drawing matter more now, or less?

[Let them argue. The animation and storyboarding students usually have opinions.]

I'll say what I believe, and mark it as a belief. I think it matters more, but differently. A drawing used to be valuable as a finished picture. Increasingly it's valuable as **the input**: the place where your decisions about composition, pose, space and story live, which the machine then renders.

It's also the one input that only you have. Anybody can type a prompt. A clear thumbnail of exactly what you mean is still a human skill, and I don't see that changing soon. The tool is a means of expression, and the person using it is not an operator."""),

vocab([("Structure input", "a sketch, pose, depth or edge map that locks layout"),
       ('"ControlNet"', "the common name for structure guidance"),
       ("Depth map", "near is light, far is dark"),
       ("Edge map", "traced outlines; the strictest input"),
       ("Node workflow", "every step visible, wired together"),
       ("Strength", "how strictly it follows the input")]),

("options",
["Pick and composite the strongest", "images from the provided", "pose and depth set."],
["Draw a layout or pose sketch", "to be used as structure input.", "I'll run it before next class."],
"""Tonight, due next class.

**Option A**: the pose and depth set on Canvas, generated on my machine. Pick the strongest images for the brief that comes with the set, composite the best parts together, and fix by hand. Say why you picked what you picked.

**Option B**: draw a layout or pose sketch for one image in your final, clear and simple, and upload it by eight tonight. I'll run it through the workflow and you'll have the outputs at the start of next class, to use in your rough set.

Next class is Milestone 2, your rough set. All three or four images, rough, critiqued against your brief and your must and must-not list."""),

("quote", "One line to take home", "Don't ask it nicely. Hand it the drawing.",
"More control comes from better input.",
"""Don't ask it nicely. Hand it the drawing. [Demo, from the home machine or the recording.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
