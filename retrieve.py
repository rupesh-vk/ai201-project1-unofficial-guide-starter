import chromadb
from sentence_transformers import SentenceTransformer

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "housing_reviews"
MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 5


def retrieve(query, top_k=TOP_K):
    model = SentenceTransformer(MODEL_NAME)

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_collection(name=COLLECTION_NAME)

    query_embedding = model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    matches = []

    for i in range(len(results["documents"][0])):
        matches.append({
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i],
        })

    return matches


def print_results(query):
    print("\n" + "=" * 100)
    print(f"QUERY: {query}")
    print("=" * 100)

    matches = retrieve(query, top_k=TOP_K)

    for idx, match in enumerate(matches, start=1):
        metadata = match["metadata"]

        print(f"\nResult {idx}")
        print(f"Apartment: {metadata.get('apartment')}")
        print(f"Source file: {metadata.get('file')}")
        print(f"Review number: {metadata.get('review_number')}")
        print(f"Distance: {match['distance']:.4f}")
        print("Chunk:")
        print(match["text"])
        print("-" * 100)


if __name__ == "__main__":
    test_queries = [
        "What unsafe conditions, break-ins, stolen packages, harassment, or unauthorized entry do residents mention?",
        "What do residents say about maintenance quality at Avalon Heights?",
        "Which apartments are described as being close to USF?",
    ]

    for query in test_queries:
        print_results(query)