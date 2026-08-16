# Quizzes: CA 140 Storyboarding

Ten short retention quizzes. Each opens at the start of a class and covers **the class before it**, lecture and exercise. Five questions drawn at random from a bank of fifteen. Self-grading in Canvas.

Together they are **6% of the course grade**, about 0.6% each.

---

## Placement

| Quiz | Opens | Covers | Bank |
|---|--:|---|---|
| Q1 | Class 2 | Class 1 Intro, and EX1 | [`Q01_Intro.md`](Q01_Intro.md) |
| Q2 | Class 3 | Class 2 Origins and Aspect Ratios, and EX2 | [`Q02_Aspect_Ratios.md`](Q02_Aspect_Ratios.md) |
| Q3 | Class 4 | Class 3 Fundamentals of the Shot, and EX3 | [`Q03_Shot_Fundamentals.md`](Q03_Shot_Fundamentals.md) |
| Q4 | Class 5 | Class 4 Continuity, The Rules | [`Q04_Continuity_Rules.md`](Q04_Continuity_Rules.md) |
| Q5 | Class 6 | Class 5 Composition | [`Q05_Composition.md`](Q05_Composition.md) |
| Q6 | Class 7 | Class 6 Perspective, and EX4 | [`Q06_Perspective.md`](Q06_Perspective.md) |
| Q7 | Class 9 | Class 7 Lighting, and EX6 | [`Q07_Lighting.md`](Q07_Lighting.md) |
| Q8 | Class 10 | Class 9 Staging and Acting | [`Q08_Staging_and_Acting.md`](Q08_Staging_and_Acting.md) |
| Q9 | Class 11 | Class 10 Continuity, The Cut, and EX5 | [`Q09_Continuity_The_Cut.md`](Q09_Continuity_The_Cut.md) |
| Q10 | Class 12 | Class 11 Animatics and After Effects, and EX7 | [`Q10_Animatics_and_AE.md`](Q10_Animatics_and_AE.md) |

Classes 8 and 14 are critique. Class 13 is the pitch. No quizzes there.

---

## The design rule

**Every question has to be answerable by a student who attended the class and did the exercise, and unanswerable by one who did neither.**

That rules out trivia, dates, and anything that only rewards having skimmed a slide. Roughly two thirds of each bank tests the lecture and one third tests the exercise, because the exercise is where the concept had to survive contact with the student's own hands.

Every question carries a source line naming the deck, handout or rubric it comes from. Anything that could not be traced was cut, because it would be testing something the course never taught.

**There is no textbook.** Nothing on any quiz comes from outside the decks, handouts and assignments in this repository.

---

## Importing into Canvas

`qti/CA140_quizzes.zip` is a QTI 1.2 package. In Canvas: **Settings, Import Course Content, QTI .zip file.** It creates ten question banks and ten quizzes, each set to draw 5 questions from its own bank.

After import, check each quiz's settings:

- **Shuffle answers:** on
- **Time limit:** 5 minutes
- **Allowed attempts:** your call. The random draw is what makes a second attempt a genuinely different quiz, which is the argument for allowing one.
- **Show correct answers:** after the due date, not immediately, since the bank is reused across a random draw.

If the import misbehaves, the markdown files are complete and standalone. Nothing here depends on the package working.

---

## Editing a question

**The markdown is the source of truth.** Edit the bank file, then re-run:

```
python3 Storyboarding/quizzes/build_qti.py
```

That regenerates the package. Do not hand-edit the XML.

---

## Format

```
### Q1.01 · MC
The stem of the question.
- * The correct answer
- A wrong answer
- Another wrong answer
- A fourth option
> Source: Deck 01 slide 12
```

`* ` marks the correct answer. `MC` is multiple choice with four options, `TF` is true/false with two. Those two types auto-grade cleanly and unambiguously, which is why they are the only two used.
