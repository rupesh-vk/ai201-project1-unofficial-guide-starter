# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?  -->
The domain of this project is unofficial student experiences with off-campus housing near the University of South Florida (USF).

The system answers questions using resident reviews collected from apartment complexes near campus. This knowledge is valuable because official apartment websites primarily contain marketing information about amenities and pricing, while resident reviews reveal practical information about maintenance quality, safety concerns, management responsiveness, parking availability, roommate experiences, and overall living conditions.

The goal of the system is to help students make more informed housing decisions using experiences shared by current and former residents.

---
```

```
## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->
 # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | 42N Apartments Reviews | Google Maps Reviews | documents/42n_reviews.txt |
| 2 | Avalon Heights Reviews | Google Maps Reviews | documents/avalon_heights_reviews.txt |
| 3 | Cambridge Woods Reviews | Google Maps Reviews | documents/cambridge_woods_reviews.txt |
| 4 | Halo 46 Reviews | Google Maps Reviews | documents/halo_46_reviews.txt |
| 5 | Lark on 42nd Reviews | Google Maps Reviews | documents/lark_on_42nd_reviews.txt |
| 6 | ON50 Reviews | Google Maps Reviews | documents/on50_reviews.txt |
| 7 | Station 42 Reviews | Google Maps Reviews | documents/station_42_reviews.txt |
| 8 | The Flats at 4200 Reviews | Google Maps Reviews | documents/the_flats_at_4200_reviews.txt |
| 9 | The Ivy Reviews | Google Maps Reviews | documents/the_ivy_reviews.txt |
| 10 | Venue at North Campus Reviews | Google Maps Reviews | documents/venue_north_campus_reviews.txt |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
Each review was treated as a single chunk. Reviews longer than approximately 900 characters were split into smaller chunks of about 700 characters.
**Overlap:**
100-character overlap was used only for long reviews that were split into multiple chunks. Short reviews were kept as a single chunk without overlap.
**Why these choices fit your documents:**
Apartment reviews are naturally self-contained pieces of information. Most reviews focus on a specific experience related to maintenance, safety, management, parking, location, or amenities. Keeping one review per chunk preserves context and source attribution while reducing the risk of mixing unrelated topics. Long reviews were split to prevent a single chunk from containing too many distinct issues.
**Final chunk count:**
The ingestion pipeline extracted 100 cleaned reviews and produced 105 final chunks after splitting a small number of long reviews.
---

## Sample Chunks

### Chunk 1 — 42N

{
    "chunk_id": 10,
    "apartment": "42N",
    "source": "Google Maps",
    "url": "https://tinyurl.com/69jxxznc",
    "file": "42n_reviews.txt",
    "review_number": 6,
    "part": 1,
    "text": "Apartment: 42N\nReview: would not recommend signing a lease here under the current management. Despite months of complaints about my door being left unlocked by staff, the issue persists—most recently within the last two weeks. Management has repeatedly dismissed my concerns, at times denying them despite video evidence, and only responded after I issued a formal Notice to Cure. I have also experienced unprofessional conduct from staff, including dismissive remarks and facial expressions when addressing safety concerns. This is especially troubling given recent incidents in the complex, such as a neighbor’s car being broken into. While the property itself is average, the lack of responsiveness and disregard for resident safety make it unacceptable."
  },

### Chunk 2 — Avalon Heights
{
    "chunk_id": 15,
    "apartment": "Avalon heights",
    "source": "Google Maps",
    "url": "https://tinyurl.com/26hkxjby",
    "file": "avalon_heights_reviews.txt",
    "review_number": 1,
    "part": 1,
    "text": "Apartment: Avalon heights\nReview: It has been already three times in just a year that the water went out. An ESSENTIAL need. It is inexcusable for this to keep happening and all they can say is “sorry for the inconvenience”??? It’s they think we have nothing to do in our lives. They are horrible and never respect or take care of your essential needs. And there is much disrespectful things they do; they never clean the pool, delay to fix the elevator, have people enter your room without permission???, my roomate even had her food stolen by a repairman. Even if this place is close to USF it will be a wayyyy much inconvenience than just living somewhere farther away, it’s not worth living here."
  },


