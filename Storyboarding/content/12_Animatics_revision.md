# Lesson: Animatics

**CA 140 Storyboarding · Class 11 notes**

> A storyboard tells you what's in a shot. It cannot tell you how long that shot stays on screen. That's why animatics exist.

---

## What an animatic is

An animatic is a moving storyboard: panels cut together and timed, so a director can see how scenes actually flow into one another. Everything already learned about boards still applies; this is the same artwork with a fourth dimension added. The pipeline runs script, then boards, then animatic, then production. Panels get brought into editing software and given a duration, sound goes underneath, and for the first time, someone can watch the film before the film exists.

There's no fixed rule for how this gets done; different studios and directors run different workflows, and the artist keeps creative license throughout, if a beat needs to breathe longer than a stopwatch says, hold it longer. What isn't optional is doing it at all: without a well-timed animatic, a shot can take three or four times longer to build in production.

Almost everyone on a production ends up using the animatic. Directors use it to see whether an imagined sequence actually works. Animators use it as a timing template and animate to those holds, frame for frame. Actors working opposite a computer-generated character use it to know what they're reacting to and when. Effects artists use it to find timing problems while they're still cheap to fix. Voice actors and sound designers use it to feel a scene's rhythm. It's often the single document an entire production is looking at.

## Four kinds of animatic

**Hand-drawn animatics**, essentially timed storyboards, are still the most common form in animation: boards cut to length, with sound, simple to produce, and effective for communicating action a static page can't convey.

**Motion tests**, including pencil tests (rough drawings shot in sequence, watched at speed, previewing motion before committing to cleanup) and motion previews (exploring camera movement, character placement, timing, and pacing). Before anyone could render a space battle, George Lucas cut together real World War Two aerial dogfight footage to preview the trench run in *Star Wars*, not testing the visuals, testing the rhythm.

**Videomatics** are rough live-action versions of a scene, shot with whoever's standing around, to work out blocking, placement, timing, and camera angles, usually shot on the studio lot against bluescreen, with minimal directing and plain cinematography, since the point isn't to look good but to test the script, timing, and feel of the shot.

**3D animatics** are built from computer-generated material instead of drawings, increasingly the default on large live-action films, where it's called previs, a real department with real job titles. A 3D artist builds low-resolution proxy models understanding all of it gets replaced later, then animates a rough layout pass. The advantage over drawn panels is a freely movable camera and setups that would be expensive to draw; the disadvantage is a slower first version and the temptation to fiddle with the model instead of solving the shot.

A **rough cut** is an animatic that never dies: it gets updated continuously as production develops, with finished shots gradually replacing boarded ones, so the film is always watchable start to finish at every stage. As each shot is approved it replaces its animatic panel, and the updated cut goes back for review. One important detail: a rough cut should reflect the techniques the finished shot will use. If a shot needs an effect, an approximation of that effect belongs in the rough cut, otherwise a version of the film that doesn't exist is what's being approved.

## Software, briefly

Photoshop and After Effects are the common pairing, and they overlap deliberately: Photoshop for the still image and its manipulation, After Effects for much of the same work in motion. Dedicated tools exist too (Storyboard Pro is the industry standard, doing boarding and animatic timing in one application; FrameForge, Storyboard Quick, and Shot Master are others worth recognizing by name). Worth remembering before diving into file formats and export settings: storyboards are not about software, they're about stories. Technology is only the means for articulating and executing a vision.

## File discipline

Work at a resolution larger than the delivery size, 1920×1080 is a baseline for 16:9, and consider working at 2x for room to push and pan. Storage is free; redrawing is not, and you can always scale down but never scale up.

The multi-panel page (three panels on one sheet) is a document for humans to read on paper or screen. An animatic needs each panel as its own image file, same drawings, two different deliverables. Set up artboards or separate documents from the start to avoid an hour of cropping later.

**Naming and numbering**: increment shot numbers by ten, not by one (`SEQ01_SH010.png`, `SEQ01_SH020.png`), so a shot requested between 020 and 030 can be named 025 without renaming everything after it. Zero-pad the numbers so they sort correctly, without it, a computer sorts shot 10 before shot 2.

**Export as PNG** for anything going into an animatic: lossless, supports transparency, universally supported. JPG is only for flat stills that will never be re-edited, since it throws away data every time it's saved. Keep the layered PSD as the master and export the PNG as what gets handed to After Effects. Keep both, always.

