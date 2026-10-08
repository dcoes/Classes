#!/usr/bin/env python3
"""Session 9. Ownership, copyright and disclosure.  Run from the repo root.

The legal slides reflect the situation as of October 2026 and must be checked
each time the course runs (the outline says so, and it is correct).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/09_Ownership_Copyright_Disclosure.pptx"

SPEC = [
("title", "Ownership, Copyright and Disclosure", "AI Digital Imaging  |  Session 9",
"""**Running time, about 50 minutes.** Spot it and recall (5). The state fair painting (4). Three different questions (3). The law, as of this term (10). The training data argument, both sides, with the argue-the-other-side exercise (12). Disclosure, how professionals do it (8). The final project introduced (7). Options (1).

**Check before every run of this course.** The law slides are current as of October 2026. Before teaching this session, spend twenty minutes checking: the US Copyright Office's AI page, the status of the artists' case against the image generator companies (Andersen v. Stability AI, in federal court in California), the studios' case against Midjourney, and anything new from the EU or UK. Update the notes rather than the slides where you can. I'd say plainly to the room that you're not a lawyer and neither is anyone they'll hear on social media.

**Prep.** The final project brief handout and the three brief options (key art for a game, chapter headers for a book, a poster series). A disclosure statement you wrote for one of your own pieces, as the worked example.

Slot images: Jason Allen's "Théâtre D'opéra Spatial" (2022), the "Zarya of the Dawn" comic cover (2022 or so), and the withdrawn generated protest images from a human rights organization's social account (2023 or so). Show these in class rather than redistributing them."""),

warmup("a generated image presented as a real photo somewhere online (yours, or a documented case)"),

("bullets", "Last time",
["Light, color, grain, edges.",
 "Camera height and focus.",
 "Nothing generated should float."],
"""Recall. [Cold call.] The four matches, in order? [Light, color, grain, edges.] Which one is easiest to skip? [Grain, because people work zoomed out.]

Today is different from the last eight. No new Photoshop technique. Today is about who owns this stuff, whether it was fair to make it, and what you owe the people who see your work. It's also when you get the final project brief, so stay to the end."""),

("bimage", "In the wild: a ribbon at the state fair",
["2022: a generated image wins an art prize.",
 "The artist: many prompts, then Photoshop.",
 "Copyright Office: no registration."],
"slot:Jason Allen's 'Théâtre D'opéra Spatial' (2022)",
"""Let's start with a story most of you have probably heard a version of. In 2022, at the Colorado State Fair, an image called "Théâtre D'opéra Spatial" won first prize in the digital art category. Its maker, Jason Allen, had generated it with Midjourney, through hundreds of prompts and variations by his account, and then worked on it in Photoshop and upscaled it.

When people found out, a lot of artists were furious. He said he'd been open about using the tool. The judges said they hadn't known, and that they'd probably have awarded it anyway.

Then he applied to register the copyright, and the US Copyright Office refused, because in their view the image's expressive parts came from the machine, not from him. He challenged that in court. [Check the current status.]

Keep this one in mind, because it touches all three of today's questions at once."""),

("boxes", "Three different questions",
["Law|can anyone own it?", "Ethics|was the training fair?", "Honesty|did you say what you did?"],
"""People argue about this as if it were one question, and that's why the arguments go nowhere. It's really three, and they have different kinds of answers.

**Law**: can anyone own a generated image, and who? That has answers, at least for now and in a given country, and they're more specific than people think.

**Ethics**: was it fair to train these systems on millions of people's work without asking? That one doesn't have a settled answer, and reasonable people disagree.

**Honesty**: did you tell people what you did? That one is entirely up to you, and it's the one that matters most for your career this month.

We'll take them in that order."""),

("section", "The law, as of this term", "United States, October 2026. Check again next time.",
"""First, the law. I'm going to describe the situation in the United States as of this term, and I want to be clear that I'm not a lawyer, that this changes, and that you should never take legal advice from a slide, including mine."""),

