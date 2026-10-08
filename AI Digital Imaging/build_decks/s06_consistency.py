#!/usr/bin/env python3
"""Session 6. Consistency.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/06_Consistency.pptx"

SPEC = [
("title", "Consistency", "AI Digital Imaging  |  Session 6",
"""**Running time, about 50 minutes.** Spot it and recall (6). An old animation problem (8). Why generators drift (5). The five features (4). The tools for holding it: reference, structure and style (10). Your own model sheet (6). Places, and relighting instead of regenerating (6). Cold reversal (3). Project 1 reminder and options (2).

**Prep before class.** The provided character for Option A, as a key image plus a short list of five features to hold (face shape, hair, costume colors, one prop, proportions). Three generated images of one character with one consistency break each, for the cold reversal. Optional, if you have time: a short set of the character run through a pose or reference workflow at home, to show what holds and what doesn't.

Slot image: a classic studio character model sheet. Fleischer and Disney-era sheets from the 1930s are easy to find in animation histories; show it, don't redistribute it. Check the reference image features on the lab license before class, the names and placement change between versions."""),

warmup("one of your generated characters, two images side by side, with one feature that changed"),

("bullets", "Last time",
["Rerolling is a slot machine.",
 "Structure, light, surface, edges.",
 "The fix matches the image."],
"""Recall. [Cold call.] What's the order of fixes? [Structure, light, surface, edges and grain last.] Why not just regenerate the hand until it's right? [Slot machine, each pull can break something new.]

Today's Spot it was a little different: two images of what's supposed to be the same character. That's today's whole topic, and it's the problem the generator is worst at."""),

("bimage", "An old problem",
["Many artists, one character.",
 "The 1930s answer: the model sheet.",
 '"Off-model" is a studio word.'],
"slot:a 1930s-era studio character model sheet",
"""Before generators, animation studios had exactly this problem, at enormous scale. A feature film might have dozens of animators drawing the same character, thousands of times, and the character had to look like the same person in every frame.

The answer, from the 1930s or so, was the **model sheet**: a page showing the character from several angles, in several expressions, with notes about proportions. "Three heads tall." "The eyes never cross the center line." Everyone drew from the sheet.

And when someone's drawing drifted away from it, the character was "off-model." That's a real studio word, and some of you in animation have probably heard it. Keep it, because it's the best description I know of what a generator does."""),

("quote", "Today's idea", 'Generators draw everyone "off-model."',
"Every run is a new artist who never saw the sheet.",
"""Here's the mechanical picture. Every time you generate, it's as if a new artist walked into the studio, heard your description, and drew the character without ever seeing the model sheet or any previous drawing.

Each one does a reasonable job of matching the words. None of them matches each other. That's why your character's hair is a different length in every image, the jacket changes color, the scar moves to the other cheek, and she's a bit older in the third one."""),

("bullets", "Why it drifts",
["No memory between runs.",
 "A name is not a face.",
 "Words describe a type, not a person."],
"""Why, mechanically? Three reasons.

**No memory between runs.** Each generation starts from new noise, steered by your words. Nothing carries over unless you hand it over.

**A name is not a face.** Calling your character "Mara" means nothing to the system. It's just a word.

**Words describe a type, not a person.** "A tall woman with short red hair and a green jacket" describes thousands of people. The generator picks a different one each time, and every one of them matches your words.

So consistency has to come from something other than words. That's what today is about."""),

("checklist", "What has to hold",
["Face shape and features", "Hair and silhouette", "Costume and its colors",
 "Props and marks", "Proportions"],
"""For Option A tonight, and for your final project, you'll keep a short list of features that must hold across every image. Five is a good number. For a character, some of these include:

**Face shape and features**, the shape of the jaw, the nose, the eyes. **Hair and silhouette**, which is the overall shape of the character, readable from a distance. **Costume and its colors.** **Props and marks**: the sword, the scar, the badge. And **proportions**: how many heads tall, how long the arms.

Silhouette is on this list on purpose. If the silhouette changes, the audience notices before they notice anything else. It's the same readability standard from storyboarding."""),

