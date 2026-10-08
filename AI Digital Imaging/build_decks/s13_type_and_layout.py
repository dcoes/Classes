#!/usr/bin/env python3
"""Session 13. Type and layout by hand.  Run from the repo root.

Boundary: static type on a single image for key art, chapter headers and posters.
Type in motion belongs to Motion Graphics; typography as a discipline belongs to
Graphic Design. This session names hierarchy, placement and legibility and stops.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/13_Type_and_Layout_by_Hand.pptx"

SPEC = [
("title", "Type and Layout by Hand", "AI Digital Imaging  |  Session 13",
"""**Running time, about 50 minutes.** Spot it and recall (5). Why type is done by hand (5). Hierarchy, placement, legibility (15). Type on busy images (5). Choosing a font, and the three formats (7). A poster cliché, for discussion (4). Worked example and cold reversal (6). Consistency of type across a series (2). Options (1).

**Prep before class.** The layout template for Option A (title area, line, credit area, margins marked) for each of the three brief types. Check which Adobe Fonts are activated on the lab machines. One image of yours with badly placed type for the cold reversal.

Slot images: two or three film or game posters with very clear hierarchy (one title, one image, small credits), and a "floating heads" poster for the cliché discussion.

Boundary note: this is type on a single still image. Type in motion is the Motion Graphics course, and typography as a discipline belongs to Graphic Design. Name hierarchy, placement and legibility and stop there; if a student wants more, point them at those courses."""),

warmup("a generated poster or sign with lettering errors (yours)",
       "Lettering on purpose today, to set up the topic."),

("bullets", "Last time",
["A series is judged as one thing.",
 "Find the weakest image.",
 "Keep your rejects, with reasons."],
"""Recall. [Cold call.] What was the most common consistency break in the rough sets? What did you do about yours last night?

Milestone 3, the corrected set, is due next class. Today adds the last layer your images need before then: type."""),

("quote", "Today's idea", "Set the type yourself.",
"Every letter spelled right, in a font you chose.",
"""Today's rule is simple. In this course, type on your images is set by hand, with Photoshop's Type tool, in a font you chose, spelled correctly. Not generated.

Even as generators get better at lettering, and some of them are getting quite a lot better, generated text comes baked into the pixels. You can't edit it, can't fix a typo, can't change the font, can't move it two millimeters to the left. Real type stays sharp at any size and stays editable forever. And a client will always, always want to change the title."""),

("boxes", "Three jobs of type on an image",
["Hierarchy|what's read first", "Placement|where it sits", "Legibility|can it be read, at size"],
"""Three jobs, and we'll take them one at a time.

**Hierarchy**: what someone reads first, second, third. **Placement**: where the type sits on the image, and what it covers. **Legibility**: whether it can actually be read, at the size people will see it.

Graphic designers spend whole courses on this. We need enough of it to put a title on an image without ruining the image."""),

("image", "Hierarchy: one thing first", "type_hierarchy.png",
"Same photo, same words. Size, weight and position decide what's read first.",
"""Same photo, same words. On the left, four pieces of text at roughly similar sizes, in four styles, in the middle of the image. Your eye doesn't know where to start, and the type sits right on top of the subject.

On the right, one thing is clearly first: the title, big and heavy, in the dark sky at the top. The subtitle is second, smaller and lighter. The practical details are third, small, in a band at the bottom where they don't fight the image.

That's **hierarchy**: size, weight and contrast deciding the reading order. Three levels is plenty. More than three and it starts to look like the left side again."""),

("bimage", "Placement",
["Leave room when you generate.",
 "Quiet areas: sky, floor, shadow.",
 "Never across the face."],
"slot:two or three well-known posters with very clear hierarchy (title, image, small credits)",
"""[Show the posters. Ask: where's the type, and what is it sitting on?]

Placement. Type goes in the **quiet areas** of the image: sky, floor, a wall, a deep shadow. Places with little detail and even value, where letters can be read.

This is why the brief asked you to decide where the type goes before generating. If you generated with an empty sky at the top, you're fine. If your image is busy edge to edge, you'll be fighting it, which is the next slide. In the worst case, use Generative Expand or a fill to make quiet space, and that's a legitimate use of the tool.

And never across a face, or across the thing the image is about. The type and the subject should share the frame, not fight for the same spot."""),

