from pathlib import Path
import json
import re

DOCUMENTS_DIR = Path("documents")
OUTPUT_DIR = Path("processed")
OUTPUT_FILE = OUTPUT_DIR / "cleaned_reviews.json"


def parse_header(text):
    apartment = ""
    source = ""
    url = ""

    for line in text.splitlines():
        line = line.strip()
        if line.lower().startswith("apartment:"):
            apartment = line.split(":", 1)[1].strip()
        elif line.lower().startswith("source:"):
            source = line.split(":", 1)[1].strip()
        elif line.lower().startswith("url:"):
            url = line.split(":", 1)[1].strip()

    return apartment, source, url


def clean_text(text):
    text = re.sub(
        r"Response from the owner.*?(?=Review\s*\d+|$)",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    junk_patterns = [
        r"Title:.*",
        r"Apartment:.*",
        r"Source:.*",
        r"URL:.*",
        r"Local Guide.*",
        r"\d+\s+reviews?.*",
        r"\d+\s+photos?.*",
        r"Edited\s+\d+.*ago",
        r"\d+\s+(second|seconds|minute|minutes|hour|hours|day|days|week|weeks|month|months|year|years)\s+ago",
        r"a year ago",
        r"Like",
        r"Share",
        r"Helpful",
        r"Thumbs up.*",
        r"Thumbs down.*",
        r"\+\d+",
        r"More",
        r"[]",
    ]

    for pattern in junk_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_reviews(text):
    pattern = re.compile(r"Review\s*\d+\s*:?", re.IGNORECASE)
    matches = list(pattern.finditer(text))

    blocks = []

    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        if block:
            blocks.append(block)

    return blocks

def remove_reviewer_name(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if len(lines) > 1:
        lines = lines[1:]

    return "\n".join(lines)
def process_file(path):
    raw = path.read_text(encoding="utf-8", errors="ignore")
    apartment, source, url = parse_header(raw)

    review_blocks = split_reviews(raw)

    records = []

    if not review_blocks:
        cleaned = clean_text(raw)
        if len(cleaned) > 30:
            records.append({
                "apartment": apartment,
                "source": source,
                "url": url,
                "file": path.name,
                "review_number": "whole_document",
                "text": cleaned
            })
        return records

    for i, block in enumerate(review_blocks, start=1):
        block = remove_reviewer_name(block)
        cleaned = clean_text(block)

        if len(cleaned) < 40:
            continue

        records.append({
            "apartment": apartment,
            "source": source,
            "url": url,
            "file": path.name,
            "review_number": i,
            "text": cleaned
        })

    return records


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    all_records = []

    for path in sorted(DOCUMENTS_DIR.glob("*.txt")):
        records = process_file(path)
        all_records.extend(records)
        print(f"{path.name}: extracted {len(records)} records")

    OUTPUT_FILE.write_text(
        json.dumps(all_records, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\nTotal records extracted: {len(all_records)}")
    print(f"Saved to: {OUTPUT_FILE}")

    if all_records:
        print("\nSample:")
        print(json.dumps(all_records[0], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()