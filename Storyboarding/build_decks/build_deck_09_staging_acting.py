#!/usr/bin/env python3
"""Deck 09: Staging and Acting for Boards. Class 9, at final-project launch.

Spec: NewLectures/decks-new-09-10-11.md
Run from the repo root:  python3 Storyboarding/build_decks/build_deck_09_staging_acting.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import *  # noqa: F401,F403

OUT = "Storyboarding/NewLectures/09_Staging_and_Acting.pptx"
prs = new_deck(OUT)

# ====================================== PART 1: ACTING IS A STAGING PROBLEM (1-5)
title_slide(prs, "Staging and Acting",
    "What the character is doing  |  CA 140 Storyboarding",
    """Today is the one class in this course that isn't about where the camera goes.

For eight classes you have been learning to place a camera, hold a line, and compose a frame. All of that is about the outside of the shot. Today is about what's happening inside it: what the character is doing, what they want, and how you draw a person who is clearly in the middle of wanting something.

This is also the class where your final gets assigned, and that is not a coincidence. You are about to board a story where people have to perform, and this is the last lecture that can still change your work.""")

bullets(prs, "The note you'll get",
    ['"It\'s stiff."',
     '"I don\'t believe them."',
     '"I can\'t tell what they want."'],
    """You have already heard at least one of these, or you will. Probably in the City Park critique.

They sound like drawing notes. They almost never are.

When somebody says a pose is stiff, the instinct is to go back and draw it better. Cleaner lines, better anatomy, more time. That fixes it approximately never, because the problem wasn't the execution. The problem was that no decision was made about what the character was doing, so there was nothing for the drawing to express.

Every one of these three is an acting note. Until today you have had no vocabulary for them, which is why they have been frustrating to receive.""")

bullets(prs, "Same skill, different decision",
    ["Same character. Same shot size.",
     "One reads as WAITING.",
     "One reads as DREADING.",
     "The difference is not drawing ability."],
    """[LIVE: draw both on the board, badly, about forty seconds each. The crudeness is the point.]

Two panels. Identical character, identical framing, identical amount of skill in the hand that made them, because it's the same hand and it isn't very good.

One reads as somebody waiting. One reads as somebody dreading. You can tell which is which from the back of the room.

Nothing about that difference is rendering. It's weight, it's where the head is, it's what the hands are doing. It is a decision, and the decision is what I'm teaching today.""")

quote(prs, "The core question",
    "What does this character want, right now, in this shot?",
    "If you can't answer it, the panel is decoration.",
    """This is the question. Everything else today is a technique for answering it on paper.

Right now, in this shot. Not what they want in the film. What they want in this panel, in this second. Those are different, and the second one is the one you draw.

If you can't answer it for a panel, that panel is decoration. It's a picture of a person in a place. It might be a nice picture. It isn't a shot.

Write the verb in the margin if you have to. Genuinely, write it next to the panel. Half of you will find that when you try, you can't, and that is the most useful thing that will happen to you today.""")

two_content(prs, "Acting in animation, acting in boards",
    ["ANIMATION", "Performance across time",
     ("Arcs, overlap, secondary action", 1),
     ("Dialogue timed to the frame", 1),
     ("Hundreds of drawings", 1)],
    ["BOARDS", "Performance in one held moment",
     ("The pose that carries the beat", 1),
     ("One drawing", 1),
     ("You pick which moment it is", 1)],
    """There's a real division of labour here and it's worth being precise, because you will take an acting class for animation and it will teach you something different.

An animator acts across time. They own the arc, the overlap, the settle, the way a hand gets to where it's going. That's performance as motion.

You act in single held moments. Your job is to look at a beat that lasts three seconds and pick the one frame that contains the performance, then draw that.

That is harder than it sounds and it is a genuine specialty. An animator handed a great key pose can make it live. Nobody can rescue a key pose that was the wrong moment.""")

