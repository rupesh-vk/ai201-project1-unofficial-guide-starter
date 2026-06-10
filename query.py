import os
from dotenv import load_dotenv
from groq import Groq
from retrieve import retrieve

load_dotenv()

MODEL_NAME = "llama-3.3-70b-versatile"


def build_context(chunks):
    context_parts = []

    for i, chunk in enumerate(chunks, start=1):
        metadata = chunk["metadata"]
        context_parts.append(
            f"""Source {i}
Apartment: {metadata.get("apartment")}
File: {metadata.get("file")}
Review Number: {metadata.get("review_number")}
Text: {chunk["text"]}
"""
        )

    return "\n---\n".join(context_parts)


def ask(question):
    chunks = retrieve(question, top_k=5)
    context = build_context(chunks)

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are answering questions about off-campus apartment reviews near USF.

Use ONLY the provided review context.
Do not use outside knowledge.
If the context does not contain enough information, say:
"I don't have enough information in the collected reviews to answer that."

Question:
{question}

Review Context:
{context}

Answer with:
1. A concise answer grounded in the reviews.
2. Source attribution by apartment and file name.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a grounded RAG assistant. Answer only from retrieved context."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content

    sources = []
    for chunk in chunks:
        metadata = chunk["metadata"]
        sources.append(
            f"{metadata.get('apartment')} — {metadata.get('file')} — Review {metadata.get('review_number')}"
        )

    return {
        "answer": answer,
        "sources": sorted(set(sources)),
        "chunks": chunks,
    }


if __name__ == "__main__":
    question = "What do residents say about maintenance quality at Avalon Heights?"
    result = ask(question)

    print(result["answer"])
    print("\nSources:")
    for source in result["sources"]:
        print("-", source)