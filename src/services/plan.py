def build_plan_en(req) -> str:
    focus = req.sales_focus
    return f"""## Sales & outreach plan (EN) — focus: {focus}

### B2B outreach (recommended)
- **Day 1:** initial email to Procurement / Marketing / HR
- **Day 4:** follow-up + product images / use cases
- **Day 10:** final follow-up + offer samples or pricing overview

### B2C growth (parallel)
- **Week 1:** optimize product listings (titles, images, keywords, description)
- **Week 2:** micro-influencer outreach (UGC)
- **Week 3:** test ads with best creatives and iterate
"""
