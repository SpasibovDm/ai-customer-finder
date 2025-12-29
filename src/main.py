from fastapi import FastAPI
from dotenv import load_dotenv

from src.models import AnalyzeRequest, AnalyzeResponse
from src.services.icp import build_icp_en
from src.services.channels import build_channels_en
from src.services.outreach import build_outreach_en
from src.services.plan import build_plan_en

load_dotenv()
app = FastAPI(title="AI Customer Finder & Outreach Assistant", version="0.1.0")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/api/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    # MVP: mock logic. Later we’ll plug in LLM generation here.
    return AnalyzeResponse(
        icp=build_icp_en(req),
        channels=build_channels_en(req),
        outreach_messages=build_outreach_en(req),
        outreach_plan=build_plan_en(req),
    )
