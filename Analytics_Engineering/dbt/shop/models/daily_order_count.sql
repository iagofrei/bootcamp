{{ config(materialized='table') }}

   SELECT
      DATE(shipping_limit_date) AS shipping_date, 
      count(order_id) AS num_orders 
   FROM 
      `dbt_shop.items` 
   WHERE 
      DATE(shipping_limit_date)='{{ var("ingestion_date") }}' 
   GROUP BY 
      1