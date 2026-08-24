# Lesson: Boarding for Games and Interactive

**CA 140 Storyboarding · Class notes**

> Everything this term was built for a medium where somebody controls the camera, the running time, and the order events happen in. Games take all three away. This lesson is a stress test on the whole course: what survives having its assumptions removed was never a film convention. It was a system.

---

## What doesn't change: the cutscene

A cutscene is a film. It gets boarded exactly the way every deck this term has been boarding: shot sizes, angles, the 180-degree rule, match on action, eyelines, coverage, all identical. Nothing from the first part of this course gets thrown out inside a games studio. Cinematic stills from any big-budget game are readable using nothing but the vocabulary from Deck 03: over the shoulder, low angle, extreme close-up, a two-shot with the line held across the cut. The grammar built this term isn't a student version of the real thing. It's the real thing.

## Why a whole lesson, then

A game contains a second thing that sits alongside its cutscenes, and that second thing isn't a film: it's gameplay, and almost nobody teaches how to board it. Boarding gameplay breaks four assumptions every earlier lesson quietly depended on.

## The four breaks

**You don't control the camera.** In a cutscene, the board artist holds it, and it boards as film. In open gameplay, the player holds it, and any panel drawn is a guess about one of thousands of possible views. In between sits cinematic gameplay, a negotiation: the player has control, but the level, lighting, and sightlines are built to make certain framings likely. That middle case is where most of the interesting work happens.

There are recognizable camera archetypes, each a different set of compositional constraints: first person (no character ever in frame, so the language of performance moves to hands, voice, and the world); third-person over-the-shoulder (a permanent obstruction in one corner of every composition); fixed cameras (the classic *Resident Evil* approach, the most film-like, since the designer chose the angle); and isometric, side-scroll, and top-down, each flattening a different axis to make a different kind of information easy to read. A board has to know which of these it's operating in before anything else.

Boarding a camera nobody owns means boarding the space rather than the view: the panel becomes what *could* be seen from here, not what *is* seen. That sounds like giving up authorship, but it only moves the authorship elsewhere, into where things are placed, what's lit, what's tall enough to see over, what draws the eye from a doorway. It's still composition. It's composing the conditions rather than the frame.

This is where the floor plan, already used for the line of action, camera height, the light plan, and blocking, stops being optional. In film, the floor plan is a helpful tool nobody enforces. In games, it's the primary document, because the camera moves through the space rather than being placed in it, and the only way to reason about what a player will see is to reason about the space itself.

Without a camera to point, attention has to be directed environmentally: light (the brightest thing in a dark space wins, every time), color used as a system, motion in the periphery that turns heads involuntarily, audio (criminally underrated, capable of turning a player around with no visual cue at all), and architecture, building a space so the comfortable sightlines from an entrance land on what matters. Level designers are composing shots nobody will ever draw.

There's also a spectrum of agency worth knowing at all times: full player control, a soft-locked camera, a forced look where the game turns the player's head, and a full cutscene. Where a moment sits on that line determines how much can be composed versus how much has to be designed instead, and modern games slide along it constantly, sometimes within a single minute.

**You don't control the timing.** A player might move through a space in eight seconds or wander it for six minutes. Every timing tool from the animatics lesson assumed a fixed, designable duration. That assumption doesn't hold here: the job is designing something that works across a wide range of durations, not designing one duration.

One consequence: boards shift from describing moments in a sequence to describing **states**. Before a pickup, after a pickup, on failure, on retry, what a room looks like the second time it's entered. Panels stop describing a timeline and start describing conditions, which is where game boards start looking like documentation, because in part, they are.

Another consequence: players see the same content many times, through death, backtracking, or a loop built into the design. Something dramatic once is tedious the fifth time, a genuine design constraint with no equivalent in film, since a film shows every frame exactly once.

The single most scrutinized cut in the medium is the handoff between gameplay and cutscene, and back. Match the camera position and character pose across that seam, or it screams: a player standing at a door in a wide shot, followed by a cutscene opening on a close-up from the other side of the room, is felt by everyone even if they can't say why.

