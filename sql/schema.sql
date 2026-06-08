CREATE TABLE IF NOT EXISTS dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date TEXT
);

CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav_value REAL
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    transaction_type TEXT,
    amount REAL
);

CREATE TABLE IF NOT EXISTS fact_performance (
    performance_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    return_percentage REAL,
    expense_ratio REAL
);

CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    aum_value REAL
);