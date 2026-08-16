#!/usr/bin/env python3
"""Deck 10: Boarding for Games and Interactive. Swap-in, recommended class 13.

Spec: NewLectures/decks-new-09-10-11.md
Run from the repo root:  python3 Storyboarding/build_decks/build_deck_10_boarding_for_games.py

Game stills are left as [ADD IMAGE: ...] markers in the speaker notes and
sourced by the instructor. Nothing copyrighted is generated or approximated.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import *  # noqa: F401,F403

OUT = "Storyboarding/NewLectures/10_Boarding_for_Games.pptx"
prs = new_deck(OUT)

# ====================================== PART 1: WHAT'S THE SAME (1-5)
title_slide(prs, "Boarding for Games and Interactive",
    "What breaks, and what survives  |  CA 140 Storyboarding",
    """This class is useful to you whether or not you ever work on a game, and I want to say why up front, because half the room has already decided this one isn't for them.

Everything you have learned this term was built for a medium where somebody controls the camera, the running time, and the order events happen in. Games take all three away.

So this is the closest thing to a stress test we can run on the whole course. What survives having its assumptions removed was never a film convention. It was a system. That is worth watching whatever you plan to work on.""")

quote(prs, "Let's get this out of the way",
    "A cutscene is a film.",
    "You board it exactly the way we've been boarding all term.",
    """A cutscene is a film. You board it exactly the way we have been boarding all term.

Shot sizes, angles, the 180 degree rule, match on action, eyelines, coverage. All identical. Nothing from the first half of this course gets thrown out when you walk into a games studio.

I lead with this because students arrive at this session expecting to be told that everything is different, and then they discount the eleven classes behind them. Don't. The grammar holds.

If this session were only about cutscenes it would not need to exist.""")

bullets(prs, "The receipts",
    ["Name the shots. Out loud.",
     "You already can."],
    """[ADD IMAGE: cinematic stills from God of War 2018, The Last of Us, Arcane, Uncharted 4. Four across, unlabelled.]

[LIVE: put these up and have the room name the shots before you say anything. Two minutes.]

Over the shoulder. Low angle. Extreme close up. Two shot with the line held across the cut.

Every one of those is vocabulary from class 3, applied to work that cost tens of millions of dollars, and you read all of it without help.

That is the point of this slide. The grammar you have is not a student version of the real thing. It is the real thing.""")

bullets(prs, "So why a whole class?",
    ["Because games contain a second thing.",
     "It isn't a film.",
     "And nobody teaches you how to board it."],
    """So why spend a class on it.

Because a game contains a second thing that sits alongside the cutscenes, and that second thing is not a film, and almost nobody teaches you how to board it.

That's gameplay. And boarding gameplay breaks four assumptions that every class so far has quietly depended on.""")

bullets(prs, "The four breaks",
    ["You don't control the camera.",
     "You don't control the timing.",
     "You don't control the order.",
     "You don't control the whole frame."],
    """Four things you lose.

You don't control the camera. The player does.

You don't control the timing. They might take four seconds or four minutes.

You don't control the order. Branching, optional content, and player choice mean the sequence isn't a sequence.

And you don't control the whole frame, because there's a permanent interface living in it.

Every one of those was a guarantee the last eleven classes depended on. We're going to take them away one at a time and see what's left.""")

# ====================================== PART 2: BREAK ONE, THE CAMERA (6-11)
bullets(prs, "Who's holding the camera?",
    ["Cutscene: you are.",
     "Gameplay: the player is.",
     "Cinematic gameplay: you're negotiating."],
    """Three situations, and they are genuinely different jobs.

In a cutscene you hold the camera. Board it as film.

In open gameplay the player holds it. You do not get to frame anything, and any panel you draw is a guess about one of thousands of possible views.

And in between there's cinematic gameplay, where you're negotiating: the player has control but the level, the lighting and the sightlines have been built to make certain framings likely. That middle case is where most of the interesting work is.""")

bullets(prs, "The camera archetypes",
    ["First person · third person over-shoulder",
     "Fixed · isometric",
     "Side-scroll · top-down"],
    """Six archetypes, and each is a different set of compositional constraints.

First person: no character in frame, ever, and the whole language of performance has to move to hands, voice and the world.

Third person over the shoulder: a permanent OTS, which means a permanent obstruction in one corner of every composition.

Fixed cameras, the classic Resident Evil approach: actually the most film-like, because the designer chose the angle.

Isometric, side-scroll, top-down: each one flattens a different axis and makes a different kind of information easy to read.

A board has to know which of these it's in before anything else.""")