# ====================================== PART 2: THE BODY (6-13)
s = title_only(prs, "Line of action",
    """One curve, drawn through the whole figure, before anything else. Before the head, before the hands, before you know what they're wearing.

[LIVE: draw both of these, ten seconds each.]

Look at the difference. The one on the left is doing something. The one on the right is standing there being drawn.

This is the first mark you make on a panel, and every other mark serves it. If you're fixing a pose that isn't working, don't fix the arms. Go back and ask whether there was ever a line of action, because usually there wasn't.""")
figure(s, Inches(4.0), Inches(2.4), Inches(3.0), lean=0.0)
label(s, Inches(2.9), Inches(5.6), Inches(2.2), "STRAIGHT SPINE\nstanding there", size=13, bold=True)
h = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.2), Inches(2.4), Inches(0.6), Inches(0.6))
h.fill.solid(); h.fill.fore_color.rgb = ACCENT; h.line.fill.background(); h.shadow.inherit = False
line(s, Inches(8.5), Inches(3.0), Inches(9.3), Inches(4.0), color=ACCENT, width=2.5)
line(s, Inches(9.3), Inches(4.0), Inches(8.6), Inches(5.4), color=ACCENT, width=2.5)
label(s, Inches(7.6), Inches(5.6), Inches(2.2), "C-CURVE\ndoing something", size=13, bold=True, color=ACCENT)

bullets(prs, "Straight against curve",
    ["Rigid on one side, flowing on the other.",
     "Never both sides the same.",
     ("All curves is mush", 1),
     ("All straights is a mannequin", 1)],
    """This is the oldest trick in figure drawing and it survives at board scale, which is why it's here and most figure drawing content isn't.

Every limb, every torso. One side does something the other side doesn't. If the outside of the arm is a long straight, the inside is a curve. If the back is a flowing C, the front has a break in it somewhere.

A figure made only of curves is mush. There's no tension, nothing holds. Made only of straights, it's a mannequin. You need both, in opposition, and the opposition is what makes the eye read it as a body under its own power.""")

bullets(prs, "Silhouette. Again.",
    ["Fill it solid black.",
     "Can a stranger name the action?",
     "If not, the pose failed."],
    """Yes, again. Week one, the composition class, and now here.

I keep bringing this back because it is the single most useful thing I can teach you, and because it is the only standard in this course completely independent of how well you draw.

A beautifully rendered figure that reads as a blob when you fill it in has failed. A stick figure that reads instantly as reaching for something on a high shelf has succeeded. Those are the actual outcomes, and the rubric says so.

Fill your pose in black. If you can't tell what they're doing, move something until you can.""")

bullets(prs, "Negative space is part of the pose",
    ["The gaps are shapes too.",
     ("Arm away from the torso, the gap reads", 1),
     ("Arm across the torso, it disappears", 1),
     "Closed shapes read. Mush doesn't."],
    """The gaps between the arm and the body, between the legs, between the head and the shoulder. Those are shapes, and the eye reads them as fast as it reads the figure.

If the arm is in front of the body you lose it. It merges into the torso and the silhouette goes solid. So move it. Rotate the figure a few degrees, lift the elbow, turn the shoulder, whatever opens a gap between the limb and the mass.

This is the cheapest fix in the whole class. It costs nothing, it requires no skill, and it will save more panels than anything else I say today.""")

s = title_only(prs, "Weight",
    """Where is the centre of gravity, and what is holding it up?

Three versions here. Balanced, weight shifted onto one leg, and off balance, which means mid fall or mid lunge, committed to something.

Characters without weight look like stickers. They look pasted onto the background rather than standing on it. And the fix is usually one line: where the feet actually contact the ground, and whether the mass above them is over that contact or not.

Balanced is neutral, fine for someone waiting. Shifted is relaxed, casual, thinking. Off balance is the interesting one, because a body that has committed past its own centre of gravity has already decided something. That's a character in the middle of an action, which is what you want in a board.""")
for i, (lean, cap) in enumerate([(0.0, "BALANCED\nneutral, waiting"),
                                 (0.12, "SHIFTED\nrelaxed, thinking"),
                                 (0.42, "OFF BALANCE\ncommitted")]):
    cx = Inches(2.6 + i * 3.7)
    figure(s, cx, Inches(2.3), Inches(2.7), lean=lean, color=ACCENT if i == 2 else INK)
    line(s, cx - Inches(1.0), Inches(5.05), cx + Inches(1.4), Inches(5.05), color=MUTE, width=1.0)
    label(s, cx - Inches(1.3), Inches(5.25), Inches(2.6), cap, size=12, bold=True)

