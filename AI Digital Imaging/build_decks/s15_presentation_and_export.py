#!/usr/bin/env python3
"""Session 15. Presentation and export.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/15_Presentation_and_Export.pptx"

SPEC = [
("title", "Presentation and Export", "AI Digital Imaging  |  Session 15",
"""**Running time, about 50 minutes.** Spot it and recall (5). Why process gets shown now (6). The presentation sheet, part by part (14). Export: screen and print, resolution, upscaling honestly, color (14). Where this work gets posted, and how it's received (5). The export checklist and options (6).

**Prep before class.** The presentation sheet template on Canvas, with areas for final images, process strip, prompt log excerpt and disclosure. An example sheet of yours. The final export spec (sizes and formats) for each of the three brief types. Know whether the lab has a printer or print service students can use, and its specs.

Slot image: an example process breakdown from a professional portfolio (concept art and VFX artists post these routinely), shown in class."""),

warmup("one image with a subtle remaining problem from a corrected set (with permission, or your own)"),

("bullets", "Last time",
["Write notes down.",
 "Do it, adapt it, or say why not.",
 "Finishing, not polishing."],
"""Recall. [Cold call.] What are the three honest responses to a note? [Do it, adapt it, decline with a reason.] What's the difference between finishing and polishing?

Today is the last session with new material. It's about how the work leaves your hands: how you present it and how you export it. Both of these are the difference between good work and good work that someone can actually use."""),

("quote", "Today's idea", "Show how it was made.",
"Before anyone has to ask.",
"""Here's the idea for today. With generated images everywhere, the first question people ask about any image is, more and more, "how was this made?" Clients ask it. Art directors ask it. Hiring managers, from what I hear from people who hire, ask it.

You can wait for the question and answer it defensively, or you can answer it **before anyone asks**, on the same page as the work. That's what the presentation sheet is for."""),

("bimage", "Professionals already do this",
["Concept and VFX artists post breakdowns.",
 "Before, during, after.",
 "The process is part of the portfolio."],
"slot:a professional process breakdown (concept art or VFX), shown in class",
"""[Show the breakdown.] This isn't something invented for this course. Concept artists, matte painters and visual effects artists have been posting breakdowns for years: the plate, the elements, the paint-over, the final. In VFX, a "breakdown reel" showing how shots were built is standard.

Why do they do it? Because the final image alone doesn't show what they did. A breakdown shows the decisions, the skill, and how much of the image is theirs.

That's exactly your situation, with one more reason added: your breakdown is also your disclosure."""),

("image", "The presentation sheet", "presentation_sheet.png",
"Final images, a process strip, a log excerpt, the disclosure. One page.",
"""Here's the layout, with placeholder images so you can see the structure.

At the top, the **final images**, large, side by side, which is how the set should be judged. In the middle, a **process strip** for one image: brief, generated, callouts, fixed, final with type. On the right, a short **prompt log excerpt**. At the bottom, the **disclosure**.

One page, landscape. It's what you present at the final critique, and it's what I'd suggest putting in your portfolio, too."""),

("bullets", "The process strip",
["Four or five stages, one image.",
 "Same size, left to right, labeled.",
 "Pick the image with the most change."],
"""The process strip. Four or five stages of one image, at the same size, left to right, each labeled.

Pick the image where the **most changed** between the generation and the final. If your focal image was mostly fine as generated and another one needed a lot of hand work, show the other one. The point is to show what you did.

The callout stage, with the red circles, is the one people find most interesting. It shows your eye, which is the thing you've been training all month."""),

("bullets", "The log excerpt",
["Two or three key prompts.",
 "At least one rejection, with its reason.",
 "Not the whole log."],
"""The log excerpt. Not the whole log, which goes in your submission separately. Two or three prompts that mattered, and at least one **rejection with its reason**.

"v4: added fog. Rejected: hides the scarf, which is a must." That one line says more about your judgment than any of the images do."""),

("bullets", "The disclosure, on the sheet",
["Tools, generated, made, sources.",
 "Plain and short.",
 "Same statement as your submission."],
"""The disclosure goes on the sheet, in the four parts from session 9: tools, what was generated, what you made, sources. Plain and short, no apology, no boasting.

It's the same statement as in your submission. Putting it on the sheet means it travels with the work: when someone sees the sheet, they see the disclosure, without having to find it."""),

("bullets", "Laying out the sheet",
["Final images largest.",
 "One grid, generous margins.",
 "Your type rules from last session."],
"""Laying out the sheet is a small version of last session.

The **final images are the largest thing** on the page. Everything else is supporting. Use one simple grid and generous margins. Use the hierarchy rules from last session: one thing read first (the series), then the process, then the text. One font family is enough.

Option A tonight uses the template. Option B is your own layout. Either way, check it at thumbnail size: someone scrolling past should see "a series of three images" before they see anything else."""),

("section", "Export", "Screen and print are different",
"""Now export, which is boring and which goes wrong all the time, usually at the last minute."""),

("two", "Screen and print",
["**Screen**", "Pixels: say, 1920 or 3840 wide.", "sRGB color.", "JPEG or PNG."],
["**Print**", "300 pixels per inch, at size.", "Proof for CMYK.", "PDF or TIFF."],
"""Screen and print want different files.

For **screen**, only pixel dimensions matter: 1920 or 3840 wide for most uses, or whatever the platform asks. The "dpi" or "ppi" number in the file doesn't matter for screens at all, which surprises people. Color in **sRGB**. Save as JPEG (high quality) for images, PNG if there's sharp type and you want it crisp.

For **print**, you need about **300 pixels per inch at the printed size**. An 11 by 17 inch poster needs roughly 3300 by 5100 pixels. Printers usually work in **CMYK**, which can't show some bright screen colors, so soft proof it in Photoshop (View, Proof Setup) to see what will change. Save as PDF or TIFF, as the printer asks."""),

