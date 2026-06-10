from pathlib import Path
import json

INPUT_FILE = Path("processed/cleaned_reviews.json")
OUTPUT_FILE = Path("processed/chunks.json")

MAX_CHARS = 900
OVERLAP = 100


def split_long_text(text, max_chars=MAX_CHARS, overlap=OVERLAP):
    if len(text) <= max_chars:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + max_chars

        if end < len(text):
            sentence_end = text.rfind(".", start, end)
            if sentence_end != -1 and sentence_end > start + 300:
                end = sentence_end + 1

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        start = max(end - overlap, end)

    return chunks


def main():
    reviews = json.loads(INPUT_FILE.read_text(encoding="utf-8"))

    chunks = []
    chunk_id = 1

    for review in reviews:
        text = review["text"]
        split_chunks = split_long_text(text)

        for part_index, chunk_text in enumerate(split_chunks, start=1):
            chunks.append({
                "chunk_id": chunk_id,
                "apartment": review["apartment"],
                "source": review["source"],
                "url": review["url"],
                "file": review["file"],
                "review_number": review["review_number"],
                "part": part_index,
                "text": f"Apartment: {review['apartment']}\nReview: {chunk_text}"
            })
            chunk_id += 1

    OUTPUT_FILE.write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Loaded {len(reviews)} cleaned reviews.")
    print(f"Created {len(chunks)} chunks.")
    print(f"Saved to {OUTPUT_FILE}")

    print("\nSample chunk:")
    print(json.dumps(chunks[0], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()