bullets(prs, "Asymmetry",
    ["Shoulders and hips opposed.",
     "Head off the spine axis.",
     "Nothing parallel.",
     "Symmetrical reads as dead or robotic."],
    """If a line in your figure is parallel to another line in your figure, one of them is probably wrong.

Shoulders tilt one way, hips tilt the other. The head sits off the axis of the spine. Weight is on one leg, not shared. Arms do different things.

Symmetrical poses read as dead, formal, or robotic, and sometimes that is exactly what you want. A soldier at attention. A judge. Something inhuman. Use it deliberately when you want it.

The rest of the time, break it. And notice this is the same principle as one dominant element from the composition class: the eye needs somewhere to go, and perfect balance gives it nowhere.""")

two_content(prs, "Gesture over anatomy",
    ["CAREFULLY CONSTRUCTED", "Correct proportions",
     ("Anatomy checks out", 1),
     ("Took twenty minutes", 1),
     ("Reads as: a person exists", 1)],
    ["LOOSE AND GESTURAL", "Proportions approximate",
     ("Line of action unmistakable", 1),
     ("Took four minutes", 1),
     ("Reads as: a person WANTS something", 1)],
    """[LIVE: put both up. The constructed one should be visibly the better drawing.]

The one on the right is better boarding, and it took a fifth of the time.

I want to be careful, because this is easy to hear as don't bother learning anatomy, and that is not what I'm saying. Anatomy is genuinely worth having and it will make you a better artist.

What I'm saying is that it is a nice to have, and intent is mandatory. Given a choice between anatomically correct and unreadable, or anatomically wrong and instantly legible, the second one ships. Every time.""")

bullets(prs, "If you want to push further",
    ["Construction, foreshortening, dynamic figures",
     "Linked on Canvas",
     "Enrichment, not required, not graded"],
    """There's a body of material on figure construction linked on Canvas. The classic Marvel Way work, foreshortening, dynamic figures.

Two honest things about it.

If you want your figures to be genuinely good, that's the path. It's the real thing and it works.

And it is not required to do well in this class, and it is not what I'm grading. Nobody in here loses a mark for skipping it. I'm putting it in front of you because some of you want it and don't know where to look, not because you owe it to me.""")

# ====================================== PART 3: THE FACE (14-17)
bullets(prs, "Faces last, not first",
    ["The body carries most of the performance.",
     "Draw the face first and the pose accommodates it.",
     "Reverse the order."],
    """Watch what happens when a student starts a panel. Nine times out of ten the first thing on the paper is a head.

Then the body gets built underneath it, and the pose ends up being whatever the head allows. Because the head was drawn before anyone decided what the character was doing, the pose is a compromise.

Reverse it. Line of action, then mass, then weight, then last the head. By the time you get to the face, the body has already told you what expression belongs on it.

The body carries most of the performance anyway. At board scale it carries more, because the face is often four marks wide.""")

bullets(prs, "Expression economy",
    ["Three marks: brow, eye line, mouth.",
     "That is a complete expression at board scale.",
     "More than that is rendering."],
    """Three marks. Brow, eye line, mouth. That is a complete, readable expression at the size you are actually working.

[LIVE: six emotions on the board, three marks each, about eight seconds apiece. Let them call out which is which.]

Nobody in that grid has a nose. Nobody has ears. It doesn't matter, you read every one of them.

If you're spending more than three marks on a face in a board panel, you're rendering, and rendering is not on the rubric.""")

