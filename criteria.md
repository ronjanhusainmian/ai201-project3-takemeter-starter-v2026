# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---



## 1. Overall accuracy

The model must achieve at least 70% accuracy on the held-out test set across all three random seeds.

**Why this target:** My classifier distinguishes between technical questions and education or career advice posts in r/computerscience. Since there are only two labels, 70% is meaningfully better than the 50% expected from random guessing on balanced data, while accounting for posts that overlap between the categories.

---

## 2. Per-label F1 score

Both `technical_questions` and `education_career` must achieve an F1 score of at least 0.60 on the held-out test set across all three seeds.

**Why this target:** Some posts discuss technical concepts while mainly asking for learning or career advice, making the categories difficult to separate. With around 200 posts and only about 30 in each test split, a minimum F1 of 0.60 is a reasonable target for both labels.

---

## 3. Dataset balance

Neither label should account for more than 60% of the 200 labeled posts.

**Why this target:** r/computerscience contains both technical discussions and questions about education and careers. Keeping each label between 40% and 60% ensures that the classifier has enough examples of both categories instead of learning to favor the more common one.

---

## 4. Labeling consistency

At least 85% of a sample of 30 posts must receive the same label when independently labeled a second time using the same definitions.

**Why this target:** The boundary between technical questions and education or career advice can be unclear when a post discusses technical topics while asking for general guidance. An 85% agreement target checks whether my decision rule produces consistent labels.

---

## 5. Prediction confidence

Among held-out test predictions with confidence of at least 80%, at least 80% must be correct across all three seeds.

**Why this target:** Posts focused on a specific technical problem or a clear career question should generally be easier to classify than posts mixing technical discussions with general advice. I want predictions with at least 80% confidence to be correct at least 80% of the time, showing that the classifier's confidence is useful.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
