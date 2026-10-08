#!/usr/bin/env python3
"""Session 2. The prompt as a brief.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/02_The_Prompt_as_a_Brief.pptx"

SPEC = [
("title", "The Prompt as a Brief", "AI Digital Imaging  |  Session 2",
"""**Running time, about 50 minutes.** Spot it and recall (7). A prompt is a brief (5). The five parts (15). Why vague words give averages (5). One variable at a time, worked example and cold reversal (8). The describe-and-sketch exercise (8). Options and close (2).

**Prep before class.** One flawed generated image for Spot it. Five versions of one prompt where only the lighting words change (lighthouse on a cliff works well, it's easy to read), saved as a strip. One film still for the describe-and-sketch exercise, kept hidden until the reveal; pick something with a strong, simple composition the room will probably recognize. A second still, unseen, for the cold reversal. The prompt log template, shared on Canvas.

Option B tonight needs a provided film still; post three on Canvas so nobody has to go hunting."""),

warmup("a generated image with an obvious problem or two (yours)",
       "Today is the first time we do this, so explain that it opens every class from now on."),

("bullets", "Last time",
["It starts from noise.",
 "Big shapes first, detail last.",
 'The "seed" makes each run different.'],
"""Thirty seconds of recall, out loud. [Cold call two people.] How does the generator make a picture? And why did your ten images come out different from each other?

What I want back: it starts from noise and removes it in steps, the words steer those steps, and every run starts from a different patch of noise, which is the seed.

Then one more question, and I'm curious rather than testing: from your ten, what never changed? [Take a few answers.] Usually it's the subject and the overall mood. Those are the words the system was listening to. Everything else, it made up. Today is about making up less of it."""),

("quote", "Today's idea", "A prompt is a brief.",
"People have been writing these for about a century.",
"""Here's the reframe for today, and I think it makes this whole activity a lot less mysterious.

A prompt is a **brief.** It's the same document an art director has handed to an illustrator, a photographer, a set designer or a concept artist, for about as long as those jobs have existed. Describe what you need precisely enough that someone who isn't you can make it.

The only thing that changed is the reader. The reader used to be a person who could ask you questions. Now it's a system that can't ask anything and will fill every gap you leave with the most average possible answer.

Which means the skill isn't "prompt engineering," whatever that is. It's art direction, and it's been taught for a long time."""),

("bullets", "What an art director hands over",
["What it is.",
 "How it should look.",
 "What has to be true.",
 "A picture of what they mean."],
"""When an art director briefs an illustrator for a book cover, say, they don't write "make it cool." Some of the things that end up in a real brief include: what the image is of, how it should look (the treatment, the mood, the light), what has to be true (the size, the format, where the title goes, what the client won't allow), and almost always a reference, a picture of what they mean.

That last part matters more than the rest put together. People who brief artists for a living know that words are a lossy way to describe a picture, so they show one.

Hold onto that, because at the end of today we're going to prove it to ourselves with an exercise, and next session and in week three we'll use reference images directly."""),

("boxes", "The five parts we'll use",
["Subject|who or what, doing what", "Composition|shot and angle", "Lens|wide or long",
 "Light|source, time, softness", "Style|medium and finish"],
"""For this course, a prompt has five parts. They're borrowed from film and photography because that's where the precise vocabulary already lives.

**Subject**, who or what, doing what. **Composition**, the shot size and the angle. **Lens**, wide or long, which changes how depth looks. **Light**, where it comes from, what time it is, hard or soft. **Style**, the medium and the finish.

You won't use all five every time. A fill that removes a trash can doesn't need a lens. But when you're generating a whole image, this is the list you go down, in roughly this order, and every part you leave out is a decision you've handed to the average."""),

("bullets", "Subject",
["Specific nouns, not categories.",
 '"A dog" or "an old wet greyhound"?',
 "Give it something to do."],
"""Subject first. The common mistake is to name a category instead of a thing.

"A dog" gets you the average dog, which is a golden-ish, medium-ish, friendly-ish dog facing the camera. "An old wet greyhound shaking off rain" gets you a decision: age, breed, condition, action.

The action part is easy to forget and it does a lot of work. A subject that's doing something has a pose, a direction, a reason to be in the frame. A subject that's just there tends to stand in the middle and look at you, which is the generator's default pose for everything.

[Ask the room for a vague subject, then make it specific together, out loud. One minute.]"""),

("bimage", "Composition",
["Wide, medium, close-up.",
 "High angle, low angle, eye level.",
 "Where in the frame?"],
"slot:two film stills, the same film: one wide shot, one close-up",
"""Composition. You already have most of this vocabulary from storyboarding or from film, so I'm only going to name it, not re-teach it.

Shot size: extreme wide, wide, medium, close-up. Angle: high, low, eye level, overhead. And placement: is the subject centered, off to one side, small in a big space?

These words work in prompts because the training images came with captions written by people who use them. "Low angle close-up" is something photographers and film people have been writing under pictures for a long time, so the system has seen it a lot.

One honest caveat: placement is where words are weakest. "Subject in the lower left third" is a request it may or may not honor. When placement really matters, you draw it, which is week three."""),

("image", "Lens", "lens_compare.png",
'Wide lens, close: depth stretches. Long lens, far back: it compresses. Say it in millimeters: "24mm," "85mm."',
"""Lens is the part most people leave out, and it changes the picture more than almost anything else.

This diagram is the same figure in the same hallway of pillars. On the left, a wide lens up close: the space looks deep, the pillars rush away from you. On the right, a long lens from far back: the same space looks flat and stacked, the pillars crowd together behind the figure.

A wide lens close to a face makes the nose big and the ears small. A long lens flattens it, which is why portrait photographers like something around 85mm.

The useful thing is that prompts understand millimeters, because camera metadata and photography captions are full of them. "24mm" and "85mm" are more precise than "wide" and "zoomed in," and the system has seen them thousands of times."""),

("image", "Light", "light_spheres.png",
"Same object, five lights. The words: overhead, golden hour, overcast, rim, practical.",
"""Light. This is the part I'd spend the most words on, if I could only spend words in one place.

Same sphere, five lighting setups. Noon, overhead and slightly cool. Golden hour, low and warm from one side with a long shadow. Overcast, soft, almost no shadow at all. Rim light from behind, where the object is mostly dark with a bright edge. And night with a warm "practical," which is a film word for a light source that's visible in the scene, like a lamp or a window.

Some of the words that tend to work include: golden hour, blue hour, overcast, hard light, soft light, rim light, backlit, practical light, single light source, light from camera left.

Notice they're all about **where the light comes from, what color it is, and how hard it is.** Those three questions are most of lighting. "Dramatic lighting" answers none of them."""),

("bullets", "Style",
["Name the medium: gouache, woodcut, 35mm.",
 "Name the finish: rough, clean, grainy.",
 "Describe the look. Don't name the artist."],
"""Last part, style. Name the medium and the finish. Gouache, ink wash, woodcut, oil on canvas, 35mm film, a phone photo, a 1990s game render. Rough or clean, grainy or smooth, saturated or muted.

Now a course rule, and I'll be upfront that it's a rule I chose. In this class, **don't put a living artist's name in a prompt.** Two reasons. One is about that artist: their name works as a shortcut because their work is in the training data, and they didn't agree to that. The other reason is about you. "In the style of" somebody is what you write when you don't know what you actually want. If you can describe the qualities you like, the palette, the line, the brushwork, the light, you have something better than a name: you have a direction you understand.

[Your call whether to keep this as a rule or as a recommendation. Either way, say why.]"""),

("section", "Why vague words give you averages", "",
"""Now the idea that ties the five parts together."""),

("quote", "Write this one down", '"Dramatic" is not a direction.',
"Neither is \"cool,\" \"epic,\" or \"beautiful.\"",
"""Vague words produce averages, because an average is the only honest answer to a vague request.

"Dramatic lighting" returns whatever dramatic lighting looks like across everything the model has ever seen, which is more or less a committee's idea of drama. "A single hard light from low camera left, the face half in shadow, the background falling to near black" returns a decision.

The same is true of "epic," "cool," "beautiful," "high quality," "masterpiece," and all the words people paste onto the end of prompts. Some of those did something in older tools. Mostly they just push everything toward the same glossy average, which is part of the "AI look" we'll name in session 4."""),

("section", "One variable at a time", "How to find out what a word is doing",
"""So how do you learn which words actually do something? The same way you'd test anything mechanical."""),

("bimage", "Change one word",
["Keep everything else identical.",
 "Change one thing.",
 "Now you know what that word does."],
"slot:your five versions of one prompt, only the lighting words changed",
"""If you've ever adjusted a rig, or tuned anything with more than one dial, you know this already. If you turn three dials at once and the result gets better, you have no idea which dial did it.

So: one prompt, held completely still, and you change one variable. Here, only the lighting words changed across five versions. [Walk through your strip. Read each prompt aloud.]

This is the worked example for today. Notice what changed beyond the light, because something always does: the composition shifts a little, the subject moves, the colors drift. That's the seed. With only one word changed, you can tell the difference between what the word did and what the noise did, more or less.

That's tonight's Option A, and the log is the deliverable as much as the images."""),

("image", "Now you try it backwards", "slot:a film still you haven't shown them, unlabeled",
None,
"""Cold reversal, and I'm not going to show you an answer.

Here's a still. Write the prompt that you think would get you close to it, using the five parts. Subject, composition, lens, light, style. Two minutes, on paper or in a text file.

[Give them two minutes. Then take three prompts aloud and put them on the board side by side. Don't say which is best.]

Look at where the three prompts agree and where they don't. Usually they agree on the subject and disagree on the light and the lens, which tells you which parts of the image are easy to see and which parts you're still learning to see.

That's also Option B tonight, done properly: describe a still, generate from your description, then compare."""),

("checklist", "The prompt log",
["The exact prompt, copied.", "What you changed from the last one.",
 "What it actually did.", "Keep or reject, and why."],
"""Every generation you keep for this course gets a line in the prompt log. The template is on Canvas.

Four columns. The exact prompt, copied, not paraphrased. What you changed from the previous one. What that change actually did, which is not always what you intended. And keep or reject, with a reason.

The reason column is the one that matters, and it's the one people leave blank. "Bad" isn't a reason. "Light comes from the right, brief says left" is a reason.

This log becomes part of your final project, so starting the habit now saves you rebuilding it from memory in week four, which never goes well."""),

("section", "Words are lossy", "An exercise",
"""Now an exercise, and it's the most fun part of today, so stay with me."""),

("bullets", "Describe and sketch",
["One person sees the image.",
 "Sixty seconds to describe it.",
 "Everyone else sketches. Two minutes."],
"""[About eight minutes in total. Pick a volunteer and show them the hidden still on your laptop or phone, not on the projector.]

Our volunteer has sixty seconds to describe this image out loud. Everyone else draws a quick thumbnail of what you hear, two minutes, boxes and stick figures are fine. The describer can't point or gesture, only talk.

[Run it. Then put a handful of sketches up next to each other, under the document camera or held up, and only then reveal the still.]

Look at how different these are from each other, and from the image. What got through? Usually the subject. What got lost? Usually where things are in the frame, how big they are, and which parts are dark and which are light.

That's exactly what happens to the generator. It's the room's sketchbooks, with your words."""),

("bullets", "What words can't carry",
["Exact placement.",
 "Exact faces and objects.",
 "The value pattern of the frame."],
"""So, the honest limits of a text prompt. Some of these include: exact placement in the frame, a specific face or a specific object (as opposed to a type), and the pattern of lights and darks that makes a composition work.

Words are good at **what** and fairly good at **how it looks.** They're bad at **where.**

That's not a problem to solve with longer prompts. Next session we'll see how the selection itself carries the "where," and in week three we'll get to reference images and drawings as input, which carry it much better than any sentence."""),

("bullets", "A few habits that help",
["Most important words first.",
 "Shorter often beats longer.",
 '"No people" can summon people.'],
"""Three practical habits, and I'll mark them as tendencies rather than laws, because each tool behaves a bit differently and they all change every few months.

Put the most important words **first.** Many systems pay more attention to the start of a prompt.

**Shorter often beats longer.** After a certain length, extra words start to fight each other and the result turns to mush.

And be careful with negatives. Writing "no people" puts the word "people" into the prompt, and some systems will happily give you people. Describe what you want there instead: "an empty street at dawn" rather than "a street with no people."

[Into the demo: build one prompt live, part by part, then run the lighting sweep.]"""),

("bimage", "In the wild: a holiday ad",
 ["A famous ad, remade with generators.",
  "The trucks change from shot to shot.",
  "What was missing from the brief?"],
 "slot:frames from the generated remake of a well-known holiday truck ad, 2024 or so",
"""[About five minutes.] Here's a real one most of you will have seen, or seen people arguing about. Around late 2024 or so, a very large soft drink company remade one of its famous holiday ads, the one with the lit-up trucks, using generators. The reaction online was rough, and a lot of it came from artists and animators.

[Show a few frames side by side.] Look at the trucks across these frames. Count the wheels. Look at the proportions of the cab. Look at the faces in the crowd.

Here's the question for the room, and it's the question for today: if you had been the art director, what would you have written into the brief that would have caught this? [Take answers. Push them toward specifics: the truck's design locked to a reference, number of wheels, the light.]

It's worth saying that a big, experienced team made this, with real budget. The tool didn't fail them so much as the checking did. Nobody in the chain said "the trucks don't match," or if they did, nobody listened."""),

("bullets", "A prompt, taken apart",
 ['"Old wet greyhound shaking off rain,"',
  '"low angle close-up, 85mm,"',
  '"overcast, soft light, muted gouache."'],
"""One full prompt, taken apart, so you can see the five parts in a real sentence.

"Old wet greyhound shaking off rain" is the **subject**, with an action. "Low angle close-up" is the **composition**. "85mm" is the **lens**. "Overcast, soft light" is the **light**. "Muted gouache" is the **style.**

It's short, about twenty words, and every word is doing a job. There's no "masterpiece," no "highly detailed," no "epic." If you can't say what a word is doing, take it out and see if anything changes. That's the one-variable rule used as an editing tool.

[Ask: which word would you change first if the result came back too cheerful? Let them argue: probably the light, maybe the style.]"""),

vocab([("Brief", "what it is, how it looks, what must be true"),
       ("Lens in mm", "24mm stretches depth, 85mm compresses it"),
       ("Practical", "a light source you can see in the scene"),
       ("Rim light", "light from behind, a bright edge"),
       ("One variable", "change one thing, learn what it does"),
       ("Prompt log", "prompt, change, result, keep or reject and why")]),

("options",
["Five versions of one prompt.", "Change only the lighting.", "Log every version."],
["Describe a provided film still.", "Generate from your description.", "Compare the two, side by side."],
"""Tonight, about 45 minutes to an hour either way, due at the start of next class.

**Option A**: the lighting sweep. One prompt, five versions, change only the lighting words, and fill in the log for each. Put the five in one layered file, named.

**Option B**: pick one of the three stills on Canvas. Describe it in words using the five parts, generate from your description, and put the still and your best result side by side in one file, with three sentences on what got through and what didn't.

Same rubric for both."""),

("quote", "One line to take home", "Vague words get you the average.",
"Specific words get you a decision.",
"""Vague words get you the average. Specific words get you a decision, and the decision is the part that's yours.

[Demo.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
