#!/usr/bin/env python3
"""Session 8. Compositing generated elements.  Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aikit import build, warmup, vocab

OUT = "AI Digital Imaging/lectures/08_Compositing_Generated_Elements.pptx"

SPEC = [
("title", "Compositing Generated Elements", "AI Digital Imaging  |  Session 8",
"""**Running time, about 50 minutes.** Spot it and recall (5). Compositing is older than all of this (6). Pasted on or sitting in (4). The four matches: light, color, grain, edges (20). Depth and atmosphere (4). Harmonize, and generating for the plate (4). Worked example and cold reversal (6). Options (1).

**Prep before class.** The Option A set: a background plate (a photo you took, with a clear light direction) and two generated elements made for it, one of which is lit from the wrong side, on Canvas. One composite of your own with three deliberate mismatches for the cold reversal. Check whether Harmonize is available on the lab version.

Slot image: Oscar Rejlander's "The Two Ways of Life" (1857), a combination print from roughly thirty negatives, public domain."""),

warmup("a generated element badly composited into a photo (yours)",
       "A composite rather than a pure generation, so the room starts thinking about today's topic."),

("bullets", "Last time",
["The note is data.",
 "Against the brief.",
 "One change at a time."],
"""Recall, quickly. [Cold call.] What's the critique format? [Brief says, image does, one change.] What did the room miss most in Project 1? [Remind them of the pattern you named at the halfway point.]

Today's subject is where a lot of those misses came from: a generated thing sitting in an image without agreeing with it."""),

("bimage", "This is old",
["1857: one print, about thirty negatives.",
 "Matte paintings on glass.",
 "Every visual effects shot since."],
"slot:Oscar Rejlander, The Two Ways of Life (1857), public domain",
"""Before anything else: compositing is old, older than Photoshop, older than film.

This is Oscar Rejlander's "The Two Ways of Life" from 1857, give or take. It's one photographic print, made by combining something like thirty separate negatives in the darkroom, because the cameras of the time couldn't capture a scene like this in one exposure. People at the time argued about whether it was cheating. Sound familiar?

After that come matte paintings on glass for films, photomontage in the 1920s or so, and essentially every visual effects shot you've ever seen. The skills we're doing today, matching light and color and grain, are the same skills compositors have used the whole time.

The generator just gives you a new source of pieces. Putting pieces together so they agree is still a craft."""),

("image", "Pasted on, or sitting in?", "composite_demo.png",
"Same background, same sphere. One floats. One belongs.",
"""Same brick floor, same sphere, two composites.

On the left, it's **pasted on.** You can feel it without being able to say why. On the right, it's **sitting in** the scene.

[Ask the room: what's different? Take answers until they've named most of it.]

On the left: lit from the wrong side, the light is cool while the scene is warm, it's perfectly clean while the floor has grain, the edge is razor sharp, and there's no shadow where it touches the ground. On the right, all of those match. That's the whole session, in two pictures."""),

("boxes", "The four matches",
["Light|direction, softness", "Color|temperature, black and white points",
 "Grain|noise and sharpness", "Edges|softness, contact, wrap"],
"""Four matches, and it's worth checking them in this order, because each one affects the next.

**Light**: direction and softness. **Color**: temperature, saturation, and where the darkest dark and brightest bright sit. **Grain**: noise and sharpness. **Edges**: how soft the outline is, whether there's a contact shadow, and whether the background's light wraps around the edge.

Let's do them one at a time."""),

("bimage", "1. Light",
["Find the plate's light first.",
 "Match direction, then softness.",
 "Wrong side: flip it, repaint it, or redo it."],
"error_light.png",
"""Light first, because if it's wrong, nothing else will save it.

Look at the **plate**, the background photograph, before you look at the element. Where's the light coming from? Hard or soft? How long are the shadows? Write it down, literally, in a note layer: "sun high, camera left, hard."

Then check the element. If the light comes from the wrong side, you have three options, from fastest to slowest. **Flip it** horizontally, if the element doesn't have text or anything else that would give away the flip. **Repaint** the light and shadow sides on a FIX_ layer. Or **generate it again** with the plate's light written into the prompt, which is often the right call when the error is large."""),

