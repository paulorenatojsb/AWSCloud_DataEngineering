---- EXERCICIO 8 SEÇÃO 4

SELECT 
    tbvendedor.cdvdd,
    tbvendedor.nmvdd
FROM 
    tbvendas
JOIN 
    tbvendedor ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE 
    tbvendas.status = 'Concluído'
GROUP BY 
    tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY 
    COUNT(tbvendas.cdven) DESC
LIMIT 1;

---- EXERCICIO 9 SEÇÃO 5

SELECT 
    tbvendas.cdpro,
    tbvendas.nmpro
FROM 
    tbvendas
WHERE 
    tbvendas.status = 'Concluído'
    AND tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY 
    tbvendas.cdpro, tbvendas.nmpro
ORDER BY 
    COUNT(tbvendas.cdven) DESC
LIMIT 1;

---- EXERCICIO 10 SEÇÃO 5

SELECT t.nmvdd as vendedor,
    SUM(t2.qtd * t2.vrunt) as valor_total_vendas,
    ROUND(SUM(t2.qtd * t2.vrunt) * (t.perccomissao)/100, 2) as comissao
FROM 
	tbvendedor t 
JOIN 
	tbvendas t2 
	ON t.cdvdd = t2.cdvdd
WHERE
	t2.status = 'Concluído'
GROUP BY
	t.nmvdd 
ORDER BY
	comissao DESC;

---- EXERCICIO 11 SEÇÃO 5

SELECT 
    tbvendas.cdcli,
    tbvendas.nmcli,
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt), 2) AS gasto
FROM 
    tbvendas
WHERE 
    tbvendas.status = 'Concluído'
GROUP BY 
    tbvendas.cdcli, tbvendas.nmcli
ORDER BY 
    gasto DESC
LIMIT 1;

---- EXERCICIO 12 SEÇÃO 5

WITH VendasPorVendedor AS (
    SELECT 
        tbvendas.cdvdd,
        SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas
    FROM 
        tbvendas
    WHERE 
        tbvendas.status = 'Concluído'
    GROUP BY 
        tbvendas.cdvdd
    HAVING 
        SUM(tbvendas.qtd * tbvendas.vrunt) > 0
    ORDER BY 
        valor_total_vendas ASC
    LIMIT 1
)

SELECT 
    tbdependente.cddep,
    tbdependente.nmdep,
    tbdependente.dtnasc,
    VendasPorVendedor.valor_total_vendas
FROM 
    tbdependente
JOIN 
    VendasPorVendedor ON tbdependente.cdvdd = VendasPorVendedor.cdvdd;

---- EXERCICIO 13 SEÇÃO 5

WITH vendas_canal AS (
    SELECT
        cdpro,
        nmcanalvendas,
        nmpro,
        SUM(qtd) AS quantidade_vendas
    FROM
        TBVENDAS
    WHERE
        nmcanalvendas IN ('Ecommerce', 'Matriz')
        AND status = 'Concluído'
    GROUP BY
        cdpro,
        nmcanalvendas,
        nmpro
)
SELECT
    cdpro,
    nmcanalvendas,
    nmpro,
    quantidade_vendas
FROM
    vendas_canal
ORDER BY
    quantidade_vendas ASC
LIMIT 10;

---- EXERCICIO 14 SEÇÃO 5

SELECT 
    estado,
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio
FROM 
    TBVENDAS
WHERE 
    status = 'Concluído'
GROUP BY 
    estado
ORDER BY 
    gastomedio DESC;

---- EXERCICIO 15 SEÇÃO 5
   
SELECT 
    cdven
FROM 
    TBVENDAS
WHERE 
    deletado = '1'
ORDER BY 
    cdven ASC;
    
---- EXERCICIO 16 SEÇÃO 5

SELECT 
    estado,
    nmpro AS nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM 
    TBVENDAS
WHERE 
    status = 'Concluído'
GROUP BY 
    estado, nmpro
ORDER BY 
    estado ASC, 
    nmpro ASC;
