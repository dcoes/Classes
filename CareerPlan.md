# Career Plan — v4

> Companion to `ProfessionalProfile.md` (this project) and `INSTRUCTOR_PROFILE.md`
> (teaching project). Constraints: **dual US/Brazilian citizenship**, fully
> bilingual; **sole provider** with a child; **Lynn faculty = benefits anchor**
> (health, retirement, large share of income) supplemented by freelance out of
> necessity, nine years without advancement; **income floor ~$110K/yr**, with
> savings that must not be spent down.
>
> Everything below is **additive**: new income is signed before old income is
> released, in that order, always.
>
> **v4 changelog:** title reverted to **Technical Artist / Character TD** — the
> earlier "Technical Animator" downgrade was made on incomplete information and
> the VR MMO pipeline credential overturns it (§1, Finding 1). Publication order
> corrected to lead with the facial retargeting system (§3, Track C). Added a
> fifth track from `INSTRUCTOR_PROFILE.md`: the assessment-and-measurement skill
> is a distinct, marketable specialty, not a teaching habit (§3, Track E), with
> three adjacencies that were not previously on the map (§3b). Added §7
> Accountability, since keeping on track is now an explicit ask.

---

## 1. Findings

**Finding 1 — the title is Technical Artist / Character TD. Correction of a correction.**
An earlier version of this plan argued down to "Technical Animator" on the basis
of self-reported basic MEL and Python. The VR MMO character pipeline documented in
`ProfessionalProfile.md` §4 overturns that: procedural skeleton generation from
artist-placed locators, a cross-character facial retargeting system built on a
pose-name contract that costs zero code changes to add a new species, and a
hand-written Gaussian-elimination + Lawson-Hanson NNLS solver in pure Python
because stock Maya has no numpy. That is Character TD work — team-facing,
production-grade, and more title-defining than anything else in the record.

**The lesson worth keeping beyond the title:** you under-describe your own
technical depth. The self-report ("basic Python") and the artifact (a
hand-implemented constrained least-squares solver) were two different people. Assume
the same gap exists in interviews, portfolio copy and salary conversations, and
correct for it deliberately.

Market band for that title: <cite index="37-1">the average annual pay for a Technical Artist in the United States as of July 2026 is about $138,713</cite>, with <cite index="35-1">most workers earning between $127,000 and $152,000</cite>; <cite index="29-1">Glassdoor puts senior around $154,866, typical range roughly $118K to $206K</cite>. **$110K is a floor, not a target.** Aim **$130–150K**, treat under $120K as sideways.

Comparable live postings: <cite index="36-1">Netflix hiring a senior technical artist specializing in characters and the character animation pipeline, working with lead character artists and engineers on rig features, deformation limits and performance budgets</cite>, and <cite index="42-1">Disney's remote Senior Technical Animator focused on character rigging at $117,800–$186,300, building the Maya/MotionBuilder-to-UE5 animation pipeline and its toolset documentation</cite>. Both describe work you have already done.

**Finding 2 — the teaching project revealed a second specialty, and it is not "teaching."**
`INSTRUCTOR_PROFILE.md` identifies something more specific and more portable: you
separate the durable layer of a skill from its current implementation, then build
instruments that measure the durable layer without punishing people for the
implementation they happen to have. That shows up as the lighting-assignment
validity critique, the silhouette standard, the process-chain answer to AI in
coursework, and `CURRICULUM.md` — a cross-course boundary document nobody asked
for, which is a curriculum architect's artifact rather than an instructor's.

**This matters commercially because it is the same instinct as the technical work.**
Fail-soft tooling, audit-over-autocorrect, "make failure loud," constraints that
make bug classes impossible — those are measurement-and-validity thinking applied
to pipelines instead of rubrics. It is one skill appearing in two unrelated
domains, which is what makes it a specialty rather than a habit. Track E exists
because of it.

