#!/usr/bin/env python3
"""Bridge lecture: Making Images with AI.

One self-contained lecture with hands-on work, written to drop into any Photoshop
course on any day. It does not refer to other sessions, projects or milestones,
and it does not re-teach value, perspective or light. Students need no accounts:
the hands-on parts run on the instructor's account on the projector.

Run from the repo root.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, vocab
import aikit2  # noqa: F401  (registers the visual slide types)

OUT = "AI Digital Imaging/bridge_lecture/Making_Images_with_AI.pptx"

SPEC = [
("title", "Making Images with AI", "How it works, how to talk to it, and where you still matter",
"""**What this is.** A self-contained lecture with two hands-on activities, written to drop into any Photoshop course on any day. It doesn't depend on anything taught before it, and nothing after it depends on it.

**Running time.** About 55 minutes of talk and about 35 minutes of hands-on, so it takes most of a session. In order: a little history (8), how the machine works (6), models (6), talking to the machine (12), describe and sketch (8), beyond words (8), consistency (9), upscaling (5), the human in the loop and ownership (7), the prompt relay (25), wrap up (2).

**Short version, about 50 minutes in total.** Skip the darkroom tray, rented or owned, the prompt log, and "context or training" (fold them into what you say around them). Run the relay with two rounds instead of three.

**Prep.**
- Your Photoshop (or Firefly) account signed in on the projector machine, with generative features working. Test it that morning.
- Three target images for the prompt relay: simple, readable pictures (a photo you took, or something you generated earlier). Print them or put them on Canvas so each team can see theirs.
- One film still, hidden, for describe and sketch.
- Two upscale examples of your own if you have them, one faithful and one creative.
- The images for the slots, listed in the prep sheet.

**If the lab license allows student generation,** let teams run their own prompts in the relay. If not, you run them, which works fine and keeps everyone looking at the same screen."""),

# ------------------------------------------------------------------ history
("timeline", "This has happened before",
 [("1804", "Jacquard loom", "Patterns stored on punched cards"),
  ("1811", "The Luddites", "Weavers break the machines used against them"),
  ("1839", "Photography", "A machine makes the likeness"),
  ("1843", "Lovelace's notes", "What a machine can and can't originate"),
  ("1990", "Photoshop", "\"Photoshopped\" becomes a verb"),
  ("2022", "Image generators", "Public, cheap, everywhere")],
"""I'd like to start somewhere other than the technology, because I think the history explains the mood in this room better than any feature list does.

Every one of these dates is a moment where a machine started doing part of a skilled person's job, and every one of them came with the same mix of excitement, fear and contempt you hear now. That doesn't mean it'll turn out the same way this time. It means the questions aren't new, and some of the answers people found back then are still useful.

[Walk the timeline left to right in about a minute, then go into the next three slides.]""",
 {"highlight": 5}),

("bimage", "The loom that read cards",
 ["1804: patterns stored on punched cards.",
  "Any pattern, without a master weaver.",
  "The cards later inspired early computers."],
 "slot:a Jacquard loom, or a stack of its punched cards (public domain engravings and photos are easy to find)",
"""Around 1804, Joseph Marie Jacquard built a loom that wove complicated patterns by reading a chain of punched cards. Each card was one row of the pattern: a hole meant a thread was lifted, no hole meant it wasn't. A pattern that used to need a highly skilled weaver could now be "stored" and run by someone with much less training.

Two things worth noticing. The **skill moved**: somebody still had to design the pattern and punch the cards, and that became a job of its own. And this machine is, in a sense, a direct ancestor of the one we're talking about today. Charles Babbage borrowed the punched card idea for his Analytical Engine in the 1830s or so, and that's the machine Ada Lovelace wrote about. We'll get to her in a minute."""),

("bimage", "The Luddites",
 ["Skilled textile workers, 1811 or so.",
  "They broke frames and looms.",
  "The fight was over wages and control."],
 "slot:an engraving of the Luddites or 'General Ludd' from around 1812 (public domain)",
"""Then, around 1811, in the textile towns of the English Midlands, groups of workers started breaking into workshops at night and smashing machines. They signed their letters "General Ludd," and we got the word Luddite.

Today the word means someone who hates technology. A lot of historians would say that's not quite fair to them. Many were skilled machine operators themselves. What they were fighting was **how** the machines were being used: to replace trained workers with cheap, untrained ones, to cut wages, and to make worse cloth faster. The government's answer was to make machine breaking punishable by death in 1812, and send soldiers.

I bring this up because I think a lot of the anger at image generators right now is closer to the Luddites' actual complaint than to "technology bad." It's about who benefits, who gets paid, and whose work was used to build the machine. That's a fair question, and it's allowed in this room."""),

