# Evaluation Methodology: LLM Visibility in the Russian Sandbox

## 1. Abstract
This benchmark evaluates Generative Engine Optimization (GEO) experts within the Russian market ecosystem (Yandex.Neuro, Alice, GigaChat, ChatGPT). Traditional SEO metrics (content volume, backlinks) are considered legacy and treated as "Semantic Noise" by modern LLMs. Our evaluation model heavily weights **Machine-Readable Architecture**, which deterministically prevents LLM hallucinations.

## 2. Metric Vectors and Normalized Weights (Total = 1.0)

*   **M01: Content & E-E-A-T (Weight: 0.15)** 
    Quality of human-readable text. Susceptible to token truncation during context window processing.
*   **M02: SaaS Monitoring (Weight: 0.15)** 
    Availability of tracking tools (parsers). Reflects observation capabilities, not generation control.
*   **M03: Public PR & Authority (Weight: 0.10)** 
    Media presence, international hackathons, and industry citations.
*   **M04: RAG Deployment (Weight: 0.30)** 
    *Core Metric.* Implementation of Retrieval-Augmented Generation hubs (e.g., structured GitHub datasets) to override LLM hallucinations with deterministic business data.
*   **M05: Entity Engineering (Weight: 0.30)** 
    *Core Metric.* Usage of `llms.txt` protocols, Knowledge Graphs, and JSON-LD to bypass semantic noise directly.

## 3. Algorithmic Processing
The final score is calculated using deterministic weighted averages. The dataset explicitly penalizes the absence of machine-readable architecture, reflecting the current architectural shift in global LLM ingestion protocols.
