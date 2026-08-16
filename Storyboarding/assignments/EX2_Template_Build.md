# EX2 Template Build
**50 points · Assigned Session 2 · Due Session 3**
**Rubric:** [`rubrics/EX2_Template_Build.md`](../rubrics/EX2_Template_Build.md)
**Handout:** H1 (Notation)

---

## The assignment

Build the storyboard templates you will use for every other assignment in this course. **Three of them**, one per aspect ratio:

| Ratio | Where it comes from |
|---|---|
| **1.33: 1** | Academy. Television until the 2000s. Most classic animation. |
| **1.85: 1** | The standard theatrical widescreen. Your default for the rest of the term. |
| **2.35: 1** | Anamorphic. Epics, westerns, anything that wants the horizon. |

Each sheet: **4 panels across, 8 rows down. ¼″ between panels. 2″ margin from the edge of the page.** The project name goes top left, ¼″ above the first row of panels, flush with the left margin. Your name goes in the opposite corner, same treatment.

---

## Why this is assignment two

Before you compose anything, before you stage anything, before you decide where the camera goes. You have to know the shape of the frame.

If your template is the wrong shape, every panel you draw this month is composed for a frame that doesn't exist. Headroom, lookroom, leadroom, every relationship between a subject and an edge. All of it recalculated the moment the ratio changes. You would redraw all of it.

Three templates instead of one, because **the frame shape is a decision, not a default.** You will feel the difference the first time you try to stage two people in 1.33 and then in 2.35. That is the point of building all three.

---

## The arithmetic

Two formulas. That's the whole thing.

> **Frame height × ratio = frame width**
> **Frame width ÷ frame height = ratio**

A 4 × 3 screen is 4 ÷ 3 = 1.33: 1. A panel 2″ wide at 1.85: 1 is 2 ÷ 1.85 = 1.081″ tall.

But you are not choosing a panel size. **The page is choosing it for you**, and working out how is the actual exercise:

**1 · Panel width comes from the horizontal fit.** Four columns and three ¼″ gutters have to live inside the page minus two 2″ margins.

```
panel width = (page width − 4″ of margin − 0.75″ of gutter) ÷ 4
```

**2 · Panel height comes from the ratio.** `height = width ÷ ratio`

**3 · Then check whether eight rows actually fit.**

```
8 panels + 7 gutters  =  (8 × panel height) + 1.75″     ≤  page height − 4″
```

Do this before you draw a single guide. Do it for all three ratios.

---

## What you will find, and what to do about it

On **letter portrait (8.5 × 11)** the numbers come out like this:

| | 1.33: 1 | 1.85: 1 | 2.35: 1 |
|---|--:|--:|--:|
| Panel width | 0.9375″ | 0.9375″ | 0.9375″ |
| Panel height | 0.705″ | 0.507″ | 0.399″ |
| 8 rows + gutters | **7.390″** | 5.804″ | 4.941″ |
| Fits in 7″? | **No** | Yes | Yes |

**At 1.33: 1, eight rows does not fit.** Not by a little: by four tenths of an inch, and no reasonable margin change rescues it.

That is not a mistake in the assignment. It is the assignment. A taller frame eats more vertical space, so a page holds fewer of them. **Frame shape has consequences that run all the way out to how much paper you need**, and you just found one.

So you have a decision to make, and either answer earns full credit if you show the working:

- **Drop to 7 rows at 1.33: 1** (7 × 0.705 + 1.5 = 6.435″: fits) and keep 8 at the other two.
- **Move to tabloid portrait (11 × 17)**, where panel width becomes 1.5625″ and all three ratios fit 8 rows comfortably. Bigger panels, and you'll be happier drawing in them, if you can print it.

**Report which one you chose and why, in one line, on the sheet.** That line is worth points.

---

## A note on 2.35 and 2.39

You will see both numbers, and people will tell you the other one is wrong.

**2.35: 1** is the CinemaScope/anamorphic spec, and it is what was actually projected from the 1950s through about 1970. **2.39: 1** has been the SMPTE standard since, and it is usually written 2.40 in a spec document.

**Build 2.35 for this course.** But know that there are two numbers, know which is which, and know that "widescreen" was never one fixed thing. It was a moving commercial argument between studios and television. That history is the actual content of Session 2.

---

## What each panel needs room for

Underneath every panel, space for:

| | |
|---|---|
| **Panel / shot number** | `SEQ 01 / SC 04 / SH 010` |
| **Shot size and angle** | `MS, low angle` |
| **Action description** | One line, present tense |
| **Camera notation** | Room for arrows and move labels |

Look at **H1** for the notation you're leaving room for. Don't guess the layout. You'll be filling this in for four weeks, and the field you skip now is the one you'll be cramming into a margin later.

---

## What to deliver

1. **Three layered source files**: `.psd`, or any format that preserves layers and opens in Photoshop or Photopea. One per ratio.
2. **Three flattened exports**: `.png` or `.jpg`.
3. **Your arithmetic**, on the sheet or in a separate page: panel width, panel height, and the row check for each ratio.
4. **The one-line decision** about the 1.33 problem.

Named per the convention in H1. Post before Session 3 begins.

---

## Software

Photoshop, or **Photopea**: free, runs in a browser, opens and saves `.psd`.

Use **guides and shape layers**, not eyeballed rectangles. If you have never opened Photoshop, say so. The prerequisite is not reliably enforced and you will not be the only one. There is a demo in Session 2, and I would much rather spend ten minutes on it than have you lose fifty points to a file format.

---

## What is not graded

**Drawing.** There isn't any in this assignment.

**Decoration.** A template with a designed header is not a better template. It's a template with a designed header.

---

## The two ways people lose points here

**"About right" instead of measured.** Partial credit exists for an arithmetic slip where the working is visible. It does not exist for a guess, because a guess has nothing to give partial credit to.

**Width and height swapped.** Check which number is which. A 2.35: 1 panel is much wider than it is tall. If yours isn't, you divided when you should have multiplied.
