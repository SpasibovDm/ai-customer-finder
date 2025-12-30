#from src.demo_page import router as demo_router
from fastapi import Response
from src.services.report_pdf import build_report_pdf
from fastapi import FastAPI
from dotenv import load_dotenv

from src.models import AnalyzeRequest, AnalyzeResponse
from src.services.icp import build_icp_en
from src.services.channels import build_channels_en
from src.services.outreach import build_outreach_en
from src.services.plan import build_plan_en
def analyze_request(req: AnalyzeRequest) -> dict:
    return {
        "icp": build_icp_en(req),
        "channels": build_channels_en(req),
        "outreach": build_outreach_en(req),
        "plan": build_plan_en(req),
    }
load_dotenv()

app = FastAPI(title="AI Customer Finder & Outreach Assistant", version="0.1.0")
#app.include_router(demo_router)
@app.post("/api/report.pdf")
def report_pdf(req: AnalyzeRequest):
    analysis = analyze(req)  # или ваша функция, которая возвращает dict/модель
    # если analyze возвращает pydantic-модель:
    if hasattr(analysis, "model_dump"):
        analysis_dict = analysis.model_dump()
    else:
        analysis_dict = analysis

    pdf_bytes = build_report_pdf(req.model_dump(), analysis_dict)
    return Response(content=pdf_bytes, media_type="application/pdf")

# ❌ УБРАТЬ ЭТИ СТРОКИ
# from src.demo_page import router as demo_router
# app.include_router(demo_router)
