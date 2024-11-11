----- EXERCICIO 1 SEÇÃO 3

SELECT 
    LIVRO.cod,
    LIVRO.titulo,
    AUTOR.nome AS autor,
    EDITORA.nome AS editora,
    LIVRO.valor,
    LIVRO.publicacao,
    LIVRO.edicao,
    LIVRO.idioma
FROM 
    LIVRO
JOIN 
    AUTOR ON LIVRO.autor = AUTOR.codAutor
JOIN 
    EDITORA ON LIVRO.editora = EDITORA.codEditora
WHERE 
    LIVRO.publicacao > '2014-12-31'
ORDER BY 
    LIVRO.cod ASC;
    
----- EXERCICIO 2 SEÇÃO 3
   
SELECT 
    titulo,
    valor
FROM 
    LIVRO
ORDER BY 
    valor DESC
LIMIT 10;

----- EXERCICIO 3 SEÇÃO 3

SELECT 
    COUNT(LIVRO.cod) AS quantidade,
    EDITORA.nome,
    ENDERECO.estado,
    ENDERECO.cidade
FROM 
    EDITORA
JOIN 
    LIVRO ON EDITORA.codEditora = LIVRO.editora
JOIN 
    ENDERECO ON EDITORA.endereco = ENDERECO.codEndereco
GROUP BY 
    EDITORA.nome, ENDERECO.estado, ENDERECO.cidade
ORDER BY 
    quantidade DESC
LIMIT 5;

----- EXERCICIO 4 SEÇÃO 3

SELECT 
    AUTOR.nome AS nome,
    AUTOR.codAutor AS codautor,
    AUTOR.nascimento AS nascimento,
    COALESCE(COUNT(LIVRO.cod), 0) AS quantidade
FROM 
    AUTOR
LEFT JOIN 
    LIVRO ON AUTOR.codAutor = LIVRO.autor
GROUP BY 
    AUTOR.codAutor, AUTOR.nome, AUTOR.nascimento
ORDER BY 
    AUTOR.nome ASC;
   
----- EXERCICIO 5 SEÇÃO 3
   
  SELECT DISTINCT
    autor.nome
FROM 
    autor
JOIN 
    livro ON autor.codautor = livro.autor
JOIN 
    editora ON livro.editora = editora.codeditora
JOIN 
    endereco ON editora.endereco = endereco.codendereco
WHERE 
    endereco.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY 
    autor.nome ASC;
   
----- EXERCICIO 6 SEÇÃO 3
 
   SELECT 
    autor.codautor,
    autor.nome,
    COUNT(livro.cod) AS quantidade_publicacoes
FROM 
    autor
JOIN 
    livro ON autor.codautor = livro.autor
GROUP BY 
    autor.codautor, autor.nome
ORDER BY 
    quantidade_publicacoes DESC
LIMIT 1;

----- EXERCICIO 7 SEÇÃO 3

SELECT 
    autor.nome
FROM 
    autor
LEFT JOIN 
    livro ON autor.codautor = livro.autor
WHERE 
    livro.cod IS NULL
ORDER BY 
    autor.nome ASC;

----- EXERCICIO 8 SEÇÃO 3


