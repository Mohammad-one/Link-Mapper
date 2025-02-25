"""Rename columns: link_id -> link_id, campaign_id -> campaign_id

Revision ID: def789ghi012
Revises: abc123def456
Create Date: 2025-02-23 12:00:00.000000
"""

# revision identifiers, used by Alembic.
revision = 'def789ghi012'
down_revision = 'abc123def456'
branch_labels = None
depends_on = None

from alembic import op

def upgrade():
    op.alter_column('adverg_campaign_link', 'link_id',
                    new_column_name='link_id',
                    schema="Link")
    op.alter_column('adverg_campaign_link', 'campaign_id',
                    new_column_name='campaign_id',
                    schema="Link")

def downgrade():
    op.alter_column('adverg_campaign_link', 'link_id',
                    new_column_name='link_id',
                    schema="Link")
    op.alter_column('adverg_campaign_link', 'campaign_id',
                    new_column_name='campaign_id',
                    schema="Link")
