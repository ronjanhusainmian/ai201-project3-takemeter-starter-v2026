
import csv
import re
from pathlib import Path

SOURCE = Path("computer_science.csv")
OUTPUT = Path("labels.csv")

education_terms = [
    "career", "job", "internship", "salary", "degree",
    "college", "university", "school", "student",
    "course", "curriculum", "study", "studying",
    "learn", "learning", "beginner", "resource",
    "book", "tutorial", "interview", "graduate",
    "major", "education", "advice", "roadmap",
]

technical_terms = [
    "algorithm", "data structure", "compiler",
    "operating system", "network", "database",
    "complexity", "recursion", "hash", "binary",
    "memory", "cpu", "thread", "process",
    "encryption", "protocol", "architecture",
    "code", "programming", "function",
    "implementation", "how does", "why does",
]

def suggest_label(title, body):
    # Use the title as the strongest signal.
    title = title.lower()
    body = body.lower()

    def score(terms):
        return (
            3 * sum(term in title for term in terms)
            + sum(term in body for term in terms)
        )

    education_score = score(education_terms)
    technical_score = score(technical_terms)

    if education_score > technical_score:
        return "education_career"

    return "technical_questions"


with SOURCE.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    posts = list(reader)

rows = []
seen = set()

for post in posts:
    title = (post.get("Title") or "").strip()
    body = (post.get("Body") or "").strip()

    # Exclude missing/deleted posts.
    if not title or not body:
        continue

    if body.lower() in {"[deleted]", "[removed]", "nan"}:
        continue

    # Keep the complete title and body.
    text = f"{title}\n\n{body}"

    # Exclude duplicate posts.
    normalized = re.sub(r"\s+", " ", text).lower()
    if normalized in seen:
        continue

    seen.add(normalized)

    label = suggest_label(title, body)

    rows.append({
        "text": text,
        "label": label,
        "note": "AI pre-labeled; review required",
    })

    if len(rows) == 200:
        break

with OUTPUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["text", "label", "note"]
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Created {OUTPUT} with {len(rows)} posts.")

for label in ["technical_questions", "education_career"]:
    count = sum(row["label"] == label for row in rows)
    percent = 100 * count / len(rows) if rows else 0
    print(f"{label}: {count} ({percent:.1f}%)")

if len(rows) < 200:
    print("WARNING: Fewer than 200 usable posts.")

if rows and any(
    sum(row["label"] == label for row in rows) / len(rows) > 0.60
    for label in ["technical_questions", "education_career"]
):
    print("WARNING: Label balance exceeds your 60% target.")

print("Review every suggested label before training.")
