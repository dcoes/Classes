#!/usr/bin/env python3
"""Session 16. Final critique.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/16_Final_Critique.pptx"

SPEC = [
("title", "Final Critique", "AI Digital Imaging  |  Session 16",
"""**Running time.** The opening is about 15 minutes, presentations take most of the session, and the closing reflection is about 15 minutes at the end. Opening: what today is, the three-minute format, how notes work today (15). Presentations, about three minutes each plus two for notes. Closing: what the month was for, what's durable, what to keep doing (15).

**Prep before class.** Collect finals with everything on the checklist. Set up the projector so each presenter can open their sheet quickly; a shared folder in presentation order saves a lot of time. Note cards for written notes. A timer that the room can see.

For the closing, look back at the room poll from session 1 if you noted the numbers. It's a nice thing to ask again."""),

("bullets", "Today",
["Finals are in.",
 "About three minutes each.",
 "Then we talk about the month."],
"""Finals are in. [Check that everyone has submitted the full set: final images, sheet, brief, board, log, rejects, layered files, disclosure.]

Today is mostly you. Each person presents for about three minutes, the room writes notes, and at the end we spend a little time on what this month was actually for.

No Spot it today. Today, the images on the screen are yours, and the eye you've been training all month gets to look at work that's already been looked at very carefully."""),

("boxes", "Your three minutes",
["The brief|thirty seconds", "The set|side by side, a moment of quiet",
 "One decision|the hardest one", "What you wouldn't generate|next time"],
"""The format, for each presenter.

**The brief**, in thirty seconds: what it's for and what it should feel like. **The set**, side by side on your sheet, and then give the room a few seconds of quiet just to look. **One decision**: the hardest decision you made, a rejection, a fix, a must you fought to keep. And **what you wouldn't use a generator for next time**, and why.

That last question is the one I'm most interested in. It's also part of Option A's process statement tonight."""),

("bullets", "Notes today",
["Brief says, image does.",
 "One thing that works, specifically.",
 "No \"one change\" today."],
"""Notes are a little different today. The work is done, so there's no point in a "one change." Instead, each note card gets two lines: **brief says, image does**, as always, and **one thing that works**, described specifically.

Remember, praise by describing what the work does, not by rating it. "The light from the left holds in all four, and the scarf reads at thumbnail size" is a much better compliment than "great job," and the presenter will actually keep it."""),

("section", "Presentations", "",
"""[Run the presentations. Keep time. After every four or five, take a minute to name something the room is seeing across several sets, good or bad.]"""),

("section", "What the month was for", "",
"""[After the last presenter. About fifteen minutes.]"""),

("bullets", "Hands up, again",
["Used one before this month?",
 "Avoid them on purpose?",
 "Changed your mind about anything?"],
"""On the first day I asked three questions. Let's ask them again, with one changed. [Ask the three questions.]

[Whatever the numbers are, say them out loud. Then ask one or two people who changed their mind, in either direction, what changed it. Also ask someone who didn't change their mind what they'd now say to someone who disagrees with them.]

All of those answers are fine. What I hoped for was that whatever you think about these tools now, you think it with more evidence than you had four weeks ago."""),

("bullets", "What you can do now",
["Write a brief someone else can follow.",
 "See what's wrong, in words.",
 "Fix it by hand.",
 "Say what you made."],
"""On the first day I put up a list called "what still costs money." Here it is again, as a list of things you've now done, each one more than once.

You've written a brief someone else could follow, and tested it on a partner. You've seen what's wrong in an image and named it in words: anatomy, perspective, light, lettering, texture, sheen. You've fixed it by hand, in a layered file anyone can read. And you've said what you made, in a disclosure statement that would stand up in front of a client.

None of those depend on which tool you used, or on which tool exists next year. That's on purpose."""),

("bullets", "What will change",
["The tools, every few months.",
 "The law, still being decided.",
 "The jobs, honestly, too."],
"""What will change, and I want to be straight about it.

**The tools** change every few months. Some of what I showed you in the menus this month will have moved or been renamed by the time you use it again. **The law** is still being decided, in courts and in other countries, and it might go in directions none of us expect. And **the jobs** are changing too, as we saw in that survey on the first day. I don't know exactly how, and anybody who says they do is guessing.

That's exactly why the course spent its time on the parts that don't depend on the menu."""),

("bullets", "What to keep doing",
["Keep drawing. It's the best input.",
 "Keep the checklist in your head.",
 "Keep your layers. Keep saying what you made."],
"""Three things I'd keep doing, after this course, whatever you decide about these tools.

**Keep drawing.** It's the input only you have, and it's the clearest way to tell any tool, or any person, what you mean. **Keep the checklist in your head**: light, perspective, anatomy, lettering, texture, sheen. It works on photographs, paintings, films and your own work, not only on generated images. And **keep your layers, and keep saying what you made.** It's a professional habit that will matter more each year, not less.

The tool is a means of expression, and the person using it is not an operator."""),

vocab([("Brief", "the first image, in words"),
       ("Checklist", "anatomy, perspective, light, lettering, texture, sheen"),
       ("Process record", "the chain of work that proves the decisions"),
       ("Disclosure", "what was generated, what you made")],
      "The whole month in four lines. Leave this up while people pack up."),

("options",
["Process statement, about 250 words,", "including what you would not", "use a generator for next time."],
["Recorded walkthrough of your", "process file, about 3 minutes."],
"""The last options, due by the deadline on Canvas.

**Option A**: a written process statement, about 250 words. What you set out to do, the hardest decision, and what you would not use a generator for next time, and why.

**Option B**: a recorded walkthrough of your layered process file, about three minutes: open the file, turn layers on and off, and talk through the decisions.

Thank you for this month. [Say something specific you saw someone in the room do over the month, without naming them if they'd rather not be named. Then let them go.]"""),

("quote", "One line to take home", "The machine made candidates.",
"You made the decisions.",
"""On the first day the line was "the machine makes candidates, somebody still has to decide." Four weeks later, that somebody was you, in every one of those files.

Thank you."""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
