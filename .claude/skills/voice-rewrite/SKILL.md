---
name: voice-rewrite
description: Rewrite or draft prose (lecture notes, handouts, slide bullets, speaker notes, emails, rubrics) to match Daniel Coes' actual writing voice. Use whenever editing text that goes out under his name in this repo tree, or whenever a draft is coming back sounding generic, corporate, or "AI-flavored" and needs to be brought back to his register. Do not use for code comments or technical build scripts.
---

# Voice rewrite

Daniel's writing has a specific, describable shape. Generic LLM output drifts toward
polish, symmetry, and confidence that his real writing doesn't have. This skill is
the checklist for closing that gap. It edits **text only** — never restructure
content, change pedagogy, or add/remove information while doing a voice pass unless
that's the explicit task.

Full source: `VOICE_ANALYSIS.md` at the repo root (a description of the voice, not
a sample — its own punctuation isn't the model). If `CLAUDE.md` exists in the tree
being edited, its voice section (if present) wins over anything here.

## Two hard bans, checked first and last

1. **No em dashes.** Anywhere. This is the single most common tell of AI-generated
   text. Replace with a comma, a colon, parentheses, or a full stop and a new
   sentence. Exception: a bolded term followed by a spaced en dash (–) then a gloss
   in a bullet — `**Term** – gloss` — is his own habit, not the same character as an
   em dash, and is fine to use or keep.
2. **No LinkedIn/corporate brain.** No "unlock," "elevate," "game changer," "dive
   in," "delve," manufactured drama, forced inspirational beats, or tidy
   thesis-and-three-supports structure. If a sentence could be a LinkedIn post,
   rewrite it flatter.

Before finishing any pass, grep the result for em dashes and for that vocabulary
list. Don't rely on having "kept it in mind."

**The real tell is rarely the literal em-dash character.** In practice, prior
passes dodge the ban on a technicality by substituting a spaced hyphen
(`word - word`) or a spaced en dash (`word – word`) doing the identical
interruption-aside job an em dash would. That's the same AI-tell with the
character swapped out, and it shows up far more often than the literal em dash
does. Grep for ` - ` and ` – ` (spaced hyphen/en dash) as the primary check, not
just `—`. Convert each one on its own merits: a comma for a soft aside, a colon
where it's introducing or explaining, parentheses for a true double-sided
interruption, or a period and a new sentence. Don't mechanically swap every
instance to the same punctuation. The one legitimate spaced-en-dash use is the
bolded-term-then-gloss bullet construction already noted above; a slug line
example like `INT. WAREHOUSE - NIGHT` is also legitimate, since that hyphen is
the actual screenplay-format convention being taught, not a stand-in dash.

While in there, also check for British spellings that slip in independently of
the dash issue (*recognise, colour, judgement, analysed, organise* → American),
and for `actually` / `genuinely` used as reassurance filler rather than adding
real meaning (see "Don't dramatize" above) — these three problems travel
together often enough to be worth checking as one pass.

**Separately, grep speaker notes for first-person contamination** (`\bI\b`,
`I've`, `I'm`, `I'd`). This is a distinct failure mode from the punctuation
issues above, not caught by the same grep, and it shows up on its own in decks
that are otherwise clean of dashes. Speaker notes are written in
instructor stage-direction register ("Say: ...", third person describing what
to do and say aloud), not as the instructor's first-person reflection — rewrite
any "I want to be honest with you..." or "I didn't test this, but..." aside into
that stage-direction voice rather than leaving it in first person.

## What to add (the voice's positive habits)

- **Anecdote or concrete situation before the principle**, where the content allows
  it. Arrive at an idea through a specific thing (a shot, a student board, a tool
  breaking) rather than declaring the rule cold.
- **Every abstraction gets a physical, mechanical object.** Pumps, valves, strings,
  puppets, wheels, tables. Don't explain the metaphor after it lands, just let it
  carry the sentence.
- **Hedge competence and confidence downward.** *Somewhat, quite, more or less,
  enough, at least some.* Never stack superlatives. State a fact and move on rather
  than selling it.
- **Hedge dates and quantities.** *Or so, around, close to, roughly.* Never a flat
  number that reads as precision he doesn't actually have.
- **"Some of these include..."** as a list opener when a list is explicitly partial.
- **Scare quotes on borrowed or imprecise vocabulary** — jargon, industry terms,
  words that are close-enough-but-not-quite. Occasionally name why the word is
  imperfect.
- **Concede the counterargument before it's raised.** *Nevertheless, it's possible
  however to argue that..., not everyone agrees.* Prefer reframing to a verdict.
- **Mark beliefs as beliefs — personal-register text only.** *I feel that, I
  believe, I think there is* belongs in letters, applications, personal essays,
  notes to Daniel, places where the claim is genuinely his own opinion. It does
  **not** belong in lecture content or CONTENT-file notes that convey established
  craft knowledge (shot terminology, film grammar, standard technique). That
  material is received knowledge passed through him, not his opinion, and he says
  so explicitly: "many voices are talking through me." In that register, state facts
  as facts, in a friendly and non-authoritative tone, with no "I think" / "I'd
  argue" / "I feel" framing on curriculum content. His actual opinions have a place
  later in the course, once students have the grounding to engage with them, not
  while he's still teaching them the vocabulary.
- **Praise by describing behavior**, not by asserting a quality — and hedge it if
  it wasn't witnessed directly.
- **Long accreting sentences joined by commas**, clauses added rather than
  subordinated. Front-load a participial or adverbial opener before the subject:
  *Being, Seeing, Without, While, Working, Before.* A run-on that sounds like speech
  can stand as written; don't tidy it into three short sentences for its own sake.
- **Small fixed set of transitions**, reused rather than varied for variety's sake:
  In addition, In other words, In a sense, Nevertheless, Actually, Though, Rather
  than, Much like, Aside from, At the end of the day.
- **Rhetorical question, then the answer**, used to move the argument, not decorate
  it.
- **Parentheses** for a qualification he wants on record but not emphasized.
- **The humanist line**, whenever tools/automation/AI come up: the technology is a
  means of expression, the person using it isn't an operator. One clause. Never a
  paragraph, never a lecture.

## Don't dramatize, don't inflate

The most common failure mode isn't missing hedges, it's adding *performance* while
adding them. Watch for:
- **Invented stakes.** Don't tell the reader something is "the whole reason the
  course works" or otherwise inflate its importance beyond what the source claimed.
  Introduce material as a matter of fact and move on.
- **Intensifiers standing in for hedges.** *Genuinely, actually, really, honestly*
  used to reassure the reader are the opposite move from *somewhat, or so, more or
  less*. Hedging undersells; intensifying oversells. Adding "genuinely" to three
  sentences in a paragraph reads as trying harder, not sounding more like him.
- **Flourish for its own sake.** A personification ("the camera has an opinion of
  its own"), a moralizing aside ("a lesson everyone learns the hard way"), or a
  filler validation ("which is a nice way to think about it") is decoration, not
  voice. If a sentence would work exactly the same with the flourish deleted, delete
  it.
- **Invented framing devices.** Don't label a session with a name it doesn't already
  have ("the vocabulary session") or build a metaphor/throughline that isn't already
  earning its place in the source. If a word like "vocabulary" gets used, it should
  be doing real work, not decorating an intro sentence. Teach the material as it
  already is; don't wrap a layer of narrative packaging around it.
- The fix isn't zero hedges, it's hedges used where the original already has a
  claim worth softening, not sprinkled evenly across every paragraph as a tic.

## What NOT to imitate

These are artifacts of fast, unproofread drafting, not style — importing them reads
as sloppy, not authentic:
- Typos (*inteligence*, *loosing*, *posses*, etc.)
- Spaces inside quotation marks (`" like this "`)
- British spellings (*visualise*, *memorise*)
- "often times" as two words — pick *oftentimes* and stay consistent
- Self-deprecation used somewhere it would cost him (a rubric defending a grade,
  portfolio copy, a credential that has to hold weight). Hedging is for lecture
  register. If a sentence starts undervaluing his own skill in a context where the
  claim needs to hold, describe the work instead of rating it.

## Register by destination

The voice is constant; sentence shape and how much personal-register material is
allowed both change by where the text lands.

| Destination | Register |
|---|---|
| **CONTENT files** (`content/NN_*_revision.md`) | Short refresher notes, a summary a student rereads before the quiz, not the lecture itself. Brief matter-of-fact intro (one sentence, no dramatized stakes, no invented framing label for the session), then the material stated plainly. No "I think" / "I'd argue" opinion-marking — this is received craft knowledge, not personal opinion. Shorter and denser than the deck's speaker notes, not a second copy of them. |
| **Slide body / bullet on screen** | 2–4 short bullets, 3–8 words each, near telegraphic. Word choice still follows the habits above (scare quotes, plain vocabulary) but full sentences and hedging clauses don't fit — the hedge, if any, has to survive in three words or get cut. |
| **Speaker notes** | Full presentation register, and the longer/fuller counterpart to the CONTENT file for the same lecture: bullets as complete spoken sentences, second person, contractions fine, bold on the key term mid-sentence, stage directions in line ("do this live," "let them get it wrong first"). End a section on one compressed line. This is where more of his own voice and framing is earned, since it's him actually talking. |
| **Handouts, rubrics, briefs, prose docs** | Full prose register, all habits above in play, organized with headings, outward-facing — thank people, hand the exchange back where relevant. |
| **Notes in chat / to Daniel directly** | Same bans, plain, no preamble, no recap of what was just said. |

## Applying this to a PowerPoint deck

Slide body and speaker notes are different registers in the same file — don't
flatten them to one voice. Edit text runs only: don't touch layout, images,
positioning, or theme. Watch specifically for prose that leaked into the slide body
(a full sentence where a bullet belongs) — that's a register violation independent
of voice, fix it as part of the same pass.

**Mechanics, via python-pptx:** most paragraphs in these decks are a single run,
so `run.text = run.text.replace(old, new)` is safe. Some paragraphs split a
bolded key term into its own run (`"Shot should convey story from "` + bold
`"viewpoint of character"`) — before rewriting one of these, dump the run
list for that paragraph and edit within existing run boundaries rather than
collapsing it to one string, or the bold emphasis is lost. Build the edit as an
explicit list of (old, new) full-string replacements rather than broad regex,
apply it in one pass over every run in every slide body and notes frame, and
verify each old string matched exactly once (zero means the wording or
capitalization differs from what you read; more than once means check you
didn't over-match). Whatever doesn't match on the first pass usually splits
across a run boundary the same way the bold example does — handle those by
locating the specific run directly rather than forcing the string search.
After: reopen the saved file and grep the rendered text for `—`, ` - `, ` – `,
and the British-spelling/filler list, since a first pass reliably misses a few.
If LibreOffice is available, render to PDF/JPEG and eyeball each slide per the
usual QA pipeline; if it isn't installed in the environment, say so explicitly
rather than skipping the check silently.

## Workflow for a rewrite pass

1. Read the source text in full before touching anything — know what it's actually
   arguing before changing how it sounds.
2. Rewrite content only where the *voice* is off (generic, over-polished, corporate,
   flatly declarative with no hedge, missing the mechanical-object habit). Don't
   rewrite a sentence that already sounds like him just to vary the prose.
3. Preserve every fact, instruction, and pedagogical point exactly. This is a voice
   pass, not a content edit or a fact-check.
4. Run the two-hard-ban check (em dashes, corporate vocabulary) as a final grep-style
   pass over the whole result, not just while drafting.
5. When editing a batch of files, do one file, then stop and show the user a
   before/after sample before continuing to the rest — voice is subjective enough
   that a full run on the wrong calibration wastes the pass.
