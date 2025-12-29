from fastapi import FastAPI
from dotenv import load_dotenv

from src.models import AnalyzeRequest, AnalyzeResponse
from src.services.icp import build_icp_en
from src.services.channels import build_channels_en
from src.services.outreach import build_outreach_en
from src.services.plan import build_plan_en

load_dotenv()

app = FastAPI(title="AI Customer Finder & Outreach Assistant", version="0.1.0")

# ❌ УБРАТЬ ЭТИ СТРОКИ
# from src.demo_page import router as demo_router
# app.include_router(demo_router)