### Chunk 3 — Avalon Heights
{
    "chunk_id": 17,
    "apartment": "Avalon heights",
    "source": "Google Maps",
    "url": "https://tinyurl.com/26hkxjby",
    "file": "avalon_heights_reviews.txt",
    "review_number": 3,
    "part": 1,
    "text": "Apartment: Avalon heights\nReview: Avoid this place at all costs. The leasing office staff is incompetent and will do nothing to help—just make excuses to defend management, who are never in the office. The living conditions here are almost getting to the point where its inhabitable. The elevator has been broken for 6-7 months, trash piles up, pool and gym gates are broken, and there are no keypads on entry gates, making deliveries impossible. Meanwhile, they find every excuse to charge residents while failing to maintain basic living conditions. Recent good reviews are fake—left by people bribed with gift cards during tours. Save yourself the headache and look elsewhere there are many better and cheaper options available around USF. just an example of how bad the situation is, these are all different trash pile ups. 5"
  }
### Chunk 4 — The Ivy
{
    "chunk_id": 92,
    "apartment": "The ivy",
    "source": "Google Maps",
    "url": "https://shorturl.at/5H0Rq",
    "file": "the_ivy_reviews.txt",
    "review_number": 8,
    "part": 1,
    "text": "Apartment: The ivy\nReview: Regretting signing a lease here. Broken furniture, roaches, appliances from the 1960 that don't work and make your bill higher, zero help with any management to replace anything, dog feces all over the property no one regulates picking up after pets the smell is horrendous. DO NOT let your child live here! There are just stealing your money."
  }

### Chunk 5 — Cambridge Woods
{
    "apartment": "Cambridge Woods",
    "source": "Google Maps",
    "url": "https://tinyurl.com/y4r73h2r",
    "file": "cambridge_woods_reviews.txt",
    "review_number": 6,
    "text": "Viktoria is the best manager I have ever seen in my 35 years of life. We only chose the place because of her, she made me feel Home away from home! I hope wish everyone in the industry was at least 10% as good as Viktoria! If you you are looking to rent a place and feel Home, work with Viktoria!"
  }


## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
The system uses the all-MiniLM-L6-v2 embedding model through the sentence-transformers library. Embeddings are stored in ChromaDB and queried using cosine similarity.
**Production tradeoff reflection:**
I selected all-MiniLM-L6-v2 because it is lightweight, free, and can run locally while still providing strong semantic retrieval performance for a relatively small dataset of apartment reviews. If deploying this system for real users, I would evaluate larger embedding models that provide better semantic understanding, stronger performance on noisy review text, multilingual support, and longer context handling. I would also consider the tradeoffs between retrieval quality, latency, storage requirements, API costs, and whether the model should be hosted locally or through a cloud provider.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
The generation model receives only the retrieved review chunks and is instructed to answer using those reviews exclusively. The prompt includes instructions such as:

“Use ONLY the provided review context. Do not use outside knowledge. If the context does not contain enough information, say: ‘I don’t have enough information in the collected reviews to answer that.’”

This prevents the model from relying on external knowledge and encourages responses to remain grounded in the retrieved reviews.
**How source attribution is surfaced in the response:**
Each retrieved chunk contains metadata including apartment name, source file, and review number. After generating a response, the system displays the sources used so users can trace the answer back to the original reviews. The interface also shows the retrieved source list separately from the generated answer, making it easy to verify where information originated.
---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |



| 1 | Which apartment reviews mention towing issues or parking-related complaints? | 42N reviews mention towing complaints and parking-related issues. Some apartments also mention parking costs or guest parking restrictions. | The system identified 42N as having towing complaints and Lark on 42nd as having parking-related complaints. | Relevant | Accurate |

| 2 | What do residents say about maintenance quality at Avalon Heights? | Reviews are mixed. Some residents praise maintenance responsiveness while others report mold, broken facilities, and unresolved issues. | The system summarized both positive and negative maintenance experiences, including fast service, mold concerns, broken elevators, and staffing shortages. | Relevant | Accurate |

| 3 | Which apartments are described as being close to USF? | Reviews mention 42N, Station 42, ON50, Venue at North Campus, and Lark on 42nd as being close to campus. | The system correctly identified multiple apartment complexes described as walking distance or very close to USF. | Relevant | Accurate |

