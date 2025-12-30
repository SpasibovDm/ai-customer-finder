from __future__ import annotations

from io import BytesIO
from typing import Any, Dict, Iterable, List, Union

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def _safe_str(x: Any) -> str:
    if x is None:
        return ""
    return str(x)


def _wrap_lines(text: str, max_chars: int = 95) -> List[str]:
    """Very simple wrapping by chars (good enough for MVP)."""
    text = text.replace("\r", "")
    lines: List[str] = []
    for raw in text.split("\n"):
        s = raw.strip()
        if not s:
            lines.append("")
            continue
        while len(s) > max_chars:
            lines.append(s[:max_chars])
            s = s[max_chars:]
        lines.append(s)
    return lines


def _draw_wrapped(c: canvas.Canvas, text: str, x: int, y: int, lh: int = 12) -> int:
    for line in _wrap_lines(text):
        c.drawString(x, y, line)
        y -= lh
    return y


def build_report_pdf(payload: Dict[str, Any], analysis: Dict[str, Any]) -> bytes:
    """
    payload: request body (same as AnalyzeRequest)
    analysis: dict-shaped AnalyzeResponse (icp/channels/outreach/plan)
    """
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4

    y = height - 50
    lh = 12

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "AI Customer Finder — Report")
    y -= 24

    c.setFont("Helvetica", 10)
    y = _draw_wrapped(c, "MVP PDF export (mock mode).", 40, y, lh)
    y -= 10

    # Input summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Input Summary")
    y -= 18

    c.setFont("Helvetica", 10)
    summary_lines = [
        f"Product: {_safe_str(payload.get('product'))}",
        f"Region: {_safe_str(payload.get('region'))}",
        f"Sales focus: {_safe_str(payload.get('sales_focus'))}",
        f"Positioning: {_safe_str(payload.get('positioning'))}",
        f"Production: {_safe_str(payload.get('production_type'))}",
        f"Language: {_safe_str(payload.get('language'))}, Tone: {_safe_str(payload.get('tone'))}",
    ]
    for line in summary_lines:
        c.drawString(40, y, line)
        y -= 14

    y -= 10

    def ensure_space(min_y: int = 120) -> None:
        nonlocal y
        if y < min_y:
            c.showPage()
            y = height - 50

    def section(title: str, body: Any) -> None:
        nonlocal y
        ensure_space()
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y, title)
        y -= 18
        c.setFont("Helvetica", 10)

        if isinstance(body, list):
            for item in body[:40]:
                ensure_space()
                y = _draw_wrapped(c, f"- {_safe_str(item)}", 50, y, lh)
        elif isinstance(body, dict):
            for k, v in list(body.items())[:40]:
                ensure_space()
                y = _draw_wrapped(c, f"{_safe_str(k)}: {_safe_str(v)}", 50, y, lh)
        else:
            ensure_space()
            y = _draw_wrapped(c, _safe_str(body), 50, y, lh)

        y -= 8

    section("ICP (Ideal Customer Profiles)", analysis.get("icp"))
    section("Channels (Where to find customers)", analysis.get("channels"))
    section("Outreach Messages", analysis.get("outreach"))
    section("Sales Plan (Next steps)", analysis.get("plan"))

    c.setFont("Helvetica-Oblique", 9)
    c.drawString(40, 40, "Note: MVP report. Next: LLM integration + real lead sourcing connectors.")
    c.showPage()
    c.save()
    return buf.getvalue()