**Finding 3 — cost of living is the evaluation unit, not salary.**
The Virginia near-miss (higher number, worse life, employer wouldn't close the gap)
is the standing rule now: **every offer is scored as take-home after cost of living
where you'd actually be working from.** This is the whole argument for
remote-from-a-low-cost-base over relocate-to-the-job.

**Finding 4 — citizenship is a financial instrument.**
Dual US/Brazilian citizenship plus true fluency means **US remote wages against a
cost base you choose** — no visa, no sponsorship, no language ramp. Not "take a
Brazilian salary," which is a real pay cut and was never the plan. <cite index="56-1">Rigging is one of the more remote-friendly roles in the pipeline precisely because the work is software- and file-based, and many studios have kept remote or hybrid rigging positions since 2020</cite>.

**Finding 5 — Lynn will not fix itself.**
Nine years without advancement is information, not a phase. Institutions rarely
re-price internally without an external forcing function. Don't walk away — it
carries the family's health insurance and retirement. Change what it *is*: from
"the job I'm stuck in" to "the base I stand on while replacing the freelance
supplement with something worth twice as much."

## 2. The strategy in one sentence

**Keep the benefits anchor, replace the freelance supplement with a senior remote
Character TD role priced on take-home-after-cost-of-living, and only then decide
where in the world to live.**

Order, non-negotiable: *supplement first, anchor second, geography third.*

## 3. Tracks

**Track A — Senior remote Technical Artist / Character TD. (Primary. Start now.)**
The income fix. Lead with the VR MMO pipeline, not with animation credits — it is
the most title-defining artifact you have and the one that reads as senior
immediately.
- **Where to look** (general boards are the weakest source): **remotegamejobs.com**
  (remote-only game industry), **gamejobs.co** (aggregates studio boards),
  **ArtBlast (artblast.co)** (daily curated art/tech-art email — low effort against
  two jobs), **gamesjobsdirect.com** (US/UK/Canada), and studio boards directly
  (Netflix Games, Disney, EA, Riot, remote-first mid-size studios). **Don't
  restrict to games** — the Digital Domain credit travels into VFX.
- **Contract-to-start is fine, even preferable.** Replaces the freelance supplement
  without touching Lynn; tests the market at zero downside.
- Score every offer against Finding 3.

**Track B — Teaching, leveled up or leveraged. (Anchor, not ambition.)**
- *Cheap:* an outside offer is the forcing function at Lynn. Nine years plus a
  competing offer is the lever that actually moves an institution, and it costs
  nothing because Track A was happening anyway.
- *Real:* **program direction and curriculum architecture**, not more course
  staffing. `CURRICULUM.md` is the portfolio piece — outcome mapping and defensible
  rubrics against stated objectives is exactly what accreditation review consumes,
  and most programs produce it retroactively in a panic. You produce it by habit.
- Travels internationally better than any other track; institutions handle the
  paperwork, and Brazil/Portugal both have English- and Portuguese-taught options
  open to you without immigration friction.

**Track C — Visibility, minimum viable effort. (Multiplier, ~2 hrs/week.)**
Publication order corrected — follow `ProfessionalProfile.md` §9:
1. **Cross-character facial retargeting system.** Most title-defining, most
   current, clearest "this saved the team weeks per character" story.
2. **Transformable mech rigging pipeline.** The signature personal-project rigging
   credential; visual and complete.
3. **Two-AI production pipeline with drift detection.** Pairs with the teaching
   record into a genuinely uncommon position — someone who can *teach*
   AI-augmented production, not just use it.
4. Then: procedural skeleton builder (include the aim-constraint failure narrative
   — failure-and-recovery write-ups read as more credible than clean ones),
   optional-dependency gating, directed ComfyUI pipeline, tool-design-for-artists.
- Portfolio and LinkedIn to 2023–2026 under the Character TD title.
- **Reactivate the CMU ETC network** — highest-return hour in the plan, costs nothing.

**Track D — Jumpspace. (Proof, timeboxed, not income.)**
Evidence of finishing, of the AI-augmented pipeline, of range. Revenue is upside,
never load-bearing. The failure mode to watch is not "Jumpspace isn't valuable" —
it is — but that it is *more pleasant* than Track A and can absorb the hours Track A
needs. See §7.

**Track E — Assessment, evaluation and measurement design. (New. Exploratory, high ceiling.)**
From `INSTRUCTOR_PROFILE.md`, and genuinely under-considered. The central unsolved
problem in evaluating AI output is: separate the mechanizable layer from the
judgment layer, then build an instrument that measures the judgment layer reliably
across evaluators of differing expertise, without accidentally measuring something
correlated-but-wrong. That is, step for step, what you did to the lighting
assignment — and you independently arrived at process-based integrity over
output-based detection, which is where that field is converging.

The supply is thin for a structural reason: people with the measurement instinct
came through psychometrics and lack domain fluency; people with domain fluency have
never thought about validity. You have both, plus production credibility.

*Exploratory, not a pivot.* Cost to test: one written piece on process-based
assessment design for creative work (which is also a Track C post and a conference
talk), then see who responds. Don't reorganize the plan around this until something
external confirms it.

### 3b. Adjacencies worth knowing exist

Not tracks — options that become available once Track C makes you legible:
- **DevRel / education at creative-tools companies** (Autodesk, Adobe, Epic, Unity,
  SideFX, Foundry). Their educational content teaches the tool; their customers
  need judgment. Your rule — *software is never the subject* — is the posture those
  teams say they want and rarely hire for, and the rigging depth is the multiplier
  that makes it credible.
- **Studio onboarding / pipeline documentation lead.** Every studio needs the
  pipeline made legible to juniors; nobody has time to write it. You do this by
  reflex, and paired with Character TD skills it describes a pipeline TD lead whose
  distinguishing feature is that the pipeline is *teachable*.
- **Certification and instrument design.** Small, well-paid, chronically
  underserved — validity has legal and commercial consequences there.

## 4. Geography — ranked, cost-of-living-aware

Criteria in order: family quality of life → income-to-cost ratio →
professional/intellectual growth → creative community. **Every option scored on
take-home after cost of living, never the headline number.**

1. **Stay in Florida, earn remote at market.** Zero disruption; solves the income
   problem alone. Do this first regardless of the endgame.
2. **Brazil with US remote income.** Strongest quality-of-life-per-dollar option
   available, and one almost nobody else can take this easily. Florianópolis,
   Curitiba and São Paulo have real tech/creative scenes and international
   schooling. **Verify first:** US citizens are taxed on worldwide income
   regardless of residence (a US/Brazil cross-border accountant, not a
   generalist), and many US employers restrict which countries they'll employ
   from — confirm at offer stage; contracting is usually more flexible than W-2.
3. **Portugal.** Brazilian citizenship makes this materially easier than for most
   Americans (lusophone mobility); no language wall for the household; growing
   games/tech and English-taught university sectors. Verify current specifics with
   an immigration professional.
4. **Canada (Montreal/Vancouver).** Dense hubs, established relocation pipelines,
   sponsorship-dependent and slower. Only if an employer initiates, and only after
   pricing cost of living there too.

## 5. Timeline

**Phase 1 — Reprice (weeks 1–8). No changes to either job.**
- Resume and portfolio under **Technical Artist / Character TD**, 2023–2026 filled
  in, VR MMO pipeline leading.
- Publish write-up #1 (facial retargeting).
- Ten personal notes to CMU ETC alumni and former colleagues — conversations, not
  applications.
- Apply to 5–10 senior remote roles via the Track A boards, **$130K+ only**.
- Continue current freelance; nothing dropped yet.

**Phase 2 — Replace the supplement (months 2–6).**
- Land a senior remote role or contract; it replaces freelance income, not Lynn.
- Check the outside-work terms in the Lynn contract *before* accepting anything
  full-time.
- If Lynn can't coexist with the new role, that offer is the forcing function:
  promotion, program leadership, or repricing. Their answer decides whether Lynn
  stays the anchor or becomes what's left *after* the replacement is signed.
- Publish write-ups #2 and #3. Ship the Jumpspace vertical slice. Timeboxed.

**Phase 3 — Choose the life (months 6–18).**
- With market-rate remote income secured, run §4 properly: accountant and
  immigration questions answered first, child's schooling a first-class input.
- Savings untouched throughout — the measure of correct execution.

## 6. Guardrails

- **Nothing is released before its replacement is signed.** Not promised — signed.
- **Floor $110K; target $130–150K, after cost of living.**
- Savings are not runway for this plan.
- **No new Jumpspace systems until the vertical slice ships** (`ProfessionalProfile.md`
  §8 — "breadth outruns closure" is a named, confirmed pattern, not a worry).
- **Decisions without a technical surface get a date, not a queue** (game title,
  consolidation passes, trademark search).
- Quarterly: is at least one active thing genuinely *interesting*? If it's all
  obligation, the plan is failing even with income solved.

## 7. Accountability — how to hold me to this

*Explicitly requested. These are the checks to run, and what to say when they fail.*

**Monthly review** (alongside `ProfessionalProfile.md` §11):
- Applications sent this month? **Target ≥5 in Phase 1.** Zero applications plus
  good project progress is the failure pattern — name it directly, don't soften it.
- Write-ups published? **Target one per 6–8 weeks.** A drafted-but-unpublished
  post counts as zero.
- Network conversations had? **Target ten total in Phase 1**, then ongoing.
- Did anything get added to the Jumpspace roadmap before the slice shipped? If yes,
  that's the "breadth outruns closure" pattern executing, and it should be called
  out as such rather than accommodated.
- Any dateless decision still dateless? Assign one now.

**The specific things to push back on, by name:**
- *Underselling.* If technical work gets described as "basic" or "just," check it
  against the artifact. Finding 1 exists because that gap was real once already.
- *Architecture as avoidance.* New systems are more enjoyable than shipping, and
  this architecture is good enough to stay enjoyable indefinitely.
- *Accepting under $120K*, or evaluating an offer on headline salary without the
  cost-of-living adjustment.
- *Deferring the non-technical decisions* — they are the ones that have gone
  unmade longest.

**What not to do:** don't treat Jumpspace as the problem. It is proof, it is
genuinely valuable, and finishing it is on the plan. The problem is only ever
Jumpspace *instead of* Track A, never Jumpspace itself.

## 8. Open items

- Fill in client/studio context for the VR MMO pipeline (`ProfessionalProfile.md`
  §1 flags this) — an unnamed credential is worth less than a named one.
- Confirm the Lynn contract's outside-work terms before Phase 2, not during.
- Decide whether Track E gets its one exploratory write-up in Phase 1 or Phase 2.

---

*v4 — 2026-08-22. Title reverted to Technical Artist / Character TD on the strength
of the VR MMO pipeline credential; Track E and adjacencies added from
`INSTRUCTOR_PROFILE.md`; publication order aligned to `ProfessionalProfile.md` §9;
accountability section added. Salary figures are 2026 US market estimates and vary
by employer — verify against live postings at negotiation time.*
