-- {{ config(materialized='view') }}

SELECT
    customers.customer_state as estado, 
    count(orders.order_id) as total
FROM 
    `dbt_shop.orders` as orders
INNER JOIN
    `dbt_shop.customers` as customers on (orders.customer_id = customers.customer_id)
GROUP BY customers.customer_state