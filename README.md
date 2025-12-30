# AI Customer Finder & Outreach Assistant (MVP)

A lightweight **sales automation assistant** for small businesses:  
it generates **Ideal Customer Profiles (ICP)**, **where to find buyers**, **ready-to-send outreach messages**, and a **short action plan**.

This repository contains an MVP API (FastAPI) + a demo case for a **Backpack Manufacturer**.

---

## What it does

Given a short product description, the assistant produces:

- **ICP (Ideal Customer Profiles)** for B2B/B2C
- **Channels** (where to find customers)
- **Outreach messages** (cold email + follow-ups)
- **Sales plan** (what to do next)

Current version uses **mock generators** (deterministic templates).  
Next milestone: connect an LLM provider (OpenAI/Azure/local model).

---

## Demo (Backpack Manufacturer)

### Input
- `docs/sample_inputs/backpack_demo_request.json`

### Output
- `docs/sample_outputs/backpack_demo_response.json`

This is what a client sees: **input → actionable sales output**.

---

## Run locally (1 minute)

### 1) Create environment & install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

uvicorn src.main:app --reload

cat > src/demo_page.py <<'EOF'
from __future__ import annotations

import json
from html import escape
from typing import Any, Dict

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

DEFAULT_PAYLOAD: Dict[str, Any] = {
    "product": "Backpacks (manufacturer)",
    "positioning": "Mid to premium quality",
    "region": "Germany",
    "sales_focus": "B2B+B2C",
    "production_type": "Own manufacturing, custom branding possible",
    "language": "EN",
    "tone": "formal",
}

def _pretty(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

@router.get("/demo", response_class=HTMLResponse)
async def demo(_: Request) -> HTMLResponse:
    payload_text = _pretty(DEFAULT_PAYLOAD)
    html = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>AI Customer Finder — Demo</title>
  <style>
    body {{ font-family: -apple-system, system-ui, Segoe UI, Roboto, Arial; margin: 24px; }}
    .container {{ max-width: 980px; margin: 0 auto; }}
    h1 {{ margin: 0 0 8px; }}
    .sub {{ color: #555; margin-bottom: 18px; }}
    .grid {{ display: grid; grid-template-columns: 1fr; gap: 14px; }}
    @media (min-width: 900px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
    textarea {{ width: 100%; min-height: 320px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas; font-size: 13px; }}
    pre {{ background: #0b1020; color: #d7e0ff; padding: 14px; overflow:auto; border-radius: 10px; min-height: 320px; }}
    .card {{ border: 1px solid #e6e6e6; border-radius: 12px; padding: 14px; }}
    .row {{ display:flex; gap: 10px; align-items:center; flex-wrap: wrap; }}
    button {{ cursor: pointer; border: none; padding: 10px 14px; border-radius: 10px; font-weight: 600; }}
    .btn {{ background:#111827; color:white; }}
    .btn2 {{ background:#e5e7eb; }}
    .hint {{ color:#6b7280; font-size: 13px; }}
    .ok {{ color:#065f46; }}
    .bad {{ color:#991b1b; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>AI Customer Finder & Outreach — Demo</h1>
    <div class="sub">Paste JSON input → generate ICP, channels, outreach messages, and a plan.</div>

    <div class="row">
      <button class="btn" onclick="runDemo()">Generate</button>
      <button class="btn2" onclick="resetDemo()">Reset</button>
      <span id="status" class="hint"></span>
    </div>

    <div class="grid" style="margin-top: 12px;">
      <div class="card">
        <h3 style="margin: 0 0 8px;">Input (JSON)</h3>
        <textarea id="payload">{escape(payload_text)}</textarea>
        <div class="hint" style="margin-top:8px;">Endpoint: <code>/api/analyze</code></div>
      </div>

      <div class="card">
        <h3 style="margin: 0 0 8px;">Output (JSON)</h3>
        <pre id="output">// Click “Generate”</pre>
      </div>
    </div>
  </div>

<script>
async function runDemo() {{
  const status = document.getElementById("status");
  const out = document.getElementById("output");
  status.textContent = "Running...";
  status.className = "hint";
  out.textContent = "";

  let payload;
  try {{
    payload = JSON.parse(document.getElementById("payload").value);
  }} catch (e) {{
    status.textContent = "Invalid JSON input";
    status.className = "bad";
    out.textContent = String(e);
    return;
  }}

  try {{
    const resp = await fetch("/api/analyze", {{
      method: "POST",
      headers: {{ "Content-Type": "application/json" }},
      body: JSON.stringify(payload)
    }});
    const text = await resp.text();
    if (!resp.ok) {{
      status.textContent = "Error: " + resp.status;
      status.className = "bad";
      out.textContent = text;
      return;
    }}
    const data = JSON.parse(text);
    status.textContent = "OK";
    status.className = "ok";
    out.textContent = JSON.stringify(data, null, 2);
  }} catch (e) {{
    status.textContent = "Request failed";
    status.className = "bad";
    out.textContent = String(e);
  }}
}}

function resetDemo() {{
  document.getElementById("payload").value = {json.dumps(payload_text)};
  document.getElementById("output").textContent = "// Click “Generate”";
  const status = document.getElementById("status");
  status.textContent = "";
  status.className = "hint";
}}
</script>
</body>
</html>
"""
    return HTMLResponse(html)