("bullets", "Legibility",
["Contrast with what's behind it.",
 "Test it at final size.",
 "The thumbnail test."],
"""Legibility. Two tests.

**Contrast**: light type on dark, or dark type on light. Medium on medium disappears. Check in gray, as always.

**Size**: test at the size people will actually see it. For key art on a store page, that might be a thumbnail on a phone. Zoom out until the image is the size of your thumb on the screen. Can you still read the title? If not, it's too small, too thin, or on too busy a background.

Students almost always make titles too small and too thin. Go bigger than feels comfortable."""),

("image", "When the image is busy", "type_on_busy.png",
"Darken behind it, soften the area, or give it a band. Subtly.",
"""When you have to put type on a busy area, some of the fixes include:

**Darken behind it**: a soft gradient, on its own layer, under the type. **Soften the area**: a slight blur on a copy of that part of the image, masked. **A solid band**: a strip of color, which is very common on chapter headers and posters. And a subtle drop shadow, which I didn't show because it's so easy to overdo: if you can see the shadow as a shadow, it's too much.

All of these on their own named layers, so you can adjust them later. And do them subtly. The goal is that nobody notices the trick, they just notice they can read the title."""),

("bullets", "Spacing, in two moves",
 ["Tracking: open up all-caps titles.",
  "Kerning: fix the pairs that gap.",
  "Leading: lines close, not touching."],
"""A little spacing, just the two moves that make the biggest difference, and they're both in the Character panel.

**Tracking** is the overall spacing between letters. All-capital titles almost always look better with the tracking opened up a bit. Lowercase text usually wants to be left alone.

**Kerning** is the space between one specific pair of letters. In big titles, some pairs look gappy: an A next to a V, a T next to an o, an L next to a T. Put the cursor between them and tighten just that pair, holding Alt and using the arrow keys.

**Leading** is the space between lines. In a two-line title, bring the lines closer than the default, until they read as one block but the letters don't touch.

[Worked example in the demo: one title, before and after. Then have them fix one pair on their own title.]"""),

("bullets", "Proofread like it matters",
 ["Typos are the loudest error.",
  "Read it backwards, word by word.",
  "Have someone else read it."],
"""The most embarrassing error on a poster isn't a bad hand. It's a typo in the title, because everyone reads the title, and nobody can unsee it. Remember "a pasadise of sweet teats." That was the generator's fault. Yours would be yours.

Three habits. **Read it slowly**, then read it again **backwards**, word by word, which stops your brain from autocorrecting what it expects. Check **names and dates** against the brief, letter by letter. And **have someone else read it**, because you'll read what you meant to write.

Thirty seconds of checking, every time."""),

("bullets", "Alignment",
 ["Left, centered, or right: pick one.",
  "Align to something in the image.",
  "Keep it the same across the set."],
"""Alignment, last. Pick one, left, centered or right, and use it for all the type in an image. Mixing alignments is one of the quickest ways to make a layout look unplanned.

Better still, **align to something in the image**: the left edge of a building, the line of the horizon, the edge of a figure. Type that lines up with the picture looks like it was designed with the picture. Type that just floats in a corner looks added at the end, which, to be fair, it was.

And, as with everything in a series, the same choice on every image."""),

("bullets", "Choosing a font",
["Match the mood of the brief.",
 "Two families, at most.",
 "Adobe Fonts, in the lab."],
"""Choosing a font, quickly, without turning this into a typography course.

**Match the mood** of your brief. A heavy, wide sans for a loud game title. A classic serif for a book. Something with more character for a festival poster. Read your brief's "what should someone feel" line, and pick the font that agrees.

**Two families at most**: one for the title, one for everything else. Often one family is enough, in two weights.

And use **Adobe Fonts**, which are licensed for this, and already in the lab. Fonts from random free sites often have licenses that don't allow commercial use, which matters the moment someone pays you."""),

