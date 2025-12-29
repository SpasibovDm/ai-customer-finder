def build_channels_en(req) -> str:
    region = req.region
    return f"""## Where to find customers — {region}

### B2B channels
- **Google Maps**
  - Search queries: "promotional products distributor", "corporate gifts supplier", "event marketing agency"
- **LinkedIn**
  - Titles: Procurement Manager, Marketing Manager, HR Manager, Office Manager
- **B2B directories**
  - Europages, Kompass, local business directories

### B2C channels
- Amazon (EU), Etsy (custom), Zalando (if brand-ready), Shopify + Google Shopping
- Instagram/TikTok: creators (UGC) + paid ads with best creatives
"""
