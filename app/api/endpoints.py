from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.affilio_mapping import AffilioMappingRequest
from app.services import affilio_service, excel_service

router = APIRouter()

@router.post("/affilio-mapping/create", response_model=AffilioMappingRequest)
def create_mapping(mapping: AffilioMappingRequest):
    try:
        mapping_obj = affilio_service.create_affilio_mapping(
            mapping.link_id,
            mapping.campaign_id
        )
        return {
            "link_id": mapping_obj.link_id,
            "campaign_id": mapping_obj.campaign_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/affilio-mapping/upload/")
def upload_excel(file: UploadFile = File(...)):
    try:
        content = file.file.read()
        mappings = excel_service.process_excel_file(content)
        return {"created_mappings": mappings}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
