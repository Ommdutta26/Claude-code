# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Run Application**: `python app.py` (Runs on port 5001 by default)
- **Database Initialization**: The database is automatically initialized and seeded on application startup via `init_db()` and `seed_db()` in `app.py`.

## Architecture and Structure

The project is a Flask-based expense tracking application called "Spendly".

### High-Level Structure
- `app.py`: Main application entry point. Contains Flask route definitions, session management, and request handling.
- `database/`: Package handling all data persistence.
    - `db.py`: Manages the SQLite connection, database schema creation (`init_db`), and basic user operations.
    - `queries.py`: Contains the business logic for data retrieval and modification (e.g., calculating summary stats, filtering expenses by date).

### Data Model
- **Users**: Stores user profiles with hashed passwords.
- **Expenses**: Linked to users via `user_id`. Tracks amount, category, date, and description.

### Key Flows
- **Authentication**: Uses Flask sessions and `werkzeug.security` for password hashing and verification.
- **Expense Management**: CRUD operations for expenses are handled through routes in `app.py` which call helper functions in `database/queries.py`.
- **Reporting**: The profile page aggregates summary stats and category breakdowns using SQLite `SUM` and `GROUP BY` queries.