("bimage", "1839: photography",
 ["\"From today, painting is dead.\"",
  "Portrait painters did lose work.",
  "Painting changed its job instead."],
 "slot:an early daguerreotype, e.g. Daguerre's Boulevard du Temple, 1838 (public domain)",
"""Closer to home. Around 1839 photography arrives, and the painter Paul Delaroche supposedly says "from today, painting is dead." Historians aren't sure he said it, but people certainly felt it.

Portrait painters, whose living was likeness, did lose work, and fairly quickly. Painting didn't die. It changed its job: within a few decades the Impressionists were painting exactly what the cameras of the time couldn't do, and painters were quietly using photographs as reference, some of them secretly.

Both things are true at once, and I think that's the honest way to look at what's happening now: real people lost real work, and the medium found a new reason to exist."""),

("cards", "What's the same this time, and what isn't",
 [("The same", ["A machine takes over part of a skilled job.",
                "The skill moves rather than vanishing.",
                "Fear and contempt, on both sides."]),
  ("Not the same", ["It learned from the work of the people it competes with.",
                    "It spread in months, not decades.",
                    "Anyone can use it, with no training."])],
"""So, what's the same and what isn't. I'll mark this as my own reading.

**The same**: a machine taking over part of a skilled job, the skill moving somewhere else (pattern designers, photographers' printers, retouchers), and a lot of fear and contempt in both directions.

**Not the same**, and this is why I don't think "it'll be fine, it always is" is a good enough answer: these systems were trained on the work of the very people they now compete with, mostly without asking. It happened in a couple of years, not a couple of generations. And it needs no training to use, which is both the appeal and the problem.

It is possible to argue that the second column makes this different in kind, not just degree. I think that's a reasonable argument, and I don't think anyone knows yet."""),

("quote", "Ada Lovelace, 1843, on Babbage's Analytical Engine",
 "\"It can do whatever we know how to order it to perform.\"",
 "\"The Analytical Engine has no pretensions whatever to originate anything.\"",
"""Ada Lovelace, writing in 1843 about Babbage's machine, the one with the punched cards. Her full sentence is: "The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform."

Not all agree that this still holds. Alan Turing argued with it directly in 1950 (he called it "Lady Lovelace's Objection"), and modern generators do surprise the people who build them.

Nevertheless, for anyone actually trying to make an image, the second half of her sentence is the practical part: **it can do whatever we know how to order it to perform.** Most of today is about getting better at ordering it."""),

# ------------------------------------------------------------------ how it works
("section", "How the machine makes a picture", "",
"""Briefly, how the thing works. I'll keep it mechanical."""),

("bullets", "It isn't a collage machine",
 ["No stored pictures inside it.",
  "It \"learned\" what captioned pictures tend to look like.",
  "It builds new pictures out of noise."],
"""The most common misunderstanding: people think a generator is a big library of pictures it cuts and pastes together. It isn't. There are no stored images in there. There's a very large set of numbers, adjusted during training until the system got good at one job.

I put "learned" in quotes. It doesn't know what a dog is, or what light is. It knows, statistically, what pictures captioned "dog" or "sunset" tend to look like. That's the difference between knowing how things look and knowing how they work, and it explains most of its mistakes."""),

("image", "An image developed out of noise", "diffusion_strip.png",
 "Each step removes a little noise, steered by the words. Big shapes arrive first, detail last.",
"""This is the mechanism, called "diffusion." It starts from pure noise, like static, and removes a little of it, step by step, often thirty to fifty times, each step nudged by the words toward something that matches.

To be honest about the slide: I made this strip by adding noise to an old NASA photo and showing it backwards. A real generator starts from static with no picture underneath.

Notice what arrives first: the big masses, the composition, the overall color. Detail comes last. That's why asking for "more detail" never fixes a composition: the composition was decided in the first few steps."""),

("bimage", "A print in a tray, with no negative",
 ["The picture comes up slowly.",
  "Big shapes first, detail last.",
  "But the picture never existed."],
 "slot:a photographic print coming up in a darkroom developer tray",
"""[Short version: skip this slide.]

If you've ever watched a print come up in a darkroom tray, that's close to what it looks like. Except in the darkroom there's a negative: a real moment, already captured. Here there's no negative at all. The picture is invented as it develops. That's why the same prompt never gives the same picture twice."""),

("cards", "Two things that shape every result",
 [("Training", ["Billions of captioned images.",
                "Mostly collected from the web.",
                "Whatever was common, it does well. Whatever was rare, it does badly."]),
  ("The seed", ["Every run starts from new random noise.",
                "New seed, new picture.",
                "Some tools let you fix the seed to repeat a result."])],
"""Two things shape every result.

**Training**: the model's habits come from what it was trained on. Common things, it does well. Rare things, specific things, things that follow strict rules, it does badly. And whose images were in there is the heart of the legal and ethical argument we'll touch on at the end.

**The seed**: the random noise each run starts from. Different seed, different picture, same words. That's not the tool being broken, it's the design. Some tools let you see and fix the seed so you can repeat a result exactly, which matters later when we talk about consistency."""),

# ------------------------------------------------------------------ models
("section", "Models", "Different machines, different habits",
"""Now, which machine. People say "AI" as if it were one thing. It's a lot of different models, and they behave differently."""),