**Separating elements for motion**: anything that moves independently needs its own layer, a waving arm, a walking figure, a foreground element the camera pushes past. Cut the element out, put it on its own layer, and fill the hole left behind, a step that gets forgotten until the first motion preview reveals the gap. The Marquee tool selects large rectangular or elliptical areas; the Magic Wand selects large flat-value areas (effective on board art, since most panels are mostly flat); the Lasso is for freehand; the Pen tool handles anything with a clean curved edge, converted to a selection when finished. Whatever the tool, name the resulting layer, not for tidiness, but to be able to find it again two weeks later.

**Pans and pushes**: for a pan, draw wider than the frame. For a push, draw at higher resolution than the frame. For a tilt, draw taller than the frame. Detail that was never drawn cannot be invented later, so plan the move before drawing the panel, not after.

Bringing panels into After Effects works two ways: import as a PNG sequence, treating panels like frames of footage in one retimeable clip, or import as individual layers, giving one layer per panel stretched to whatever hold length is wanted, usually easier to control for a board-driven animatic. Set the composition's frame rate before starting to time anything; changing it later reinterprets all existing timing.

## Sound changes everything

An animatic without audio is a slideshow. An animatic with audio is a film. Play the same twenty seconds silent, then with a temp music track under it, and it's not the same piece of work, even though nothing about the drawings changed. This is about the cheapest improvement available on this project, and it's often skipped simply because it doesn't feel like it's on the list of graded things.

What goes under it: temp music to establish tone and drive pacing, ambience so the world feels inhabited, a few key sound effects only where they carry a beat, and scratch dialogue, recorded on a phone, badly, by the artist themselves. That's standard professional practice at this stage, not a shortcut: timing needs something to time against, and a silent animatic with dialogue means guessing at every line's length, and guessing wrong.

Source audio legally: Freesound, YouTube Audio Library, Pixabay, Incompetech, and look for Creative Commons or royalty-free licenses. In the industry, temp tracks get pulled from released films and swapped before anything ships; that luxury doesn't exist for a portfolio piece, which is the version that goes on a reel, so it needs to be shown without being taken down later. Credit sources; it costs nothing now and protects the work later.

## Timing

Every production has a specified length, whether a 30-second spot or a two-hour feature, a fixed container to work inside. The mood and pace of the whole thing comes from the cutting and motion of every scene, and acting affects the timing of every shot, a character who hesitates needs the extra beat. Bad timing is obvious in any medium, felt by an audience even by people who couldn't say what a cut is.

Timing does for images what it does for notes in music: it's what turns a set of drawings into something with rhythm. Two failure modes, and they're opposites. Too long, and the pace drags and the audience gets bored. Too short, and the shot is ambiguous and the audience is confused. Both feel like "this animatic is bad," and they need completely different fixes; telling them apart is most of the skill.

Starting points for hold length, not rules: an establishing shot, 3-4 seconds. A wide shot with new information, 2-3 seconds. A dialogue beat, around 2 seconds. A reaction, 0.75-1.5 seconds. An insert or detail, 0.5-1 second. An action cut, as fast as it still reads. A held silence for effect, 2-5 seconds. These exist to be deviated *from*; guessing from zero is why timing feels random and why a bad animatic becomes hard to diagnose. Start here, watch it back, then break these numbers on purpose. Deliberately holding a reaction for four seconds is a directing choice. Accidentally holding it for four seconds is a mistake. From the outside they look identical, so it matters to know which one is happening.

If a shot's ideal length isn't obvious, make an educated guess and move on rather than stalling; the animatic exists precisely to block out timing, and nonlinear editing software makes adding or removing frames trivial. Budget for multiple passes and don't treat the first one as a verdict.

The single most important technical factor in timing is **frame rate**: frames per second is the ruler, how many frames equal one second of real time, and frame count, blocking, dialogue tracks, and camera movements are all measured against it. Film runs at 24 fps, broadcast television at 30, games vary widely and often target 60, and modern high-frame-rate cameras are what let a director slow time down smoothly rather than stretching frames. Pick a frame rate at the start and never change it mid-project.

## Building a sense for timing

Some people have a natural sense for timing; most don't, and that includes plenty of working professionals. It's a learned skill, developed with a stopwatch, actually used rather than owned. Observing the real world is the other half: video reference is a crucial professional tool, not a beginner's crutch. Long before motion capture existed, animators shot film reference to understand timing and find natural poses. No matter the skill level, reference makes the work better, and what it captures isn't just the gesture and not just the timing, but the relationship between the two, which is nearly impossible to invent from imagination alone.

## Previs, AI, and what the job actually is

Previs is now a real department on most large productions. Generative tools can produce panels quickly, and studios are testing them. What they can't do: know which shot serves *this* story, hold a sequence in their head, or take a note and understand what it really meant. That judgment is the job. The drawing was only ever how it got delivered.
