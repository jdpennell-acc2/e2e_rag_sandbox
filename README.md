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