("cards", "Some models you'll run into",
 [("Firefly (Adobe)", ["Inside Photoshop and on the web.", "Trained on licensed images, per Adobe.", "Tags its output with Content Credentials."]),
  ("Midjourney", ["A strong \"look\" by default.", "Style and character references.", "Its own website and app."]),
  ("Chat-based", ["Gemini, ChatGPT and others.", "You edit by talking to it.", "Often better with text and instructions."]),
  ("Open models", ["Flux, Stable Diffusion and others.", "Run on your own computer.", "You can train your own add-ons."])],
"""A model is, more or less, a set of habits. Each one learned from different pictures, in a different way, so each one has a different idea of what "average" looks like. That's why the same prompt looks so different from one tool to another.

Some of the ones you'll run into include: **Firefly**, Adobe's, which is the one inside our Photoshop, trained on licensed and public domain images according to Adobe. **Midjourney**, which has a strong look of its own and good tools for references. **Chat-based** image tools like Google's Gemini and OpenAI's ChatGPT, where you edit by having a conversation, and which tend to follow instructions and handle lettering better than most. And **open models** like Flux and Stable Diffusion, which you can run on your own machine and extend.

This list changes every few months. Photoshop itself now offers some partner models in its dropdown. [Check what's current, and say which ones you've actually used and what you thought.]"""),

("cards", "Rented or owned",
 [("Rented", ["Runs on someone else's servers.", "Their rules, their filters, their prices.", "Nothing to install. Works on a lab machine."]),
  ("Owned", ["Runs on your own computer.", "Your rules, your add-ons, your training.", "Needs a strong graphics card and an afternoon of setup."])],
"""[Short version: skip this slide.]

The practical difference between them. **Rented** tools run on a company's servers: easy, nothing to install, but you live with their content rules, their pricing, and their changes. **Owned** tools run on your computer: much more control, including training your own add-ons, but they need a strong graphics card and some patience to set up.

Everything we do in the lab is rented. The things I do at home, with node-based tools like ComfyUI, are owned. Neither is better in general. It depends on how much control you need."""),

("cards", "Three ways of working",
 [("Text to image", ["Words in, picture out.", "Fast, and you give away the most decisions."]),
  ("Edit an image", ["Your picture in, part of it changed.", "Fill, expand, image to image."]),
  ("Conversation", ["Talk to it, one change at a time.", "\"Make it night. Keep everything else.\""])],
"""Three ways of working, and most people only know the first.

**Text to image**: type, get a picture. The fastest, and the one where the machine makes the most decisions for you. **Editing an image**: you bring a picture, a photo or a painting, and it changes part of it: Generative Fill inside a selection, Expand past the edge, or reworking the whole image a little or a lot. **Conversation**: newer chat-based tools let you edit by talking to them, one change at a time, and they remember the image between turns.

For a painter, the second one is usually the most useful, because your picture is doing most of the work."""),

# ------------------------------------------------------------------ prompting
("section", "Talking to the machine", "Prompting, without the mystery",
"""Now the main part: how do you talk to the machine so it makes what you want?"""),

("statement", "A prompt is a brief",
 "A prompt is a brief, for a reader who can't ask you questions.",
 "Art directors have written briefs for illustrators and photographers for about a century. The difference is that a person asks what you meant. A generator fills every gap with the average.",
"""Here's the reframe that I think makes prompting a lot less mysterious. A prompt is a **brief**, the same document art directors have handed to illustrators and photographers for about a century: what it is, how it should look, what must be true.

The only real difference is the reader. A person reads your vague brief and calls you to ask what you meant. A generator can't ask anything. It fills every gap you leave with the most average possible answer.

So the skill isn't "prompt engineering," whatever that is. It's being specific, which is something art directors have been teaching for a long time."""),

("rows", "What goes in a prompt",
 [("Subject", "Who or what, doing what. Specific nouns."),
  ("Composition", "Shot size, camera angle, where in the frame."),
  ("Lens", "In millimeters: 24mm stretches depth, 85mm flattens it."),
  ("Light", "Where it comes from, what time it is, hard or soft."),
  ("Style", "The medium and the finish: gouache, woodcut, 35mm film.")],
"""Five parts, borrowed from film and photography. They work because the training images came with captions written by people who use exactly this vocabulary.

**Subject**: specific nouns and an action. **Composition**: wide or close, high or low angle, where in the frame. **Lens**: in millimeters, because camera metadata is full of them. **Light**: where it comes from, what time it is, hard or soft. **Style**: the medium and the finish: gouache, woodcut, 35mm film, a phone photo.

You won't use all five every time. A fill that removes a trash can doesn't need a lens. But every part you leave out is a decision you've handed to the average."""),

