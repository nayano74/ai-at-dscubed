CREATE SCHEMA IF NOT EXISTS project_two;

CREATE TABLE IF NOT EXISTS project_two.nayan (
    id SERIAL PRIMARY KEY,
    math_problem TEXT NOT NULL,
    solution TEXT NOT NULL,
    difficulty TEXT CHECK (difficulty IN ('easy', 'medium', 'hard')),
    solved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
