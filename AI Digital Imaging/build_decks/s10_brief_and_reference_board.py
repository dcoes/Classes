#!/usr/bin/env python3
"""Session 10. Brief and reference board (Milestone 1 due).  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/10_Brief_and_Reference_Board.pptx"

SPEC = [
("title", "The Brief and the Reference Board", "AI Digital Imaging  |  Session 10",
"""**Running time, about 50 minutes.** Spot it and Milestone 1 check-in (6). The brief: purpose, audience, content, look, constraints (16). Weak and strong brief lines (4). The reference board: what goes on it and where references can come from (10). The swap-briefs exercise (8). Must and must-not (4). Options (2).

**Prep before class.** Collect Milestone 1 (brief and reference board, even rough). The brief template on Canvas. Your own one-page example brief and an example reference board built as a Photoshop artboard file, for the worked example. A short list of permitted reference sources (students' own photos, public domain collections, openly licensed images with the license noted).

Slot images: your example brief, your example board."""),

warmup("one image from a generated series where one image breaks the set"),

("bullets", "Milestone 1 is in",
["Brief and reference board.",
 "Rough is fine. Missing isn't.",
 "Today we make them better."],
"""Milestone 1 is due today: your brief and your reference board. [Check that everyone has submitted something.]

Rough is fine. Today's whole session is about improving both, and your options tonight are about tightening them. What matters for the milestone is that it exists, on time, and that the next stage visibly comes out of it.

If you didn't submit, talk to me at the break. Remember the arithmetic: a final without its milestones is capped at Average."""),

("quote", "Today's idea", "The brief is the first image.",
"Everything after it gets checked against it.",
"""Here's how I'd like you to think about the brief. It isn't paperwork that comes before the real work. It's **the first image**, made of words, and everything after it gets checked against it.

Every critique we've done has started from the brief. Every ranking. Every "is this the weakest image?" If the brief is vague, none of those questions have answers, and critique turns into taste, which is where we said we don't want to be."""),

("bimage", "What a real brief looks like",
["About a page.",
 "Specific enough to check.",
 "Written for someone else."],
"slot:your one-page example brief",
"""[Put your example brief up. Read a few lines aloud.]

Some things to notice about real briefs. They're short, about a page. They're **specific enough to check**: you can look at an image and say yes or no to each line. And they're **written for someone else**: an illustrator, a photographer, a team, or now a generator, none of whom can read your mind.

That last one is the test we'll use in the exercise later today. If somebody else can't picture your image from your brief, neither can the machine."""),

("boxes", "The five parts of the brief",
["Purpose|what and for whom", "Audience|who sees it, where", "Content|what's in each image",
 "Look|light, palette, medium", "Constraints|format, size, musts"],
"""The template on Canvas has five parts.

**Purpose**: what this is, and who it's for. **Audience**: who will see it, and where: on a phone, on a wall, on a store page. **Content**: what's in each image, one line per image. **Look**: the light, the palette, the medium, borrowing the vocabulary from session 2. **Constraints**: format, size, and the things that must or must not happen.

Let's take them one at a time, quickly."""),

("bullets", "Purpose and audience",
["What is it for?",
 "Where will it live?",
 "What should someone feel?"],
"""Purpose and audience. What is it for, where will it live, and what should someone feel when they see it?

That last question is one some of you will know from game design: what experience do you want the player, or here the viewer, to have? Not "make it cool," but "it should feel lonely," or "it should feel like the start of an adventure," or "it should make you a little uneasy."

That one sentence ends up deciding a lot of the other choices. A lonely image has a small figure and a lot of space. An adventure has a horizon and a path. Write it down first."""),

("bullets", "Content: one line per image",
["Image 1: who, where, doing what.",
 "What changes across the series.",
 "What never changes."],
"""Content. One line per image: who's in it, where, doing what. Keep it to a line.

Then two more lines that are about the **series** rather than any single image: what changes across the set (the location, the time of day, the action, the chapter's event) and what never changes (the character, the palette, the light quality, the format).

That second pair is what makes three images a series instead of three images. It's the consistency work from session 6, written down before you generate anything."""),

("bullets", "Look and constraints",
["Light, palette, medium: in words.",
 "Format and size: exact.",
 "Leave room for the type."],
"""Look and constraints.

**Look**: the five-part vocabulary, at the level of the whole series. "Late afternoon, low warm light from the left, long shadows, muted greens and ochres, painterly, a little grain."

**Constraints**: exact format and size. Key art might be 16:9 with a vertical crop for phones. Chapter headers might all be the same wide strip. Posters might be 2:3.

And one thing almost everyone forgets: **leave room for the type.** In session 13 you'll add a title or text to your images by hand, and it needs a quiet area to sit in: sky, floor, shadow. Decide where it goes now, and write it in the brief, so you generate with that space in mind rather than fighting it later."""),

("two", "Weak line, strong line",
["**Weak**", '"A cool fantasy vibe."', '"She looks heroic."'],
["**Strong**", '"Late sun, low left, long shadows, muted greens."', '"She\'s small in frame. The landscape is the threat."'],
"""One worked example of turning weak brief lines into strong ones.

"A cool fantasy vibe" can't be checked. Any image passes. "Late sun, low from the left, long shadows, muted greens" can be checked: you look at the image and it either does those things or it doesn't.

"She looks heroic" is also uncheckable, and it'll give you the most average heroic pose there is. "She's small in frame, the landscape is the threat" is a decision about composition that also tells you the story.

[Cold reversal: put a weak line from your own experience, or ask a volunteer for one from their brief, and have the room rewrite it. Don't give an answer.]"""),

("section", "The reference board", "",
"""Now the second half of Milestone 1."""),

("bullets", "Why a board",
["Shows what words can't carry.",
 "Decides the look before you generate.",
 "The thing you check against."],
"""Remember the describe-and-sketch exercise in session 2? Words are lossy. They lose placement, value pattern, the exact quality of a light.

A reference board carries what words can't. It decides the look before you generate anything, so you're not discovering your look by accident in the outputs. And it's the thing you check every image against, alongside the brief.

Art directors, production designers and concept artists make these at the start of almost every project. Some call it a mood board. I'd rather think of it as the brief's other half."""),

("bimage", "What goes on it",
["Light and time of day.",
 "Palette swatches.",
 "Character and place.",
 "Your model sheet, when you have one."],
"slot:your example reference board, built on a Photoshop artboard",
"""[Show your example board.]

Some of the things that belong on it: **light references**, photos or stills showing the kind of light you're after. **Palette swatches**, sampled colors, five to eight of them. **Character and place** references: costume, faces, architecture, landscape. And, once you've made it, **your model sheet** from session 6.

Notice what isn't on mine: a pile of other people's finished illustrations. That's on purpose, and it's the next slide."""),

("checklist", "Where references can come from",
["Your own photos (the best)", "Public domain collections", "Openly licensed, license noted",
 "Film stills, for light only, labeled", "Never: someone's art as generator input"],
"""Where references can come from, for this course.

**Your own photos** are the best reference there is, and nobody can argue about them. **Public domain** collections, which include an enormous amount of historical photography and painting. **Openly licensed** images, with the license noted. **Film stills**, for light and color only, labeled with the film.

And one firm rule. Looking at other artists' work for inspiration is fine, artists always have. But you don't **feed someone else's artwork into the generator** as a reference image. That's using their work as raw material without their say. Adobe's own terms require you to have the rights to anything you upload as a reference, too.

Label every reference with where it came from. Those labels become the "sources" part of your disclosure statement."""),

("boxes", "Building it in Photoshop",
["Artboard|one per board", "Sections|light, color, character, place", "Label|every image, REF_ and source",
 "Swatches|sample the palette"],
"""Building the board, quickly, and I'll show it in the demo.

One **artboard** in Photoshop, landscape, sized for a screen. **Sections** for light, color, character and place. Every image on its own layer, **labeled** REF_ with where it came from. And a row of **swatches** sampled from your references, which becomes the palette you check your images against.

It doesn't need to be beautiful. It needs to be useful to you at 1 a.m. when you're trying to remember what the light was supposed to be."""),

("bimage", "In the wild: a color script",
 ["A whole film's color, planned first.",
  "Small paintings, in order.",
  "A series, decided before it's made."],
 "slot:a published animated feature color script (Pixar's are widely reproduced in art-of books)",
"""[About four minutes.] Here's a tool from animation that's very close to what your reference board is doing, and some of you will recognize it.

Animation studios plan the color of an entire film before it's made, with a **color script**: a long strip of small, rough paintings, one per scene, in order. Pixar's are the famous ones, from the 1990s or so onward. You can see, at a glance, how the color and light change across the story: warm here, cold here, the darkest moment here, the release here.

[Ask: what does a color script let a director decide that a single beautiful painting doesn't?] The relationship between images. Which is exactly your problem with a series of three or four.

So, a suggestion, not a requirement: on your board, add a tiny color script. Three or four small rectangles, one per image, in the colors and light you're planning. Five minutes of work, and it'll keep your series together more than any prompt."""),

("bullets", "Choosing your format",
 ["Where will it be seen first?",
  "What has to repeat exactly?",
  "Where does the type go?"],
"""You've picked one of three formats: key art, chapter headers, or a poster series. Some of you are still deciding. Rather than tell you what each one should look like, three questions that will decide it for you.

**Where will it be seen first?** A store page thumbnail, a printed book, a wall. That decides the size, the shape, and how simple the composition has to be.

**What has to repeat exactly?** Chapter headers repeat a format almost rigidly. Posters repeat a style but can vary layout. Key art often has one hero image and supporting ones.

**Where does the type go?** If you can't answer that yet, you're not ready to generate.

[Have them answer the three questions for their own brief, in writing, two minutes.]"""),

("bullets", "Using the board while you work",
 ["Board open on a second screen.",
 "Sample the swatches, don't guess.",
 "Compare every keeper to it."],
"""How to actually use the board, once it exists, because a board that you make and then never look at again is just homework.

Keep it **open**, on a second screen or as a second document tab, while you generate and fix. When you paint corrections, **sample colors from the swatches** rather than guessing. And every time you decide to keep an image, put it **next to the board** for a few seconds. Does the light match the light references? Does the palette match the swatches?

If it doesn't, either the image goes in REJECTS, or, occasionally, you've found something better than your plan. That's allowed, but then you update the board and the brief, and write down why. The brief can change. It just can't change silently."""),

("section", "Swap briefs", "An exercise",
"""Now let's test your briefs."""),

("bullets", "Swap briefs",
["Trade briefs with a partner.",
 "Read theirs. Describe image 1 out loud.",
 "Did they get it? If not, the brief did that."],
"""[About eight minutes.] Swap briefs with a partner, without the reference board. Read your partner's brief, and then describe out loud what you think image 1 looks like: what's in it, where, what light, what feeling. Two minutes each.

The brief's author listens and doesn't correct. Then compare: how close was it?

[Then ask the room.] Where did the descriptions go wrong? Usually: the light, the composition, how big the figure is. Those are the lines in your brief that need to get more specific tonight.

This is exactly what the generator does with your brief, except your partner was trying to understand you and the generator isn't."""),

("two", "Must and must not",
["**Must**", "Her red scarf, every image.", "Light from the left.", "Room for a title, top third."],
["**Must not**", "No text in the generated image.", "No modern objects.", "Never the full face."],
"""Option B tonight adds a short list to your brief: five musts and five must-nots. Here are three of each from an example.

**Musts** are the things that make the series work: a feature that holds, a light direction, a space for type. **Must-nots** are the failures you can already predict: generated lettering, objects from the wrong period, a face shown when the brief wants mystery.

The list does two jobs. It makes your generating faster, because you reject anything that breaks it in a second. And it's what the rough set gets critiqued against in session 12. The rubric's first criterion literally says "including its must and must-not list.\""""),

vocab([("Brief", "purpose, audience, content, look, constraints"),
       ("Reference board", "the brief's other half, in pictures"),
       ("Artboard", "a Photoshop canvas inside the file, for boards"),
       ("Swatches", "the palette, sampled from references"),
       ("Must / must not", "the checkable rules for the series"),
       ("Permitted reference", "yours, public domain, or licensed, labeled")]),

("options",
["Tighten your brief", "using the provided template."],
["Add five \"must\" and five", "\"must not\" items to your brief."],
"""Tonight, due next class.

**Option A**: tighten your brief using the template on Canvas, all five parts, taking the notes from the swap exercise into account. Rewrite every line that your partner misread.

**Option B**: add the must and must-not list to your brief, five of each, each one checkable.

Either way, update your reference board if the brief changed. Next class is about control: how to get the generator to put things where you want them, which is where your rough set starts."""),

("quote", "One line to take home", "If someone else can't picture it from your brief,",
"the machine can't either.",
"""If someone else can't picture it from your brief, the machine can't either. [Demo: building the reference board artboard.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
