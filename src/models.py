from pydantic import BaseModel
from typing import List, Optional, Literal

class ICPItem(BaseModel):
    segment: str
    why_fit: str
    buyer_titles: List[str]
    examples: List[str]

class ChannelItem(BaseModel):
    channel: str                    # e.g. "Google", "LinkedIn", "Amazon"
    where: List[str]                # конкретные площадки/места
    search_queries: List[str]       # готовые поисковые запросы

OutreachChannel = Literal[
    "email",
    "linkedin_dm",
    "instagram_dm",
    "marketplace_message",
    "whatsapp"
]

class OutreachMessage(BaseModel):
    channel: OutreachChannel
    subject: Optional[str] = None
    message: str
    followups: List[str] = []

class PlanStep(BaseModel):
    timeframe: str   # "Day 1", "Week 1"
    action: str
    outcome: str

class AnalyzeRequest(BaseModel):
    product: str
    positioning: str
    region: str
    sales_focus: str
    production_type: str
    language: str = "EN"
    tone: str = "formal"

class AnalyzeResponse(BaseModel):
    icp: List[ICPItem]
    channels: List[ChannelItem]
    outreach: List[OutreachMessage]   # <-- ВОТ КЛЮЧЕВОЕ
    plan: List[PlanStep]