("bimage", "2. Color",
["Match the darkest dark and brightest bright.",
 "Then the midtones.",
 "Clipped Curves, per channel."],
"slot:a screenshot of a Curves adjustment clipped to an element, red channel showing",
"""Color second. The classic method, and it's been the classic for a long time:

Put a **Curves** adjustment layer above the element and **clip** it to the element (Alt-click between the layers), so it only affects that one layer. Then, channel by channel, red, green, blue, match the element's darkest dark to the plate's darkest dark, and its brightest bright to the plate's brightest bright. Then adjust the midtones until the overall temperature matches.

And check it in gray, the same check as always. If the element is brighter or darker in value than things at the same distance in the plate, it'll pop out no matter how good the color is.

There's also Image, Adjustments, Match Color, which can give you a rough first pass."""),

("image", "3. Grain and sharpness", "composite_zoom.png",
"Generated pieces are too clean. Add noise, match the softness.",
"""Third, grain and sharpness, at 100% zoom.

Generated elements are usually **too clean**: smooth gradients, no noise, sharpness that's perfectly even. Real photographs have grain, compression, slight softness, and the sharpness changes with focus.

So: clip a layer to the element, fill with 50% gray, set it to Overlay, and add noise to that until it matches the plate. Then, if the plate is slightly soft, blur the element very slightly. Compare at 100% by toggling.

This is the step people skip because they're working zoomed out. It's also the step that makes the biggest difference when someone looks closely."""),

("bullets", "4. Edges",
["Match the plate's edge softness.",
 "A contact shadow, where it touches.",
 'Light "wrap" from behind.'],
"""Fourth, edges.

**Softness**: zoom into the edges of things in the plate at the same distance. Are they razor sharp or a little soft? Match that with a slightly feathered mask on the element. Hair and fur need extra care: Select and Mask, and sometimes painting stray hairs back in by hand.

**Contact shadow**: wherever the element touches the ground or another surface, there's a small, dark, soft shadow right at the contact point, even in soft light. Without it, things float. Paint it on its own layer, set to Multiply.

**Light wrap**: when there's a bright background behind something, a little of that light bleeds around its edges. A thin, soft edge of the background's color on the element's outline sells it. Subtle, but it's in every good composite."""),

("bullets", "Depth and atmosphere",
["Far things are lower contrast.",
 "Far things shift toward the sky's color.",
 "Check scale against the horizon."],
"""One more thing if your element sits at a distance.

Far things are **lower contrast** and shift toward the color of the sky, usually lighter and bluer, because of the air in between. Painters call it atmospheric perspective. An element placed far away with full contrast and saturation will jump forward, even if the size is right.

And check **scale** against the horizon, the perspective check from session 4. In a photo from standing height, a standing person's head sits more or less on the horizon wherever they are. Use that to size people and most other things."""),

("bullets", "Camera height and focus",
 ["Same camera height as the plate.",
  "Same lens, same distortion.",
  "Same focus: sharp where the plate is sharp."],
"""Two more matches that sit underneath the four, and they're the ones that make a composite feel wrong when you can't say why.

**Camera height.** If the plate was shot from standing height and the element was generated looking down from above, you'll see the top of the element when you should be seeing its side. No amount of color matching fixes that. Check where the horizon would be in the element, and make sure it agrees with the plate's horizon. If it doesn't, regenerate with the camera height in the prompt ("eye level," "shot from low") or pick a different variation.

**Lens and focus.** A wide-lens element in a long-lens plate looks subtly stretched. And if the plate's background is out of focus, an element placed back there has to be equally out of focus, with a Lens Blur or Gaussian Blur to match. A perfectly sharp thing in a blurry zone jumps straight to the front.

[Ask: has anyone seen a movie poster where a face looks pasted on? Usually it's one of these two.]"""),

("checklist", "Before you call it done",
 ["Light from the same side", "Blacks and whites match", "Grain matches at 100%",
  "Edges as soft as the plate's", "Contact shadow present", "Camera height agrees",
  "Focus matches the distance", "Checked in gray"],
"""Eight checks, a photo-friendly slide for your phone. Go down it before you call any composite done, including tonight's option.

It's long on purpose. Notice that only the last one asks how it looks overall. Everything above it is a specific thing you can check and either pass or fail, which is much easier to do honestly at one in the morning than "does it look good?\""""),