("section", "The tools for holding it", "",
"""Now the tools that help, and where each one stops helping."""),

("bullets", "Reference images",
["Hand it the character.",
 "It matches the look, roughly.",
 "It still drifts in the details."],
"""The first tool is a **reference image**. Instead of describing the character, you hand the generator a picture of her, and ask for her in a new pose or scene.

Photoshop's Generative Fill can take a reference image now, and some of the partner models in the dropdown are noticeably better at keeping a character than others. [Check what's on the lab license this term and say which ones.]

It works much better than words. It does not work perfectly. Expect the overall look to hold, and the details to drift: the number of buttons, the exact pattern on the fabric, which side the part in her hair is on. Which is why the checklist exists."""),

("two", "Structure versus style",
["**Structure reference**", "Pose, layout, shapes.", '"Arrange it like this."'],
["**Style reference**", "Color, texture, rendering.", '"Make it look like this."'],
"""Two different kinds of reference, and people confuse them.

A **structure** reference says: arrange it like this. The pose, the layout, where the big shapes are. It doesn't care about color. A **style** reference says: make it look like this. The palette, the texture, the way it's rendered. It doesn't care about arrangement.

Firefly has offered both of these under those names for a while, and other tools have their own versions. The names and the menus move around between versions, so I'll show you where they are today in the demo rather than promise a menu path.

Keeping them separate in your head is the useful part. When something's wrong, ask: is it a structure problem or a style problem? Then you know which reference to change."""),

("bullets", "Where it breaks",
["Back views and turnarounds.",
 "Hands holding props.",
 "Small things: buttons, logos, scars."],
"""Where consistency tends to break, even with good references. Some of these include:

**Back views and unusual angles.** The reference usually shows the front, so the back is invented, differently each time. **Hands holding props**: the sword changes shape. **Small details**: buttons, logos, patterns, scars, jewelry, the number of stripes. And **age and build**, which drift slowly across a set, so each neighbor looks fine but the first and last don't match.

None of these are hard to fix by hand once you've seen them. All of them are easy to miss if you only look at one image at a time."""),

("section", "The hand keeps it consistent", "",
"""So the real answer to consistency, as of now, is the same as it was in the 1930s."""),

("boxes", "Your own model sheet",
["Choose the key|your best image", "List|five features", "Build a sheet|front, three-quarter, side",
 "Check|every image against it"],
"""Make a model sheet before you make a series.

**Choose the key**: your strongest image of the character, the one everything else has to match. **List** the five features. **Build a sheet**, a single Photoshop artboard with the character from a few angles, generated, fixed by hand, or drawn, and the feature list written on it. **Check** every new image against the sheet, feature by feature.

For your final project, that sheet is part of your reference board, and it's what you'll defend your series against in critique."""),

("bullets", "Checking across a set",
["Side by side, same size.",
 "Flip between them quickly.",
 "Squint for the silhouette."],
"""How to actually check a set, since looking at one image at a time is how drift hides.

Put them **side by side**, at the same size, on one canvas. Then **flip between them**: make them layers in one file and toggle visibility quickly, which is a trick from animation, flipping drawings to catch changes. And **squint**, so detail disappears and you only see silhouettes and big color shapes. If one silhouette is different, you'll see it immediately.

Go down your five features, one at a time, across all the images. Not one image at a time down all the features. That direction matters."""),

("bimage", "Places drift too",
["Same layout, three times of day.",
 "Lock the layout. Change the light.",
 "Check windows, doors, horizon."],
"slot:one place of yours at three times of day, same layout",
"""Places drift exactly like characters. Generate "the same village square" three times and you get three different villages.

Option B tonight is a place at three times of day, consistent in layout. The trap is to generate it three times with "morning," "noon" and "night" in the prompt. You'll get three villages.

The better approach: get **one** layout you like, lock it, and then **change only the light.** Same idea as the lighting sweep in session 2, but now the image itself is held still instead of the prompt. Check the things that give it away: windows, doors, the horizon, the shape of the roofline."""),

