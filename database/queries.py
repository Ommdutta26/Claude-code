from database.db import get_db

def get_user_by_id(user_id):
    """Retrieves a user by their ID."""
    with get_db() as conn:
        return conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

def get_summary_stats(user_id, date_from=None, date_to=None):
    """
    Calculates summary stats for a user: total spent and total transactions.
    Filters by date if provided.
    """
    query = "SELECT SUM(amount) as total, COUNT(*) as count FROM expenses WHERE user_id = ?"
    params = [user_id]

    if date_from:
        query += " AND date >= ?"
        params.append(date_from)
    if date_to:
        query += " AND date <= ?"
        params.append(date_to)

    with get_db() as conn:
        return conn.execute(query, params).fetchone()

def get_recent_transactions(user_id, date_from=None, date_to=None):
    """Retrieves recent expenses for a user, sorted by date descending."""
    query = "SELECT * FROM expenses WHERE user_id = ? ORDER BY date DESC"
    params = [user_id]

    if date_from:
        query += " AND date >= ?"
        params.append(date_from)
    if date_to:
        query += " AND date <= ?"
        params.append(date_to)

    # Re-evaluating query to ensure AND logic is handled correctly with ORDER BY
    # Correct logic: WHERE ... AND ... ORDER BY ...
    sql = "SELECT * FROM expenses WHERE user_id = ?"
    params = [user_id]
    if date_from:
        sql += " AND date >= ?"
        params.append(date_from)
    if date_to:
        sql += " AND date <= ?"
        params.append(date_to)
    sql += " ORDER BY date DESC"

    with get_db() as conn:
        return conn.execute(sql, params).fetchall()

def get_category_breakdown(user_id, date_from=None, date_to=None):
    """Returns total spent per category for a user."""
    sql = "SELECT category, SUM(amount) as total FROM expenses WHERE user_id = ?"
    params = [user_id]

    if date_from:
        sql += " AND date >= ?"
        params.append(date_from)
    if date_to:
        sql += " AND date <= ?"
        params.append(date_to)

    sql += " GROUP BY category"

    with get_db() as conn:
        return conn.execute(sql, params).fetchall()

def insert_expense(user_id, amount, category, date, description):
    """Inserts a new expense record."""
    with get_db() as conn:
        conn.execute(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            (user_id, amount, category, date, description)
        )
        conn.commit()

def get_expense_by_id(expense_id, user_id):
    """Retrieves a specific expense, ensuring it belongs to the given user."""
    with get_db() as conn:
        return conn.execute(
            "SELECT * FROM expenses WHERE id = ? AND user_id = ?",
            (expense_id, user_id)
        ).fetchone()

def update_expense(expense_id, user_id, amount, category, date, description):
    """Updates an existing expense record."""
    with get_db() as conn:
        conn.execute(
            "UPDATE expenses SET amount = ?, category = ?, date = ?, description = ? WHERE id = ? AND user_id = ?",
            (amount, category, date, description, expense_id, user_id)
        )
        conn.commit()

def delete_expense_by_id(expense_id, user_id):
    """Deletes an expense record."""
    with get_db() as conn:
        conn.execute(
            "DELETE FROM expenses WHERE id = ? AND user_id = ?",
            (expense_id, user_id)
        )
        conn.commit()
