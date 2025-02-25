CREATE SCHEMA IF NOT EXISTS "Link";

DO $$
BEGIN

    CREATE TABLE IF NOT EXISTS "Link".adverg_campaign_link (
        id SERIAL PRIMARY KEY,
        link_id INTEGER NOT NULL,
        campaign_id INTEGER NOT NULL
    );

    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'Link'
          AND table_name = 'adverg_campaign_link'
          AND column_name = 'link_id'
    ) THEN
        ALTER TABLE "Link".adverg_campaign_link
        ADD COLUMN link_id INTEGER NOT NULL;
    END IF;

    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'Link'
          AND table_name = 'adverg_campaign_link'
          AND column_name = 'campaign_id'
    ) THEN
        ALTER TABLE "Link".adverg_campaign_link
        ADD COLUMN campaign_id INTEGER NOT NULL;
    END IF;


    IF NOT EXISTS (
        SELECT 1
        FROM pg_indexes
        WHERE schemaname = 'Link'
          AND indexname = 'idx_link_id'
    ) THEN
        CREATE INDEX idx_link_id
        ON "Link".adverg_campaign_link(link_id);
    END IF;

    IF NOT EXISTS (
        SELECT 1
        FROM pg_indexes
        WHERE schemaname = 'Link'
          AND indexname = 'idx_campaign_id'
    ) THEN
        CREATE INDEX idx_campaign_id
        ON "Link".adverg_campaign_link(campaign_id);
    END IF;
END $$;