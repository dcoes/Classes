"""Deck helpers for the AI Digital Imaging lectures (and the bridge lectures).

Same method as Storyboarding/build_decks/deckkit.py: copy a finished deck as the
theme carrier, strip its slides, add new ones, so masters, fonts and layouts are
inherited rather than approximated (CLAUDE.md section 3).

Additions over deckkit: right-side and full-width image placement using the
coordinates taken from Deck 07's real layout, an image slot for pictures the
instructor supplies, speaker notes with **bold** beats, and a standard A/B options
slide.

Each lecture script calls build(spec, out_path), where spec is a list of slide
tuples. Run any lecture script from the repo root.
"""
import os
import re
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from PIL import Image

THEME_CARRIER = "Storyboarding/NewLectures/07_Storytelling_through_Lighting_REVISED.pptx"
IMG_DIR = "AI Digital Imaging/images"

L_TITLE = 0
L_TITLE_CONTENT = 1
L_SECTION = 2
L_TWO_CONTENT = 3
L_COMPARISON = 4
L_TITLE_ONLY = 5
L_QUOTE = 11

# Coordinates from Deck 07 (inches)
CONTENT_LEFT = (1.42, 2.80, 5.85, 3.70)      # bullets beside a right image
RIGHT_IMAGE = (7.60, 2.70, 4.89, 3.75)       # single right-side image box
FULL_IMAGE = (1.42, 2.62, 10.50, 3.80)       # full width under the title rule
FULL_IMAGE_CAPTIONED = (1.42, 2.60, 10.50, 3.55)

INK = RGBColor(0x2B, 0x2B, 0x2B)
MUTE = RGBColor(0x8A, 0x8A, 0x8A)
ACCENT = RGBColor(0xC0, 0x50, 0x4D)
PAPER = RGBColor(0xF2, 0xF0, 0xEA)