bullets(prs, "The brow does the work",
    ["Same eyes. Same mouth.",
     "Four different brows.",
     "Four different emotions."],
    """Here is the same face four times. Identical eyes, identical mouth. The only thing that changes is the angle of the brow.

Angry, worried, surprised, sceptical. Four completely different people, and the only variable is two short lines.

The mouth gets all the attention and it does much less than you think. If you're going to learn one feature properly, learn the brow. It does most of the emotional work in almost every face you have ever read.""")

bullets(prs, "When the face doesn't matter",
    ["Long shots. Silhouettes. Back of the head.",
     "Withholding the face can be the performance.",
     "Don't draw a face because there's a head."],
    """Sometimes the right answer is no face at all.

A character turned away at the moment they get the news. A figure in silhouette in a doorway. Someone in a long shot where a face would be four marks anyway.

Withholding the face can be the performance. The audience fills it in, and what they fill in is more specific to them than anything you could have drawn.

The failure here is drawing a face out of obligation. There's a head in the frame, so it gets eyes. Ask whether the shot is better without it. Surprisingly often it is.""")

# ====================================== PART 4: STAGING RELATIONSHIPS (18-24)
s = title_only(prs, "With two characters, the relationship is the composition",
    """Before you draw either character, decide what the relationship is in this moment. The staging follows automatically. You won't have to invent it.

Four arrangements here, and each says something before anybody opens their mouth.

Facing each other, level: equals, engaged, a negotiation between peers. One turned away: refusal, or shame, or dismissal, and the audience reads that instantly without being told. One higher: power, and we'll come back to that. Distance: the physical gap between two people is a dial you control, and it is one of the loudest signals available to you.

Every one of these is a decision you make before drawing, not a discovery you make afterward.""")
for cap, i in [("FACING\nequals", 0), ("TURNED AWAY\nrefusal", 1),
               ("ONE HIGHER\npower", 2), ("DISTANT\nisolation", 3)]:
    x0 = Inches(1.1 + i * 3.0)
    if i == 0:
        figure(s, x0 + Inches(0.6), Inches(2.6), Inches(1.9))
        figure(s, x0 + Inches(1.9), Inches(2.6), Inches(1.9))
    elif i == 1:
        figure(s, x0 + Inches(0.6), Inches(2.6), Inches(1.9))
        figure(s, x0 + Inches(1.9), Inches(2.6), Inches(1.9), lean=-0.25, color=MUTE)
    elif i == 2:
        figure(s, x0 + Inches(0.6), Inches(3.1), Inches(1.5))
        figure(s, x0 + Inches(1.9), Inches(2.2), Inches(2.3), color=ACCENT)
    else:
        figure(s, x0 + Inches(0.25), Inches(2.6), Inches(1.9))
        figure(s, x0 + Inches(2.3), Inches(2.6), Inches(1.9))
    line(s, x0 + Inches(0.1), Inches(4.85), x0 + Inches(2.6), Inches(4.85), color=MUTE, width=1.0)
    label(s, x0, Inches(5.05), Inches(2.7), cap, size=12, bold=True)

bullets(prs, "Height and power",
    ["Who is higher in the frame?",
     "This stacks with camera angle.",
     ("Low angle on someone already higher is redundant", 1),
     ("Sometimes you want the contradiction", 1)],
    """Height reads as power. That is not a film convention, it's something people bring into the cinema with them.

Here's the part worth thinking about. You now have two independent controls for it: where the characters are in the space, and where the camera is. They stack.

A low angle on a character who is also physically standing above the other one is redundant. You've said the same thing twice and the shot gets a bit shouty.

The interesting case is the contradiction. A high angle on the powerful character. A low angle on the one who's losing. That's a shot saying two things at once, and audiences feel it even when they can't name it. It's available to you, and almost nobody in this room will use it unless I say so out loud. So: it's available to you.""")

