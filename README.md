# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

**Community:**

I chose r/computerscience, a subreddit where people discuss computer science concepts, programming, education, and careers in technology.

**Three candidate distinctions:**

**Technical vs. education/career questions:** Some posts ask about specific computer science concepts or technical problems, while others seek advice about learning resources, degrees, or career opportunities.

**Context provided:** Some posts explain the author's background, technical knowledge, and what they have already tried, while others ask questions without providing much context.

**Specific vs. broad questions:** Some posts ask about a particular technical concept or problem, while others ask broader questions about improving their computer science knowledge or preparing for a career.


---



## Label Taxonomy

### `technical_questions`

**Definition:** Posts that ask for help understanding a specific computer science concept, solving a technical problem, or explaining how a programming or computing system works.

**Example 1:**
> [Has the format for email addresses changed after RFC 5322?](https://www.reddit.com/r/computerscience/comments/hg4vtl/) - The author asks about email formatting standards and how to correctly validate email addresses.

**Example 2:**
> [Centralized vs Decentralized Networks](https://www.reddit.com/r/computerscience/comments/gxnkce/) - The author asks for help understanding and comparing technical properties of different network structures.

### `education_career`

**Definition:** Posts that ask for advice about learning computer science, choosing educational resources, developing skills, pursuing degrees, or preparing for careers in technology.

**Example 1:**
> [What to learn for cs?](https://www.reddit.com/r/computerscience/comments/hkco74/) - The author asks which computer science topics to study before starting college.

**Example 2:**
> [Java intermediate learner](https://www.reddit.com/r/computerscience/comments/h0ooev/) - The author discusses their programming experience and asks how to continue improving their Java skills.

### The hardest boundary

**Which two labels:** `technical_questions` and `education_career`

**Borderline post:** [I'm a professional software engineer, but need help finding CS fundamentals resources](https://www.reddit.com/r/computerscience/comments/gili8e/)

The author is an experienced programmer who wants to improve their understanding of computer science fundamentals. Although the post discusses technical knowledge, the main request is for learning resources rather than an explanation of a specific technical problem.

**The decision rule I used every time:**

If the main purpose of a post is to understand or solve a specific technical problem, I label it `technical_questions`. If the main purpose is to seek advice about education, learning resources, skill development, or career preparation, I label it `education_career`, even if technical topics are mentioned.


---


## The Dataset

**Where the posts came from:**

I used a publicly available Reddit dataset from Kaggle containing posts from r/computerscience. I selected 200 posts and combined each post's title and full body into the text column.

**How I labelled them:**

I used a Python script to suggest labels based on keywords in the titles and bodies of the posts. The two labels were technical_questions and education_career. The suggested labels require manual review, especially for posts that discuss both technical topics and education or careers.

**Counts per label:**

| Label | Count | Share |
|---|---:|---:|
| `technical_questions` | 96	 | 48% |
| `education_career` | 104 | 52% |
| **Total** | **200** | **100%** |

**Three hard cases**

**1.**
> *The post:* "How can I improve all my computer science skills as a whole?"

> *Could have been:* `technical_questions` or `education_career`

> *I chose, because:* `education_career`. Although the post discusses technical skills, the author mainly asks for advice about improving their computer science knowledge rather than solving a specific technical problem.

**2.**
> *The post:* "What operating system do most computer science students and professionals use?"

> *Could have been:* `technical_questions` or `education_career`

> *I chose, because:* `education_career`. Although operating systems are a technical topic, the author is asking about the tools used by students and professionals rather than how operating systems work.

**3.**
> *The post:* "Is it a good practice to hash the contents of two files for comparing them or is it better to compare the bytes?"

> *Could have been:* `technical_questions` or `education_career`

> *I chose, because:* `technical_questions`. The author asks about a specific technical approach to comparing files. Although the question could help someone improve their programming skills, its main purpose is to understand a technical solution.


---

## The Training Run

**Base model:**

DistilBERT (`distilbert-base-uncased`), fine-tuned to classify posts from r/computerscience into `technical_questions` and `education_career`.

**Settings:**

- **Epochs:** 3
- **Learning rate:** 2e-5
- **Batch size:** 16
- **Random seed:** 42
- **Maximum sequence length:** 128 tokens
- **Device:** CPU

**Anything I changed from the defaults, and why:**

I configured training to use the CPU and disabled pinned memory to prevent kernel crashes. I kept the default learning rate and trained for three epochs.

**Split sizes:**

The dataset contains 200 labeled posts, divided into:

- **Training:** 139 posts
- **Validation:** 31 posts
- **Test:** 30 posts

Per-label counts in the test split:

| Label | Test count |
|---|---:|
| `technical_questions` | 14 |
| `education_career` | 16 |
| **Total** | **30** |


---

## How I Used AI

**Moment 1**

- **What I asked for:** I asked ChatGPT to clean and label a dataset of Reddit posts from r/computerscience from Kaggle.
- **What came back:** ChatGPT provided Python code to clean the original Kaggle dataset, extract the relevant text and assign labels.
- **What I changed:** I used the script to generate labels.csv and kept the two categories.

**Moment 2**

- **What I asked for:** I asked ChatGPT to help troubleshoot a Jupyter kernel crash that occurred when training my DistilBERT classifier.
- **What came back:** ChatGPT suggested checking whether PyTorch and DistilBERT worked independently, then recommended changing the training configuration to reduce memory usage and avoid the crash.
- **What I changed:** I switched training to the CPU and disabled pinned memory. After these changes, the model successfully completed three training epochs.

**Pre-labelling disclosure:**

I used AI-assisted Python code to pre-label the Reddit posts based on their titles and content. I labeled the first 20 myself, and made sure to check all the remaining AI-labeled ones.


<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|
| Overall accuracy | 0.600 |
| Macro F1 | 0.583 |
| F1 — `education_career` | 0.500 |
| F1 — `technical_questions` | 0.667 |


**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->
I expect the fine-tuned DistilBERT model to perform better overall because it was trained on posts from r/computerscience using my two labels. I expect the biggest improvement in education_career, where the baseline achieved a lower F1 score.

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