| 4 | What unsafe conditions, break-ins, stolen packages, harassment, or unauthorized entry do residents mention? | Reviews mention harassment, stolen packages, vehicle break-ins, unauthorized entry, security concerns, and poor living conditions. | The system summarized multiple safety-related concerns across several apartment complexes and cited supporting reviews. | Relevant | Accurate |

| 5 | Which apartments receive positive feedback about staff and leasing experiences? | Several apartments including 42N, Avalon Heights, Venue at North Campus, Halo 46, and Cambridge Woods contain positive staff reviews. | The system identified several apartments with positive staff feedback but omitted some apartments that also contained relevant reviews. | Relevant | Partially Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target

**Response accuracy:** Accurate / Partially accurate / Inaccurate

## Retrieval Test Results

## Retrieval Test Results

# Query 1

Question:
What do residents say about maintenance quality at Avalon Heights?

Top Retrieved Chunks:

1. Avalon Heights — Review 9 (Distance: 0.30)
   - Resident describes maintenance as "great and speedy" and notes a mold issue that was resolved quickly.

2. Avalon Heights — Review 5 (Distance: 0.46)
   - Resident reports broken AC, lack of maintenance staff, ignored emails, and delayed repairs.

3. Avalon Heights — Review 3 (Distance: 0.40)
   - Resident describes broken elevators, trash buildup, and poor upkeep.

Why relevant:
All retrieved chunks directly discuss maintenance experiences at Avalon Heights and provide both positive and negative perspectives, which matches the query.

---

# Query 2

Question:
Which apartments are described as being close to USF?

Top Retrieved Chunks:

1. Station 42 — Review 1 (Distance: 0.33)
   - Describes the property as being within walking distance of USF.

2. 42N — Review 7 (Distance: 0.40)
   - Mentions a close-to-campus location and student-focused amenities.

3. Venue at North Campus — Review 9 (Distance: 0.40)
   - States the apartment is very close to the university.

Why relevant:
Each retrieved chunk explicitly discusses proximity to USF, making them strong semantic matches for the query.

---

# Query 3

Question:
What unsafe conditions, break-ins, stolen packages, harassment, or unauthorized entry do residents mention?

Top Retrieved Chunks:

1. 42N — Review 5 (Distance: 0.40)
   - Mentions harassment, stolen packages, unsafe roommate situations, and poor management response.

2. 42N — Review 6 (Distance: 0.47)
   - Describes security concerns, unlocked doors, and a vehicle break-in.

3. Venue at North Campus — Review 6 (Distance: 0.52)
   - Reports unauthorized entry into apartments without notice.

Why relevant:
The retrieved reviews directly contain the safety concerns mentioned in the question, including theft, harassment, break-ins, and unauthorized access.
---

## Query Interface
Input:

The system accepts a natural-language question entered through a Gradio textbox. Users can ask questions about apartment maintenance, safety, parking, management, location, amenities, and other topics discussed in resident reviews.

Output:

The system returns a grounded answer generated from the retrieved reviews along with source attribution showing which apartment reviews were used to generate the response.

Sample Interaction:

User Query:
What do residents say about maintenance quality at Avalon Heights?

System Response:
Residents have mixed opinions about maintenance quality at Avalon Heights. One resident (Avalon Heights, avalon_heights_reviews.txt, Review 9) found maintenance to be "overall great and speedy", while others reported issues such as a mold situation (Avalon Heights, avalon_heights_reviews.txt, Review 9), roaches (Avalon Heights, avalon_heights_reviews.txt, Review 8), broken elevator (Avalon Heights, avalon_heights_reviews.txt, Review 3), and unaddressed maintenance requests (Avalon Heights, avalon_heights_reviews.txt, Review 4). Another resident (Avalon Heights, avalon_heights_reviews.txt, Review 4) mentioned that there is only 1 maintenance person and no maintenance manager, leading to unresolved issues. 

Source: Apartment: Avalon Heights, File: avalon_heights_reviews.txt, Reviews 8, 9, 3, 4, 5.

Retrieved Sources:

