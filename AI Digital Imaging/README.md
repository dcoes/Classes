# AI Digital Imaging: lectures

Built October 2026 from the block course outline (16 sessions) and the Canvas rubrics.

## What's here

| Folder or file | What it is |
|---|---|
| `lectures/` | Sixteen lectures, one per session, `01` to `16`. About 50 minutes each on teaching days; sessions 7, 12, 14 and 16 are critique days with a shorter opening (about 30 minutes, or 15 plus 15 on the last day). |
| `bridge_for_Digital_Imaging_and_Painting/` | Three stand-alone lectures that bring the thinking behind AI workflows into the painting course as it stands. Students generate nothing. `B2` is written as that course's session 12 lecture (the paint-over), with the outline's own options; `B1` and `B3` can run as extra meetings or in place of a lighter lecture. |
| `PREP_AND_IMAGE_LIST.md` | What to make or check before each class, and every image slot by slide number. Regenerate it after any change. |
| `images/` | Diagrams and demo images made for these lectures, from scratch or from scikit-image's bundled sample photos. Nothing copyrighted. |
| `build_decks/` | The build scripts, one per lecture, plus `aikit.py` (helpers) and `gen_images.py`. |

## How every lecture is laid out

Title slide (speaker notes: running time by block, prep), a "Spot it" warm-up from session 2 on, a recall slide, the lecture, one worked example followed by a cold reversal with no answer shown, at least one "In the wild" case for discussion, a "Words from today" glossary slide, the A/B options slide, and a closing line. Slide text is short; the full spoken script is in the speaker notes, with stage directions in square brackets.

Image slots are dashed boxes labeled with what goes in them. Drag the picture in, size it over the box, delete the box.

## Rebuilding

From the repo root:

```
python3 "AI Digital Imaging/build_decks/gen_images.py"
for f in "AI Digital Imaging/build_decks/"[sb][0-9]*.py; do python3 "$f"; done
python3 "AI Digital Imaging/build_decks/make_prep_sheet.py"
```

The theme comes from `Storyboarding/NewLectures/07_Storytelling_through_Lighting_REVISED.pptx`, loaded as the base file with its slides cleared, the same method as `Storyboarding/build_decks/deckkit.py`. Rebuilding overwrites the .pptx files, so any images you've dropped into slots by hand need to go back in afterwards; edit the script and rebuild only for text changes, or edit the .pptx directly once the images are in.

## Things to check each time the course runs

- Session 9's copyright and court-case slides (current as of October 2026).
- Which generative features and models are on the lab's Adobe license, and their menu names (sessions 1, 3, 6, 8, 11, 15).
- The GDC survey figures in session 1 and bridge lecture 1 (2026 report).
