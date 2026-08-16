#!/usr/bin/env python3
"""Deck 11: The Pitch. Class 13, paired with PR5.

Spec: NewLectures/decks-new-09-10-11.md
Run from the repo root:  python3 Storyboarding/build_decks/build_deck_11_the_pitch.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import *  # noqa: F401,F403

OUT = "Storyboarding/NewLectures/11_The_Pitch.pptx"
prs = new_deck(OUT)

# ====================================== PART 1: WHAT A PITCH IS (1-6)
title_slide(prs, "The Pitch",
    "Making the room see the film  |  CA 140 Storyboarding",
    """Today you learn the part of this job that requires no drawing ability at all, and which will probably matter more to your career than anything else in this course.

Then most of you pitch, this afternoon.

I want to say at the top: nerves are not a deduction. Nobody has ever lost a mark in here for being nervous. What costs you is a different thing entirely and I'll get to it.""")

quote(prs, "The thing nobody tells you",
    "You will spend more of your career explaining boards than drawing them.",
    "And almost nobody teaches it.",
    """That's the sentence. You will spend more of your career explaining boards than drawing them.

Meetings, reviews, pitches, interviews, sitting next to a director going through a sequence page by page. That's the job, most days.

And almost nobody teaches it, which is exactly why being decent at it is such an advantage. You are about to be better at this than people with ten years on you, because they were never made to practise it and you are.""")

bullets(prs, "This is where the format came from",
    ["Disney pinned the Snow White boards to a wall.",
     "Then acted the entire film out for the crew.",
     "The storyboard was invented as a pitching tool."],
    """Here's the part that surprises people.

Disney pinned the Snow White boards to a wall and acted the whole film out for his crew. Performed it. Did the voices. Walked the room through the picture before a frame of it existed.

Pinning drawings to a wall so you could perform them is not something that happened to storyboards later. It is the origin of the format. The artifact exists because somebody needed to pitch.

So when I ask you to stand up and perform your sequence, I am not adding a public speaking requirement to a drawing course. I am asking you to use the thing the way it was built to be used.""")

bullets(prs, "What a pitch is",
    ["Standing in front of your boards.",
     "Performing the sequence.",
     "Action, voices, timing.",
     "So the room experiences the film."],
    """A pitch is standing in front of your boards and performing the sequence. Reading the action, doing the voices, indicating the timing, so the room experiences the film before it exists.

Experiences it. Not understands it, not learns about it. Experiences it.

That's the bar, and it's higher than describing what happens, which is what almost everyone does the first time.""")

bullets(prs, "What it isn't",
    ["Not a defense.",
     "Not an apology.",
     "Not reading your captions aloud."],
    """Three things it isn't, and you will be tempted by all three.

It is not a defense. You are not there to justify choices to a hostile room. Nobody is hostile.

It is not an apology. Do not open with what isn't finished, what you ran out of time for, or what you would have done with another week. Everyone's is unfinished. That is expected and it is fine.

And it is not reading your captions aloud. If your pitch consists of narrating what I am already looking at, the boards have failed and the pitch will not save them.""")

bullets(prs, "Where this happens",
    ["Story meetings. Client presentations.",
     "Festivals and grant applications.",
     "Interviews and portfolio reviews.",
     "Crowdfunding."],
    """Where you'll actually do this.

Story meetings, constantly. Client presentations. Pitching your own project to somebody who might fund it. Festival pitch sessions. Grant applications, which are a written pitch with the same structure. Interviews and portfolio reviews, which are a pitch about you.

And crowdfunding, if you go that way.

For an independent artist that list is not a list of opportunities. It is your entire funding pipeline. Nobody funds a folder of drawings. They fund a person who can make them see the film.""")