("prompt", "A prompt, taken apart",
 [("An old wet greyhound shaking off rain,", "Subject"),
  ("low angle close-up,", "Composition"),
  ("85mm,", "Lens"),
  ("overcast soft light,", "Light"),
  ("muted gouache, visible brushwork", "Style")],
"""Here's one, taken apart, so you can see the five parts in an actual sentence.

"An old wet greyhound shaking off rain": subject, with a specific animal, a condition and an action. "Low angle close-up": composition. "85mm": lens. "Overcast soft light": light. "Muted gouache, visible brushwork": style.

About twenty words, and every one is doing a job. There's no "masterpiece," no "highly detailed," no "epic." Compare that to "a cool dog picture, dramatic lighting, 8k," which tells it almost nothing.

[If there's time, ask the room which word they'd change first if the result came back too cheerful, and why. Usually it's the light or the style.]""",
 {"caption": "About twenty words, and every one decides something."}),

("cards", "Words that fill space, words that decide",
 [("Fill space", ["masterpiece, 8k, ultra detailed", "epic, stunning, beautiful", "dramatic lighting, cinematic"]),
  ("Decide", ["low from camera left", "85mm, overcast, blue hour", "gouache, wet, mid-shake"])],
"""Vague words produce averages, because an average is the only honest answer to a vague request.

"Dramatic lighting" gets you whatever dramatic lighting looks like across everything the model has seen, which is a committee's idea of drama. "A single hard light low from camera left, the face half in shadow" gets you a decision. Words like "masterpiece" and "8k" did something in some older tools. In most current ones they mostly push everything toward the same glossy look people now recognize as "AI."

A good test: if you can't say what a word is doing, take it out and see if anything changes."""),

("cards", "Habits that help",
 [("Order", ["Put what matters most first.", "Many models weigh the start more."]),
  ("Length", ["Short often beats long.", "Past a point, words fight each other."]),
  ("Negatives", ["\"No people\" can summon people.", "Describe what's there instead: \"an empty street at dawn.\""])],
"""Three habits, and I'll mark them as tendencies rather than laws, because each model behaves a bit differently and they change.

**Order**: put the most important words first. **Length**: shorter often beats longer; past a certain point extra words start to fight each other and you get mush. **Negatives**: writing "no people" puts the word "people" into the prompt, and some models will happily give you people. Describe what you want there instead. (Some tools have a separate "negative prompt" field, which is a different thing and works better.)"""),

("cards", "Talking to a conversational model",
 [("Turn 1", ["\"A lighthouse on a cliff at dusk, wide shot, painterly, muted colors.\""]),
  ("Turn 2", ["\"Keep everything the same. Make the sky stormy.\""]),
  ("Turn 3", ["\"Same image. Move the lighthouse to the left third of the frame.\""])],
"""Chat-based image tools want a different style of talking. Full sentences, the way you'd brief a person. And then, instead of rewriting the whole prompt, you **change one thing per turn**, and you say out loud what has to stay the same.

"Keep everything the same, make the sky stormy" is the most useful sentence in this kind of tool. Without the first half, it often redraws the whole picture.

The habit underneath is the same as before: one change at a time, so you know what each change did."""),

("image", "One variable at a time", "light_spheres.png",
 "Same prompt five times, only the light words changed. Hold everything else still.",
"""Which brings us to the most important habit of all. If you change three things in a prompt and the picture improves, you have no idea which change did it. It's the same as adjusting a rig, or any machine with more than one dial: you turn one dial at a time.

So: hold the prompt completely still, change **one** word or phrase, and look at what moved. This strip is an illustration I made, the same object with only the light changed. With a real generator, some other things will shift too because of the seed, and comparing tells you what the word did and what the noise did, more or less.

That's also exactly what you'll do in the relay at the end."""),

("checklist", "Keep a prompt log",
 ["The exact prompt, copied", "What you changed from the last one",
  "What it actually did", "Keep or reject, and why"],
"""[Short version: mention it in a sentence and skip the slide.]

When you're working seriously, keep a log. Four columns: the exact prompt, what you changed, what that actually did (which is not always what you meant), and keep or reject with a reason. "Bad" isn't a reason. "Light comes from the right, I wanted left" is.

The log is how you get better at this instead of just busier. And it's your record of what was generated, which matters when someone asks."""),

# ------------------------------------------------------------------ hands-on 1
("section", "Hands-on: describe and sketch", "About eight minutes",
"""Now a game, and it proves something about prompting better than I can explain it."""),

("bullets", "Describe and sketch: how it works",
 ["One person sees a picture. Nobody else does.",
  "Sixty seconds to describe it. No pointing.",
  "Everyone else thumbnails it in two minutes."],
"""[Show the hidden still to one volunteer only, on your laptop or phone.]

Our volunteer has sixty seconds to describe this picture out loud, no pointing, no gestures. Everyone else draws a quick thumbnail of what they hear, two minutes, boxes and stick figures are fine.

[Run it. Then hold up several thumbnails side by side, or put them under the document camera, and only then reveal the still. Leave the next slide hidden until after the reveal.]"""),

