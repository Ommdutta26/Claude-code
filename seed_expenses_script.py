import random
from datetime import datetime, timedelta
from database.db import get_db

def seed_expenses(user_id, count, months):
    categories = {
        "Food": {"range": (50, 800), "weight": 30, "desc": ["Zomato Order", "Street Food", "Grocery store", "Cafe Coffee", "Dinner at home"]},
        "Transport": {"range": (20, 500), "weight": 20, "desc": ["Ola/Uber Ride", "Auto Rickshaw", "Petrol Fill", "Metro Recharge", "Bus Ticket"]},
        "Bills": {"range": (200, 3000), "weight": 15, "desc": ["Electricity Bill", "Water Bill", "Mobile Recharge", "WiFi Bill", "Gas Cylinder"]},
        "Health": {"range": (100, 2000), "weight": 5, "desc": ["Pharmacy", "Doctor Visit", "Medicine", "Lab Test", "Health Supplement"]},
        "Entertainment": {"range": (100, 1500), "weight": 5, "desc": ["Movie Tickets", "Netflix Subscription", "Bowling", "Gaming Zone", "Book Purchase"]},
        "Shopping": {"range": (200, 5000), "weight": 15, "desc": ["Amazon Order", "Myntra Clothing", "Supermarket", "Gift Purchase", "Electronics"]},
        "Other": {"range": (50, 1000), "weight": 10, "desc": ["Misc Expense", "Donation", "Parking Fee", "Stationery", "Random Purchase"]}
    }

    cat_list = list(categories.keys())
    weights = [categories[c]["weight"] for c in cat_list]

    expenses = []
    today = datetime.now()
    start_date = today - timedelta(days=months * 30)

    for _ in range(count):
        category = random.choices(cat_list, weights=weights)[0]
        amount = round(random.uniform(*categories[category]["range"]), 2)
        description = random.choice(categories[category]["desc"])

        # Random date within the specified range
        days_offset = random.randint(0, months * 30)
        expense_date = (start_date + timedelta(days=days_offset)).strftime('%Y-%m-%d')

        expenses.append((user_id, amount, category, expense_date, description))

    try:
        conn = get_db()
        with conn:
            conn.executemany(
                "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
                expenses
            )

        # Get details for confirmation
        cursor = conn.execute(
            "SELECT date, amount, category, description FROM expenses WHERE user_id = ? ORDER BY id DESC LIMIT ?",
            (user_id, count)
        )
        inserted = cursor.fetchall()

        dates = [row['date'] for row in inserted]
        print(f"Successfully inserted {len(inserted)} expenses.")
        print(f"Date range: {min(dates)} to {max(dates)}")
        print("\nSample records:")
        for row in inserted[:5]:
            print(f"{row['date']} | {row['category']} | Rs.{row['amount']} | {row['description']}")

    except Exception as e:
        print(f"Error occurred: {e}")
        raise e
    finally:
        conn.close()

if __name__ == "__main__":
    seed_expenses(2, 5, 3)