bullets(prs, "Boarding a camera you don't own",
    ["You board the space, not the view.",
     "The panel becomes what could be seen from here.",
     "Not what is seen."],
    """This is the real shift, and it takes a while to get comfortable with.

You board the space and the possibilities, not a single view. Your panel stops being "this is the shot" and becomes "this is what could be seen from around here."

Which sounds like giving up authorship, and it isn't. It moves the authorship somewhere else: into where things are placed, what is lit, what is tall enough to see over, what draws the eye from the doorway.

You are still composing. You are composing the conditions rather than the frame.""")

bullets(prs, "The floor plan comes back",
    ["Class 4. Class 6. Class 7. Class 9.",
     "And now here, where it stops being optional.",
     "The camera moves through the space."],
    """Here it is again.

The floor plan. Class 4 for the line, class 6 for camera height, class 7 for the light plan, class 9 for blocking, and now here.

In film the floor plan is a helpful tool that nobody makes you use. In games it is the primary document, because the camera moves through the space rather than being placed in it, and the only way to reason about what the player will see is to reason about the space itself.

Fifth appearance this term. I keep telling you this course is six tools wearing different hats, and this is the one that has turned up in every single unit.""")

bullets(prs, "Directing attention without a camera",
    ["Light. Colour. Motion.",
     "Audio. Architecture. Sightlines.",
     "Negative space."],
    """If you can't point the camera, how do you make someone look at something?

Light, first and strongest. The brightest thing in a dark space wins, every time, and level designers know it.

Colour, when it's used as a system rather than decoration. Motion in the periphery, which turns heads involuntarily. Audio, which is criminally underrated and can turn a player around with no visual cue at all.

And architecture: you build the space so that the comfortable sightlines from the entrance land on the thing that matters.

[ADD IMAGE: the glowing ledges in Mirror's Edge, and the way Journey keeps the mountain on the horizon.]

Every one of those is composition, done environmentally. Level designers are composing shots you will never see.""")

bullets(prs, "Agency and the authored moment",
    ["Full control · soft-locked camera",
     "· forced look · cutscene",
     "Where you are on that line tells you",
     "how much you're allowed to compose."],
    """There's a spectrum, and knowing where you are on it is most of the job.

Full player control at one end. Then a soft locked camera, where you're gently constrained. Then a forced look, where the game turns your head for you. Then a full cutscene at the other end.

Where you sit on that line tells you exactly how much you are allowed to compose, and how much you have to design instead.

Modern games slide along it constantly, sometimes within a single minute, and the seams are where the craft is.""")

# ====================================== PART 3: BREAK TWO, TIMING (12-15)
bullets(prs, "Duration is unknown",
    ["Eight seconds, or six minutes.",
     "Every timing tool you have",
     "assumed a fixed length."],
    """The player might sprint through this space in eight seconds or wander around it for six minutes.

Everything from the animatics class assumed a fixed duration you could design against. Hold lengths, rhythm, the shape of a sequence over time. All of it assumed you knew how long.

Throw that assumption away here. You are not designing a duration, you are designing something that has to work across a wide range of them.""")

bullets(prs, "Board a state, not a shot",
    ["Before pickup. After pickup.",
     "On failure. On retry.",
     "This is where boards look like documentation."],
    """So instead of boarding moments in a sequence, you board states.

Before the player has the key. After they have it. On failure. On retry. What the room looks like the second time they walk in.

Panels stop describing a timeline and start describing conditions.

And yes, this is where boards start looking like documentation, which answers a question people always ask about whether game boards are really design documents. Partly, they are.""")

bullets(prs, "Loops and repetition",
    ["Players see the same content many times.",
     "Dramatic once is tedious the fifth time.",
     "Film has no equivalent."],
    """Players see the same content repeatedly, because they died, or backtracked, or the game is built on a loop.

Something that reads as dramatic the first time is tedious the fifth. A long unskippable beat that was beautiful on the first pass becomes the thing people complain about.

This is a genuine design constraint and it has no equivalent in film, because a film shows you every frame exactly once in a fixed order. It's the constraint that most often surprises people coming from a film background.""")