("cards", "What survives a description",
 [("Usually gets through", ["The subject.", "The mood.", "The main colors."]),
  ("Usually lost", ["Where things are in the frame.", "How big they are.", "Which parts are dark and which are light."])],
"""[After the reveal.] What got through? Almost always the subject, the mood, the main colors. What got lost? Where things were, how big they were, and the pattern of lights and darks: the composition.

That's exactly what happens when you describe a picture to a generator. Words carry **what** quite well, and **where** very badly. Your sketches are what the machine does with your words.

So if words can't carry "where," what can? That's next."""),

# ------------------------------------------------------------------ beyond words
("section", "Beyond words", "Other ways to tell it what you mean",
"""How to give the machine more than words."""),

("ladder", "The ladder of control",
 [("Words", "what it is"),
  ("Reference image", "how it looks"),
  ("Rough paint", "roughly where"),
  ("Structure input", "exactly where"),
  ("Trained add-on", "always this character or style")],
"""A ladder, from least control to most. **Words** say what. A **reference image** says how it should look. **Rough paint** under a generated fill says roughly where things go. A **structure input**, a drawing or a map the model has to follow, says exactly where. And a **trained add-on** makes it produce one particular character or style every time, which we'll get to under consistency.

Each step up, you supply more of the decision and less of it gets made for you. The people who get the best results from these tools are almost all near the top of this ladder. And notice that a painter is already halfway up it."""),

("image", "Four kinds of structure input", "control_inputs.png",
 "A sketch locks layout. A pose locks gesture. A depth map locks space. An edge map locks almost everything.",
"""Four kinds of structure input. All of these were made for this slide; the last one was traced automatically from an old NASA photo.

A **sketch**: your layout and shapes. A **pose**: a stick-figure skeleton (the colors tell left from right). A **depth map**: near is light, far is dark. An **edge map**: traced outlines. In node-based tools the part that reads these is often called a "ControlNet," a name from a research paper in 2023 or so. I put it in quotes; it really just means "structure guidance."

Each one locks something different and leaves the rest to the model. 3D students: a depth map is exactly the depth pass you can render out of Maya, so a rough 3D blockout is one of the best inputs there is."""),

("image", "ID maps work too", "id_map_pair.png",
 "One flat color per object or material, the same idea as a Substance color ID map.",
"""Some of you have seen this kind of image in Substance: a **color ID map**, one flat color per material or object, used to make selections fast. It works with generators too, in two ways.

The simple way, which works in Photoshop today: use the ID map to **select one region at a time** (Magic Wand or Select Color Range on the ID layer), then run Generative Fill on just that region with its own prompt. "Weathered stone tower" in the yellow, "dry grass" in the brown. Each part gets its own instructions, and the layout can't drift. People call this regional prompting.

The more technical way, in node-based tools: some structure inputs read a "segmentation" map, which is the same idea, except the model expects specific colors for specific things, so you recolor your IDs to its color code.

Either way, it's the same discipline as in Substance: decide the parts first, then fill them."""),

("slider", "How much it's allowed to change",
 "Keep my picture", "Invent freely",
 [(0.18, "Low", "Surface and texture change. Your drawing survives."),
  (0.5, "Middle", "Forms get redrawn. Layout stays."),
  (0.85, "High", "Only the rough idea of your picture survives.")],
"""When you give the generator your own image to work from, there's usually a setting for how much it may change it. It goes by different names, "strength," "denoise," "variation" or "creativity," but it's the same dial.

At the **low** end it keeps your picture and changes surface: texture, rendering, small details. In the **middle**, it redraws the forms but keeps your layout. At the **high** end, only the general idea of your picture survives.

Mechanically, it's how much noise gets added back to your image before the denoising steps run. A little noise, a little change.""",
 {"caption": "Different tools call it strength, denoise, variation or creativity. Same dial."}),

("bimage", "Paint rough, then generate over it",
 ["Block it in yourself: shapes, values, colors.",
  "Generate over it at low or middle strength.",
  "Paint back into the result. Repeat if needed."],
 "slot:your rough block-in beside two generated passes over it, one at low and one at middle strength",
"""This is, I think, the most useful workflow for anyone in this room who paints. Block in the picture yourself, the big shapes, values and colors, roughly. Then generate over it at a low or middle strength, inside Photoshop with a fill over your painting, or in another tool. Then paint back into the result, fixing what it got wrong and keeping what it got right.

The generation sits **inside** your painting rather than replacing it. All the decisions that make the picture work were made by you, in the block-in. The machine renders.

[Show your own example if you have one.]"""),

# ------------------------------------------------------------------ consistency
("section", "Getting the same thing twice", "Consistency",
"""Now the hardest problem in this whole area: getting the same character, or the same place, or the same style, more than once."""),

("statement", "Why it drifts",
 "Every run is a new artist who never saw the model sheet.",
 "No memory between runs. A character's name means nothing to it. \"A tall woman with short red hair\" describes thousands of people, and it picks a different one each time.",
"""Animation students know the word "off-model": a drawing that drifted from the character's model sheet. Generators draw everyone off-model, because every run is like a new artist walking into the studio, hearing your description, and drawing the character without ever seeing a model sheet or any earlier drawing.

There's no memory between runs. Calling your character "Mara" means nothing to it. And words describe a type of person, not a person. So consistency has to come from somewhere other than words."""),

