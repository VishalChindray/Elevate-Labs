-- Total Revenue
SELECT SUM(total_amount) AS total_revenue FROM orders;

-- Average Revenue per User
SELECT AVG(total_amount) AS avg_revenue_per_user FROM orders;

-- Orders with Customer Info
SELECT o.order_id, c.name, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- Total Spend per Customer
SELECT c.name, SUM(o.total_amount) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.name
ORDER BY total_spent DESC;

-- Customers with No Orders
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Create a View
CREATE VIEW order_summary AS
SELECT o.order_id, c.name AS customer_name, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- Subquery: Customers Who Spent Above Average
SELECT c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
HAVING SUM(o.total_amount) > (
    SELECT AVG(total_amount) FROM orders
);

-- Optimize with Index
CREATE INDEX idx_customer_id ON orders(customer_id);

-- Handle NULLs
SELECT COALESCE(SUM(total_amount), 0) AS revenue FROM orders;
