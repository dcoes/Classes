# H8 — After Effects & File Discipline
**CA 140 Storyboarding · Issued Session 12 · Keep this for PR3 and PR4**

> The five operations you need, the settings that break things, and the file habits that decide whether your animatic takes an afternoon or a weekend. This outlives the demo.

---

## Part 1 — The five operations

### 1 · Import a `.psd` with its layers

**File → Import → File**, then set **Import As: Composition — Retain Layer Sizes.**

| Setting | What you get |
|---|---|
| **Footage** | One flat image. Nothing is separable. |
| **Composition** | Layers, resized to the comp. |
| **Composition — Retain Layer Sizes** | Layers at their own dimensions, with usable anchor points. **Use this one.** |

Getting this wrong at import costs you the whole session, and it is not obvious until you try to move something.

### 2 · Anchor points

**The anchor point is the joint.** A layer rotates and scales around it, and by default it sits in the middle of the layer — which is almost never where a joint is.

Press **Y** for the Pan Behind tool, then drag the anchor to the shoulder, the hip, the hinge. Press **V** to get back.

An arm rotating around its own middle looks like a propeller. An arm rotating around the shoulder looks like an arm. That is the entire difference, and it is one drag.

### 3 · Parenting

In the timeline, use the **Parent & Link** column: pick the child layer, drag its pick-whip to the parent.

The child now inherits the parent's position, rotation and scale, and **keeps its own on top.** Move the body and the arm goes with it. Rotate the arm and only the arm moves.

Build the chain outward from the root: body → upper arm → forearm → hand.

> A parented layer's values are now *relative to the parent.* This surprises everyone once. It stops surprising you after that.

### 4 · Masks

Select a layer, take the **Pen tool (G)**, and draw a closed shape on it. Everything outside the shape disappears.

**The move that matters:** to make something in a flat background pass *in front of* a character —

1. Duplicate the background layer (**Ctrl/Cmd + D**)
2. Mask the copy down to just the thing that should be in front — the doorway, the pillar, the foreground wall
3. Drag that copy **above** the character in the layer stack

The character now walks behind it.

**Mask Feather** softens the edge. A 1–2 pixel feather hides a lot of imprecision and costs nothing.

### 5 · Import a numbered sequence

Name your panels `SEQ01_SH010.png`, `SEQ01_SH020.png`, `SEQ01_SH030.png` — **incrementing by ten.**

In the import dialog, select the first file and tick **PNG Sequence**. They come in as a single footage item, one frame each.

Increment by ten so you can insert `SH015` later without renaming everything downstream. You will need to. Everyone does.

---

## Part 2 — Settings that break things

**Frame rate.** Pick 24 or 30 at the start of the project and **never change it.** Changing frame rate mid-project shifts every keyframe you have already set.

**Composition size.** Match your delivery ratio. 1920 × 1080 for 16:9. For 1.85 : 1, 1920 × 1038. For 2.35 : 1, 1920 × 817.

**Work at 2× anywhere you have planned a push or a pan.** You cannot invent detail you didn't draw. A pan needs artwork wider than the frame; a push needs artwork larger than the frame. Decide this *before* you draw the panel, not in the timeline.

**Export.** File → Export → **Add to Adobe Media Encoder**, preset **H.264 / Match Source – High Bitrate**. The default *AVI / Lossless* output from the render queue produces files in the gigabytes and won't play for anyone.

If Media Encoder isn't available: render queue → Output Module → Format **QuickTime**, Codec **H.264**.

---

## Part 3 — File discipline

This is graded on PR3, and it is the part of the job nobody teaches until someone loses a week to it.

### Naming

```
SEQ01_SH010_v03.psd
PROJECT_animatic_v07.aep
lastname_PR3_animatic_v02.mp4
```

- **No spaces.** Underscores.
- **Version numbers are zero-padded** — `v03`, not `v3`. Otherwise `v10` sorts before `v2`.
- **`final` is not a version number.** Neither is `final_FINAL`, `final_real`, or `final_actual_v2`. Everybody laughs at this and everybody does it.

### Structure

```
project/
  01_boards/        panels, layered
  02_exports/       flattened PNGs, numbered by ten
  03_audio/         temp music, scratch dialogue, sfx
  04_project/       .aep files
  05_renders/       output movies
  sources.txt       where every audio file came from
```

### Panels for an animatic

- **Separate files or artboards** — not one big page. The page layout is for the printed board; the animatic wants individual frames.
- **Anything that moves independently gets its own layer, with the hole behind it filled.** An arm you plan to raise needs the torso drawn underneath it.
- **Deliver both `.psd` and `.png`.**

Sloppy file prep is not a minor sin. It makes the next three stages take four times as long — which is exactly what it does on a real production, at four times the cost.

### Versions

Save a new version before any change you might want to undo tomorrow. Disk is free; your Sunday is not.

Keep **at least three timing passes** of your animatic as separate files. PR3 asks you to show them, and reconstructing them afterward is both obvious and more work than saving them was.

### Audio sources

Every temp track, every sound effect, logged in `sources.txt` with where it came from and its licence. Freesound, YouTube Audio Library, Pixabay, Incompetech, CC-licensed tracks.

The industry pulls temp music from released films and replaces it later. **You can't** — because you want to be able to show this work, and a portfolio piece with an unlicensed track is a portfolio piece you have to take down.

---

## The thing worth carrying out of this

**The move you want determines the artwork you need.**

Every awkward moment in After Effects traces back to a decision made — or not made — while drawing. A doorway that isn't its own layer. A pan with no artwork past the frame edge. An arm drawn overlapping the torso it has to rotate away from.

You find this out either by planning it, or by discovering it at 2am. The tool is not the subject. The planning is.