("ladder", "Ways to keep it consistent",
 [("Same seed", "repeat one image exactly"),
  ("Reference image", "show it every time"),
  ("Character and style references", "tools built for this"),
  ("Saved context", "a library it reads every time"),
  ("Training", "a LoRA or custom model")],
"""Five ways, from the lightest to the heaviest.

**Same seed**: repeat one image exactly, change one word. Good for variations, useless for a new pose. **Reference image**: hand it a picture of the character every time. **Character and style references**: tools built for exactly this, like Midjourney's style and omni references, or the reference image option in Photoshop's Generative Fill. **Saved context**: a library of definitions and images the tool reads every time. **Training**: actually changing the model, with a LoRA or a custom model.

The first four hand the model information each time. The last one changes the model. That difference is worth a slide."""),

("cards", "Context or training",
 [("Context", ["You hand it the material every time.", "References, project files, moodboards.", "Like a reference binder on the desk.", "The model itself doesn't change."]),
  ("Training", ["You change the model itself.", "A LoRA, or a custom model.", "Like muscle memory.", "Needs 20 to 50 good images, and time."])],
"""[Short version: fold this into the previous slide.]

**Context** is like a reference binder on the artist's desk: every time they draw, they look at it. The artist doesn't change, the binder does the work. **Training** is like muscle memory: the artist has drawn this character so many times they don't need the binder anymore.

Context is quick, cheap, and you can change it any time. Training takes more effort and good source images, but it holds much better, especially for a style or a face."""),

("cards", "Saved context, in tools you already know",
 [("Chat assistants", ["Claude and ChatGPT both have Projects.", "Files and instructions it reads at the start of every conversation."]),
  ("Research tools", ["NotebookLM answers only from the \"sources\" you give it."]),
  ("Image tools", ["Midjourney: style and omni references, moodboards.", "Photoshop: reference images.", "Firefly: style references."])],
"""You've probably already used saved context without calling it that.

In **chat assistants**, Claude and ChatGPT both have Projects: you put files and instructions in, and it reads them every time you start a conversation inside that project. Some also keep a memory of things you've told them. **NotebookLM** goes further: it answers only from the "sources" you've given it. And **image tools** have their own versions: Midjourney's style and omni references and moodboards, Photoshop's reference images, Firefly's style references.

It's the same idea everywhere: a library of definitions the machine reads before it does anything. For image work, the most useful version is a **style bible**: a page of fixed descriptions of your character and place, word for word, a few reference images, your palette, a must and must-not list, and the exact phrases that worked. You paste from it rather than retyping from memory, because retyping from memory is how drift starts."""),

("lora", "What a LoRA is",
"""Now training. The most common way to train an image model on something specific is a **LoRA**, short for "low-rank adaptation," from a research paper in 2021 or so. Ignore the name.

Mechanically: the base model is huge, several gigabytes, and knows a little about everything. A LoRA is a small add-on file, usually trained on somewhere around 20 to 50 good images of one character, one object or one style. You load it alongside the model, use its trigger word in your prompt, and set how strongly it applies.

The mechanical picture I'd use is a clip-on lens: the camera stays the same, but one thing about every picture it takes changes. Studios use these to keep a character on-model across hundreds of images. You train them on your own computer with open models, or through some online services. Adobe now offers its own version, Firefly custom models, trained on your images."""),

("cards", "Training, responsibly",
 [("Train on your own work", ["Your drawings, your paintings.", "Your style, made repeatable.", "Ownership is much clearer."]),
  ("Use the tools built for it", ["Firefly custom models (Adobe).", "LoRAs with open models.", "Read the terms first."]),
  ("Not on someone else's art", ["Many shared LoRAs copy living artists.", "Without their say, or credit.", "That's exactly the complaint."])],
"""Some lines on training, and I'd hold to these.

**Train on your own work.** This is where it gets interesting for a painter: a model trained on twenty of your own paintings produces your style, repeatably, and the ownership question is much clearer because the source is you.

**Use the tools built for it**, and read their terms about who can use what you train and what happens to your images.

And **not on someone else's art.** A lot of the add-ons people share online were trained on a specific living artist's work, without asking. That's the Luddites' complaint again, in its most direct form: someone's skill, taken to build the thing that replaces them."""),

# ------------------------------------------------------------------ upscaling
("section", "Upscaling", "Possibly the most useful tool a painter has",
"""Now something more cheerful. I think upscaling may be the single most useful AI tool for a painter, and it's the least controversial."""),