# ====================================== PART 2: HOW TO DO IT (7-15)
bullets(prs, "Know your sequence cold",
    ["You should not be reading.",
     "You should be performing.",
     "Looking at your own boards to remember",
     "means you're not ready."],
    """Know it cold. You should not be reading, you should be performing.

Here's the tell, and I will notice it: if you are looking at your own boards to remember what happens next, you are not ready. Your eyes should be on the room, and the boards should be there for them, not for you.

This is not a memory test. It's twelve to twenty panels of your own work. If you made them, you know them. Rehearse enough that you trust that.""")

bullets(prs, "Set it up in one sentence",
    ["Where we are.",
     "Who we're with.",
     "What just happened.",
     "Then start."],
    """One sentence. Where we are, who we're with, what just happened. Then start.

"It's the last night of a school year, and she's been waiting outside for an hour for someone who isn't coming."

That's it. The room is oriented, and now you can go.

Everything between that sentence and the sequence is stalling. You will be tempted to explain your process, or say how you arrived at the idea, or apologise. Don't. One sentence, then start.""")

bullets(prs, "Perform the action",
    ["Present tense. Active voice.",
     '"She turns. She sees it. She runs."',
     'Not "in this shot we see a character who is turning."'],
    """Present tense, active voice.

"She turns. She sees it. She runs."

Not "in this shot we see a character who is turning, and then in the next panel here she's noticed something."

The second version puts the room outside the film, watching you describe a document. The first puts them inside it. It's the same information and it is a completely different experience, and the only difference is grammar.

Present tense. Active voice. Short sentences.""")

bullets(prs, "Do the voices",
    ["Badly is fine.",
     "Silently is not.",
     "You will feel ridiculous.",
     "Everyone feels ridiculous."],
    """Do the voices.

Badly is completely fine. Nobody is assessing your acting and nobody expects a range. What is not fine is silence, because the room needs to hear the dialogue timed against the cut, and reading it flat tells them nothing about the rhythm.

You will feel ridiculous. Everybody feels ridiculous. The people who look comfortable doing this have simply done it enough times that the feeling stopped mattering, and the only route to that is through.

So: feel ridiculous, out loud, for three minutes.""")

bullets(prs, "Pitch the timing",
    ["Pause where the film pauses.",
     "Speed up where it speeds up.",
     'Say "hold" on a hold.',
     "You are performing the edit."],
    """This is the one that separates a pitch from a description, and it's the one most people never think to do.

Pause where the film pauses. Speed up where it speeds up. If a shot holds for four seconds on somebody's face, hold. Actually stop talking and let four seconds go by. It feels like an eternity when you're standing there and it is exactly right.

Say "hold" on a hold if you need to.

You are not summarising the edit. You are performing it. The room should be able to feel the shape of the sequence in the rhythm of your voice with their eyes shut.""")

bullets(prs, "Match the energy",
    ["A chase pitched calmly is a chase that doesn't work.",
     "The room's read on your sequence",
     "follows your read on your sequence."],
    """Match the energy of the thing.

A chase pitched calmly is a chase that doesn't work. A quiet, sad scene pitched at high volume is a scene nobody believes.

This is worth being deliberate about, because the room's read on your sequence will be heavily shaped by your read on your sequence. If you sound uncertain about whether a moment lands, they will decide it doesn't. If you deliver it like it works, they'll look for why it works.

That is not manipulation. It's the same information delivered with the confidence the finished thing would have.""")

bullets(prs, "Know your one thing",
    ["Every sequence has one moment it exists for.",
     "Know which one.",
     "Land it.",
     "Or the room decides for you."],
    """Every sequence has one moment it exists for. One beat that everything else is setup or aftermath for.

Know which one it is, and land it. Build toward it in the pitch, slow down when you get there, let it sit.

If you don't know what your sequence is about, the room will decide for you, and they will pick something you didn't intend, and then all their notes will be about the wrong thing. That's not their fault. You gave them nothing to aim at.

This is also the question I will ask you if the pitch is vague: what is this about. Have an answer.""")

