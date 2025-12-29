def build_icp_en(req) -> str:
    product = req.product
    return f"""## Ideal Customer Profiles (ICP) — {product}

### B2B segments
1) **Corporate & Promotional buyers**
- Roles: Procurement, Marketing, HR
- Use cases: employee onboarding, corporate gifts, event giveaways
- Trigger: need a practical branded product with long lifetime

2) **Retail / e-commerce brands**
- Outdoor, travel, lifestyle brands
- Looking for white-label / OEM manufacturing

3) **Schools / universities / sports clubs**
- Bulk orders, logo branding, seasonal demand

### B2C segments
- Urban commuters, travelers & digital nomads, students, outdoor enthusiasts
"""