s = title_only(prs, "Distance and intimacy",
    """Proxemics. Four rough zones, cross cultural enough to rely on, and audiences read them instantly without knowing the word.

Intimate, out to about eighteen inches. Lovers and threats, and almost nothing in between. Personal, out to about four feet: friends, real conversation. Social, four to twelve: colleagues, transactions, strangers being polite. Public, beyond that: performance, address, isolation.

The dial is yours. Two characters at intimate distance having a work conversation is uncomfortable and the audience feels it. Two characters at social distance arguing about their marriage is cold, and they feel that too.

You don't have to name the zone when you're boarding. You do have to notice that you're choosing one.""")
cx, cy = Inches(3.6), Inches(4.1)
for r, col in [(Inches(2.5), MUTE), (Inches(1.85), MUTE), (Inches(1.2), INK), (Inches(0.55), ACCENT)]:
    o = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - r, cy - r, r * 2, r * 2)
    o.fill.background(); o.line.color.rgb = col; o.line.width = Pt(1.25); o.shadow.inherit = False
label(s, Inches(6.6), Inches(2.1), Inches(5.4),
      "INTIMATE   to 18in\nlovers, or threats\n\n"
      "PERSONAL   to 4ft\nfriends, real conversation\n\n"
      "SOCIAL   4 to 12ft\ncolleagues, strangers\n\n"
      "PUBLIC   12ft and beyond\naddress, isolation",
      size=14, align=PP_ALIGN.LEFT)

bullets(prs, "Open and closed",
    ["Arms, shoulders, orientation.",
     "Toward or away.",
     "Legible at thumbnail size."],
    """Open: arms away from the body, shoulders square to the other person, torso oriented toward them. Closed: arms crossed or in front, shoulders turned off, body angled away.

This is a blunt instrument and I'm recommending it anyway, for one reason. It is legible at thumbnail size.

A subtle facial expression is invisible at the scale you're actually working. Body language isn't. When you're doing your thumbnail sprint and each panel is under an inch, open versus closed is one of very few performance signals that still survives.

Use the tools that work at the size you're drawing.""")

bullets(prs, "Three or more",
    ["Triangular staging, nobody redundant.",
     "Groupings read as sides.",
     "One character isolated is a story beat."],
    """Two people is a relationship. Three is a structure, and a different problem.

Triangular staging is the default. Three characters at different depths and different heights, so nobody is hidden and nobody is decorative. Straight lines of people read as a chorus.

Groupings read as sides. If two of your three are near each other and the third isn't, the audience has already decided there's an alliance, whether you meant it or not.

Which means the isolated character is never a layout accident. Proximity is the same principle from the composition class, things near each other belong together, applied to people. Who is grouped with whom is the story.""")

bullets(prs, "Stage the listener",
    ["Beginners board the person talking.",
     "The performance is usually on the other face.",
     "Acting is reacting."],
    """This is the one I'd most like you to take out of today.

Watch any well directed dialogue scene and count how much screen time goes to the person who isn't speaking. It's usually more than half, and often the most memorable shot in the scene is somebody listening.

Beginners board the talker. Line of dialogue, cut to whoever said it, repeat. It's a reasonable instinct and it produces flat scenes.

The information in a scene is usually the effect the line has, not the line. Which means the reaction is the shot. When you're boarding your final and you're not sure where to cut, try cutting to the person who isn't talking and see what it does.""")

bullets(prs, "Blocking across a sequence",
    ["Characters move, and the movement is dramatic.",
     ("Starts across the room. Ends beside her.", 1),
     "Twelve panels in the same places? Ask why."],
    """Everything so far has been one panel. This is about the sequence.

Characters move during a scene, and where they move is dramatic information. Someone who starts across the room and ends up beside the other person has performed the entire scene with their feet. You could cut the dialogue and still know what happened.

The failure is a scene where two people stand in fixed positions for twelve panels and only their faces change. That's radio with pictures.

So when you plan your final, look at your floor plan and ask where people are at the start and where they are at the end. If it's the same place, ask whether that's a decision or an oversight.""")