("boxes", "Relight, don't regenerate",
["One base image|fixed by hand", "Duplicate|three copies", "Adjust|curves, color, shadows",
 "Fill small|only the sky, the windows"],
"""The worked example for relighting.

**One base image**, checked and fixed. **Duplicate** it three times. On each copy, **adjust** the light with Curves, Color Balance and painted shadow layers: warm and long shadows for evening, cool and dark for night. Then, if you need it, **fill small**: generate only the sky, or only the lit windows at night, inside tight selections, so the layout can't move.

That's the general principle: generate the parts that are allowed to change, and protect the parts that aren't with your selection."""),

("image", "Now you: find the breaks", "slot:three generated images of one character, one consistency break in each",
None,
"""Cold reversal. Three images of the same character. Each one has one break. Use the five features. Two minutes, in pairs.

[Take answers, one image at a time. Don't confirm until they've argued it a bit.]

Notice how you found them: probably by comparing two at a time, and by checking silhouette and color first. That's the method."""),

("bullets", "Project 1, due next class",
["Three images, three briefs.",
 "CALLOUT layer, numbered.",
 "Every fix on a FIX_ layer.",
 "Dated .psd for each."],
"""Project 1 is due at the start of next class, and next class is critique, so bring it ready to show.

For each of the three images: a CALLOUT layer with every significant error numbered, fixes on their own named FIX_ layers, and the image doing what its brief asks. A dated, layered .psd for each, and a short list of the callouts.

If something's going wrong with it tonight, it's better to bring an honest unfinished version with a good process record than a finished-looking file with nothing in it. You know how the rubric works."""),

("bimage", "In the wild: a title sequence",
 ["A streaming series, 2023.",
  "Generated, shifting imagery.",
  "Artists were not happy."],
 "slot:frames from the generated opening titles of a 2023 superhero streaming series",
"""[About five minutes.] Here's a case where the inconsistency was, at least according to the studio, the point.

In 2023, a superhero series about shape-shifting aliens opened with a title sequence made with generators. Faces and figures morph and flicker from frame to frame, never quite the same person twice. The production said the shifting look fit a story about not knowing who anyone really is. A lot of artists and animators were angry anyway, partly about the look and partly about what it meant for the people who'd normally have made a title sequence.

[Show it. Then ask two questions.] First: is the drift a choice here, or a limitation they made a virtue of? Second: would it have worked for a story where you're supposed to trust the characters?

There's no tidy answer, and I don't think you need one. The useful point is that inconsistency reads as **unease.** If you want unease, it's a tool. If you don't, it's a mistake."""),

("bullets", "Consistency is a design decision",
 ["What must never change?",
  "What may change?",
  "Write both down before you start."],
"""Last idea before the cold reversal. Consistency isn't only a technical problem, it's a design decision you make up front.

For your final, you'll write a short **must and must-not** list in session 10. Today's version is simpler: what must never change across the set, and what is allowed to change? The character's face must never change. Her pose may. The village layout must never change. The time of day may.

Once that's written down, the generator stops being a source of surprises and becomes a source of variations inside rules you set. That's the rigging idea, honestly: you don't ask the animator to be careful, you lock the controls that shouldn't move."""),

vocab([("Model sheet", "one page that defines how a character looks"),
       ("Off-model", "a drawing that drifted from the sheet"),
       ("Key image", "the one everything else must match"),
       ("Structure reference", "arrange it like this"),
       ("Style reference", "make it look like this"),
       ("Relight", "change the light, keep the layout")]),

("options",
["The provided character", "in three poses.", "Keep the five listed features."],
["A place of your choosing", "at three times of day.", "Consistent in layout."],
"""Tonight, due next class, on top of Project 1, so keep it to about 45 minutes.

**Option A**: the provided character, three poses, with the five listed features holding in all three. Use references, fix by hand, and include your feature checklist.

**Option B**: a place of your choosing, three times of day, same layout. Relight rather than regenerate.

Same rubric."""),

("quote", "One line to take home", "Make a model sheet before you make a series.",
"Then check every image against it.",
"""Make a model sheet before you make a series. [Demo: one character, three poses, and the checking method.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
