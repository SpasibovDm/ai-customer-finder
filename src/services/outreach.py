def build_outreach_en(req) -> str:
    tone = req.tone
    product = req.product
    positioning = req.positioning or "high-quality"
    production = req.production_type or "custom branding available"

    subject = "Custom-branded backpacks for corporate use"
    opener = "Hello Mr./Ms. <Name>,"
    if tone == "friendly":
        opener = "Hi <Name>,"
        subject = "Quick question about custom backpacks"
    elif tone == "direct":
        opener = "Hello <Name>,"
        subject = "Backpack manufacturing (custom branding) — 15 min?"

    return f"""## Outreach messages (EN)

### B2B cold email (tone: {tone})
**Subject:** {subject}

{opener}

We are a {positioning} {product} supplier ({production}).
Many companies choose backpacks as a practical alternative to traditional giveaways — useful for employees and customers.

Would you like a short overview with examples and pricing options?

Best regards,  
<Your Name>

### Follow-up (Day 4)
Hi <Name>,  
just following up — would a 10–15 minute call be useful? I can share examples and typical price ranges.

### Final follow-up (Day 10)
Hi <Name>,  
last quick message from my side. If backpacks are relevant for your upcoming campaigns, I can share a short product overview and MOQ options.
"""
