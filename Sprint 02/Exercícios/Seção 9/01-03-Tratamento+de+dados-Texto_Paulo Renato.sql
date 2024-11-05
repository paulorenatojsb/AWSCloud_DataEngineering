-- EXEMPLOS ########################################################################

-- (Exemplo 1) Corrija o primeiro elemento das queries abaixo utilizando os comandos 
-- de tratamento de texto para que o resultado seja sempre TRUE 

-- select 'São Paulo' = 'SÃO PAULO'

select upper('São Paulo') = 'SÃO PAULO'

-- select 'São Paulo' = 'são paulo'

select lower('São Paulo') = 'são paulo'

-- select 'SÃO PAULO     ' = 'SÃO PAULO'

select trim('SÃO PAULO     ') = 'SÃO PAULO'

-- select 'SAO PAULO' = 'SÃO PAULO'

select replace('SAO PAULO', 'SAO', 'SÃO') = 'SÃO PAULO'