bullets(prs, "The cutscene handoff",
    ["Gameplay to cutscene, and back.",
     "The two most-noticed cuts in the medium.",
     "Match camera and pose across the seam."],
    """The transition from gameplay into a cutscene and back out is the most scrutinised cut in the entire medium, because it's where the two halves of the thing are joined.

Match the camera position and the character pose across the transition or the seam screams. If the player is standing at the door in a wide and the cutscene opens on a close up from the other side of the room, everyone feels it even if they can't say why.

The best productions hide the cut entirely.

[ADD IMAGE: the God of War 2018 continuous shot, if a clean still is available.]""")

# ====================================== PART 4: BREAK THREE, ORDER (16-19)
bullets(prs, "Sequences that aren't sequences",
    ["Branching. Optional content.",
     "Missable beats. Non-linear exploration."],
    """The third break. The order isn't fixed.

Branching paths. Optional content a player may never see. Beats that are missable entirely. Areas explored in any order the player likes.

Which means your sequence isn't a sequence. It's a set of things that might happen, in an order you don't control, some of which won't happen at all.

Everything you know about how one panel relates to the panel before it assumed there was a panel before it.""")

bullets(prs, "Boarding branches",
    ["Flowchart plus panels.",
     "One node per beat.",
     "Arrows for player choice."],
    """So the document changes shape. A flowchart with panels hanging off it. One node per beat, arrows for the choices that lead between them.

Some studios call it a beat map, some a narrative flow, and the name varies by building.

[LIVE: draw a simple two branch structure on the board. Node, two arrows, two nodes, both converging on a third.]

It is genuinely a different document from a film board, and it is the first thing that looks alien to somebody arriving from film. It's also mostly just a floor plan for time instead of space.""")

bullets(prs, "What must every player see?",
    ["Critical path versus optional.",
     "Board the critical path fully.",
     "Board optional content as key frames."],
    """Then the resourcing question, which is a real job skill and one of the few places a junior gets noticed.

What must every player see? That's the critical path, and you board it fully, because it carries the story and everybody gets it.

Everything else is optional content, and you board it as key frames. The important moment, not the full coverage.

Being able to make that call, and defend it, is worth more than being able to draw twice as fast.""")

bullets(prs, "Environmental storytelling",
    ["The story told by a room with nobody in it.",
     "Composition with no camera,",
     "no character, and no cut.",
     "And it's still staging."],
    """The last thing about order, and it's the one that makes film people sit up.

A room with nobody in it, telling you what happened here. Two chairs pulled close together. A meal half eaten. A door barricaded from the inside.

[ADD IMAGE: Rapture in Bioshock, Gone Home, or any Souls level, if clean stills are available.]

No camera, because the player brings their own. No character, because nobody's there. No cut, because nothing is edited.

And it is unmistakably staging. Somebody decided where everything sits and what the eye finds first. Which tells you that staging never needed the camera, the cut, or the actor. Hold on to that, because a later module takes it further.""")

# ====================================== PART 5: BREAK FOUR, THE FRAME (20-23)
bullets(prs, "The frame has furniture",
    ["HUD. Health. Minimap. Reticle.",
     "Subtitles. Objective markers. Prompts.",
     "Your thirds may already be occupied."],
    """Fourth break. The frame is not empty.

Health, minimap, reticle, subtitles, objective markers, button prompts. Some of it permanent, some of it appearing when you least want it.

[LIVE: overlay a HUD mockup on one of the film stills from class 5 and let the room see what it does to the composition.]

Your rule of thirds intersections may already be occupied. The bottom third of the frame may be spoken for. You compose around what is permanently there, which is a constraint film simply does not have.

And notice what that isn't: it isn't a reason to abandon composition. It's a reason to know the frame you actually have rather than the one on the template.""")

bullets(prs, "Safe areas and variable displays",
    ["Handheld. TV at ten feet.",
     "Ultrawide. Phone.",
     "Aspect ratio, with higher stakes."],
    """The same content plays on a handheld six inches from someone's face, a television across a room, an ultrawide monitor, and a phone.

That is the safe area conversation from class 2, with more variables and higher stakes, because a game ships to all of them simultaneously rather than being remastered per format.

Text legibility on the smallest target sets your type size everywhere. Critical information has to sit inside the tightest safe area. And the widest display shows things you may not have wanted visible.""")

