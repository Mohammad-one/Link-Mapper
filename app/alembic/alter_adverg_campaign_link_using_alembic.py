from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection


def upgrade():
    op.execute('CREATE SCHEMA IF NOT EXISTS "Link"')

    # Get a connection and use the inspector to check existing schema/table details
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


    inspector = reflection.Inspector.from_engine(bind)
    indexes = inspector.get_indexes('adverg_campaign_link', schema="Link")
    index_names = [idx['name'] for idx in indexes]


    if 'idx_link_id' not in index_names:
        op.create_index('idx_link_id', 'adverg_campaign_link', ['link_id'], schema="Link")
    if 'idx_campaign_id' not in index_names:
        op.create_index('idx_campaign_id', 'adverg_campaign_link', ['campaign_id'], schema="Link")


def downgrade():
    # Drop the indexes first
    op.drop_index('idx_link_id', table_name='adverg_campaign_link', schema="Link")
    op.drop_index('idx_campaign_id', table_name='adverg_campaign_link', schema="Link")
    # Then drop the table
    op.drop_table('adverg_campaign_link', schema="Link")