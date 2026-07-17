-- Solutions library schema (SQLite)
-- Run: sqlite3 data/solutions.db < sql/schema.sql

CREATE TABLE IF NOT EXISTS solutions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    use_case TEXT,
    problem TEXT,
    architecture TEXT,
    iterable_components TEXT,
    integrations TEXT,
    demo_url TEXT,
    guru_card_path TEXT,
    tags TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_solutions_use_case ON solutions(use_case);
CREATE INDEX IF NOT EXISTS idx_solutions_tags ON solutions(tags);
