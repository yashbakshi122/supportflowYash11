from fastapi import FastAPI
from .schemas import SupportRequest, SupportResponse
from .knowledge import retrieve
from .llm import generate_response

app = FastAPI(title="SupportFlow AI", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "supportflow-ai"}

@app.post("/support", response_model=SupportResponse)
def support(req: SupportRequest):
    context = retrieve(req.message)
    result = generate_response(req.message, context)
    return result

@app.get("/knowledge/search")
def search_knowledge(q: str, top_k: int = 3):
    return {"query": q, "results": retrieve(q, top_k)}
