CREATE TABLE IF NOT EXISTS example_table (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO example_table (name) VALUES
('Alice'),
('Bob'),
('Charlie');