("slider", "Faithful or creative",
 "Faithful: invent nothing", "Creative: re-render the detail",
 [(0.12, "Faithful", "Preserve Details, Real-ESRGAN-type models. Sharper edges, no new things."),
  (0.5, "Generative", "Photoshop's generative upscale and similar. Some invented texture."),
  (0.88, "Creative", "Magnific, tiled diffusion. New detail, and it can change faces.")],
"""Upscaling means making an image bigger, with more pixels, without it going soft. The reason it matters to a painter: you can paint at a size your computer handles comfortably, then finish at the size a print needs. Or rescue an old scan, or a small thumbnail you love.

There are two kinds, really ends of a slider. **Faithful** upscalers enlarge and sharpen and invent nothing: Photoshop's Preserve Details resampling, and AI models of the Real-ESRGAN type. **Creative** upscalers re-render the image at the larger size and invent new detail: skin pores, brush texture, leaves, stone. Tools like Magnific, or tiled diffusion in node workflows, sit at that end, and Photoshop's own generative upscale is somewhere in between.

Creative upscaling is amazing on textures and dangerous on faces, hands and lettering, because it's a generation, with a generation's mistakes."""),

("image", "On surfaces, it's excellent", "upscale_texture.png",
 "A 64-pixel crop, enlarged four times. The rim, the spoon and the wood come back sharp.",
"""A real example, made for this slide on this workspace's computer. A tiny crop of a photo, 64 pixels square, enlarged four times. On the left, plain resampling, which is what Photoshop's basic Image Size does: soft and blurry. On the right, Real-ESRGAN, a free, faithful AI upscaler: the rim of the saucer, the highlights on the spoon, the grain of the wood all come back crisp.

On surfaces like these (stone, wood, fabric, foliage, brushwork) this is close to magic, and it's why I'd call upscaling the most useful AI tool a painter has."""),

("image", "On faces, it invents", "upscale_compare.png",
 "Same model, same settings. The helmet and suit are sharp. The eyes and teeth were never in those 64 pixels.",
"""Same model, same settings, different picture. The helmet ring and the suit come back beautifully. The face does not. There was no information about her eyes or teeth in 64 pixels, so the model **invented** some, and they're wrong in a way that's hard to look at.

I didn't plan this slide this way. I expected a clean result, and this is what came out, which is exactly the point of the whole section. Even a "faithful" upscaler invents when you push it far enough, and it invents most on the things people look at hardest: faces, hands, lettering.

So: upscale, then look at it at 100% before you trust it."""),

("loop", "A painter's upscale workflow",
 [("Paint", "at a working size"), ("Faithful upscale", "to the print size"),
  ("Creative pass", "on its own layer"), ("Mask it in", "only where it helps"),
  ("Check at 100%", "faces, hands, text")],
"""A workflow I'd recommend.

**Paint** at a size you can work at comfortably. **Faithful upscale** to the final print size; this is your base, and it invents nothing. Then, if you want more rendered texture, a **creative pass** on a separate layer. **Mask it in** only where it helps: the stone, the foliage, the fabric. Keep your own brushwork where it matters, usually faces and the focal area. Then **check at 100%**, especially faces, hands and any lettering, because that's where a creative upscale invents things you didn't ask for.

Same principle as everything else today: the machine renders, you decide where.""",
 {"human": [0, 3, 4]}),

# ------------------------------------------------------------------ human in the loop
("section", "The human in the loop", "",
"""Last major piece. Why the person still has to be there, even when the machine is very good."""),

("bimage", "The Pope in a white puffer jacket",
 ["2023 or so: a generated image goes around the world.",
  "Millions believed it, including professionals.",
  "Ten seconds of looking would have caught it."],
 "slot:the generated image of the Pope in a white puffer jacket, 2023 or so",
"""You've probably seen this one. In 2023 or so, a generated image of the Pope in a huge white designer puffer jacket went around the world, and a lot of people, including people who work with images, believed it for a while.

[Give the room thirty seconds with it, then point out what gives it away.] The hand doesn't actually close around the cup. The glasses melt into the cheek. The crucifix chain does something no chain does. The light on the face is a little too even for the scene.

Nobody needed special software to catch it. They needed someone to look at it carefully for ten seconds instead of one. The person who made it has said he didn't expect it to spread the way it did. Which is the point: the machine had no idea what it had made, and nobody in between checked."""),

("cards", "What the machine can't check for you",
 [("Whether it's wrong", ["It's equally confident about good and bad results."]),
  ("Whether it's real", ["\"AI detectors\" misfire in both directions."]),
  ("What it's for", ["The brief, the audience, and whether the picture has to be true."])],
"""Three things the machine can't do for you.

It can't tell you **when it's wrong**: a generator is exactly as confident about a hand with six fingers as about a perfect one. It can't reliably tell you **what's real**: the tools that claim to detect generated images misfire in both directions, flagging real photos and missing fakes. And it doesn't know **what the image is for**: the brief, the audience, whether the picture is making a claim about the world that has to be true.

That's the human's job, and I don't think it's going anywhere."""),

("loop", "Where the person sits",
 [("Brief", "what it's for"), ("Generate", "candidates"), ("Evaluate", "against the brief"),
  ("Fix", "by hand"), ("Disclose", "what you made")],
"""So here's the loop, with the human steps in red. You write the **brief**. The machine **generates** candidates. You **evaluate** them against the brief, looking for errors. You **fix** what's wrong, by hand. You **disclose** what was generated and what you made. And if it isn't right yet, around again.

One step out of five is the machine's. The other four are the job.""",
 {"human": [0, 2, 3, 4], "caption": "Red: only a person can do it."}),

