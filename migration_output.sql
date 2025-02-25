BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> abc123def456

CREATE SCHEMA IF NOT EXISTS "Link";

CREATE TABLE IF NOT EXISTS "Link".campaign_link (
                id SERIAL PRIMARY KEY,
                link_id INTEGER NOT NULL,
                campaign_id INTEGER NOT NULL
            );

CREATE INDEX IF NOT EXISTS idx_link_id ON "Link".campaign_link(link_id);

CREATE INDEX IF NOT EXISTS idx_campaign_id ON "Link".adverg_campaign_link(campaign_id);

INSERT INTO alembic_version (version_num) VALUES ('abc123def456') RETURNING alembic_version.version_num;

COMMIT;

