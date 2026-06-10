from pathlib import Path

import json

import chromadb

from sentence_transformers import SentenceTransformer

CHUNKS_FILE = Path("processed/chunks.json")

CHROMA_DIR = Path("chroma_db")

COLLECTION_NAME = "housing_reviews"

MODEL_NAME = "all-MiniLM-L6-v2"

def main():
    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    texts = [chunk["text"] for chunk in chunks]
    ids = [str(chunk["chunk_id"]) for chunk in chunks]

    metadatas = []

    for chunk in chunks:
        metadatas.append({
            "apartment": chunk["apartment"],
            "source": chunk["source"],
            "url": chunk["url"],
            "file": chunk["file"],
            "review_number": str(chunk["review_number"]),
            "part": str(chunk["part"]),
        })

    print(f"Loaded {len(chunks)} chunks.")
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(texts, show_progress_bar=True,  normalize_embeddings=True).tolist()
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"})

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    print(f"Stored {collection.count()} chunks in ChromaDB.")
    print(f"Collection name: {COLLECTION_NAME}")
    print(f"Database folder: {CHROMA_DIR}")

if __name__ == "__main__":
    main()