bullets(prs, "Readability at speed and at scale",
    ["Silhouette, again.",
     "Enemies, interactables, hazards.",
     "Small, in motion, under pressure.",
     "It is a hiring criterion."],
    """Silhouette. Again. Week one, and here it is doing a job with real money attached.

A player has to distinguish an enemy from a barrel from a health pickup at small size, in motion, while under pressure, often in bad light. The only thing that reliably survives all of that is the outline.

Character silhouette design in games is a hiring criterion. Studios test for it. There are people whose entire job is making sure two enemy types don't read the same at a distance.

Which is the same test I gave you in week one with a black marker. Same test, higher stakes, and now somebody pays for it.""")

bullets(prs, "Accessibility as composition",
    ["Colourblind-safe signalling.",
     "Subtitle space. Contrast requirements.",
     "Increasingly a legal requirement, not a nicety."],
    """Accessibility, which belongs in this section because it is a composition problem and not a compliance checkbox.

If the only difference between a safe object and a dangerous one is red versus green, some percentage of your players cannot play your game. The fix is shape, or value, or motion, or all three, and that fix is a design decision made early.

Subtitle space has to exist in the composition. Contrast minimums constrain your value structure.

This is increasingly a legal and commercial requirement rather than a nicety, and knowing it in an interview is a genuine differentiator, because a lot of people still treat it as something the QA pass will catch.""")

# ====================================== PART 6: THE JOB (24-28)
bullets(prs, "What game boards actually look like",
    ["Cinematic boards, film-identical.",
     "Gameplay previs. Flow diagrams.",
     "Beat maps. Level layouts with camera sketches."],
    """Five kinds of document, and most game artists touch several.

Cinematic boards, identical to what you have been making all term. Gameplay previs, which is closer to blocking in 3D. Flow diagrams for branching. Beat maps. And level layouts with camera sketches on them, which is the floor plan doing its fifth job.

In games these frequently live inside a larger design document rather than standing alone, which means you will be writing as well as drawing.""")

bullets(prs, "Who reads them",
    ["Not just a director.",
     "Designers, engineers, level artists,",
     "animators, audio, UI.",
     "They need your intent, not just your image."],
    """This is the biggest practical difference and it's worth ending the technical half on.

A film board goes to people executing a fixed plan. A game board goes to designers, engineers, level artists, animators, audio, and UI, and those people are going to build something interactive out of it.

They need your intent, not just your image. Why is the door on that side. What is the player supposed to feel when they come around this corner. What happens if they approach from the other direction.

Which means the annotation matters as much as the panel, and a beautiful board with no reasoning attached is close to useless to them.""")

bullets(prs, "The roles",
    ["Cinematic artist. Previs artist.",
     "Narrative designer. Level designer. UX.",
     "Several hire this exact skill set."],
    """Five job titles that hire people who can do what this course teaches.

Cinematic artist, which is the most direct translation. Previs artist. Narrative designer. Level designer, more than people expect. And UX, which is composition and attention under a different name.

Several of these hire on breakdown ability and staging judgment rather than rendering, and they are considerably less crowded than feature animation.

If you came into this course as a game production major thinking storyboarding was a requirement to sit through, that's the paragraph to remember.""")

bullets(prs, "Adjacent, and worth knowing",
    ["VR and 360. AR.",
     "Immersive theatre. Interactive film.",
     "In VR, framing evaporates entirely."],
    """A few neighbours worth knowing exist.

VR and 360, where there is no frame at all and you are staging a room and hoping. AR, which composites onto a world you didn't build. Immersive theatre, which solved a lot of these problems decades before games did. Interactive film.

In VR the entire discipline of framing evaporates, and what's left is staging.

Which is a good argument that staging was always the real subject, and framing was one very successful way of delivering it. There's a module on that if you want to go further.""")

bullets(prs, "Before you leave: one beat, two ways",
    ["Take one beat from your final.",
     "Board it as a linear cutscene.",
     "Then as an interactive moment.",
     "What did you give up? What did you add?"],
    """Take one beat from your final project. Board it twice.

Once as a linear cutscene, the way you have been doing all term. Once as an interactive moment where the player controls the camera.

Then answer two questions. What did you have to give up, and what did you have to add?

You will find you gave up framing and gained a floor plan. You gave up timing and gained states. You gave up certainty about what gets seen and gained a lot of thinking about light and sightlines.

That trade is the whole class in one exercise. Post them before you leave.""")

n = finish(prs, OUT, expected=28)
print(f"OK  {OUT}  {n} slides")
