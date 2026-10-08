#!/usr/bin/env python3
"""Session 3. Generative Fill and Expand.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/03_Generative_Fill_and_Expand.pptx"

SPEC = [
("title", "Generative Fill and Expand", "AI Digital Imaging  |  Session 3",
"""**Running time, about 50 minutes.** Spot it and recall (6). The selection is the instruction (10). Remove, replace, extend (14). How generated layers behave, and naming (8). Worked example and cold reversal (6). When is removing something a lie (4). Options (2).

**Prep before class.** The three provided photos for Option A (one with something to remove, one with something to replace, one to extend), posted on Canvas. One photo of your own with an object removed by Fill where a tell is still visible (a leftover shadow is ideal), for the cold reversal. Check credits and sign-in on the lab machines.

Images for the slots: a before and after removal, and one of the "expanded famous painting" images that went around in 2022 or so (August Kamp's outpainted Girl with a Pearl Earring is the well-known one; the original painting is public domain, the expanded version is hers, so show it in class rather than redistributing it)."""),

warmup("a generated image with a problem the room hasn't seen yet"),

("bullets", "Last time",
["Subject, composition, lens, light, style.",
 "One variable at a time.",
 "Words can't carry \"where.\""],
"""Recall, thirty seconds. [Cold call.] What are the five parts? And what did you find when you only changed the light?

[Take one or two answers from people who did Option A. Usually: changing the light also changed the color of everything, and sometimes the composition moved, which was the seed.]

And from Option B: what got through from the film still, and what didn't? [Almost always: placement and value pattern got lost.]

Good, because today's tools are the answer to the "where" problem, at least partly. Today the selection carries the "where.\""""),

("bullets", "Two tools, one idea",
["**Fill** – inside a selection.",
 "**Expand** – outside the frame.",
 "In both, the selection is the instruction."],
"""Two tools today, and they're really one tool.

**Generative Fill** works inside a selection. You make a selection on an image, click Generative Fill in the contextual bar, type something or nothing, and you get three variations on a new layer.

**Generative Expand** works outside the frame. You use the Crop tool to drag the canvas bigger than the image, and it fills the new area.

In both cases the most important input isn't the words. It's **the selection**: where it is, how big it is, and what it includes. The words matter less than people expect. The shape you draw matters more."""),

("section", "The selection is the instruction", "",
"""So let's look at selections first."""),

("image", "How much you hand over", "selection_panels.png",
"A tight selection fills a gap. A loose one invites invention. Everything is a new picture.",
"""Three selections on the same photo.

On the left, a **tight** selection around one small area. The generator has a lot of real image around it to match, and only a small hole to fill, so it behaves: it continues the textures and the light that are already there.

In the middle, a **loose** selection. Now it has room, and it'll use the room. It invents. Things appear that weren't in the photo, sometimes useful, sometimes strange.

On the right, select everything and you haven't asked for an edit at all, you've asked for a new picture that happens to be shaped like your canvas.

So the size of the selection is really a dial for how much of the decision you're keeping and how much you're handing over."""),

("bullets", "What the selection tells it",
["Where to work.",
 "How much to invent.",
 "What to match at the edges."],
"""Three things the selection tells it. Where to work, which is obvious. How much to invent, which we just saw. And what to match, because the generator looks at the pixels just outside your selection to decide what goes inside.

That last one is why a selection that hugs an object too tightly gives you a bad result. If you select a person and their outline exactly, the generator sees the edge of the person and tries to continue it, and you get a ghost of them. **Select a little past the object**, into the background, so it can see what's behind.

And it's why feathering matters. A soft-edged selection blends; a hard edge leaves a seam."""),

("boxes", "Three jobs",
["Remove|leave the prompt empty", "Replace|describe only the new thing",
 "Extend|grow the canvas"],
"""Three jobs, and almost everything you'll do with these tools is one of them.

**Remove**: get something out of the picture. **Replace**: swap something for something else. **Extend**: make the picture bigger than it was.

Each one has its own habits, and I'm going to go through them quickly, because Option A tonight is one of each."""),

("bimage", "Remove",
["Leave the prompt empty.",
 "Select a little past the object.",
 "Check the shadow and the reflection."],
"slot:a photo before and after Generative Fill removed an object",
"""Remove. Select the thing plus a margin around it, and **leave the prompt empty.** An empty prompt tells it to fill with whatever belongs there, which is what you want. (There's also a dedicated Remove tool, a brush, that's often better for small things like wires or blemishes.)

Then check two things that it very often forgets: **the shadow** and **the reflection.** You remove a person from a beach, and their shadow is still lying on the sand with nobody attached to it. You remove a car, and it's still reflected in the shop window.

That leftover shadow is one of the most common tells in the world, and it's been a tell since long before generators. Retouchers have been missing shadows since the darkroom."""),

("bullets", "Replace",
["Select the shape of the new thing.",
 "Describe only the new thing.",
 "Not the whole scene."],
"""Replace. Two habits.

First, **the selection is a silhouette.** If you want a tall lamp, draw a tall thin selection. If you want a cat curled up, draw a round low one. The generator tends to fill the shape you give it, so you're drawing the silhouette of the new object with your lasso. (Silhouette again, the same idea that runs through storyboarding and painting.)

Second, describe **only the new thing.** Not "a living room with a red armchair in the corner." Just "a red leather armchair." It can already see the living room. If you describe the whole scene inside a small selection, it tries to fit the whole scene in there, and you get a tiny living room inside your living room."""),

("bimage", "Extend",
["Crop tool, past the edge.",
 "Everything outside gets invented.",
 "The further out, the weaker it gets."],
"expand_diagram.png",
"""Extend. Pick the Crop tool, drag the edges out past the image, and Generative Expand fills the new area. You can type something or leave it empty.

Look at the diagram. Everything grey is invented. The parts right next to the original photo are strong, because there's real image to continue. The further out you go, the less there is to go on, and the more it starts to make things up: repeated patterns, objects that don't quite make sense, perspective that wanders off.

Two habits: extend in **smaller steps**, checking each one, rather than one huge jump. And extend **away from the subject**, into sky, floor and background, where invention is less likely to be noticed."""),

("bimage", "Expanding changes what it means",
["What's outside the frame matters.",
 "Most extensions add wallpaper.",
 "A good one adds a fact."],
"slot:an outpainted famous painting from 2022 or so (e.g. the expanded Girl with a Pearl Earring)",
"""Here's something to look at, and then argue about. Back in 2022 or so, when this first became possible, people expanded famous paintings to show "what was outside the frame." This one went around everywhere.

[Show it. Give them thirty seconds.] Does the extension add anything to the painting? What does it tell you that you didn't know?

[Let them answer.] Usually, the honest answer is: not much. It's a nice room. It's wallpaper. The original frame was a decision, and the extension mostly dilutes it.

A good extension adds **a fact**: something in the new space that changes what the image says. Who is she looking at? What's on the table? That's the difference between expanding a canvas and making a decision about it, and it's what Option B asks for: when you expand your photo, note each choice you made, and why."""),

("section", "How generated layers behave", "",
"""Now some practical file behavior, because it affects your process record."""),

("bullets", "What you get back",
["A new layer, with a mask.",
 "Three variations each time.",
 "Regenerate, or pick in Properties."],
"""When Fill or Expand runs, it doesn't touch your original pixels. It makes a new **generative layer** with a mask in the shape of your selection. The original stays underneath. That's good, it means everything is reversible.

Each run gives you three variations, and you can flip between them in the Properties panel, or generate more. Pick one, and the others are still there until you delete them.

One thing to watch: the generated area can be lower resolution or softer than the photo around it, especially on big images or big selections. It can look fine zoomed out and mushy at 100%. Zoom in before you accept it. We'll fix that properly when we get to grain and sharpness in session 8."""),

("checklist", "Naming, for this course",
["GEN_ for anything generated", "FIX_ for a hand correction",
 "REF_ for reference you brought in", "CALLOUT for error markup",
 "Date in the file name", "Never \"Layer 12 copy 3\""],
"""Here's the naming standard for the rest of the course, and it's worth photographing.

**GEN_** at the start of anything generated: GEN_sky_v2. **FIX_** for any hand correction: FIX_shadow_left. **REF_** for any reference or photo you brought in. **CALLOUT** for the layer where you mark up errors. And the date in the file name.

This sounds fussy and it takes about five seconds per layer. It's also the process record: when I open your file I can see at a glance what was generated and what you made, which is exactly what the rubric asks, and exactly what a studio would ask too. Nobody should have to guess."""),

("bullets", "Getting more control",
["Smaller selections.",
 "Several small passes.",
 "Paint rough first, then fill."],
"""Three ways to get more control, from easiest to most useful.

Use **smaller selections**, so it has less room to invent. Do **several small passes** instead of one big one, accepting or rejecting each step.

And the most useful: **paint something rough first.** Block in the shape and color of what you want with a brush, badly is fine, then select over it and fill. The generator looks at what's inside the selection as well as around it, so your rough paint steers it more than words do.

This is the first appearance of an idea we'll keep coming back to: the more of the decision you supply, the less of it gets made for you."""),

("boxes", "Worked example: one removal",
["Select|lasso, past the edge", "Prompt|leave it empty", "Pick|one of three, say why",
 "Check|shadow, edge, grain", "Name|GEN_remove_sign"],
"""One worked example, which I'll do live in the demo, but here's the order.

**Select** the object with the lasso, including a margin of background. **Prompt**: nothing. Generate. **Pick** one of the three variations, and say out loud why that one: "the brick lines continue in this one," not "it looks better." **Check** the three tells: is there a shadow or reflection left behind, is there a seam at the edge, does the patch match the grain of the photo. **Name** the layer.

Five steps, about two minutes. The thinking is in the pick and the check."""),

("image", "Now you: what was the selection?", "slot:a photo of yours where an object was removed with Fill, one tell left visible",
None,
"""Cold reversal. Something was removed from this photo with Generative Fill. I'm not going to tell you what.

Three questions, in pairs, two minutes. What was there? Roughly what did the selection look like? And what gives it away?

[Take answers. Don't confirm until several pairs have answered, and then only confirm what was removed, not the whole list of tells. Let them argue about the rest.]

If you found it from a shadow, or a pattern that stops at an invisible line, or an area that's smoother than the rest, you've just done session 4 a day early."""),

("bullets", "When is removing something a lie?",
["A news photo?",
 "An ad?",
 "Concept art?"],
"""Short discussion, four minutes or so. When is removing something from a photo fine, and when is it a lie?

[Let them work it out. Usually they get there: it depends on what the picture claims to be.]

News agencies have had firm rules on this for a long time: in a news photo you don't add or remove anything, because the photo is a claim about what happened. An ad is understood by most people to be constructed, though even there, removing something about the product itself can get a company in trouble. Concept art makes no claim to be true at all.

So it isn't the tool that makes it a lie. It's **what the image says it is.** Keep that, because it's the whole basis of disclosure in week three.

[Into the demo.]"""),

("bimage", "In the wild: a family photo",
 ["A royal family photo, 2024.",
  "Agencies pulled it within hours.",
  "Nothing generated. Still a problem."],
 "slot:the 2024 Princess of Wales Mother's Day photo, with the agency notice",
"""[About five minutes.] A real case, and a useful one exactly because no generator was involved.

In March of 2024, the Princess of Wales released a family photo for Mother's Day. Within hours, several of the big news agencies withdrew it and told their clients not to use it, a "kill notice," because people had spotted signs of editing: a sleeve that didn't line up, a zipper, bits of background that didn't continue. She later said she had been experimenting with editing, and apologized for the confusion.

[Ask: why did the agencies care so much about a sleeve?] Because a news agency's whole value is that its photos are what happened. One edited photo, even a harmless one, makes people question every other one.

Notice the tells, too. They're the same ones we're learning for generated images: edges that don't line up, patterns that stop at an invisible line. A careless edit and a careless fill leave the same fingerprints."""),

vocab([("Generative Fill", "generates inside a selection"),
       ("Generative Expand", "generates past the canvas edge"),
       ("Generative layer", "its own layer, with a mask, three variations"),
       ("Feather", "a soft selection edge"),
       ("Aspect ratio", "the shape of the frame, like 16:9"),
       ("GEN_ / FIX_ / REF_", "the naming standard for every file")]),

("options",
["Three provided photos.", "Remove, replace, extend.", "One each, layers named."],
["Expand your own photo", "to a new aspect ratio.", "Note each choice you made."],
"""Tonight, due at the start of next class.

**Option A**: three photos on Canvas, three jobs. Remove something from the first, replace something in the second, extend the third. Layers named to the standard: GEN_, FIX_ if you touched it up, and so on.

**Option B**: one of your own photos, expanded to a new aspect ratio, for example a horizontal photo made vertical for a phone screen. Write down each choice you made: what you let it invent, what you rejected, what the new space adds to the image (or doesn't).

Same rubric, either way."""),

("quote", "One line to take home", "The selection is the instruction.",
"The words matter less than the shape you draw.",
"""The selection is the instruction. The words matter less than the shape you draw. [Demo.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