• Avalon heights — avalon_heights_reviews.txt — Review 3
• Avalon heights — avalon_heights_reviews.txt — Review 5
• Avalon heights — avalon_heights_reviews.txt — Review 6
• Avalon heights — avalon_heights_reviews.txt — Review 8
• Avalon heights — avalon_heights_reviews.txt — Review 9

## ## Example Responses

### Example 1

Question:
What do residents say about car towing and parking?

Response:
Residents report that cars are frequently towed, especially if parked backwards in the spaces, and that management is strict about parking rules. Additionally, some residents have reported issues with guest parking passes and extra fees for parking. 

Source attribution: 
42N (42n_reviews.txt), The Flats at 4200 (the_flats_at_4200_reviews.txt), Lark on 42nd (lark_on_42nd_reviews.txt)

Retrieved Sources:
• 42N — 42n_reviews.txt — Review 4
• 42N — 42n_reviews.txt — Review 6
• Lark on 42nd — lark_on_42nd_reviews.txt — Review 2
• Lark on 42nd — lark_on_42nd_reviews.txt — Review 7
• The Flats at 4200 — the_flats_at_4200_reviews.txt — Review 5

---

### Example 2

Question:
Which apartments are described as being close to USF?

Response:
Residents describe Station 42, 42N, Venue at North Campus, ON50, and Lark on 42nd as being close to USF or within walking distance of campus.

Sources Used:
- Station 42 Review 1
- 42N Review 7
- Venue at North Campus Review 9
- ON50 Review 5
- Lark on 42nd Review 6

---

### Out-of-Scope Example

Question:
Which CS professor is best for COP4530?

Response:
I don't have enough information in the collected reviews to answer that.
## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

Which apartments receive positive feedback about staff and leasing experiences?

**What the system returned:**

The system returned On50, 42N, Halo 46, and Cambridge Woods as apartments with positive staff or leasing feedback.

**Root cause (tied to a specific pipeline stage):**

This was a retrieval limitation. Positive staff comments were spread across many apartment documents, but the system only retrieved the top 5 chunks. Because of that, some relevant apartments such as Venue at North Campus and Avalon Heights were not included in the retrieved context, so the LLM could not mention them.

**What you would change to fix it:**

I would increase top-k for broad comparison questions or add metadata-aware aggregation so the system can collect relevant reviews from more apartment complexes before generating the final answer.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The planning document helped me break the project into clear stages before writing code. Defining the ingestion process, chunking strategy, retrieval approach, and evaluation questions early made it easier to implement and debug each component independently. The architecture diagram was especially useful because it provided a clear roadmap from raw review files to grounded answers.
**One way your implementation diverged from the spec, and why:**
My original evaluation plan included broad comparison questions such as identifying which apartment received the most complaints about management responsiveness. During testing, I found that semantic retrieval works best for specific, evidence-based questions rather than questions that require counting information across many documents. As a result, I revised some evaluation questions to focus on topics like maintenance quality, safety concerns, and parking issues, which better matched the capabilities of the retrieval pipeline.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

* What I gave the AI:
    I provided examples of raw Google Maps review files, my Domain section, and the Chunking Strategy from planning.md. I also explained how the reviews contained owner responses, timestamps, ratings, and other Google Maps artifacts that needed to be removed.
* What it produced:
    It generated an initial version of the ingestion and cleaning pipeline (ingest.py) that extracted reviews and stored them in a structured JSON format.
* What I changed or overrode:
    The initial implementation failed to extract reviews correctly from my document format. I debugged the extraction process, modified the review splitting logic, improved the cleaning rules, and adjusted the output structure until all reviews were correctly processed and stored.

**Instance 2**

* What I gave the AI:
    I provided the Retrieval Approach section, Architecture diagram, chunk structure, and requirements for using all-MiniLM-L6-v2 with ChromaDB and Groq.
* What it produced:
    It generated code for embedding generation, ChromaDB indexing, semantic retrieval, grounded generation, and a Gradio interface.
* What I changed or overrode:
    During testing, retrieval scores were weak and several results were only partially relevant. I rebuilt the vector store using cosine similarity and normalized embeddings, modified retrieval testing queries, and adjusted the generation prompt so the model would refuse to answer questions that were not supported by the retrieved reviews.
