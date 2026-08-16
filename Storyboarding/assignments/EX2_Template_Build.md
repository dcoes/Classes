# EX2 Template Build
**4% of the course grade · Assigned Class 2 · Due Class 3**
**Rubric:** [`rubrics/EX2_Template_Build.md`](../rubrics/EX2_Template_Build.md)
**Handout:** H1 (Notation)

---

## The assignment

Build the storyboard templates you will use for every other assignment in this course. **Three of them**, one per aspect ratio:

| Ratio | Where it comes from |
|---|---|
| **1.33 : 1** | Academy. Television until the 2000s. Most classic animation. |
| **1.85 : 1** | Standard theatrical widescreen. Your default for the rest of the term. |
| **2.39 : 1** | Anamorphic scope. Epics, westerns, anything that wants the horizon. |

Each sheet: **8 panels across, 4 rows down. A quarter inch between panels. A 2 inch margin from the edge of the page.** The project name goes top left, a quarter inch above the first row of panels, flush with the left margin. Your name goes in the opposite corner, same treatment.

Then build a **second sheet per ratio**, with bigger panels. Described below.

---

## Why this is assignment two

Before you compose anything, before you stage anything, before you decide where the camera goes, you have to know the shape of the frame.

If your template is the wrong shape, every panel you draw this month is composed for a frame that doesn't exist. Headroom, lookroom, leadroom, every relationship between a subject and an edge, all of it gets recalculated the moment the ratio changes. You would redraw all of it.

Three templates instead of one, because **the frame shape is a decision, not a default.** You will feel the difference the first time you stage two people in 1.33 and then in 2.39.

---

## About that third number

You will see **2.35 : 1** in plenty of places, including older textbooks, and someone will tell you 2.39 is wrong. Here is the actual history.

2.35 was the CinemaScope spec once optical sound took its bite out of the frame, and it was accurate from about 1953 to 1970. In 1970 SMPTE revised the projection aperture slightly, and **2.39 : 1 has been the standard ever since.** In a spec document you'll usually see it written 2.40. DCI Scope is exactly 2.39 : 1, which is 2048 x 858 pixels.

So both numbers are real, they describe the same format, and they are about seventeen years apart. **Build 2.39.** Say "two thirty-five" out loud like everyone else if you want, but know which number is current and why there are two.

That is the actual content of this class. Widescreen was never one fixed thing. It was a commercial argument between the studios and television, fought with aspect ratios, and the numbers are the fossil record.

---

## The arithmetic

Two formulas. That's the whole thing.

> **Frame height x ratio = frame width**
> **Frame width / frame height = ratio**

A 4 x 3 screen is 4 / 3 = 1.33 : 1. A panel 2 inches wide at 1.85 : 1 is 2 / 1.85 = 1.081 inches tall.

But you are not choosing a panel size. **The page is choosing it for you**, and working out how is the exercise.

**1 . Panel width comes from the horizontal fit.** Eight columns and seven quarter-inch gutters have to live inside the page minus two 2 inch margins.

```
panel width = (page width - 4" of margin - 1.75" of gutter) / 8
```

**2 . Panel height comes from the ratio.**

```
panel height = panel width / ratio
```

**3 . Then check the rows fit.**

```
4 panels + 3 gutters = (4 x panel height) + 0.75"   must be <=   page height - 4"
```

Do all three, for all three ratios, before you draw a single guide.

---

## What you will find

| | 1.33 : 1 | 1.85 : 1 | 2.39 : 1 |
|---|--:|--:|--:|
| **Letter landscape, 11 x 8.5** | | | |
| Panel width | 0.656" | 0.656" | 0.656" |
| Panel height | 0.493" | 0.355" | 0.275" |
| 4 rows plus gutters | 2.72" | 2.17" | 1.85" |
| Fits inside 4.5"? | yes | yes | yes |
| **Tabloid landscape, 17 x 11** | | | |
| Panel width | 1.406" | 1.406" | 1.406" |
| Panel height | 1.057" | 0.760" | 0.588" |
| 4 rows plus gutters | 4.98" | 3.79" | 3.10" |
| Fits inside 7"? | yes | yes | yes |

**Everything fits. That is not the interesting part.**

The interesting part is that on letter paper your panels are two thirds of an inch wide. You cannot board in that. You can *thumbnail* in it, which is a real and useful thing, but a finished panel needs more room than that.

So the grid you were given is a **working sheet**, and finding that out by measuring it is the point of the exercise.

---

## The second sheet

Build a **presentation sheet** for each ratio, using the same rules with two numbers changed: **3 columns instead of 8, and 3 rows instead of 4.** Same quarter-inch gutters, same 2 inch margins.

On letter landscape that gives you:

```
panel width = (7" - 0.5" of gutter) / 3 = 2.167"
```

Nine panels at 2.167 inches wide, which is a bit over three times the working sheet. Drawable.

**From here on the two sheets have different jobs:**

- **Working sheet**, 32 small panels: thumbnails, exploration, anything disposable.
- **Presentation sheet**, 9 large panels: finished boards, anything submitted as final art.

That division is not bookkeeping. A thumbnail scaled up from 0.656 inches to 2.167 inches looks exactly like what it is, so you cannot quietly promote a thumbnail into a final panel. If that turns out to be inconvenient later, it's the mechanism doing its job.

---

## What each panel needs room for

Underneath every panel on the **presentation sheet**, space for:

| | |
|---|---|
| **Panel / shot number** | `SEQ 01 / SC 04 / SH 010` |
| **Shot size and angle** | `MS, low angle` |
| **Action description** | One line, present tense |
| **Camera notation** | Room for arrows and move labels |

Look at **H1** for the notation you're leaving room for. Don't guess the layout. You'll be filling this in for four weeks, and the field you skip now is the one you'll be cramming into a margin later.

The working sheet needs none of that. It's for thinking.

---

## What to deliver

1. **Six layered source files:** three working sheets, three presentation sheets. `.psd`, or any format that keeps layers and opens in Photoshop or Photopea.
2. **Six flattened exports,** `.png` or `.jpg`.
3. **Your arithmetic,** on the sheet or on a separate page: panel width, panel height, and the row check, for every ratio and both layouts.

Named per the convention in H1. Post before Class 3 begins.

---

## Software

Photoshop, or **Photopea**, which is free, runs in a browser, and opens and saves `.psd`.

Use **guides and shape layers**, not eyeballed rectangles. If you have never opened Photoshop, say so. The prerequisite is not reliably enforced and you will not be the only one. There's a demo in Class 2, and I would much rather spend ten minutes on it than have you lose the assignment to a file format.

---

## What is not graded

**Drawing.** There isn't any in this assignment.

**Decoration.** A template with a designed header is not a better template. It's a template with a designed header.

---

## The two ways people lose points here

**"About right" instead of measured.** Partial credit exists for an arithmetic slip where the working is visible. It does not exist for a guess, because a guess has nothing to give partial credit to.

**Width and height swapped.** Check which number is which. A 2.39 : 1 panel is much wider than it is tall. If yours isn't, you divided where you should have multiplied.
