SELECT 
    case
        when customer_state like 'AM' then 'Norte'
        when customer_state like 'RR' then 'Norte'
        when customer_state like 'AP' then 'Norte'
        when customer_state like 'PA' then 'Norte'
        when customer_state like 'TO' then 'Norte'
        when customer_state like 'RO' then 'Norte'
        when customer_state like 'AC' then 'Norte'
        when customer_state like 'RN' then 'Nordeste'
        when customer_state like 'CE' then 'Nordeste'
        when customer_state like 'MA' then 'Nordeste'
        when customer_state like 'PI' then 'Nordeste'
        when customer_state like 'PE' then 'Nordeste'
        when customer_state like 'PB' then 'Nordeste'
        when customer_state like 'SE' then 'Nordeste'
        when customer_state like 'AL' then 'Nordeste'
        when customer_state like 'BA' then 'Nordeste'
        when customer_state like 'MT' then 'Centro-Oeste'
        when customer_state like 'MS' then 'Centro-Oeste'
        when customer_state like 'GO' then 'Centro-Oeste'
        when customer_state like 'DF' then 'Centro-Oeste'
        when customer_state like 'SP' then 'Sudeste'
        when customer_state like 'RJ' then 'Sudeste'
        when customer_state like 'MG' then 'Sudeste'
        when customer_state like 'ES' then 'Sudeste'
        when customer_state like 'PR' then 'Sul'
        when customer_state like 'SC' then 'Sul'
        when customer_state like 'RS' then 'Sul'

    end as regiao,
    count (customer_id) as numero_de_clientes
FROM `dbt_shop.customers`
GROUP BY regiao