# Local AI Operations (AIOps) Sandbox: End-to-End RAG Observability & Security

A production-style, locally containerized AI Operations (AIOps) environment built to simulate, evaluate, and secure Enterprise Retrieval-Augmented Generation (RAG) pipelines. 

This repository documents a local home lab setup replicating a secure 3-tier enterprise AI infrastructure: **Observability/Telemetry** (Argus layer), **Orchestration/Semantic Routing** (Pathfinder layer), and **Reasoning/Knowledge Base** (Sage layer).

---

## 🏗️ Architecture Overview

    ┌────────────────────────────────────────────────────────┐
    │            1. TELEMETRY & GUARDRAILS (Argus)           │
    │                👉 Langfuse (Docker) + Llama Guard3     │
    └──────────────────────────┬─────────────────────────────┘

                               ▼

    ┌────────────────────────────────────────────────────────┐
    │            2. ORCHESTRATION & ROUTING (Pathfinder)     │
    │                👉 Python Client API Middleware         │
    └──────────────────────────┬─────────────────────────────┘

                               ▼

    ┌────────────────────────────────────────────────────────┐
    │            3. INTELLIGENCE & KNOWLEDGE (Sage)          │
    │                👉 Ollama (Llama3) + Qdrant (Vector DB) │
    └────────────────────────────────────────────────────────┘

*   **Telemetry Layer**: Locally hosted **Langfuse** tracking real-time latency, token usage, and system call hierarchies.
*   **Orchestration Layer**: Python middleware parsing payloads, managing context extraction, and structural sanitization.
*   **Intelligence/Knowledge Layer**: Dedicated vector embedding hosting via **Qdrant DB**, with model execution running on a localized **Ollama** server (**Llama 3** & **Nomic-Embed-Text**).

---

## 🛠️ Environment Initialization

### 1. Launch Containerized Services
To avoid local port collision defaults (such as existing PostgreSQL services on `5432`), the telemetry cluster runs on an isolated network bridge with host-facing database rerouting.
```bash
docker compose down -v --remove-orphans
docker compose up -d --force-recreate
```

### 2. Hydrate Local Models
```bash
ollama run llama3
ollama pull nomic-embed-text
ollama run llama-guard3
```

---

## 📈 Engineering Triage & Debugging Case Studies

### Case Study A: Resolving API Payload Failures
*   **Symptom**: During initial pipeline integration, upstream model calls returned empty multi-dimensional arrays `{'model': 'llama3', 'embeddings': []}` triggering list indexing limits `IndexError: list index out of range`.
*   **Root Cause**: General-purpose autoregressive chat models (`llama3`) frequently drop string batches when exposed to modern `/api/embed` batch endpoint arrays.
*   **Resolution**: Migrated backend services to a dedicated text-embedding utility (`nomic-embed-text`) and structurally wrapped single-string payloads into continuous arrays `[text]` to satisfy batch-parsing protocols.

### Case Study B: Simulating a Data Poisoning & "Jailbreak via Roleplay" Exploit
To test the resilience of the pipeline against adversarial prompt injections, a data-poisoning vector was simulated inside a mock academic tracking scenario.

1.  **The Prompt Vector**: A malicious client injected structural grading sheets hidden inside advanced high-school level matrix syntax, wrapper-clothed in a fantasy history lore request.
2.  **The Flaw**: The reasoning model complied with the request, hallucinating a fictional history scenario to mathematically calculate and leak sensitive data coordinates.
3.  **The Database Collision**: Due to the heavy mathematical jargon, the vector's cosine angle was dragged into the advanced tracking database, returning a critical boundary-line **Cosine Similarity Score of `0.5067`** against the wrong curriculum parameter.

```python
# Modern query_points retrieval showcasing the borderline collision
search_result = qdrant_client.query_points(
    collection_name="alphalearn_curriculum",
    query=query_vector, 
    limit=1
)
# Returns: Topic: Advanced Math Matrix | Score: 0.5067 (Exploit Succeeded)
```

---

## 🛡️ Production Mitigation Strategies Developed
To address data-poisoning vulnerabilities and boundary-crossing exposures, the sandbox implements three core infrastructure patches:

*   **Strict Metadata Filtering**: Enforces hard tenancy metadata tags (e.g., `grade_level == 8`) at the Pathfinder routing tier. This prevents semantic drift from pulling answers from unauthorized indices, even if the similarity score is high.
*   **Structural Input Sanitization**: Configures the Argus layer to run raw data parsing. If un-sanitized layout inputs (CSV rows, markdown tables, or direct URL links) are detected within student boundaries, the transaction is rejected prior to inference.
*   **Outbound Firewall Validation**: Utilizes localized `llama-guard3` evaluations inside Langfuse skills to monitor response output variables for embedded links or script injections to block Self-XSS and phishing vector delivery.