def new_deck(dest):
    shutil.copyfile(THEME_CARRIER, dest)
    prs = Presentation(dest)
    lst = prs.slides._sldIdLst
    for sldId in list(lst):
        rId = sldId.get(
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        prs.part.drop_rel(rId)
        lst.remove(sldId)
    return prs


# ------------------------------------------------------------------ notes
def _add_runs(paragraph, text):
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if not part:
            continue
        r = paragraph.add_run()
        if part.startswith("**") and part.endswith("**"):
            r.text = part[2:-2]
            r.font.bold = True
        else:
            r.text = part


def notes(slide, text):
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    paras = [p.strip() for p in text.strip().split("\n\n")]
    first = True
    for para in paras:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        _add_runs(p, " ".join(line.strip() for line in para.splitlines()))
        p.space_after = Pt(8)
    return slide


# ------------------------------------------------------------------ helpers
def _fill_body(tf, items):
    tf.clear()
    for i, item in enumerate(items):
        text, level = (item, 0) if isinstance(item, str) else item
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        _add_runs(p, text)
        p.level = level


def _place_picture(slide, path, box):
    x, y, w, h = box
    im = Image.open(path)
    ar = im.width / im.height
    if w / h > ar:
        ph = h
        pw = h * ar
    else:
        pw = w
        ph = w / ar
    left = x + (w - pw) / 2
    top = y + (h - ph) / 2
    return slide.shapes.add_picture(path, Inches(left), Inches(top), Inches(pw), Inches(ph))


def _slot(slide, desc, box):
    x, y, w, h = box
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = PAPER
    sh.line.color.rgb = MUTE
    sh.line.width = Pt(1.25)
    sh.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    sh.shadow.inherit = False
    sh.name = "IMAGE SLOT"
    tf = sh.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.text = "image: " + desc
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    for r in p.runs:
        r.font.size = Pt(13)
        r.font.italic = True
        r.font.color.rgb = MUTE
    return sh


def visual(slide, v, box):
    """v is an image filename in IMG_DIR, or 'slot:description'."""
    if v.startswith("slot:"):
        return _slot(slide, v[5:].strip(), box)
    return _place_picture(slide, os.path.join(IMG_DIR, v), box)


def _caption(slide, text, top):
    tb = slide.shapes.add_textbox(Inches(1.42), Inches(top), Inches(10.5), Inches(0.45))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    _add_runs(p, text)
    p.alignment = PP_ALIGN.CENTER
    for r in p.runs:
        r.font.size = Pt(15)
        r.font.color.rgb = INK
    return tb


def _strip_empty(slide):
    for shape in list(slide.placeholders):
        if shape.placeholder_format.idx in (10, 11, 12):
            continue
        if shape.has_text_frame and not shape.text_frame.text.strip():
            shape._element.getparent().remove(shape._element)


# ------------------------------------------------------------------ slide types
def s_title(prs, title, subtitle, note):
    s = prs.slides.add_slide(prs.slide_layouts[L_TITLE])
    s.shapes.title.text = title
    s.placeholders[1].text = subtitle
    return notes(s, note)


def s_section(prs, title, sub, note):
    s = prs.slides.add_slide(prs.slide_layouts[L_SECTION])
    s.shapes.title.text = title
    s.placeholders[1].text = sub
    return notes(s, note)


def s_bullets(prs, title, items, note):
    s = prs.slides.add_slide(prs.slide_layouts[L_TITLE_CONTENT])
    s.shapes.title.text = title
    _fill_body(s.placeholders[1].text_frame, items)
    return notes(s, note)


def s_bullets_image(prs, title, items, v, note):
    s = prs.slides.add_slide(prs.slide_layouts[L_TITLE_CONTENT])
    s.shapes.title.text = title
    body = s.placeholders[1]
    x, y, w, h = CONTENT_LEFT
    body.left, body.top, body.width, body.height = Inches(x), Inches(y), Inches(w), Inches(h)
    _fill_body(body.text_frame, items)
    visual(s, v, RIGHT_IMAGE)
    return notes(s, note)


def s_image(prs, title, v, caption, note):
    s = prs.slides.add_slide(prs.slide_layouts[L_TITLE_ONLY])
    s.shapes.title.text = title
    if caption:
        visual(s, v, FULL_IMAGE_CAPTIONED)
        _caption(s, caption, 6.18)
    else:
        visual(s, v, FULL_IMAGE)
    return notes(s, note)


def s_quote(prs, label, big, caption, note):
    """The big line goes in the quote-marked title; the label sits small under it."""
    s = prs.slides.add_slide(prs.slide_layouts[L_QUOTE])
    s.shapes.title.text = big
    s.placeholders[13].text = label
    s.placeholders[1].text = caption
    return notes(s, note)


def s_two(prs, title, left, right, note):
    s = prs.slides.add_slide(prs.slide_layouts[L_TWO_CONTENT])
    s.shapes.title.text = title
    _fill_body(s.placeholders[1].text_frame, left)
    _fill_body(s.placeholders[2].text_frame, right)
    return notes(s, note)


def s_compare(prs, title, lhead, left, rhead, right, note):
    s = prs.slides.add_slide(prs.slide_layouts[L_COMPARISON])
    s.shapes.title.text = title
    s.placeholders[1].text = lhead
    _fill_body(s.placeholders[2].text_frame, left)
    s.placeholders[3].text = rhead
    _fill_body(s.placeholders[4].text_frame, right)
    return notes(s, note)


def s_options(prs, a, b, note, title="Before next class: pick one",
              heads=("Option A, guided", "Option B, own material")):
    return s_compare(prs, title, heads[0], a, heads[1], b, note)


def s_boxes(prs, title, labels, note, sub=None, accent_last=False):
    """A row of 3 to 6 boxes joined by arrows: a process or a list of parts."""
    s = prs.slides.add_slide(prs.slide_layouts[L_TITLE_ONLY])
    s.shapes.title.text = title
    n = len(labels)
    gap = 0.32
    total_w = 10.5
    bw = (total_w - gap * (n - 1)) / n
    top = 2.95
    bh = 1.85
    longest = max(len(w) for lab in labels for w in lab.partition("|")[0].split())
    fit = int((bw - 0.3) * 72 / (0.75 * max(longest, 1)))
    head_size = max(11, min(22 if n <= 4 else 18, fit))
    for i, lab in enumerate(labels):
        x = 1.42 + i * (bw + gap)
        sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(top), Inches(bw), Inches(bh))
        sh.fill.solid()
        last = accent_last and i == n - 1
        sh.fill.fore_color.rgb = ACCENT if last else PAPER
        sh.line.color.rgb = INK
        sh.line.width = Pt(1.25)
        sh.shadow.inherit = False
        tf = sh.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        head, _, tail = lab.partition("|")
        tf.text = head.strip()
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        for r in p.runs:
            r.font.size = Pt(head_size)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF) if last else INK
        if tail.strip():
            p2 = tf.add_paragraph()
            p2.text = tail.strip()
            p2.alignment = PP_ALIGN.CENTER
            for r in p2.runs:
                r.font.size = Pt(min(16, max(11, head_size - 4)))
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF) if last else INK
    if sub:
        _caption(s, sub, 5.15 + 0.25)
    return notes(s, note)