bullets(prs, "The physical part",
    ["Stand beside the boards, not in front.",
     "Point deliberately, not constantly.",
     "Finish, then stop talking."],
    """Three small physical things that make a disproportionate difference.

Stand beside the boards, not in front of them. You would be amazed how many people spend a pitch blocking the thing they're pitching.

Point deliberately, not constantly. A hand that's always moving stops meaning anything. Point when you want an eye somewhere specific.

And finish, then stop talking. This is the hard one. When you get to the end there will be a silence, and it will feel enormous, and you will want to fill it with "so, yeah, that's basically it." Don't. The silence is not your problem to solve. Let it sit. Somebody will speak.""")

bullets(prs, "Length",
    ["Three to four minutes for a sequence.",
     "Rehearse out loud, timed, three times.",
     "Reading it in your head does not work."],
    """Three to four minutes. That's the length of your pitch this afternoon and it's roughly the professional length too.

Rehearse it out loud, with a timer, at least three times.

Out loud. Not in your head. I say this every term and every term people run over by two minutes, and it is always the people who rehearsed silently, because your inner voice reads at about twice the speed you talk.

Three times, out loud, timed. It takes twelve minutes total and it is the single highest return thing you can do before this afternoon.""")

# ====================================== PART 3: TAKING NOTES (16-21)
bullets(prs, "The room will have notes",
    ["Always.",
     "Including on excellent work.",
     "Notes are not a verdict. Notes are the job."],
    """The room will have notes. Always. Including on excellent work, and often especially on excellent work, because good work is worth engaging with.

This is the part I most want you to get right, because it is the most professionally valuable thing in this course and it is where I've watched the most talented students hurt themselves.

Notes are not a verdict on you. Notes are the job. A room that has nothing to say about your sequence is a room that isn't interested in it.""")

bullets(prs, "Don't defend",
    ["The response to a note is: got it.",
     "Or a clarifying question.",
     "Not an explanation of what you meant."],
    """The response to a note is "got it," or a clarifying question. That is the whole list.

Not an explanation of what you meant. Not the reasoning behind the choice. Not the constraint you were working under.

This is hard, it feels unnatural, and it is non negotiable in here, for one reason:

If you have to explain what you meant, the boards didn't say it. And that is the note. The moment you start explaining, you have confirmed the thing they were telling you.

You can respond after all the notes are in. During, you write them down.""")

bullets(prs, "Write everything down",
    ["Including the notes you disagree with.",
     "Especially those."],
    """Write everything down. All of it, including and especially the notes you disagree with.

Two reasons. The first is practical: you will not remember, and a note you half remember three days later is worse than no note.

The second is that the ones you disagree with are the ones worth revisiting. A note that lands immediately is easy. A note that annoys you is usually pointing at something you already suspected and didn't want to deal with. Write it down and look at it tomorrow when it's stopped stinging.""")

bullets(prs, "The note behind the note",
    ["People are good at spotting that something's wrong.",
     "Unreliable at saying why.",
     '"Make the monster bigger" often means',
     '"I\'m not scared here."'],
    """Here's the most useful idea in this section.

People are excellent at noticing that something is wrong and unreliable at identifying why. So the note you receive is usually a proposed solution to a problem they've felt but not diagnosed.

"Make the monster bigger" often means "I'm not scared here." And the fix might be a bigger monster. It might also be a longer hold before the reveal, or a tighter shot on the character's face, or cutting the shot that gave it away two panels early.

Your job is to diagnose, not to comply. If you solve the stated note when the real problem is somewhere else, you waste everybody's week and the note comes back.""")

bullets(prs, "Ask about intent, not solutions",
    ['Good: "What\'s the feeling you want here?"',
     'Bad: "So should I make it a low angle?"',
     "They hired you to solve it."],
    """Which leads to the right kind of question.

Good: "What's the feeling you want coming out of this moment?" That gets you the problem.

Bad: "So should I make it a low angle?" That asks them to do your job, and worse, it usually gets a yes, and now you've implemented somebody else's guess.

They hired you to solve it. Ask what the target is, then hit it your way.""")

