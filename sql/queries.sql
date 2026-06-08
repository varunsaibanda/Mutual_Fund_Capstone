-- 1. Top 5 funds by AUM
SELECT * FROM fact_aum ORDER BY aum_value DESC LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav_value) FROM fact_nav;

-- 3. Maximum NAV
SELECT MAX(nav_value) FROM fact_nav;

-- 4. Minimum NAV
SELECT MIN(nav_value) FROM fact_nav;

-- 5. Total Transactions Amount
SELECT SUM(amount) FROM fact_transactions;

-- 6. Count Transactions
SELECT COUNT(*) FROM fact_transactions;

-- 7. Average Expense Ratio
SELECT AVG(expense_ratio) FROM fact_performance;

-- 8. Funds with Expense Ratio < 1
SELECT * FROM fact_performance
WHERE expense_ratio < 1;

-- 9. Top Performing Funds
SELECT * FROM fact_performance
ORDER BY return_percentage DESC
LIMIT 5;

-- 10. Total AUM
SELECT SUM(aum_value) FROM fact_aum;