("cards", "Who owns it (US, as of 2026)",
 [("Purely generated", ["No copyright.", "Courts and the Copyright Office agree.", "The Supreme Court declined to revisit it in 2026."]),
  ("Prompt only", ["Usually not enough to make you the author, however detailed the prompt."]),
  ("Your hand in it", ["Selection, arrangement, edits, painting and drawing can be protected."])],
"""And the property question, briefly, because people are surprised by it. I'm not a lawyer, this is the US only, and it changes, so check it before you rely on it.

**Purely generated images can't be copyrighted.** The Copyright Office has said so consistently, the courts agreed in a case brought by a man named Stephen Thaler, and in March 2026 the Supreme Court declined to take that case. **A prompt alone usually isn't enough** to make you the author, according to the Office's 2025 report, however detailed it is. What **can** be protected is what a person adds: selecting, arranging, editing, painting. In 2023 a comic book called "Zarya of the Dawn" got protection for its text and its arrangement, but not for the generated images in it.

In other words, in a sense, the painting is the part that's yours. Which is one more reason to keep your layers, and to **say what you made**: name the tools, what was generated, what you did by hand, and any sources you brought in. A few sentences, without being asked."""),

# ------------------------------------------------------------------ hands-on 2
("section", "Hands-on: the prompt relay", "About twenty-five minutes",
"""Now let's actually do it."""),

("cards", "The prompt relay",
 [("Round 1", ["Teams of three get a target image.", "Write one prompt, five parts.", "I run every team's prompt on screen."]),
  ("Round 2", ["Change one thing only.", "Write down what you expect to change.", "Run it again. Were you right?"]),
  ("Round 3", ["Swap results with another team.", "Check theirs against their target.", "Name what's wrong, and where."])],
"""[About twenty-five minutes. Put students in teams of three and give each team one of the three target images. More than one team can have the same target, which makes the comparisons more interesting.]

**Round one, eight minutes.** Each team writes one prompt, using the five parts, to get as close to their target as they can. Then I run every team's prompt live on the projector, one after another, and we put each result next to its target.

**Round two, eight minutes.** Each team changes **one** thing in their prompt, and writes down, before I run it, what they expect to change. Then we run them. Were they right? This is the part where people actually learn what words do.

**Round three, five minutes.** Teams swap results. Check the other team's best result against their target: what doesn't match, what's wrong with it, and where. Point at it.

[If the lab license allows students to generate, teams can run their own prompts instead. Either way, keep the projector for comparing results. Short version: drop round two or three.]"""),

("loop", "From start to finish",
 [("Brief", "what it's for, in words"), ("Input", "sketch, ID map, reference"),
  ("Generate", "and choose, with a reason"), ("Fix and upscale", "by hand, where it matters"),
  ("Check and disclose", "then say what you made")],
"""To finish, the whole thing on one slide, which is also a summary of today.

Start with a **brief**, specific enough that a person could make it. Give the machine **input** beyond words: a sketch, an ID map, a reference, your own block-in. **Generate** and choose, with a reason you can say out loud. **Fix and upscale**: correct what's wrong by hand, enlarge for where it's going. **Check and disclose**: look at it the way nobody looked at the puffer jacket, and say what was generated and what you made.

Lovelace's line holds up better than people think: it can do whatever we know how to order it to perform. Today was about ordering it well, and about the four steps in that loop that are still ours.""",
 {"human": [0, 1, 3, 4], "ret": False, "caption": "Red: the steps that are yours."}),

vocab([("Diffusion", "an image developed out of noise, step by step"),
       ("Seed", "the random noise a run starts from"),
       ("Model", "a set of habits learned from training images"),
       ("Strength / denoise", "how much it may change your image"),
       ("LoRA", "a small trained add-on for one character or style"),
       ("Upscaling", "faithful invents nothing; creative re-renders")]),

("options",
 ["A prompt log for one target image.", "Five versions, one change each.", "What each change actually did."],
 ["A one-page style bible for a character or place.", "Fixed descriptions, references, palette.", "A must and must-not list."],
"""[Optional, if you want to attach homework when you drop this lecture in. About 45 minutes either way.]

**Option A**: a prompt log. Take one target image (one of today's, or one I post) and write five versions of a prompt for it, changing one thing each time. If you can generate, include the results. If you can't, write what you expect each change to do. The log is the deliverable.

**Option B**: a one-page style bible for a character or a place of your own: five fixed descriptions written word for word, three references (your own photos or drawings, or properly licensed images), a palette, and a must and must-not list. No generation required. This is the document you'd hand a generator, a person, or a team, so it's useful whatever you think of these tools.""",
 {"title": "If you want to take it further"}),
]

if __name__ == "__main__":
    build(SPEC, OUT)