("bullets", "What the law says now (US)",
["Copyright needs a human author.",
 "A prompt alone usually isn't enough.",
 "Your selection, arrangement and edits can be."],
"""Three points, and they're fairly well established now.

**Copyright needs a human author.** The Copyright Office has said this consistently, and the courts have agreed. In the best-known case, a man named Stephen Thaler tried to register an image he said his AI system made on its own. He lost, the appeals court agreed in 2025, and in March 2026 the Supreme Court declined to take the case. So, purely machine-made images can't be copyrighted in the US.

**A prompt alone usually isn't enough.** The Office's 2025 report on this says that typing instructions, even very detailed ones, generally doesn't make you the author of what comes out, because you don't control how the machine turns them into an image.

**Your own contributions can be protected**: what you selected, how you arranged things, what you changed by hand, what you drew yourself. The more of the image is genuinely your decisions and your hand, the more of it is yours."""),

("bimage", "A comic book, 2023",
["Text: hers.",
 "Selection and arrangement: hers.",
 "The generated images: nobody's."],
"slot:the cover of the comic 'Zarya of the Dawn' (2022 or so)",
"""The clearest example of where the line sits is a comic book called "Zarya of the Dawn." The author wrote it and laid it out, and generated the images with Midjourney.

In 2023 the Copyright Office decided that the text was hers, and the selection and arrangement of the pages was hers, but the individual generated images were not protected. Anyone could, in principle, copy one of those pictures on its own.

[Ask: does that seem fair to you? Take two answers, one from each side if you can.]

It's worth noticing what that means: the parts of the book that were most clearly human decisions are the parts that are protected."""),

("bullets", "What that means for your final",
["Your corrections and choices: yours.",
 "The raw generation: probably nobody's.",
 "Your layers are the evidence."],
"""So, practically, for you.

The parts of your final that are your decisions and your hand work are yours: your brief, your selection, your composition, your corrections, your type and layout, anything you painted or photographed. The raw generated pixels, untouched, probably belong to nobody.

And here's something I didn't plan when I set up the process record, but it turns out to matter: **your layered file is the evidence** of what you contributed. A flattened JPEG can't show anyone which parts are yours. A file with GEN_ and FIX_ layers can."""),

("bullets", "Elsewhere, and in contracts",
["Other countries draw the line differently.",
 "Europe now requires labels on some content.",
 "Your client's contract may matter most."],
"""Briefly, outside the US. Other countries handle this differently. The UK, for example, has an older rule about "computer-generated works" that gives a kind of authorship to whoever made the arrangements, and it's been under review. The European Union's AI Act includes transparency rules: from around August 2026, some kinds of generated or manipulated images, especially realistic ones of real people or events, have to be disclosed as such, and generator companies have to mark their output in a machine-readable way.

But for most of you, most of the time, the rule that matters is the one in **your contract.** Many clients, publishers and studios now ask whether generated material was used, and some forbid it entirely. If you can't answer the question, you can't sign the delivery."""),

("section", "The training data argument", "Both sides, as fairly as I can",
"""Now the ethics question, and I'm going to try hard to give both sides fairly, because I think both have real points, and because some of you hold each of them strongly."""),

("two", "Two cases",
["**Against**", "Trained on artists' work, unasked.", "No credit, no pay.", "Then competes with them."],
["**For**", "Learning patterns isn't copying.", "Artists learn from others too.", "No stored pictures inside."],
"""The case **against**, as its strongest defenders would put it: these systems were built by collecting billions of images, including the life's work of living illustrators and photographers, without asking anyone, crediting anyone, or paying anyone. The result is a product that competes directly with those same artists for work, and sometimes imitates them by name. Many working artists see that as taking their labor to build their replacement.

The case **for**, also as its strongest defenders would put it: the system doesn't store or paste the images, it learns statistical patterns, more or less the way an art student learns by looking at thousands of paintings. Every artist learns from other people's work without paying them. And copyright has never protected a style, only specific works.

[Don't resolve it. Move on.]"""),

("bullets", "Where it's being fought",
["Artists versus generator companies (US).",
 "A stock photo agency versus a generator (UK and US).",
 "Film studios versus a generator (US)."],
"""This is being argued in court right now, and none of it is finished. Some of the cases include:

A group of illustrators, including Karla Ortiz, Kelly McKernan and Sarah Andersen, sued several image generator companies in 2023. Parts of that case have survived attempts to dismiss it, and it's still moving through federal court. [Check the status.]

Getty Images sued Stability AI in both the UK and the US. The UK court ruled in late 2025 or so, mostly in Stability's favor on the central copyright question, finding that the trained model itself wasn't a copy of the photos, though Getty won a narrower point about its watermarks showing up in some outputs.

And in 2025, Disney and Universal sued Midjourney, arguing among other things that it reproduces their characters on request.

The honest summary: the law hasn't decided this yet, and anybody who tells you it's settled, either way, is ahead of the courts."""),

