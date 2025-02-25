from app.models.models import AdvergCampaignLink
from app.database.db import SessionLocal


def create_affilio_mapping(link_id: int, campaign_id: int):
    db = SessionLocal()
    try:
        mapping = AdvergCampaignLink(
            link_id=link_id,
            campaign_id=campaign_id
        )
        db.add(mapping)
        db.commit()
        db.refresh(mapping)
        return mapping
    finally:
        db.close()
