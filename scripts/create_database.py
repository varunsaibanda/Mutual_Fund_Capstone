import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav_value REAL
)
""")

conn.commit()
conn.close()

print("Database and table created successfully")