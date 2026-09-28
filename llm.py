import re
from typing import Any

INTENTS = {
    "refund": ["refund", "money back", "reimburse"],
    "password_reset": ["password", "reset", "login", "sign in"],
    "shipping": ["shipping", "delivery", "deliver", "dispatch"],
    "cancellation": ["cancel", "cancellation"],
    "other": []
}


def detect_intent(message: str) -> str:
    lower = message.lower()
    for intent, keywords in INTENTS.items():
        if any(k in lower for k in keywords):
            return intent
    return "other"


def mock_generate(message: str, context: list[dict]) -> dict[str, Any]:
    intent = detect_intent(message)
    best = context[0] if context else None
    confidence = min(0.98, 0.58 + (best["score"] * 0.4 if best else 0))
    supported = bool(best and best["score"] >= 0.18)

    if not supported:
        return {
            "intent": intent,
            "confidence": round(confidence, 2),
            "answer": "I’m not confident I can answer this from the available support knowledge. I’ll route it to a support specialist.",
            "source_ids": [],
            "escalate": True,
            "escalation_reason": "Insufficient knowledge-base support"
        }

    answer = best["text"]
    escalate = intent in {"other"} or intent == "refund" and "dispute" in message.lower()
    return {
        "intent": intent,
        "confidence": round(confidence, 2),
        "answer": answer,
        "source_ids": [best["id"]],
        "escalate": escalate,
        "escalation_reason": "Potential payment dispute or unsupported intent" if escalate else None
    }


def generate_response(message: str, context: list[dict]) -> dict[str, Any]:
    # Portfolio demo deliberately uses deterministic mock generation so the API is runnable.
    # A real provider can be plugged into this boundary without changing the product API.
    return mock_generate(message, context)
