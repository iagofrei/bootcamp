SELECT
    *
FROM 
    `dataset_iago.totais_pedidos_por_estado`
WHERE
    total > CAST('{{ var("number_of_orders") }}' as INT64)