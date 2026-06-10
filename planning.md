# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

The domain for this project is unofficial student experiences with off-campus housing near the University of South Florida (USF). Students often rely on reviews and community discussions when choosing housing because official apartment websites primarily highlight amenities and marketing information. Resident reviews provide practical insights about maintenance responsiveness, safety concerns, parking availability, management quality, noise levels, and overall living experiences that are difficult to find through official channels
 

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain.  -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | 42N Apartments Reviews | Student housing reviews discussing management, safety, parking, maintenance, amenities, and resident experiences near USF. | documents/42n_reviews.txt |
| 2 | Avalon Heights Reviews | Reviews covering maintenance quality, cleanliness, management responsiveness, apartment conditions, and affordability. | documents/avalon_heights_reviews.txt |
| 3 | Cambridge Woods Reviews | Resident experiences related to pricing, maintenance, amenities, safety, and overall living conditions. | documents/cambridge_woods_reviews.txt |
| 4 | Halo 46 Reviews | Student reviews discussing apartment quality, staff responsiveness, amenities, location, and maintenance issues. | documents/halo_46_reviews.txt |
| 5 | Lark on 42nd Reviews | Reviews describing move-in experiences, management quality, apartment conditions, and resident satisfaction. | documents/lark_on_42nd_reviews.txt |
| 6 | ON50 Reviews | Student feedback regarding affordability, maintenance response times, amenities, location, and management. | documents/on50_reviews.txt |
| 7 | Station 42 Reviews | Reviews covering resident experiences with facilities, maintenance, safety, management, and community atmosphere. | documents/station_42_reviews.txt |
| 8 | The Flats at 4200 Reviews | Reviews discussing apartment conditions, roommate experiences, maintenance, safety concerns, and management quality. | documents/the_flats_at_4200_reviews.txt |
| 9 | The Ivy Reviews | Student reviews focused on roommate matching, management responsiveness, maintenance, amenities, and affordability. | documents/the_ivy_reviews.txt |
| 10 | Venue at North Campus Reviews | Reviews covering leasing experiences, apartment quality, management performance, maintenance, amenities, and pricing concerns. | documents/venue_north_campus_reviews.txt |

---

## Chunking Strategy

<!-- How will you split documents into chunks?

     Overlap: 100 characters for long reviews only.

     Reasoning: Apartment reviews are naturally self-contained. Most reviews describe one resident experience involving maintenance, safety, parking, staff, cleanliness, or location. Keeping one review as one chunk preserves context and source attribution. Very long reviews are split so one chunk does not contain too many unrelated issues.
     -->

**Chunk size:**
Chunk size: One review per chunk. Reviews longer than 900 characters will be split into smaller chunks of about 700 characters. 
**Overlap:**
Overlap: 100 characters for long reviews only.

**Reasoning:**

Reasoning: Apartment reviews are naturally self-contained. Most reviews describe one resident experience involving maintenance, safety, parking, staff, cleanliness, or location. Keeping one review as one chunk preserves context and source attribution. Very long reviews are split so one chunk does not contain too many unrelated issues


---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
`all-MiniLM-L6-v2` through the `sentence-transformers` library. 
**Top-k:**
5 chunks per query.
**Production tradeoff reflection:**
For this project, I chose `all-MiniLM-L6-v2` because it is lightweight, free, and runs locally without an API key. This fits the scale of my dataset, which contains about 100 student apartment reviews. 
For a production system, I would compare larger embedding models with better semantic accuracy, 
longer context support, and stronger performance on messy review-style text. I would also consider 
tradeoffs such as latency, storage cost, API cost, multilingual support, and whether the model should run locally or through a hosted API.
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Which apartment receives the most complaints about management responsiveness? | Reviews for Avalon Heights, Venue at North Campus, and 42N frequently mention ignored complaints, poor communication, slow responses, or management failing to resolve resident concerns. |
| 2 | What do residents say about maintenance quality at Avalon Heights? | Reviews are mixed. Some residents praise the maintenance team for being fast and helpful, while others report unresolved issues such as mold, broken elevators, dirty facilities, and poor upkeep. |
| 3 | Which apartments are described as being close to USF? | Multiple reviews for 42N, Avalon Heights, ON50, and other student-focused complexes mention convenient access to USF, nearby bus routes, or walking-distance locations. |
| 4 | What safety concerns are mentioned by residents across the apartment complexes? | Residents mention unauthorized room entry, stolen packages, vehicle break-ins, smoking violations, security guard complaints, roommate conflicts, and concerns about management's response to safety issues. |
| 5 | Which apartments receive positive feedback about staff and leasing experiences? | Venue at North Campus, 42N, ON50, and Avalon Heights contain reviews praising staff members, helpful leasing offices, smooth move-in experiences, and responsive maintenance teams. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

## Anticipated Challenges

1. Reviews contain noisy and inconsistent text because they were manually collected from Google Maps. Some reviews include navigation elements, timestamps, owner responses, ratings, emojis, or formatting artifacts that are not useful for retrieval. The ingestion pipeline must correctly remove this noise while preserving the actual review content.

2. Apartment reviews often discuss multiple topics in a single review, such as management, maintenance, safety, and amenities. If chunking splits these ideas incorrectly, retrieval may return incomplete context. Conversely, if chunks are too large, retrieval may return irrelevant information that reduces answer quality.



---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

## Architecture


Raw Google Maps Reviews (.txt files)
                │
                ▼
     Document Ingestion Pipeline
          (ingest.py)
    Load review files
    Remove owner responses
    Remove Google Maps noise
    Extract structured reviews
                │
                ▼
      cleaned_reviews.json
                │
                ▼
         Chunking Pipeline
           (chunk.py)
    One review per chunk
    Split very long reviews
    Add apartment metadata
                │
                ▼
            chunks.json
                │
                ▼
      Embedding Generation
      all-MiniLM-L6-v2
   (sentence-transformers)
                │
                ▼
      Vector Database Store
            ChromaDB
                │
                ▼
       Semantic Retrieval
        Top-k = 5 chunks
                │
                ▼
      LLM Grounded Response
              Groq
    Uses retrieved chunks only
    Includes source attribution
                │
                ▼
           User Answer

---


## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->


**Milestone 3 — Ingestion and chunking:**
I used ChatGPT to help implement the ingestion and chunking pipeline. I provided the project requirements, Domain section, Chunking Strategy, and examples of raw Google Maps review files. ChatGPT helped generate ingest.py and chunk.py, while I tested the output, identified extraction issues, and refined the cleaning and chunking logic. I verified the implementation by checking extracted review counts and inspecting the generated JSON files.
**Milestone 4 — Embedding and retrieval:**
I plan to use ChatGPT to help implement embeddings and semantic retrieval. I will provide the Retrieval Approach, Architecture diagram, and chunk structure. I expect it to generate code using all-MiniLM-L6-v2 and ChromaDB for storing and retrieving relevant chunks. I will verify the implementation using my evaluation questions and manually inspect retrieval quality.

**Milestone 5 — Generation and interface:**
I plan to use ChatGPT to help implement grounded answer generation and a simple query interface. I will provide the project requirements related to grounding and source attribution, along with examples of retrieved chunks. I expect it to generate code that answers questions using only retrieved reviews and cites the source documents. I will verify this by checking that responses remain grounded and do not introduce unsupported information.