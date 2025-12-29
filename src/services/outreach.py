from typing import List
from src.models import AnalyzeRequest, OutreachMessage

def build_outreach_en(req: AnalyzeRequest) -> List[OutreachMessage]:
    return [
        OutreachMessage(
            channel="email",
            subject=f"Backpacks for {req.positioning} — quick question",
            message=(
                f"Hi {{Name}},\n\n"
                f"I'm reaching out because we manufacture backpacks with {req.positioning} "
                f"and can do custom branding.\n\n"
                f"Is your team currently sourcing backpacks for promotions, employee kits, or resale?\n"
                f"If yes, I can share a short catalog + pricing.\n\n"
                f"Best,\n{{Your Name}}"
            ),
            followups=[
                "Hi {Name}, quick follow-up — happy to send a 1-page overview + pricing tiers. Interested?",
                "Last note — should I speak with someone else on your team about sourcing backpacks?"
            ],
        ),
        OutreachMessage(
            channel="linkedin_dm",
            message=(
                "Hi {Name} — quick one: we manufacture backpacks (custom branding possible). "
                "Are you the right person for sourcing promotional merchandise / employee gifts?"
            ),
            followups=[
                "Thanks! If helpful, I can send a short catalog + typical MOQs.",
            ],
        ),
        OutreachMessage(
            channel="instagram_dm",
            message=(
                "Hi! We manufacture backpacks and can do custom branding. "
                "Do you collaborate with suppliers for your shop/brand? "
                "I can share examples + MOQ/pricing."
            ),
            followups=[
                "Just checking if you saw my message — want me to send a few sample designs?"
            ],
        ),
        OutreachMessage(
            channel="marketplace_message",
            message=(
                "Hello! We manufacture backpacks (private label/custom branding). "
                "If you’re looking for a reliable supplier, I can share MOQ, lead times, and a quick catalog."
            ),
            followups=[
                "Can I send you our standard MOQ/lead time + 3 best-selling models?"
            ],
        ),
    ]
