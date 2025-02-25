import io
import pandas as pd
from app.services.affilio_service import create_affilio_mapping


def process_excel_file(file_content: bytes):
    df = pd.read_excel(io.BytesIO(file_content))

    required_columns = {'link_id', 'campaign_id'}
    if not required_columns.issubset(df.columns):
        raise ValueError("Excel file must contain columns: link_id and campaign_id")

    created_mappings = []
    for _, row in df.iterrows():
        mapping = create_affilio_mapping(
            int(row['link_id']),
            int(row['campaign_id'])
        )
        created_mappings.append({
            "id": mapping.id,
            "link_id": mapping.link_id,
            "campaign_id": mapping.campaign_id
        })
    return created_mappings