# ====================================== PART 5: GETTING IT RIGHT (25-30)
bullets(prs, "Reference is not cheating",
    ["It never was.",
     "Disney shot live action for the features.",
     "Every professional uses it."],
    """I want to kill this one properly because it costs students real quality.

Disney shot live action test footage for the features. Actors performed the scenes, the footage was projected, animators drew from it. That was not a shortcut somebody snuck in. That was the pipeline, at the studio that invented the pipeline.

Every professional uses reference. The ones who appear not to have simply looked at so much of it that it's in their head already, which is the same thing on a delay.

Photo reference, video, acting it out, shooting it on your phone. All encouraged, all professional practice, and none of it needs disclosing or apologising for.""")

bullets(prs, "Act it out",
    ["Stand up. Do the action.",
     "Notice what your body actually does.",
     "Best reference model available, and it's free."],
    """[LIVE: get the room standing. Sixty seconds. Give them one beat, you have just realised you left something important somewhere, and have everyone play it. Then sit and draw the pose they found.]

Everybody up.

What you will notice, every single time, is that your body does something you didn't predict. You expected a hand to the head. What actually happened was a stop, a half turn, and a hand that never made it up.

That gap between what you imagine a body does and what a body actually does is where stiff drawings come from. And you own the best reference model available to you. It's free, it's here, and it's the one nobody uses because they feel ridiculous.

Feel ridiculous. It's four seconds and it works.""")

bullets(prs, "Shoot it",
    ["Phone video.",
     "Scrub for the extreme.",
     "Draw from that frame."],
    """Same thing, recorded.

Do the action on your phone, then scrub through frame by frame and find the extreme. The moment where the pose is at its most legible, usually a bit earlier than you would guess.

That frame is your panel. Draw it.

And notice what you just did. You shot reference, found the key moment, and used it to plan a drawing. That is a videomatic, which is a real thing productions pay for, and you did it with a phone and no crew.""")

bullets(prs, "Mirror",
    ["For faces and hands specifically.",
     "Hands are the hardest thing to invent",
     "and the easiest thing to just look at."],
    """A mirror, for faces and hands.

Hands especially. Hands are the single hardest thing in figure drawing to invent from memory, and one of the easiest things in the world to look at. You have two of them, they're free, and they will hold any pose you ask.

Pull a face in a mirror before you draw one. Your own face does something more specific than the generic version in your head.""")

bullets(prs, "The acting checklist",
    ["What does this character want in this panel?",
     "Is there a line of action?",
     "Does the silhouette read?",
     "Is the weight believable?",
     "Is anything symmetrical that shouldn't be?",
     "Did I draw the face before the body?"],
    """This is on H6, which you're getting today. Run it before you call a pose finished.

Six questions, about twenty seconds. Same idea as the composition checklist. The value isn't that the questions are clever, it's that you actually ask them instead of assuming the answer.

The last one is the one people skip and the one that catches the most. If the face went down first, the pose was built around a decision you hadn't made yet. Start again. It costs two minutes and it usually fixes the panel.""")

bullets(prs, "Before you leave: one beat, three performances",
    ["Same character. Same shot size. Same moment.",
     "SHE REALISES SHE HAS BEEN LIED TO.",
     ("contained · explosive · collapsing", 1),
     "Nothing about the camera changes."],
    """Three panels. Same character, same framing, same moment. She realises she has been lied to.

Play it three ways. Contained: she takes it and gives nothing away. Explosive: it comes straight out. Collapsing: something goes out of her and the body follows.

Nothing about the camera changes. Same shot size, same angle, same distance. The only variable is the performance, which is the point. You have spent eight classes learning to change the camera. Today is about what you can change when the camera is fixed.

Post them before you leave.

[Before they go: the final and the pitch are both assigned today, briefs are up. Say why they land here rather than later, which is that this is the last lecture that can still change what they make.]""")

n = finish(prs, OUT, expected=30)
print(f"OK  {OUT}  {n} slides")
