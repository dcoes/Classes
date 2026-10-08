#!/usr/bin/env python3
"""Session 1. What "generative" actually means.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, vocab

OUT = "AI Digital Imaging/lectures/01_What_Generative_Means.pptx"

SPEC = [
("title", 'What "Generative" Actually Means', "AI Digital Imaging  |  Session 1",
"""**Running time, about 50 minutes.** Open and the room poll (5). History, short (6). How it works (12, including the live ten-image look). What we have in the lab (5). The rules (8). The job market (8). The course and the options (6).

**Prep before class.** Run one prompt ten times in Photoshop and save all ten, unedited, as a single grid. Check that Generative Fill is actually live on the lab machines today (license, sign-in, credits). If it isn't, the grid you made at home carries the whole demo, so don't skip making it.

Images to drop into the slots: a daguerreotype (Daguerre's Boulevard du Temple works and is public domain), the National Geographic pyramids cover from 1982 or so, and a photo of a print coming up in a darkroom tray. Your ten-image grid goes on the ten-from-one slide."""),

("quote", "Let's start with the room", "Some of you think this is cheating.",
"That's allowed here.",
"""I want to start with this rather than end with it, because some of you walked in thinking it, and it would be strange to spend four weeks pretending you didn't.

Some of the best students I've had think these tools are a kind of cheating. Some of them think they are worse than that. Those are **reasonable positions**, they are held by working professionals, and nothing in this course asks you to give them up.

What I will ask is that you learn to see what these tools do and what they get wrong, because that part is useful whatever you decide about the rest. Several of the session options in this course are critical work rather than generating anything, and they are graded on the same rubric.

Staying skeptical is allowed. Staying uninformed is the only thing I'll push on."""),

("bullets", "Hands up",
["Used an image generator before?",
 "Avoid them on purpose?",
 "Haven't decided yet?"],
"""Quick show of hands, and nobody gets graded on this. [Do the three questions. Count out loud so the room hears itself.]

The point is just for all of us to see that the room is split, because it always is. Every time I've asked this, there's a group that uses these tools every day, a group that won't touch them, and a larger group in the middle who tried it once, got something weird, and moved on.

All three groups are going to be fine in here. The people who use it a lot will find out that a lot of what they've been accepting has problems in it. The people who avoid it will find out exactly what those problems are, which is a better argument than avoidance. And the middle will get to make up their minds with more information than they had this morning.

[Your story here, two minutes: the first time a generator surprised you, or disappointed you. Something specific. The room trusts the rest of the session more if it starts with a real thing that happened.]"""),

("section", "This has happened before", "A short history of tool panic",
"""Before we get into how the thing works, a few minutes of history. Not because history settles anything here, it doesn't, but because it's useful to know that artists have been through a version of this at least twice, and what actually happened to them."""),

("bimage", "1839 or so",
["Photography arrives.",
 '"From today, painting is dead."',
 "Painting changed jobs instead."],
"slot:a daguerreotype, e.g. Daguerre's Boulevard du Temple (public domain)",
"""Around 1839 or so, the daguerreotype shows up in Paris, and the painter Paul Delaroche supposedly looks at one and says, **"From today, painting is dead."** I say supposedly because historians aren't sure he actually said it. It's one of those quotes that's too good not to repeat.

What actually happened is more interesting. Portrait painters who made their living on likeness did lose work, quite a lot of it, and fairly quickly. Nevertheless painting didn't die. It changed jobs. Within a few decades you get the Impressionists, who are painting exactly the things a camera of that time couldn't do: light, movement, color, the feeling of a moment rather than the record of it.

And painters used photographs, constantly, almost from the start. Some of them hid it.

I'm not telling you this to say it'll all work out. Some people didn't come out of that well. I'm telling you because the question "what is the human part of this job" got asked then too, and the answer moved."""),

("bimage", "1990 or so",
['Photoshop arrives.',
 '"Photoshopped" becomes a verb.',
 "Nobody trusts a magazine cover again."],
"slot:National Geographic pyramids cover, 1982 or so (the pyramids moved closer)",
"""Second round. Photoshop 1.0 comes out around 1990, and within a few years "photoshopped" is a verb, and it isn't a compliment.

The cover here is from a little before that, 1982 or so, and it's National Geographic moving one of the pyramids at Giza closer to the other so the photo would fit a vertical cover. They did it with early digital retouching, people found out, and it became a famous embarrassment. The problem wasn't the tool. It was that **nobody said they'd done it.** Keep that in mind, because it's going to come back in a few minutes and again in week three.

Then around 2010 or so Photoshop adds Content-Aware Fill, which fills in a hole with something plausible, and people had more or less the same reaction you're hearing now. That feature is the direct ancestor of what we're using this month.

It is possible however, to argue that this time really is different, because of scale and because of where the training images came from. I think that's a fair argument. We'll give it a full session in week three."""),

("section", "What it's actually doing", "No magic, a lot of arithmetic",
"""Now the part that most people never get explained to them, which is how the thing actually works. I'm going to keep it mechanical and plain, because "artificial intelligence" is a word that makes this sound much more mysterious than it is. I put it in quotes on purpose. It's the field's word, and I'm not sure it's the right one."""),

("bullets", "It isn't a collage machine",
["It doesn't store pictures and paste them.",
 'It "learned" what things tend to look like.',
 "Then it builds new pictures from noise."],
"""First, the most common misunderstanding. A lot of people think a generator is a giant library of pictures, and when you type "a cat on a couch" it goes and finds some cats and some couches and cuts them together.

That isn't what happens. There's no library of stored images inside it. What there is, is a very large set of numbers that got adjusted, over a long training process, until the system was good at one specific job, which I'll show you in a second.

I put **"learned"** in quotes, because it isn't learning the way you learn. It doesn't know what a cat is. It knows, statistically, what pictures that were captioned "cat" tended to look like.

That difference, between knowing what something looks like and knowing how it works, is going to explain almost every mistake you see this month."""),

("image", "An image developed out of noise", "diffusion_strip.png",
"Each step removes a little of the noise, guided by the words.",
"""This is the mechanism, and it's called **"diffusion."**

The generator starts with pure noise, like television static. Then it runs a step that guesses which part of that static is "noise" and removes a little of it. Then it does that again, and again, often somewhere around thirty to fifty times. Each guess is steered by your words, so the static gets nudged, step by step, toward something that matches the description.

A note on this slide so I'm honest about it: I made this strip by adding noise to an old NASA photograph and showing it in reverse. A real generator doesn't start from a hidden photo. It starts from static and there's no picture underneath at all. The strip just shows you what the steps look like.

[Point at step 10 and step 20.] Notice when the big shapes arrive. The composition, the big lights and darks, the overall color, all of that gets decided early. The detail comes last. That's going to matter when we talk about why you can't fix composition by asking for more detail."""),

("bimage", "A print in a tray",
["The picture comes up slowly.",
 "Big shapes first, detail last.",
 "Except here, there's no negative."],
"slot:a photographic print coming up in a darkroom developer tray",
"""If you've ever seen a print come up in a darkroom tray, you've seen something quite close to this. The paper goes in blank, and the picture develops, the dark masses first and the fine detail last.

The analogy breaks in one place, and it's the important place. In the darkroom there's a negative. Light went through a real photograph and onto the paper, so the picture was already in there, waiting.

Here **there is no negative.** The picture never existed anywhere. It's being invented as it comes up, steered by the words, and by everything the system absorbed during training about what pictures with those words usually look like.

That's why two runs of the same prompt don't give you the same picture. There's no single picture in there to find."""),

("bullets", 'Training, in plain words',
["Millions of pictures with captions.",
 "Add noise, learn to remove it.",
 "Learn which words go with which looks."],
"""So where does the "steering" come from? Training.

Somebody collects an enormous number of images that have text attached to them, captions, alt text, descriptions. For some of the well-known open models that was around five billion image and text pairs, scraped from the public web. Then the system is shown those images with noise added, over and over, and adjusted until it gets good at predicting the noise so it can take it back out. Along the way it builds connections between words and visual patterns.

Notice what that means. Whatever is common in the training pictures, the model is good at. Whatever is rare, it's bad at. And whatever was in those pictures, including the work of living artists who were never asked, is somewhere in what it absorbed.

Adobe says Firefly, the model inside our Photoshop, was trained on licensed Adobe Stock images and public domain material rather than scraped web images. That's Adobe's claim, it's a better position than some, and not everyone accepts it at face value. That argument gets its own session in week three."""),

("bullets", "Why it fails where it fails",
["It knows what things usually look like.",
 "Not how they work.",
 "Hands, light, text: rules, not textures."],
"""Here's the payoff of all that, and it's the most useful idea in today's session.

The system is very good at **surface**: textures, materials, the general feel of a lighting style, what a forest or a city or a face usually looks like.

It's much worse at things that follow **rules**. A hand has five fingers and the joints only bend one way. Light comes from somewhere, so every shadow in a scene has to agree. A street has one horizon. A word is spelled one way. Those aren't textures, they're structure, and averaging a few million pictures doesn't give you structure reliably.

So the mistakes aren't random. They cluster around anatomy, light direction, perspective and lettering, and if you know that, you know where to look first. That's session 4, and it's the checklist you'll use for the rest of the course."""),

("bimage", "Same words, different answer",
["Every run starts from new noise.",
 'That starting noise is the "seed."',
 "Nothing is broken. That's the design."],
"same_prompt_three_tries.png",
"""This is a simple illustration rather than real output, but it's the idea. Same request, three tries, three different answers.

Each run starts from a different patch of random noise, and that starting noise is called the **seed.** Different seed, different picture. Some tools let you fix the seed so you can repeat a result. Photoshop mostly doesn't show it to you, it just gives you three variations each time.

Students sometimes take this as the tool being broken, or as proof that it's random and therefore no skill is involved. Neither is quite right. The variation is the design, and it's also where your job starts, because somebody has to look at the three and choose, and say why."""),

("image", "Ten from one prompt", "slot:your grid of ten images from one prompt, unedited, all ten kept",
None,
"""[LIVE, about five minutes. Put up your ten-image grid. If Generative Fill is working in the lab, run the same prompt once more live so they see it come in.]

Here's one prompt, run ten times, and I kept every one of them, including the bad ones.

Two questions for the room, and I want answers out loud. **What changed** between them? And **what never changed**?

[Let them answer. Push for specifics. Usually what never changes is the general subject, the overall mood, often the lighting style and the palette. What changes is the composition, the pose, the camera angle, the small details, and how many things went wrong.]

That's your Option A tonight, done yourself with your own prompt. Notice that the useful part of the exercise isn't the images. It's the list you make of what moved and what held still, because that list tells you which words in your prompt the system is actually listening to."""),

("section", "What we have in this room", "Inside Photoshop, nothing to install",
"""Now, practically, what we're going to use, and what we aren't."""),

("bullets", "The tools this month",
["**Generative Fill** – inside a selection.",
 "**Generative Expand** – past the edge of the frame.",
 "**Reference images** – show it, don't describe it.",
 "All inside Photoshop. No outside accounts."],
"""Everything in this course happens inside Photoshop, using the generative features that come with it.

**Generative Fill** works inside a selection. You select an area, optionally type something, and it generates three options for that area on their own layer. **Generative Expand** is the same idea past the edge of the canvas, which is how you change an aspect ratio. And **reference images** let you hand it a picture instead of a paragraph, which, as you'll see, oftentimes works better than words.

Photoshop's menu here changes every few months. As of this term there may be more than one model in the dropdown (Adobe's Firefly, plus some partner models from other companies), and features get added and renamed. What's actually on our lab license is what we use. [Check this the week before the course runs, and say what you found.]

If the generative features are down on a given day, and that happens, I'll have image sets ready so nobody's work stops."""),

("bullets", "What's not on the menu",
["No installs, no sign-ups.",
 "Local models and node workflows: I run those.",
 "You get the output as image sets."],
"""There's a whole world of these tools outside Photoshop, some of them quite powerful, and some of them run on your own computer with a lot of setup. I use some of those at home.

We're not doing that here, on purpose. Installs, accounts, subscriptions and graphics card requirements are exactly where a class like this falls apart, and it would turn the course into IT support rather than image making.

So where the course needs something those tools do well, like controlling a pose or the depth of a scene (week three), I'll run it at home and bring you the results as image sets. You'll work with the output. **The decisions stay with you**, which is the point anyway."""),

("section", "The rules", "Three of them, and they don't change",
"""Three rules for the month. They're short, they apply to every assignment, and they're the reason nobody in this room needs to worry about being accused of anything."""),

("bullets", "The process record",
["A dated, layered .psd.",
 "Named layers, every time.",
 "The chain of work is what gets graded."],
"""Rule one. Every submission is a **dated, layered Photoshop file with named layers.** Not a flattened JPEG. The file, with the steps in it.

So the generated layer is in there, named as generated. Your correction is on its own layer, named for what it fixes. "Fix hand" or "Repaint shadow left" rather than "Layer 37 copy 2". Somebody opening your file should be able to read what you did, more or less like reading a recipe.

This takes about thirty extra seconds per layer, and it's the most important habit in the course."""),

("quote", "What that means for you",
"You won't be accused of anything based on how something looks.",
"Your grade rests on whether the chain of work exists.",
"""Here's why that rule exists. You will not be accused of anything here based on how something looks. Nobody's grade rests on my judgment about whether an image "looks AI." I can't reliably tell, and honestly nobody can, including the detection tools that claim to.

What I can see is whether the chain of work exists. Brief, choices, corrections, each one on a layer, each stage coming out of the one before it.

That's also how the final project works, in milestones. A final submitted without its milestones is capped at Average, whatever it looks like. That's not a punishment, it's arithmetic: skipping the process just doesn't pay."""),

("bullets", "Disclosure, from day one",
["What was generated.",
 "What you made.",
 "Said plainly, without being asked."],
"""Rule two. You say what was generated and what you made, plainly, every time, without anyone having to ask. Remember the pyramids. The problem wasn't the retouching, it was the silence.

For most assignments that's one or two sentences in the submission. For the final it's a short disclosure statement, and we'll look at how professionals actually do this in session 9.

Photoshop also attaches something called **Content Credentials** to some generated images, a kind of tag in the file that records that a generator was used. That's useful, but it isn't a substitute for you saying it. Tags get stripped. Sentences don't."""),

("bullets", "The skeptic's route",
["Several options are critical work.",
 "Same rubric, same weight.",
 "You can finish this course skeptical."],
"""Rule three is really a promise. Many sessions in this course have an option that asks for critical work instead of generating something: ranking outputs against a brief, marking up errors, writing an argument, correcting someone else's generated image by hand.

Those options are graded on the same session rubric as the others. Choosing them is about how you like to work, not about which one earns more.

You can finish this course still skeptical of all of it. I'd just like you to be skeptical with more evidence than you have today."""),

("section", "Where this sits in the job market", "Plainly",
"""Last big piece today, and I'd rather be straight with you about it than reassuring."""),

("image", "What working developers think", "gdc_chart.png",
"Same survey, three years. 36% of these developers use generative tools at work anyway.",
"""This is from the Game Developers Conference's yearly survey of people working in games, a bit over 2,300 of them in the most recent one, released early in 2026.

The share who say generative AI is having a **negative impact** on the industry went from 18% to 30% to 52% in three years. Among people in visual and technical art, people more or less like you will be, it's around 64%. At the same time, about a third of them use these tools at work anyway. And roughly 28% of the people surveyed had been laid off at some point in the previous two years, for many reasons, not only this one.

So the honest picture is this: the industry is using these tools and largely doesn't like it. Entry-level image making, the kind of work that used to be how juniors got in, has contracted.

I'm not going to tell you the field is fine. I'm going to tell you which half of the job is durable, and then train you in it.

[Ask: does this match what you've heard from people working? Take two or three answers.]"""),

("bullets", "What still costs money",
["Knowing what you want.",
 "Seeing what's wrong.",
 "Fixing it by hand.",
 "Saying what you made."],
"""Here's the durable half, as best I can tell, and I want to mark it as a belief rather than a fact, because nobody knows how this goes.

**Knowing what you want**, which means a brief, references, decisions made before anything is generated. **Seeing what's wrong**, which means a trained eye that catches the hand, the shadow, the horizon. **Fixing it by hand**, because the last ten percent of almost every generated image is still paint, clone and liquify. And **saying what you made**, honestly, so a client or a studio can actually use your work.

In my experience these tools are most useful in the hands of people who already know something about what they're trying to achieve. They make a skilled person faster. They don't make an unskilled person skilled, and the gap shows.

That's the whole course in four lines. The tool is a means of expression, and the person using it is not an operator."""),

("boxes", "The month",
["Week 1|What the tools do", "Week 2|Correcting and combining",
 "Week 3|Briefs, control, ownership", "Week 4|Finishing"],
"""The four weeks, quickly.

Week one is what the tools do: prompting as a brief, Fill and Expand, and how to judge what comes back. Week two is fixing it by hand, keeping things consistent, and compositing generated parts into real photographs, with Project 1 due at session 7. Week three is the brief, control, and the ownership and copyright question. Week four is type, presentation, and finishing the final.

Every session runs the same way: a lecture like this one, a demo, lab time with me walking the room, and a quick look at work before you leave.""",
{"sub": "Project 1 due session 7. Final project in milestones: sessions 10, 12, 14, then 16."}),

("two", "Two projects",
["**Project 1: The Fix-It Set**",
 "Three flawed images, fixed by hand.",
 "Due session 7."],
["**Final: Art-Directed Series**",
 "Three or four images, one brief.",
 "Milestones at 10, 12, 14."],
"""Two projects.

**Project 1, the Fix-It Set**, due session 7. I give you three generated images with problems in them and a short written brief for each. You find the problems, and you fix them by hand, every correction on a named layer.

**The final, an Art-Directed Series**, due session 16. Three or four images for one brief, say key art for a game or chapter headers for a book, that look like they belong together: same character, same place, same light. It comes with the brief, a reference board, a prompt log, the images you rejected, the hand corrections, and a disclosure statement.

The final runs in milestones: brief and reference board at session 10, a rough set at 12, a corrected set at 14. As I said, a final without its milestones is capped at Average."""),

vocab([("Diffusion", "an image built up out of noise, step by step"),
       ("Seed", "the random starting noise for one run"),
       ("Training data", "the captioned pictures it learned from"),
       ("Process record", "your dated, layered, named file"),
       ("Disclosure", "saying what was generated and what you made"),
       ("Content Credentials", "a tag in the file, not a substitute for you")]),

("options", ["Generate ten images from one prompt.", "Keep all ten.", "Note what changed and what didn't."],
["About 150 words:", "one thing these tools are good for,", "one thing they shouldn't be used for."],
"""Tonight's options, due at the start of next class. About 45 minutes to an hour either way.

**Option A**: one prompt, ten generations, keep all ten in one layered file. Then a short list, what changed between them and what stayed the same. Same thing we did on the screen.

**Option B**: about 150 words. One thing you think these tools are genuinely good for, and one thing you think they shouldn't be used for. I mean your actual opinion. If your answer to the first half is "nothing," then make the case for that, specifically.

Both are graded on the same session rubric. Whatever you submit goes in a dated file."""),

("quote", "One line to take home",
"The machine makes candidates.",
"Somebody still has to decide.",
"""If you keep one thing from today: the machine makes candidates. Somebody still has to decide which one, and why, and what's wrong with it, and how to fix it.

That somebody is you, all month. [Into the demo.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