("bullets", "And the tool in our lab",
["Adobe says: licensed and public domain.",
 "Contributors were paid a bonus.",
 "Critics say: not as clean as claimed."],
"""What about Firefly, the model in our Photoshop? Adobe says it trained Firefly on images it had the rights to: Adobe Stock, openly licensed work, and public domain material, and it has paid Adobe Stock contributors a bonus. That's a meaningfully better position than scraping the open web, and I think it's fair to say so.

Nevertheless, not everyone accepts it at face value. Stock contributors uploaded their work before generators existed and didn't agree to this specific use in advance. And there were reports in 2024 or so that some of the Stock images used for training were themselves generated by other tools.

I'm not going to tell you what to conclude. I'd like you to know the actual argument, rather than the slogan version from either side."""),

("bullets", "Argue the other side",
["Pick the side you disagree with.",
 "Ninety seconds to your partner.",
 "Then switch."],
"""[About six minutes.] An exercise, and it's Option B tonight in longer form.

In pairs. Each of you picks the side of the training data argument you **disagree** with. Then you make the best case you can for it, to your partner, in ninety seconds. Then switch.

[Run it. Then ask: did anyone hear an argument they hadn't thought about? Did anyone find their own side harder to defend afterward?]

This is a very old way of thinking clearly, and it's hard. If you can only argue your own side, you don't fully understand it yet. And it's quite useful in a job, where you'll work with people who see this differently from you, sometimes the person paying you."""),

("section", "Disclosure", "The part that's entirely up to you",
"""Now the third question, the one that's in your hands."""),

("bullets", "How professionals disclose",
["A line in the credits or caption.",
 "A note to the client, before delivery.",
 "A form on the store page."],
"""Some of the ways disclosure actually happens in the industry now.

A line in the **credits or caption**: "background elements generated with Adobe Firefly." A note to **the client**, before delivery, often required by contract. And **forms**: Steam, the big PC game store, has asked developers since early 2024 or so to disclose generated content in their games, and shows it on the store page. Publishers and competitions increasingly ask too.

And, as we said in session 1, **Content Credentials**, the tag Firefly attaches to the file. Useful, but not a substitute for saying it, because tags get stripped when files are copied and re-saved."""),

("bimage", "In the wild: a disclosure, too late",
["A human rights group, 2023 or so.",
 "Generated photos of real protests.",
 "Labeled, but only in small print."],
"slot:the withdrawn generated protest images posted by a human rights organization, 2023 or so",
"""[About four minutes.] A real case that shows why this matters even for people with good intentions.

In 2023 or so, a regional account of a major human rights organization posted generated images illustrating real protests in Colombia, including police violence. They said they did it to protect the identities of real protesters, which is a genuinely good reason. There was a small label saying the images were generated. But the images looked like news photos, the flag colors were wrong, the faces were smooth and strange, and people were angry that an organization whose whole job is documenting what really happened had used invented pictures of it. They took them down.

[Ask: what would have made this acceptable, if anything?] Usually the room gets to: a different visual style that couldn't be mistaken for a photo, and a much clearer label. Remember the news photo rule from session 3. The trouble is always the gap between what an image is and what it seems to claim."""),

("boxes", "Writing your disclosure",
["Tools|name them", "Generated|which parts", "Made|which parts, by hand", "Sources|photos, references"],
"""For your final, and for tonight's Option A, the disclosure statement has four parts.

**Tools**: name them. **Generated**: which parts. **Made**: which parts you did by hand, painted, photographed, corrected, composed, set in type. **Sources**: any photos or references you brought in, and where they came from.

Here's a worked example, from one of my own pieces. [Read your statement. If you don't have one, something like: "The background and the figure's coat were generated in Photoshop with Generative Fill, from my prompts. I corrected the hands, the cast shadows and the window lettering by hand, and composited a photograph of my own hand for the left hand. The layout and type are mine."]

Short, specific, no apology and no boasting."""),

