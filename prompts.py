SYSTEM_PROMPT = """
You are a customer-support copilot. Answer only from the supplied knowledge base.
If the context does not support a safe answer, set escalate=true.
Return structured fields: intent, confidence, answer, source_ids, escalate, escalation_reason.
Keep the answer concise and customer-friendly.
""".strip()


def build_prompt(message: str, context: list[dict]) -> str:
    sources = "\n".join(
        f"[{x['id']}] {x['title']}: {x['text']}" for x in context
    )
    return f"{SYSTEM_PROMPT}\n\nKnowledge:\n{sources}\n\nCustomer message:\n{message}"