def s_checklist(prs, title, rows, note, cols=2):
    """Rows of short items laid out as a printed checklist (phone-photo friendly)."""
    s = prs.slides.add_slide(prs.slide_layouts[L_TITLE_ONLY])
    s.shapes.title.text = title
    longest = max(len(r) for r in rows)
    size = 21
    if longest > 30 and len(rows) <= 6:
        cols = 1
    elif longest > 26:
        size = 17
    per = (len(rows) + cols - 1) // cols
    colw = 10.5 / cols
    for i, row in enumerate(rows):
        c, r = divmod(i, per)
        x = 1.42 + c * colw
        y = 2.75 + r * 0.62
        box = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y + 0.1), Inches(0.3), Inches(0.3))
        box.fill.background()
        box.line.color.rgb = INK
        box.line.width = Pt(1.25)
        box.shadow.inherit = False
        tb = s.shapes.add_textbox(Inches(x + 0.4), Inches(y), Inches(colw - 0.5), Inches(0.45))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        _add_runs(p, row)
        for run in p.runs:
            run.font.size = Pt(size)
            run.font.color.rgb = INK
    return notes(s, note)


def s_vocab(prs, left, right, note):
    s = s_two(prs, "Words from today", left, right, note)
    for idx in (1, 2):
        for para in s.placeholders[idx].text_frame.paragraphs:
            para.space_after = Pt(6)
            for r in para.runs:
                r.font.size = Pt(19)
    return s


KIND = {
    "vocab": s_vocab,
    "title": s_title, "section": s_section, "bullets": s_bullets,
    "bimage": s_bullets_image, "image": s_image, "quote": s_quote,
    "two": s_two, "compare": s_compare, "options": s_options,
    "boxes": s_boxes, "checklist": s_checklist,
}


def build(spec, out):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    prs = new_deck(out)
    for kind, *args in spec:
        kw = {}
        if args and isinstance(args[-1], dict):
            kw = args.pop()
        KIND[kind](prs, *args, **kw)
    for slide in prs.slides:
        _strip_empty(slide)
    prs.save(out)
    print(f"{out}: {len(prs.slides)} slides")
    return prs


# ------------------------------------------------------------------ recurring slides
def warmup(desc, extra=""):
    """The recurring 'Spot it' opener: one flawed image, ninety seconds, out loud."""
    note = ("**Spot it, about four minutes.** Put the image up and say nothing for a few "
            "seconds. Then: what's wrong with it? Hands up, one error per person, and make "
            "them say where it is and what kind of error it is, in the checklist words once "
            "we have them (anatomy, perspective, light, lettering, repeated texture, sheen). "
            "Count the errors out loud as they come in. Don't confirm or correct until the "
            "room stops finding things, then add the one they missed, if there is one.\n\n"
            "This opener runs every class. The point is repetition: by week four the room "
            "finds the shadow problem before the hand problem, which is the right order."
            + ("\n\n" + extra if extra else ""))
    return ("bimage", "Spot it",
            ["One image. Ninety seconds.", "What's wrong with it?", "Say where, and what kind."],
            "slot:" + desc, note)


def vocab(pairs, note=None):
    """'Words from today': a retention slide, term and short gloss, two columns."""
    items = [f"**{t}** \u2013 {g}" for t, g in pairs]
    half = (len(items) + 1) // 2
    note = note or ("Thirty seconds. Read the terms aloud and ask the room for any they "
                    "can't explain yet. These are on Canvas as a running glossary, which "
                    "helps everyone and helps accommodated students most, on a schedule "
                    "where the next class is often tomorrow.")
    return ("vocab", items[:half], items[half:], note)
