# Data Dictionary

## 01_fund_master.csv

| Column | Description |
|----------|-------------|
| amfi_code | Unique fund identifier |
| fund_name | Name of the mutual fund |
| fund_house | Fund management company |
| category | Fund category |
| sub_category | Fund sub category |

---

## 02_nav_history.csv

| Column | Description |
|----------|-------------|
| amfi_code | Fund identifier |
| date | NAV date |
| nav | Net Asset Value |

---

## 07_scheme_performance.csv

| Column | Description |
|----------|-------------|
| amfi_code | Fund identifier |
| return_percentage | Scheme return |
| expense_ratio | Expense ratio |

---

## 08_investor_transactions.csv

| Column | Description |
|----------|-------------|
| transaction_id | Transaction identifier |
| amount | Transaction amount |
| transaction_type | SIP/Lumpsum etc. |