("checklist", "The three formats",
["Key art: title, logo area, vertical crop", "Chapter headers: same spot every time",
 "Posters: title, one line, small credits"],
"""The three brief types each have a typical layout.

**Key art**: a title or logo area, usually with room for a platform badge or rating, and a version that still works when cropped vertical for phones. **Chapter headers**: the chapter number and title in exactly the same position and size on every one. **Posters**: a title, one line of description, and small credits or details, consistent across the series.

The templates on Canvas have these areas marked. You can use them or design your own, which is the difference between tonight's two options."""),

("bimage", "A poster cliché",
["Floating heads.",
 "Orange and blue.",
 "Why does everything look like this?"],
"slot:a typical 'floating heads' film poster",
"""[About four minutes.] A discussion, and a bit of fun. Here's a type of poster you've seen a thousand times: the cast's heads floating in the sky, orange and blue color, title at the bottom.

[Ask: why does this look the way it does?] Usually the room gets there: contracts that specify how big each actor's face is, marketing departments, the fact that it works well enough as a thumbnail.

Here's the connection to this course. A generator trained on thousands of these posters will happily make you more of them, because that's the average poster. If you want something that doesn't look like everything else, that has to come from your brief and your layout. The average is always available, and nobody needs you to make it."""),

("boxes", "Worked example: a chapter header",
["Template|areas and margins", "Quiet area|check in gray", "Type|title, then number",
 "Support|band or gradient", "Thumbnail test|zoom way out"],
"""The worked example, which I'll do live.

Place the image in the **template** with its margins. Find the **quiet area** and check its value in gray. Set the **type**: the title first, at the largest size that works, then the chapter number, smaller. Add a **support** layer only if needed: a band or a soft gradient. Then the **thumbnail test**: zoom out until it's tiny. Can you still read it? Does the image still read?

Then save the type layers as a group you can reuse on every other image in the series."""),

("image", "Now you: what's wrong with this layout?", "slot:one of your images with badly placed type",
None,
"""Cold reversal. Here's an image with a layout that isn't working. In pairs: what's wrong with the hierarchy, the placement, and the legibility, and what would you change first? Two minutes.

[Take answers. Don't fix it on screen. Different first moves are fine if they can say why.]"""),

("bullets", "Type across a series",
["Same position, same size.",
 "Build it once, reuse it.",
 "Only the words change."],
"""Last thing. In a series, the type is part of what makes it a series.

Same position, same size, same fonts, same treatment on every image. The easiest way to guarantee that: build the type group once, perfectly, on your strongest image, then copy the whole group into the other files and change only the words. If you're comfortable with Smart Objects or artboards, use those, but copying a group works fine.

If your type moves around from image to image, the set stops looking like a set, even if the pictures are perfectly consistent."""),

vocab([("Hierarchy", "the order things are read in"),
       ("Quiet area", "low detail, even value: where type can sit"),
       ("Tracking", "the overall spacing between letters"),
       ("Margin", "the empty edge no type should cross"),
       ("Legibility", "can it be read, at the size it's seen"),
       ("Thumbnail test", "zoom out until it's tiny; still readable?")]),

("options",
["Add type to one image of your set", "from the provided layout template."],
["Design your own layout", "for one image of your set,", "with a note on the hierarchy."],
"""Tonight, due next class, along with Milestone 3, so keep this to about 45 minutes.

**Option A**: add type to one image from your set, using the layout template on Canvas for your brief type.

**Option B**: design your own layout for one image, and write two or three sentences on the hierarchy: what's read first, second, third, and why.

Milestone 3 next class: the corrected set, critiqued in small groups, with written notes from each reader."""),

("quote", "One line to take home", "Set the type yourself.",
"Biggest thing first, in a quiet place, readable at thumbnail size.",
"""Set the type yourself. [Demo: the chapter header, live.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