("two", "Too vague, too much, about right",
["**Too vague**", '"AI-assisted."', "**Too much**", "Every click you made."],
["**About right**", "What a client would need", "to know before they paid you."],
"""Two ways to get it wrong.

**Too vague**: "AI-assisted" or "made with AI tools." That tells nobody anything. Assisted how? Which parts? It reads like you're hiding something, even when you're not.

**Too much**: a page-long list of every step. Nobody reads it, and it also reads as a bit defensive.

**About right**: what a client would need to know before they paid you. Which parts came from a generator, which parts you made, and anything you brought in from elsewhere. A few sentences."""),

("section", "The final project", "Art-Directed Series, due session 16",
"""Last part today, and the one you'll be living with for the next two weeks."""),

("bullets", "The Art-Directed Series",
["Three or four images, one brief.",
 "Key art, chapter headers, or a poster series.",
 "Same character, place and light."],
"""The final project. Three or four images for one brief, that look like they belong together: consistent in character, place and light.

Three brief options. **Key art for a game**: the images that would go on a store page or a box. **Chapter headers for a book**: one image per chapter, same format. Or **a poster series**: three or four posters for an event or a film, meant to hang side by side.

You pick one. [Hand out the brief sheet.] Everything from the first two weeks lands here: the brief, judging, fixing by hand, consistency, compositing. Week four adds type and presentation."""),

("checklist", "What you hand in",
["The brief", "A reference board", "The prompt log", "Rejected selections",
 "Hand corrections, layered", "A disclosure statement"],
"""What you hand in with the final, and it's the same list as the rubric's process criterion.

The brief. A reference board. Your prompt log. The images you rejected, with a reason for each, because the rejections show your judgment as clearly as the keeps. Your hand corrections, on named layers. And a disclosure statement, written the way we just practiced.

It sounds like a lot. Most of it is stuff you'll produce anyway if you work the way we've been working. The milestones make sure it happens in order."""),

("boxes", "Milestones",
["Session 10|brief and reference board", "Session 12|rough set", "Session 14|corrected set",
 "Session 16|final, presented"],
"""Milestones, and the rule.

**Session 10**, next class: your brief and reference board. **Session 12**: a rough set, all three or four images, not finished, critiqued against the brief. **Session 14**: the corrected set, critiqued in small groups. **Session 16**: the final, presented.

And the rule from session 1: a final submitted without its milestones is capped at Average, whatever it looks like. Each milestone is checked for being on time and complete, coming out of the stage before it, and responding to the notes from the last critique.""",
{"sub": "No milestones, no grade above Average. That's arithmetic, not punishment."}),

("boxes", "How the final is graded",
["Brief|25", "Consistency|20", "Hand fixes|25",
 "Type|10", "Process|20"],
"""The rubric for the final, which is on Canvas.

**Fit to the brief**, including your must and must-not list, 25. **Consistency** across the series, 20. **Hand correction and compositing**, 25. **Type and presentation**, 10. **Process record and disclosure**, 20, and the top level there needs a disclosure that accurately separates what was generated from what you made.

Once again, more than half of it is about decisions you made and things you did by hand.""",
{"sub": "100 points. Rubric on Canvas."}),

vocab([("Human authorship", "what US copyright requires"),
       ("Selection and arrangement", "your choices, which can be protected"),
       ("Training data", "the images a model learned from"),
       ("Kill notice", "an agency telling clients to stop using an image"),
       ("Disclosure statement", "tools, generated, made, sources"),
       ("Content Credentials", "a tag in the file; not a substitute for saying it")]),

("options",
["Write the disclosure statement", "for your Project 1."],
["About 200 words arguing the side", "of the training data debate", "you disagree with."],
"""Tonight, due next class, along with Milestone 1, so plan your time.

**Option A**: write the disclosure statement for your Project 1, in the four parts. Short and specific.

**Option B**: about 200 words arguing the side of the training data debate you disagree with, as well as you can. I'm grading how fairly and specifically you make the case, not which side you're on.

And for Milestone 1 next class: start your brief and reference board tonight. Session 10 goes through both in detail, so a rough start is fine."""),

("quote", "One line to take home", "Say what you made.",
"Your layers are the evidence.",
"""Say what you made. Your layers are the evidence. [Demo: the final project brief, and building a reference board artboard.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
