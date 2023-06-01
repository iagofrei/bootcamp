{{ config(materialized='table') }}

   SELECT
      extract(year from order_approved_at) as ano_do_pedido,
      count (order_id) as total
   FROM 
      `dbt_shop.orders` 
    WHERE
      order_approved_at IS NOT NULL
   GROUP BY 
      ano_do_pedido