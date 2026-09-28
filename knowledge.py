import json
from pathlib import Path
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = Path(__file__).resolve().parent.parent
KB_PATH = BASE / "data" / "knowledge_base.json"

with open(KB_PATH, "r", encoding="utf-8") as f:
    KNOWLEDGE = json.load(f)

_vectorizer = TfidfVectorizer(stop_words="english")
_matrix = _vectorizer.fit_transform([x["text"] for x in KNOWLEDGE])


def retrieve(query: str, top_k: int = 3) -> List[Dict]:
    q = _vectorizer.transform([query])
    scores = cosine_similarity(q, _matrix)[0]
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]
    return [
        {**KNOWLEDGE[i], "score": round(float(score), 4)}
        for i, score in ranked
        if score > 0
    ]
