#!/usr/bin/env python3
"""Session 7. Project 1 critique.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/07_Project_1_Critique.pptx"

SPEC = [
("title", "Project 1 Critique", "AI Digital Imaging  |  Session 7",
"""**Running time.** This is a critique day, so the lecture is deliberately shorter, about 30 minutes, and the rest of the morning is critique. Spot it (4). How critique works here (12). A practice round on an image of mine (8). How today runs (4). Then critique in small groups, with the room-wide look partway through, and the revision options at the end.

**Prep before class.** Project 1 collected at the start (dated, layered .psd for each image). One image of your own, a Project-1-style fix with a written brief, for the practice round. It helps a lot if it's genuinely imperfect, so the room can give real notes to the instructor. Printed or shared note sheets: three columns, "brief says," "image does," "one change.\""""),

warmup("an image from earlier in the week that the room hasn't seen, with a light or perspective problem",
       "Keep it short today, two minutes."),

("bullets", "Today",
["Project 1 is in.",
 "We critique against the brief.",
 "Not against taste."],
"""Project 1 is in. [Confirm everyone has submitted the files before going on.]

Today we look at each other's work, in small groups and then together, and the rule for the whole day is on the slide: we critique against **the brief**, not against what any of us happens to like.

This is the same critique format you'll use in session 12 and session 14, so it's worth getting comfortable with it now."""),

("quote", "Write this down", "The note is data, not a verdict.",
"Write it down. Don't defend.",
"""Here's the rule that makes critique work, and it's the same rule in every course in this program, on purpose.

A note about your work is **information** about how the image reads to someone who isn't you. It isn't a judgment of you, and it isn't a ruling you have to accept. It's data.

So when you get a note, you write it down, and you don't defend. Not yet. You can decide later whether the note is right. Explaining what you meant, in the moment, mostly just stops people from telling you what they actually see. And what they see is the only thing you can't get by yourself."""),

("bimage", "An old studio habit",
["Yesterday's work, shown to the team.",
 'Called "dailies."',
 "Notes go to the work, not the person."],
"slot:a studio dailies or review session (animation or VFX), or a sweatbox photo",
"""This isn't a school invention. Some of you heard about this in storyboarding: animation studios, as far back as the 1930s or so, had the team look at yesterday's work every morning. In film it got called "dailies," and it's still how animation and visual effects studios run.

Everybody gets notes, including the most senior people in the room. The best studios are quite strict that the notes go to **the work**, not to the person who made it. "The shadow under the car is too light," never "you always mess up shadows."

That's the culture we're trying to borrow for a morning."""),

("two", "Taste or brief?",
["**Taste**", '"I don\'t like the colors."', "Tells us about you."],
["**Brief**", '"The brief says dusk. This reads as noon."', "Tells us about the image."],
"""Here's the difference in one example.

"I don't like the colors" is **taste.** It might be true, but it tells the artist about you, not about the image, and they can't do anything with it.

"The brief says dusk, and this reads as noon, because the shadows are short and the sky is blue overhead" is **brief.** It's specific, it's checkable, and it points at something to change.

Taste isn't banned from the planet. But today, if you catch yourself saying "I like" or "I don't like," translate it: what does the brief ask for, and what is the image actually doing?"""),

("boxes", "The format",
["The brief says|read it aloud", "The image does|what you actually see", "One change|the most important one"],
"""Every note today has three parts, and there's a sheet with three columns for them.

**The brief says**: the presenter reads their brief aloud, and the note starts from it. **The image does**: what you actually see, using the checklist words where they fit. **One change**: the single most important thing to fix. Just one.

Why only one? Because a list of eleven notes is overwhelming and gets ignored, and because the one most important note is the hardest thing to find. Picking it is the skill."""),

("two", "A weak note, a useful note",
["**Weak**", '"The hand looks weird."', '"Maybe fix the lighting?"'],
["**Useful**", '"Three fingers on her left hand merge into the cup."', '"Shadows fall left; the window is on the left."'],
"""One worked example of the difference.

"The hand looks weird" is true and useless. Which hand, weird how? "Three fingers on her left hand merge into the cup handle" is the same note, made useful. Now the artist knows exactly where to look.

"Maybe fix the lighting?" is a question pretending to be a note. "The shadows fall to the left, but the window is on the left" names the check, points at the evidence, and implies the fix.

The useful notes are longer. That's fine. They're also the only ones anyone can act on."""),

