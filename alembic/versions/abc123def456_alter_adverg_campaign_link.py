"""create or alter adverg_campaign_link table in schema "Link"

Revision ID: abc123def456
Revises:
Create Date: 2025-02-22 10:00:00.000000
"""

# revision identifiers, used by Alembic.
revision = 'abc123def456'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection
from alembic import context

def upgrade():
    # Ensure the "Link" schema exists.
    op.execute('CREATE SCHEMA IF NOT EXISTS "Link"')

    if context.is_offline_mode():
        # Offline mode: Emit static SQL without using reflection.
        op.execute('''
            CREATE TABLE IF NOT EXISTS "Link".adverg_campaign_link (
                id SERIAL PRIMARY KEY,
                link_id INTEGER NOT NULL,
                campaign_id INTEGER NOT NULL
            )
        ''')
        op.execute('CREATE INDEX IF NOT EXISTS idx_link_id ON "Link".adverg_campaign_link(link_id)')
        op.execute('CREATE INDEX IF NOT EXISTS idx_campaign_id ON "Link".adverg_campaign_link(campaign_id)')
    else:
        # Online mode: Use reflection to inspect the current state.
        bind = op.get_bind()
        inspector = reflection.Inspector.from_engine(bind)
        tables = inspector.get_table_names(schema="Link")

        if 'adverg_campaign_link' not in tables:
            op.create_table(
                'adverg_campaign_link',
                sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                sa.Column('link_id', sa.Integer, nullable=False),
                sa.Column('campaign_id', sa.Integer, nullable=False),
                schema="Link"
            )
        else:
            existing_columns = [col['name'] for col in inspector.get_columns('adverg_campaign_link', schema="Link")]
            if 'link_id' not in existing_columns:
                op.add_column('adverg_campaign_link',
                              sa.Column('link_id', sa.Integer, nullable=False),
                              schema="Link")
            if 'campaign_id' not in existing_columns:
                op.add_column('adverg_campaign_link',
                              sa.Column('campaign_id', sa.Integer, nullable=False),
                              schema="Link")

        # Refresh the inspector to check for indexes.
        inspector = reflection.Inspector.from_engine(bind)
        indexes = inspector.get_indexes('adverg_campaign_link', schema="Link")
        index_names = [idx['name'] for idx in indexes]

        if 'idx_link_id' not in index_names:
            op.create_index('idx_link_id', 'adverg_campaign_link', ['link_id'], schema="Link")
        if 'idx_campaign_id' not in index_names:
            op.create_index('idx_campaign_id', 'adverg_campaign_link', ['campaign_id'], schema="Link")


def downgrade():
    # Downgrade: drop indexes then drop the table.
    op.drop_index('idx_link_id', table_name='adverg_campaign_link', schema="Link")
    op.drop_index('idx_campaign_id', table_name='adverg_campaign_link', schema="Link")
    op.drop_table('adverg_campaign_link', schema="Link")