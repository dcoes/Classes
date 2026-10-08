#!/usr/bin/env python3
"""Session 14. Peer critique (Milestone 3 due).  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/14_Peer_Critique.pptx"

SPEC = [
("title", "Peer Critique: The Corrected Set", "AI Digital Imaging  |  Session 14",
"""**Running time.** A critique day: the lecture is about 30 minutes, then small-group critique with written notes. Spot it (3). Milestone 3 check-in (3). Written notes, and why (6). Addressing a note: three honest responses (6). The focal image, and where detail goes (6). Practice round (6). How today runs (2). Then critique.

**Prep before class.** Collect Milestone 3 (the corrected set, with type on at least one image). Printed or shared written-note cards: reader's name, the three columns, and a line for "the one change I'd make first." One corrected set of your own for the practice round."""),

warmup("one image from a corrected set where the remaining problem is subtle (an edge, a grain mismatch)",
       "Pick something subtle on purpose. By now the room should be finding the quiet errors."),

("bullets", "Milestone 3 is in",
["The corrected set.",
 "Type on at least one image.",
 "Two classes left."],
"""Milestone 3, the corrected set. [Check submissions.]

Two classes left after today: presentation and export next time, then the final critique. So the notes you get today are the last round of notes before the final. Take them seriously, and write them down."""),

("quote", "Today's idea", "Write the note down, for them.",
"A spoken note is gone by tonight.",
"""Today is different from the last two critiques in one way: every reader **writes** their notes, on a card, and hands it to the presenter.

The reason is simple. A spoken note is gone by tonight. You'll remember the one that stung and forget the three useful ones. A written note is still there at midnight when you're actually doing the fixes.

It's also how notes work at most studios: they're written down, by someone, and they get tracked until they're addressed."""),

("checklist", "The note card",
["Your name", "Brief says", "Image does", "One change, first", "Which image is weakest now"],
"""The card has five lines.

Your **name**, so the presenter can ask you about it later. The three columns we've been using: **brief says, image does, one change.** And one more line: **which image is weakest now**, after the corrections.

Keep the notes specific. "The scarf is orange in image 3, red everywhere else" is a note. "Looks great!" is kind, and also not a note. You can say it out loud, but it doesn't go on the card."""),

("boxes", "Three honest responses to a note",
["Do it|and say so", "Adapt it|fix the problem a different way", "Decline it|with a reason, in writing"],
"""Here's something we haven't said yet. You don't have to do every note. What you have to do is **address** every note, and there are three honest ways to do that.

**Do it**, and say that you did. **Adapt it**: you agree there's a problem, but you fix it a different way than the reader suggested. And **decline it**, with a reason, in writing: "I kept the light from the right because the brief's must list requires the window on the right."

The milestone rubric says exactly this: every note is addressed, or a reason is given for not addressing it. Declining with a reason is a full mark. Ignoring a note isn't."""),

("bullets", "The focal image",
["One image leads the set.",
 "It gets the most care.",
 "Detail goes where the eye goes."],
"""Every series has a focal image, the one that leads: the main key art, the first chapter header, the poster in the middle of the wall. It's the one people see first and judge the others by.

That image deserves the most care in these last few days. It's Option B tonight: one more hand-painted correction pass on your focal image.

And within that image, **detail goes where the eye goes.** The focal area, usually a face or the main action, gets the sharpest edges, the most contrast and the most finish. The rest can be simpler, softer, quieter. Generated images do the opposite: they put the same amount of detail everywhere. Taking detail out of the parts that don't matter is often the best correction you can make."""),

("bullets", "Finishing, not polishing",
["Finishing: the brief is met.",
 "Polishing: changing things that work.",
 "Know which one you're doing."],
"""A warning for the last stretch. There's a difference between finishing and polishing.

**Finishing** is closing the gaps between the image and the brief, fixing the remaining callouts, addressing the notes. **Polishing** is changing things that already work, because you're nervous, or because rerolling is a habit, or because it's 2 a.m.

Polishing feels like work, and sometimes it makes things worse. When you catch yourself regenerating a part that was fine, stop, and go back to your list of notes."""),

("image", "Practice round: my corrected set", "slot:your own corrected set, side by side, with type on one image",
"Write a card for me. Then we compare.",
"""[About six minutes.] One more time, on me first. Here's my corrected set. Everyone write a note card for it, all five lines, in two minutes.

[Collect four or five cards and read them aloud. Point out which notes are specific, and which ones you'd do, adapt, or decline, saying why for each. Decline at least one, with a reason, so they see that it's allowed.]"""),

("checklist", "How today runs",
["Groups of three or four", "Set side by side, then the focal image", "Read your brief and musts aloud",
 "Every reader writes a card", "Hand the cards to the presenter", "I rotate between groups"],
"""Same as before, with the cards.

Groups of three or four, about six minutes each. Show the set side by side, then the focal image large. Read your brief and must list aloud. Every reader writes a card and hands it to the presenter. Presenters: read them tonight and decide, for each one, do, adapt or decline.

I'll rotate and add my own card for each of you."""),

vocab([("Note card", "a written note, with the reader's name"),
       ("Address a note", "do it, adapt it, or decline with a reason"),
       ("Focal image", "the one that leads the set"),
       ("Finishing vs polishing", "closing gaps versus changing what works")]),

("options",
["Address two critique notes,", "each on a named layer."],
["One more hand-painted pass", "on your focal image,", "plus one critique note."],
"""Tonight, due next class.

**Option A**: address two of today's notes, each on its own named layer, and write a line for each: did it, adapted it, or declined it and why.

**Option B**: one more hand-painted correction pass on your focal image, concentrating detail where the eye goes, plus addressing one critique note.

Next class: the presentation sheet and export. Bring your final files."""),

("quote", "One line to take home", "Address every note.",
"Do it, adapt it, or say why not.",
"""Address every note. Do it, adapt it, or say why not. [Into the groups.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
