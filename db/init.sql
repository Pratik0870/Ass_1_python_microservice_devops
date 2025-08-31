CREATE TABLE IF NOT EXISTS heartbeats (
    id SERIAL PRIMARY KEY,
    details JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