bullets(prs, "Disagreeing well",
    ['"Let me try both."',
     '"Can I show you why I went the other way?"',
     "Then let the work argue."],
    """You are allowed to disagree. You're not allowed to be precious. There's a difference and it's mostly about timing and tone.

"Let me try both" is a professional answer, and it usually ends the argument, because one of them will obviously be better when you see them side by side.

"Can I show you why I went the other way" is also fine. Then show them, and let the work make the case instead of you.

What doesn't work is defending in the moment, at volume, with your own certainty as the evidence. Let the work argue. It's better at it than you are.""")

# ====================================== PART 4: THE CAREER CONTEXT (22-26)
bullets(prs, "Pitching yourself",
    ["Portfolio reviews. Interviews.",
     "Your reel. Your artist statement.",
     "Same skill: set it up, perform it, stop."],
    """Everything you just learned applies to pitching yourself, which you will do far more often than you pitch a sequence.

Portfolio review. Interview. Your reel, which is a pitch with no narrator. Your artist statement, which is a pitch in writing.

Same structure every time. Set it up in one line, perform it rather than describe it, know your one thing, and stop talking when you're finished.

The people who are good at interviews are not more confident than you. They have just noticed that an interview is a pitch and prepared it like one.""")

bullets(prs, "The independent path",
    ["Grants. Crowdfunding.",
     "Festival pitch sessions. Finding collaborators.",
     "Nobody funds a folder of drawings."],
    """If you go independent, this is the whole machine.

Grants are pitches. Crowdfunding is a pitch you deliver once and it runs for a month without you. Festival pitch sessions are literally this, with a timer. And finding collaborators, which is the one nobody mentions, is a pitch: talented people choose projects, and they choose the ones somebody made them see.

Nobody funds a folder of drawings. They fund a person who can make them see the film.""")

bullets(prs, "The honest version",
    ["Entry-level 2D board roles have contracted.",
     "Generative tools are being tested widely.",
     "What holds value: judgment, taste, art direction.",
     "And the ability to defend a choice in a room."],
    """I'm going to be straight with you for a minute, because you'll hear this eventually and I'd rather you hear it from someone who is also handing you a plan.

Entry level 2D board roles have contracted. That's real. Generative tools produce panels quickly and studios are testing them widely, and some of that testing will stick.

What is holding its value: judgment, taste, art direction, and the ability to sit in a room and defend a choice. Viable paths run through 2D and 3D hybridity, previs, games, strong generalism, and being fluent in more than one industry.

I'm not going to tell you the field is fine. I'm going to tell you which half of the job is durable, and then train you in it. That's what this whole course has been, and it's why the pitch is on the syllabus at all.""")

quote(prs, "What the room is for",
    "A machine can generate a panel. It cannot sit in a room, understand what a director is actually worried about, and propose the fix.",
    "That's the job. It always was.",
    """A machine can generate a panel. It cannot sit in a room, understand what a director is actually worried about, and propose the fix.

That's the job. It always was. The drawing was only ever how you delivered it.

And the thing you're about to do this afternoon, standing up and making a room see something that doesn't exist yet, is the part of it that nothing on the horizon touches.""")

bullets(prs, "This afternoon",
    ["Three to four minutes, in front of your boards.",
     "Whatever state the sequence is in.",
     "Two notes minimum, received without defending.",
     "Post your notes within 24 hours."],
    """Right. What happens next.

Three to four minutes each, in front of your boards, in whatever state the sequence is in. Incomplete is expected. Pitch what exists and describe what's coming.

You'll get notes from me and from three assigned peers. Giving notes is graded too, so when it isn't your turn you are still working.

Take at least two notes without defending, ask at least one question about intent, and write them down.

And within twenty four hours, post the notes you received and one line on what you'll change. That's what turns this from a performance into a revision, and it's the difference between a pitch that was an experience and a pitch that was useful.

If you want to swap the assigned script for your own premise, this is where you ask. The gate is real, a pitch can be declined, and a declined pitch costs you nothing but the swap.""")

n = finish(prs, OUT, expected=26)
print(f"OK  {OUT}  {n} slides")