("bullets", "Resolution, honestly",
["Generated images are often small.",
 "Upscaling invents detail.",
 "Check it like any other generation."],
"""A problem specific to this course. Generated images often come out smaller than a print needs, and generated fills can be softer than the image around them.

Photoshop has upscaling options: Image Size with "Preserve Details," and a generative upscale feature. These work, sometimes quite well. But a generative upscale **invents detail** to fill the new pixels. It's another generation, and it can add the same errors: odd textures, changed faces, new lettering-like marks.

So: upscale, then run the checklist again at 100%, especially on faces and hands. Name the upscaled layer or file so the record shows it, and mention it in the disclosure."""),

("bullets", "Color, briefly",
["Work in sRGB unless told otherwise.",
 "Embed the profile on export.",
 "Check on a second screen, or your phone."],
"""Color, briefly. Work in sRGB unless a printer or client tells you otherwise. **Embed the color profile** when you export (there's a checkbox), so other software shows your colors correctly.

And check your exported file on a second screen, ideally your phone, because that's where most people will see it. Colors and darks that looked fine on the lab monitor can look quite different on a phone. Shadows often go muddy. Better to find out tonight than at the critique."""),

("bimage", "Where this work gets posted",
["Portfolio sites have opinions.",
 "Some label or restrict generated work.",
 "Your disclosure decides how it's received."],
"slot:the late 2022 'No AI' protest images on a major art portfolio site",
"""[About five minutes.] Where will you post this, and how will people react?

In late 2022, artists on one of the biggest portfolio sites for concept artists flooded the front page with a "No AI" protest image, after generated images started appearing there. The site added ways for artists to label their work and opt out. Other sites and communities have their own rules, and they change.

[Ask: would you post your final there? How would you label it?]

My suggestion: post it where the audience you want is, label it accurately, and lead with the process. Work that hides how it was made and gets found out tends to get a much worse reception than work that says so up front. The presentation sheet is the version that says so up front."""),

("checklist", "Before you export",
["Layered .psd saved, dated", "Flattened copies, separate folder", "Right pixel size for the use",
 "sRGB, profile embedded", "Checked at 100% after upscaling", "Checked on a phone",
 "Files named: name_project_image_date", "Disclosure included"],
"""Photograph this one. Eight checks before you hand anything in, for this course or for a client.

Keep the **layered file**, dated: never export over it. **Flattened copies** go in their own folder. **Right size** for the use. **sRGB, profile embedded.** Checked at **100%** after any upscale. Checked on a **phone.** **Named** clearly, with your name, the project, the image number, and the date. And the **disclosure** included.

The file name thing sounds petty. Anybody who's received thirty files called "final_final2.jpg" will tell you it isn't."""),

("bullets", "Three minutes about your work",
 ["The brief, in one breath.",
  "Point at things.",
  "Practice it once, out loud, tonight."],
"""Next class you'll present for about three minutes. Some preparation, because three minutes goes quickly and goes badly if it's improvised.

Say **the brief in one breath**: what it's for and how it should feel. Then let the images sit. Then **point at things** while you talk about the hardest decision, on the sheet or in the file: "this shadow," "this rejected version," "this must." Pointing keeps you specific and keeps the room looking at the work instead of at you.

And **practice it once, out loud**, tonight, with a timer. Not memorized, just once. Almost everyone who does this is noticeably better than almost everyone who doesn't."""),

("bullets", "Where this piece goes next",
 ["One strong series beats ten single images.",
  "Put the breakdown next to it.",
  "Label it honestly."],
"""What to do with the final after this course, if it turns out well.

In my experience, a small number of really strong pieces, with their process visible, do more for a portfolio than a large number of single images. That's even more true now, when single generated images are everywhere and cost nothing. A **series** that holds together, with a **breakdown** showing the brief, the rejections and the hand work, shows exactly the judgment that's hard to find.

Label it honestly. Put the disclosure with it. The people worth working for will read it as a sign that you know what you're doing, rather than as a confession."""),

("bullets", "Handing files to someone else",
 ["The layered file, named and dated.",
  "A note on the fonts.",
  "The disclosure, in writing."],
"""One more professional habit: handing your files to someone else, which happens with every client and every studio job.

The **layered file**, named and dated, with the layer naming standard we've used all month. The person opening it should be able to understand it without calling you. **A note on the fonts** you used, because Photoshop doesn't bundle them, and a missing font silently changes your title on someone else's computer. And the **disclosure**, in writing, in the delivery email or a text file next to the images.

That's the whole hand-off. It's also, more or less, what your final submission is."""),

vocab([("Process strip", "one image, stage by stage, same size"),
       ("Breakdown", "the industry's name for a process strip"),
       ("Pixels per inch", "matters for print, not for screens"),
       ("sRGB", "the color space for screens"),
       ("CMYK", "print color; proof before you print"),
       ("Generative upscale", "adds pixels by inventing detail; check it")]),

("options",
["Build the presentation sheet", "from the provided template."],
["Build your own", "presentation sheet layout."],
"""Tonight, due next class, together with the final itself.

**Option A**: build your presentation sheet from the template on Canvas.

**Option B**: design your own presentation sheet layout, with the same four parts.

Next class is the final critique. Bring the final files, the sheet, and everything on the final checklist: brief, reference board, prompt log, rejects, layered corrections, disclosure. Each of you will present for about three minutes."""),

("quote", "One line to take home", "Show how it was made.",
"Before anyone has to ask.",
"""Show how it was made, before anyone has to ask. [Demo: building the sheet and the export, live.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