("bullets", "Harmonize, and other shortcuts",
["Photoshop can try the match for you.",
 "Treat it as a first pass.",
 "Then check the four by hand."],
"""Recent versions of Photoshop have a feature called Harmonize that tries to do some of this automatically: it adjusts an element's color and lighting to the background, and sometimes adds shadows. [Check whether it's on the lab version and show it in the demo if it is.]

It can be quite good, and it's worth trying. Treat it like any generated output: as a **first pass**, which you then check against the four matches and fix by hand. In my experience these tools are better at color than at light direction, and least reliable on shadows. Check those first.

And name the layer so the record shows what it did."""),

("bullets", "Generate for the plate",
["Write the plate's light into the prompt.",
 "Or fill it in place, inside the plate.",
 "In place usually matches better."],
"""You can make your life a lot easier before compositing, by generating with the plate in mind.

If you generate an element separately, write the plate's light into the prompt: "lit from camera left, late afternoon sun, hard shadows." You wrote it down in step one, so use it.

Or skip the separate generation and **fill in place**: select an area inside the plate itself and generate the element there, so the generator can see the surrounding light and color. That usually matches better from the start. It's not always possible (the element might need to come from somewhere specific), but when it is, start there."""),

("boxes", "Worked example, in order",
["Place|scale to the horizon", "Light|flip or repaint", "Color|clipped Curves",
 "Grain|noise, softness", "Edges|mask, contact, wrap", "Check|in gray, at 100%"],
"""The whole thing in order, which I'll do live in the demo.

**Place** and scale it against the horizon. **Light**: flip or repaint until it agrees. **Color**: clipped Curves, channel by channel. **Grain**: noise and softness, at 100%. **Edges**: soft mask, contact shadow, a touch of light wrap. **Check** in gray and at 100%, then zoomed all the way out, which is how most people will actually see it.

Each step on its own named layer, clipped to the element where it makes sense, so the whole composite can be adjusted later."""),

("image", "Now you: name the mismatches", "slot:your composite with three deliberate mismatches",
None,
"""Cold reversal. This composite has three mismatches. In pairs: name them, using the four matches, and put them in the order you'd fix them. Two minutes.

[Take answers. Don't confirm. Ask the pairs who disagree about the order to defend it. The right instinct is light before color before grain before edges, but a pair who argues for something else with a reason is doing the thinking.]"""),

("bimage", "In the wild: a famous portrait",
 ["A head from one man,", "a body from another,", "1860s or so."],
 "slot:the 1860s Lincoln print with Lincoln's head on John C. Calhoun's body (public domain)",
"""[About four minutes.] A historical one, and it's my favorite example of compositing done well and disclosed badly.

There's a well-known portrait of Abraham Lincoln from the 1860s or so, standing heroically next to a desk. It's Lincoln's head on someone else's body, a portrait of the politician John C. Calhoun, with the head swapped. The light on the head and the body roughly agree, the scale is right, the edges are handled. It fooled people for about a century.

[Ask: why did the printmaker do it?] Probably because there wasn't a suitably grand full-length photograph of Lincoln to work from. A practical reason, not a sinister one.

So: excellent compositing, and no disclosure. Which is a preview of next week, when we talk about why the second part matters as much as the first."""),

vocab([("Plate", "the background photo you composite into"),
       ("Clipping mask", "an adjustment that affects one layer only"),
       ("Contact shadow", "the dark shadow where things touch"),
       ("Light wrap", "background light bleeding onto an edge"),
       ("Atmospheric perspective", "far things fade and turn toward the sky"),
       ("Combination print", "one photo built from many negatives")]),

("options",
["Composite two provided elements", "into the provided plate."],
["Composite one generated element", "into a photo you took."],
"""Tonight, due next class.

**Option A**: the plate and two generated elements on Canvas. Composite both. One of them is lit from the wrong side, on purpose. Every match on its own named layer.

**Option B**: take a photo yourself, with a clear light direction, and composite one generated element into it. Write down the plate's light before you generate, and put it in the prompt.

Same rubric. Next class starts week three: ownership, copyright and disclosure, and the final project brief."""),

("quote", "One line to take home", "Nothing generated should float.",
"Light, color, grain, edges. In that order.",
"""Nothing generated should float. Light, color, grain, edges. [Demo.]"""),
]

if __name__ == "__main__":
    build(SPEC, OUT)
