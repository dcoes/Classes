#!/usr/bin/env python3
"""Session 12. Rough set critique (Milestone 2 due).  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/12_Rough_Set_Critique.pptx"

SPEC = [
("title", "Rough Set Critique", "AI Digital Imaging  |  Session 12",
"""**Running time.** A critique day, so the lecture is shorter, about 30 minutes, and the rest is critique. Spot it (3). Milestone 2 check-in and the Option B outputs handed back (4). Critiquing a series rather than an image (10). The weakest image (5). Rejections as evidence (4). How today runs (4). Then critique, with a room-wide look partway through.

**Prep before class.** Collect Milestone 2 (the rough set). Hand back the outputs from Option B sketches run on your machine. One rough set of your own, three or four images for a brief, with one image clearly weaker and one consistency break, for the practice round. Note sheets with an added column for the must and must-not list."""),

warmup("two images from one generated series, with a consistency break between them",
       "Short today, two minutes."),

("bullets", "Milestone 2 is in",
["All three or four images, rough.",
 "Option B outputs: back to you now.",
 "Today: does it read as a series?"],
"""Milestone 2: your rough set, all images, unfinished. [Check submissions.]

For those who did Option B last night, here are the outputs from your sketches. [Hand them back.] Take one minute to look at them. Notice which parts of your sketch held and which parts the generator reinterpreted. That's useful information about your drawing, too.

Today's critique is different from Project 1 in one important way. We're not just asking whether each image works. We're asking whether the images work **together.\""""),

("quote", "Today's idea", "A series is judged as one thing.",
"One image that breaks the set breaks the set.",
"""Here's the idea for today. A series is judged as one thing.

Someone looking at your three posters, or your book's chapter headers, or a store page with your key art, sees them together. If one of them is from a different world, a different light, a different version of the character, the whole set reads as unfinished, even if each image is good on its own.

That's harsh, and it's also how it works in practice. An art director will throw out a beautiful image because it doesn't match the other three."""),

("boxes", "Critiquing a series",
["Brief|does the set answer it?", "Musts|held in every image?", "Consistency|character, place, light",
 "Each image|the usual checks"],
"""So the critique has a different order today.

**The brief** first: does the set, as a whole, answer it? **The musts and must-nots**: go down your list, image by image. Every must in every image, no must-not anywhere. **Consistency**: character, place and light across the set, using the side-by-side and flipping methods from session 6. And only then **each image** on its own, with the checklist.

Most of you will want to start with the last one, because it's familiar. Resist that. If the set doesn't hold together, polishing one image is time spent in the wrong place."""),

("bullets", "Reading a set, practically",
["All images, same size, side by side.",
 "Squint: silhouettes and color.",
 "Flip through them quickly."],
"""How to actually look at a set, as a reader in your group.

Ask the presenter to show all the images **side by side, the same size**, on one screen. **Squint**, so you see the silhouettes and the big color shapes. If one has a different palette or a different light, it'll jump out. Then **flip through** them one at a time, quickly, which catches a character whose face or hair changed.

Then, and only then, look closely."""),

("bullets", "The weakest image",
["Every set has one.",
 "Name it, and say why.",
 "Replace it, or fix the break."],
"""Every set has a weakest image. Yours does, mine does. A useful note in a series critique is: "this one is the weakest, and here's why."

It might be weakest because it misses the brief, because it breaks consistency, because the composition is muddier than the others, or because it's simply the one you liked least and kept anyway.

That's tonight's Option A: replace the weakest image in your set and explain why it was the weakest. Option B is the other common fix: correct the most visible consistency break. Either one improves the whole set more than polishing your favorite."""),

("bullets", "Rejections are evidence",
["Keep what you threw away.",
 "Note why, in a line.",
 "It shows your judgment."],
"""A reminder about rejected images, since you'll make more of them this week than any other.

Keep them. Put them in a folder or a hidden layer group called REJECTS, and add a line in your log saying why each one was rejected: "breaks the must on the scarf," "light from the right," "pose too static for chapter 3."

The final asks for rejected selections because they show your judgment better than the keeps do. Anybody can show a good image. Showing the four you didn't use, and why, shows that you know the difference."""),

("image", "Practice round: my set", "slot:your own rough set, three or four images side by side, with its brief and must/must-not list",
"Brief, then musts, then consistency, then each image.",
"""[About eight minutes.] As before, you critique me first. Here's a rough set of mine and its brief, with the must and must-not list. [Read them aloud.]

In order: does the set answer the brief? Go down the musts. Consistency across the set. Then individual images. And then, which is the weakest one, and why?

[Take notes in the columns on the board. Model taking notes without defending. If the room goes straight to individual errors, redirect them to the order.]

Thank you. Now you know what's coming for you."""),

("checklist", "How today runs",
["Groups of three or four", "Set shown side by side first", "Brief and musts read aloud",
 "Notes in the format, written down", "Each reader names the weakest image", "I rotate between groups"],
"""Same structure as Project 1 critique, with two additions.

Groups of three or four, about six minutes per person. Show the set **side by side first**, then read your brief and must and must-not list aloud. Notes in the format: brief says, image does, one change. Written down. And each reader names **which image is weakest and why**, even if it's uncomfortable.

I'll rotate. Halfway through we stop and look across the room."""),

("bullets", "Across the room",
["What held across most sets?",
 "What broke most often?",
 "What to fix first this week."],
"""[Use at the halfway point, filled in live from what you saw.]

What held across most sets? [Often the palette.] What broke most often? [Usually the character's face or costume details, or the light direction in one image.] What should everyone fix first this week? [Usually the consistency break, before any polish.]

[Name patterns, not people.]"""),

vocab([("Series", "images judged as one thing"),
       ("Weakest image", "the one that most weakens the set"),
       ("Consistency break", "a feature that changed between images"),
       ("REJECTS", "kept, with a reason, as evidence")]),

("options",
["Replace the weakest image", "in your set.", "Explain why it was weakest."],
["Correct the most visible", "consistency break", "across the set."],
"""Tonight, due next class.

**Option A**: replace the weakest image in your set, and write two or three sentences on why it was the weakest. Keep the old one in REJECTS.

**Option B**: correct the most visible consistency break across the set, by hand, on named FIX_ layers.

Milestone 3, the corrected set, is due at session 14. Next class is type and layout, which you'll be adding to your images."""),

("quote", "One line to take home", "Fix the set before you polish an image.",
"An art director sees all of them at once.",
"""Fix the set before you polish an image. [Into the groups.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
