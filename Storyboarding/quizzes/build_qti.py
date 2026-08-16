#!/usr/bin/env python3
"""Build a Canvas QTI 1.2 package from the markdown quiz banks.

The markdown in this folder is the source of truth. Edit a question there,
re-run this script, re-import. Never hand-edit the generated XML.

    python3 Storyboarding/quizzes/build_qti.py

Output: quizzes/qti/CA140_quizzes.zip

Each quiz becomes one assessment containing a single question group holding
all fifteen questions, with the group set to draw five at random. Keeping the
group inside the assessment rather than referencing a separate question bank
avoids cross-file identifier resolution, which is the part of QTI that Canvas
is least forgiving about on import.
"""
import html
import os
import re
import zipfile
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "qti")
OUT_ZIP = os.path.join(OUT_DIR, "CA140_quizzes.zip")

DRAW = 5          # questions Canvas serves per attempt
TIME_LIMIT = 5    # minutes
POINTS = 1.0      # per question

HEAD_RE = re.compile(r"^###\s+(Q\d+\.\d+)\s*·\s*(MC|TF)\s*$")
OPT_RE = re.compile(r"^-\s+(\*\s+)?(.*)$")


class Question:
    def __init__(self, ident, qtype):
        self.ident = ident
        self.qtype = qtype
        self.stem = ""
        self.options = []      # list of (text, is_correct)
        self.source = ""

    def validate(self, bank):
        n_correct = sum(1 for _, c in self.options if c)
        assert self.stem, f"{bank} {self.ident}: no stem"
        assert n_correct == 1, f"{bank} {self.ident}: {n_correct} correct answers, need exactly 1"
        if self.qtype == "MC":
            assert len(self.options) == 4, f"{bank} {self.ident}: {len(self.options)} options, MC needs 4"
        else:
            assert len(self.options) == 2, f"{bank} {self.ident}: TF needs 2 options"
        assert self.source, f"{bank} {self.ident}: no source line"


def parse_bank(path):
    """Read one Qnn_*.md into (title, [Question])."""
    title, questions, cur = None, [], None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if title is None and line.startswith("# "):
            title = line[2:].strip()
            continue
        m = HEAD_RE.match(line)
        if m:
            cur = Question(m.group(1), m.group(2))
            questions.append(cur)
            continue
        if cur is None:
            continue
        if line.startswith("> Source:"):
            cur.source = line[len("> Source:"):].strip()
            continue
        m = OPT_RE.match(line)
        if m and not line.startswith("- ["):
            cur.options.append((m.group(2).strip(), bool(m.group(1))))
            continue
        if line.strip() and not line.startswith(("#", ">", "-", "*", "|")):
            cur.stem = (cur.stem + " " + line.strip()).strip()
    return title, questions


def item_xml(q, qid):
    """One QTI <item>. Canvas reads question_type from the metadata field."""
    qtype = "multiple_choice_question" if q.qtype == "MC" else "true_false_question"
    labels, correct_ident = [], None
    for i, (text, is_correct) in enumerate(q.options):
        ident = f"{qid}_a{i}"
        if is_correct:
            correct_ident = ident
        labels.append(
            f'          <response_label ident="{ident}">\n'
            f'            <material><mattext texttype="text/plain">{escape(text)}</mattext></material>\n'
            f'          </response_label>'
        )
    stem_html = f"<p>{html.escape(q.stem)}</p>"
    return f"""      <item ident="{qid}" title="{escape(q.ident)}">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield><fieldlabel>question_type</fieldlabel><fieldentry>{qtype}</fieldentry></qtimetadatafield>
            <qtimetadatafield><fieldlabel>points_possible</fieldlabel><fieldentry>{POINTS}</fieldentry></qtimetadatafield>
            <qtimetadatafield><fieldlabel>assessment_question_identifierref</fieldlabel><fieldentry>{qid}_aq</fieldentry></qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material><mattext texttype="text/html">{escape(stem_html)}</mattext></material>
          <response_lid ident="response_{qid}" rcardinality="Single">
            <render_choice>
{chr(10).join(labels)}
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>
          <respcondition continue="No">
            <conditionvar><varequal respident="response_{qid}">{correct_ident}</varequal></conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""


def assessment_xml(slug, title, questions):
    items = "\n".join(item_xml(q, f"{slug}_i{i:02d}") for i, q in enumerate(questions))
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="{slug}" title="{escape(title)}">
    <qtimetadata>
      <qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>1</fieldentry></qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
      <section ident="{slug}_group" title="{escape(title)} bank">
        <selection_ordering>
          <selection>
            <selection_number>{DRAW}</selection_number>
            <selection_extension>
              <points_per_item>{POINTS}</points_per_item>
            </selection_extension>
          </selection>
        </selection_ordering>
{items}
      </section>
    </section>
  </assessment>
</questestinterop>
"""


def meta_xml(slug, title, n_drawn):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<quiz xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" identifier="{slug}" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{escape(title)}</title>
  <description>Covers the previous class. {n_drawn} questions drawn at random.</description>
  <shuffle_answers>true</shuffle_answers>
  <scoring_policy>keep_highest</scoring_policy>
  <hide_results></hide_results>
  <quiz_type>assignment</quiz_type>
  <points_possible>{n_drawn * POINTS}</points_possible>
  <allowed_attempts>1</allowed_attempts>
  <time_limit>{TIME_LIMIT}</time_limit>
  <one_question_at_a_time>false</one_question_at_a_time>
  <cant_go_back>false</cant_go_back>
  <available>false</available>
</quiz>
"""


def manifest_xml(entries):
    resources = []
    for slug, title in entries:
        resources.append(
            f'    <resource identifier="{slug}" type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment" href="{slug}/{slug}.xml">\n'
            f'      <file href="{slug}/{slug}.xml"/>\n'
            f'      <dependency identifierref="{slug}_meta"/>\n'
            f'    </resource>\n'
            f'    <resource identifier="{slug}_meta" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{slug}/assessment_meta.xml">\n'
            f'      <file href="{slug}/assessment_meta.xml"/>\n'
            f'    </resource>'
        )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="CA140_quizzes" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd">
  <metadata>
    <schema>IMS Content</schema>
    <schemaversion>1.1.3</schemaversion>
  </metadata>
  <organizations/>
  <resources>
{chr(10).join(resources)}
  </resources>
</manifest>
"""


def main():
    banks = sorted(f for f in os.listdir(HERE) if re.match(r"Q\d\d_.*\.md$", f))
    assert banks, "no quiz banks found"
    os.makedirs(OUT_DIR, exist_ok=True)
    entries, total = [], 0

    with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for fname in banks:
            slug = fname[:-3].lower()
            title, questions = parse_bank(os.path.join(HERE, fname))
            for q in questions:
                q.validate(fname)
            stems = [q.stem for q in questions]
            assert len(set(stems)) == len(stems), f"{fname}: duplicate stems"
            assert len(questions) == 15, f"{fname}: {len(questions)} questions, expected 15"
            total += len(questions)
            z.writestr(f"{slug}/{slug}.xml", assessment_xml(slug, title, questions))
            z.writestr(f"{slug}/assessment_meta.xml", meta_xml(slug, title, DRAW))
            entries.append((slug, title))
            print(f"  {fname:34s} {len(questions):2d} questions, draws {DRAW}")
        z.writestr("imsmanifest.xml", manifest_xml(entries))

    print(f"\n{len(entries)} quizzes, {total} questions -> {os.path.relpath(OUT_ZIP)}")


if __name__ == "__main__":
    main()
