from pydantic import BaseModel, Field
from typing import Literal, Optional

class AnalyzeRequest(BaseModel):
    product: str = Field(..., examples=["Backpacks (manufacturer)"])
    positioning: Optional[str] = Field(None, examples=["Mid to premium quality"])
    region: str = Field(..., examples=["Europe", "Germany"])
    sales_focus: Literal["B2B", "B2C", "B2B+B2C"] = "B2B+B2C"
    production_type: Optional[str] = Field(None, examples=["Own manufacturing, custom branding possible"])
    language: Literal["EN", "DE"] = "EN"
    tone: Literal["formal", "friendly", "direct"] = "formal"

class AnalyzeResponse(BaseModel):
    icp: str
    channels: str
    outreach_messages: str
    outreach_plan: str