**You don't control the order.** Branching paths, optional content a player may never see, missable beats, and non-linear exploration mean a sequence isn't a sequence, it's a set of things that might happen, in an order nobody controls, some of which won't happen at all. The document that results looks alien to someone arriving from film: a flowchart with panels hanging off it, one node per beat, arrows for the choices between them (sometimes called a beat map or narrative flow). It's mostly a floor plan for time instead of space.

This forces a resourcing decision that's a real job skill: what must every player see? That's the critical path, and it gets boarded fully, since it carries the story everyone experiences. Everything else is optional content, boarded as key frames only, the important moment rather than full coverage. Making that call, and defending it, is worth more than drawing twice as fast.

The most extreme version of order-independence is **environmental storytelling**: a room with nobody in it, telling you what happened there. Two chairs pulled close together, a meal half eaten, a door barricaded from the inside. No camera, because the player brings their own. No character, because nobody's there. No cut, because nothing is edited. And it's unmistakably staging: somebody decided where everything sits and what the eye finds first. Staging never needed the camera, the cut, or the actor.

**You don't control the whole frame.** A permanent interface lives in it: HUD, health, minimap, reticle, subtitles, objective markers, prompts, some permanent, some appearing when least wanted. Rule-of-thirds intersections may already be occupied, and the bottom third of the frame may be spoken for. Composing around what's permanently there is a constraint film simply doesn't have, but it's not a reason to abandon composition, it's a reason to know the frame that actually exists rather than the one on a template.

This connects to the aspect-ratio mismatch problem from Class 2, with more variables and higher stakes: the same content plays on a handheld six inches from a face, a television across a room, an ultrawide monitor, and a phone, all at once, rather than being remastered per format. Text legibility on the smallest target sets type size everywhere; critical information has to sit inside the tightest safe area.

## Readability and accessibility

The silhouette test returns, now with real money attached. A player has to distinguish an enemy from a barrel from a health pickup at small size, in motion, under pressure, often in bad light, and the only thing that reliably survives all of that is the outline. Character silhouette design in games is a genuine hiring criterion; studios test for it, and some people's entire job is making sure two enemy types don't read the same at a distance. Same test as week one, with a black marker. Higher stakes.

Accessibility belongs in this discussion because it's a composition problem, not a compliance checkbox. If the only difference between a safe object and a dangerous one is red versus green, a meaningful share of players can't play the game; the fix is shape, value, or motion (or all three), made as a design decision early. Subtitle space has to exist in the composition. Contrast minimums constrain the value structure. This is increasingly a legal and commercial requirement rather than a nicety.

## What game boards actually look like, and who reads them

Several kinds of document live under this job: cinematic boards, identical to standard film boards; gameplay previs, closer to blocking in 3D; flow diagrams for branching; beat maps; and level layouts with camera sketches, the floor plan doing its job again. These frequently live inside a larger design document rather than standing alone, which means writing as well as drawing.

A film board goes to people executing a fixed plan. A game board goes to designers, engineers, level artists, animators, audio, and UI, people who are going to build something interactive out of it. They need intent, not just image: why is the door on that side, what's the player supposed to feel coming around this corner, what happens if they approach from the other direction. Annotation matters as much as the panel; a beautiful board with no reasoning attached is close to useless to them.

## Where this skill gets hired

Cinematic artist, previs artist, narrative designer, level designer, and UX all hire the exact skill set this course teaches. Several hire on breakdown ability and staging judgment rather than rendering, and the field is considerably less crowded than feature animation.

Worth knowing as neighboring territory: VR and 360 video, where there's no frame at all and the job is staging a room and hoping; AR, compositing onto a world nobody built; immersive theater, which solved a lot of these problems decades before games did; and interactive film. In VR, the entire discipline of framing evaporates, and what's left is staging, a good argument that staging was always the real subject, and framing was one very successful way of delivering it.
