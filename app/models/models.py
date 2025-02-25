from sqlalchemy import Column, Integer
from app.database.db import Base


class AdvergCampaignLink(Base):
    __tablename__ = "adverg_campaign_link"
    __table_args__ = {'schema': 'Link'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    link_id = Column(Integer, nullable=False)       # renamed
    campaign_id = Column(Integer, nullable=False)     # renamed


