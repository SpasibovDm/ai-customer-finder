# AI Customer Finder & Outreach Assistant (MVP)

A lightweight **sales automation assistant** for small businesses.
It generates an **ICP (Ideal Customer Profile)**, **where to find buyers**, **ready-to-send outreach messages**, and a **short action plan**.

✅ Works in **mock mode** (no API keys needed).  
🧩 Designed to later plug in an LLM provider (OpenAI/Azure/local).

---

## Demo (Backpack Manufacturer)

- **Input:** `docs/sample_inputs/backpack_demo_request.json`
- **Output:** `docs/sample_outputs/backpack_demo_response.json`

---

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000

cd ~/ai-customer-finder
grep -n "heredoc" README.md || echo "OK: no heredoc in README"

git add README.md
git commit -m "Fix README (remove heredoc artifacts)"
git pull --rebase origin main
git push

cd ~/ai-customer-finder

python - <<'PY'
from pathlib import Path
p = Path("README.md")
s = p.read_text(encoding="utf-8").splitlines()
p.write_text("\n".join(s2).rstrip() + "\n", encoding="utf-8")
PY

# 2) проверить, что больше нет
grep -n "heredoc" README.md || echo "OK: no heredoc in README"

# 3) закоммитить и запушить (с rebase, чтобы не было reject)
git add README.md
git commit -m "Fix README (remove heredoc artifacts)"
git pull --rebase origin main
git push

cd ~/ai-customer-finder

cat > README.md <<'EOF'
# AI Customer Finder & Outreach Assistant (MVP)

A lightweight **sales automation assistant** for small businesses.
It generates:
- **ICP (Ideal Customer Profiles)**
- **Where to find buyers** (channels + ideas)
- **Ready-to-send outreach messages**
- **Short action plan**

✅ Works in **mock mode** (no API keys needed).  
🧠 Designed to later plug in an LLM provider (OpenAI/Azure/local).

---

## Demo (Backpack Manufacturer)

- **Input:** `docs/sample_inputs/backpack_demo_request.json`
- **Output:** `docs/sample_outputs/backpack_demo_response.json`

---

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000

curl -s -X POST "http://127.0.0.1:8000/api/analyze" \
  -H "Content-Type: application/json" \
  -d @docs/sample_inputs/backpack_demo_request.json

curl -L -o report.pdf -X POST "http://127.0.0.1:8000/api/report.pdf" \
  -H "Content-Type: application/json" \
  -d @docs/sample_inputs/backpack_demo_request.json
open report.pdf


> Важно: после `EOF` **ничего не вставляйте**, просто нажмите Enter.

---

## 2) Проверка, что heredoc исчез
```bash
grep -n "heredoc" README.md || echo "OK: no heredoc in README"

git add README.md
git commit -m "Update README (clean instructions)"
git pull --rebase origin main
git push
