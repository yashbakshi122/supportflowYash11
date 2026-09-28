# SupportFlow AI – LLM Customer Support Copilot

An AI-powered customer-support workflow that classifies incoming queries, retrieves relevant knowledge, generates grounded responses, and escalates uncertain cases for human review.

## What this demonstrates
- LLM-based intent classification
- Retrieval-augmented generation (RAG) with a local knowledge base
- Structured outputs for downstream workflows
- Confidence-aware escalation
- FastAPI endpoints for product integration
- PostgreSQL-ready interaction logging

## Architecture

```text
Customer Query
     |
     v
Intent Classification -----> Low confidence? -----> Human Review
     |
     v
Knowledge Retrieval
     |
     v
Grounded LLM Response
     |
     v
Structured JSON Response
     |
     v
Interaction Log
```

## Run locally

Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: `http://127.0.0.1:8000/docs`

The project runs in **demo mode without an API key** using a deterministic mock LLM. To connect a real provider, set environment variables documented in `.env.example` and replace the mock client in `app/llm.py`.

## Example request

```json
{
  "message": "How long do refunds take?",
  "customer_id": "C102"
}
```

## Product decisions

- Low-confidence requests are escalated rather than answered aggressively.
- Retrieved knowledge is included in the response so the answer is traceable.
- Structured output separates intent, confidence, answer, sources, and escalation state.

## GitHub

Suggested repository topics: `llm`, `rag`, `customer-support`, `fastapi`, `product-management`, `ai-product`, `generative-ai`.

## Note

This repository is a portfolio project. Metrics and evaluation claims should be added only after running the evaluation suite on real test data.
