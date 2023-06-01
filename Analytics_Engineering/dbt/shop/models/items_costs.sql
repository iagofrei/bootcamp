{{ config(materialized='table') }}

   SELECT
      order_id,
      order_item_id, 
      product_id,
      ((price + freight_value)) as item_cost
   FROM 
      `dbt_shop.items`