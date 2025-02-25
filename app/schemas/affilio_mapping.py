from pydantic import BaseModel

class AffilioMappingRequest(BaseModel):
    link_id: int
    campaign_id: int

    model_config = {"arbitrary_types_allowed": True}
