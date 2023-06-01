SELECT 
    orders.order_id, 
    orders.order_status, 
    items.price, 
    items.freight_value, 
    ROUND((items.price + items.freight_value), 2) as full_price 
FROM 
    `dbt_shop.orders` as orders
INNER JOIN 
    `dbt_shop.items` as items on (items.order_id = orders.order_id)
WHERE 
    order_status like "shipped"