from pydantic import BaseModel, Field
from typing import Optional, List

class SupportRequest(BaseModel):
    message: str = Field(min_length=3)
    customer_id: Optional[str] = None

class SupportResponse(BaseModel):
    intent: str
    confidence: float
    answer: str
    source_ids: List[str]
    escalate: bool
    escalation_reason: Optional[str] = None
