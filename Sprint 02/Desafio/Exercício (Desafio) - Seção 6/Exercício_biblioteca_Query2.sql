------ ETAPA 1

SELECT 
    livro.cod AS CodLivro,
    livro.titulo AS Titulo,
    autor.codAutor AS CodAutor,
    autor.nome AS NomeAutor,
    livro.valor AS Valor,
    editora.codEditora AS CodEditora,
    editora.nome AS NomeEditora
FROM 
    livro
JOIN 
    autor ON livro.autor = autor.codAutor
JOIN 
    editora ON livro.editora = editora.codEditora
ORDER BY 
    livro.valor DESC
LIMIT 10;


------ ETAPA 2

SELECT 
    editora.codEditora AS CodEditora,
    editora.nome AS NomeEditora,
    COUNT(livro.cod) AS QuantidadeLivros
FROM 
    editora
JOIN 
    livro ON editora.codEditora = livro.editora
GROUP BY 
    editora.codEditora, editora.nome
ORDER BY 
    QuantidadeLivros DESC
LIMIT 5;