("bullets", "Giving a note",
["Point at it.",
 "Name the check.",
 "Suggest, don't redesign."],
"""Three habits for giving a note.

**Point at it**, literally, on the screen or the print. **Name the check**: anatomy, light, perspective, lettering, texture, sheen, or "the brief asks for X." **Suggest, don't redesign**: "the shadow should fall right" rather than "I'd have made it a night scene." It's their image and their brief, not yours."""),

("bullets", "Taking a note",
["Write it down.",
 "Don't explain yourself yet.",
 "One question, if you need one."],
"""And three for taking one.

**Write it down**, in the third column of your sheet, word for word if you can. **Don't explain yourself yet.** Resist "yes, but what I was going for was..." You'll get your chance later, and usually you'll find you don't need it. **One question**, if a note isn't clear: "Which shadow do you mean?" That's it.

This is genuinely hard and almost nobody is good at it at first, me included. It gets easier with practice, which is why we do it four times this month."""),

("image", "Practice round: my image", "slot:your own Project-1-style corrected image, with its brief on screen",
"Read the brief. Then notes in the format, on my work.",
"""[About eight minutes.] Before you critique each other, you critique me. Here's an image I fixed, and its brief. [Read the brief aloud.]

Notes in the format, please. Brief says, image does, one change. Point at things.

[Take notes. Write them on the board in the three columns. Model the taking-a-note behavior on purpose: write it down, don't defend, ask one clarifying question at most. If someone gives a taste note, translate it out loud with them: "what in the brief does that relate to?"]

Thank you. Notice what I did with those: I wrote them down and I didn't argue with any of them, even the one I'm not sure I agree with. I'll decide about that one later."""),

("boxes", "What I'm looking at",
["Errors found|25", "Hand corrections|30", "Meets the brief|25", "Process record|20"],
"""A reminder of what the grade looks at, so your notes can help each other with what counts.

Errors found, including light and perspective, not only anatomy. Corrections that sit naturally in the image. Each image meeting its brief. And the process record: callouts numbered, every fix on its own named layer.

Notice that "is it beautiful" isn't on the list. That's on purpose."""),

("checklist", "How today runs",
["Groups of three or four", "About five minutes per person", "Brief read aloud first",
 "Toggle before and after", "Notes written on the sheet", "I rotate between groups"],
"""How the morning runs.

Groups of three or four. Each person gets about five minutes. You start by reading your brief aloud, then you show the image, toggling your FIX_ layers so we see before and after, and you name the fix you found hardest. Then the group gives notes in the format, and you write them on your sheet.

I'll rotate between groups. About halfway through, we'll stop and look across the whole room for a few minutes."""),

("bullets", "Across the room",
["What everyone caught.",
 "What almost everyone missed.",
 "What to look for next time."],
"""[Use this slide at the halfway point. Fill it in live on the board from what you saw in the groups.]

Let's step back. What did everyone catch? [Usually hands and lettering.] What did almost everyone miss? [Usually a light direction problem, a perspective problem, or one image drifting from its brief.] What should we look for next time?

[Name the pattern without naming students. This is where the room's eye improves fastest, because they hear that the miss was common, and it stops being embarrassing.]"""),

("section", "After critique", "Revising on one note",
"""One more short piece, about what to do with your notes tonight."""),

("bullets", "Revising on one note",
["Pick the note that matters most.",
 "Change only that.",
 "Before and after, on named layers."],
"""Option A tonight is a revision on one note. Here's the discipline.

Pick the note that matters **most**, not the easiest one. Change **only that**. It's the one-variable rule from session 2 again: if you change five things, you won't know which one made it better, and neither will I. Keep the earlier version as a layer or layer group, so the before and after are both in the file."""),

vocab([("Dailies", "the team reviews recent work, every day"),
       ("Note", "one observation about the work, written down"),
       ("Brief note", "what the brief asks versus what the image does"),
       ("Taste note", "what you like; translate it before you say it")]),

("options",
["Revise one image on one note.", "Before and after, named layers."],
["Written self-critique, about 150 words,", "or a 2 minute recording."],
"""Tonight, due next class.

**Option A**: revise one of your three images on one critique note, before and after on named layers, with the note written at the top of the file or in your submission.

**Option B**: a written self-critique of about 150 words, or a two-minute recording if you'd rather talk than write. Name two decisions you made and one fix you'd make now, using the brief and the checklist words.

Same rubric."""),

("quote", "One line to take home", "Against the brief, every time.",
"The note is data. Write it down.",
"""Against the brief, every time. [Into the groups.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
