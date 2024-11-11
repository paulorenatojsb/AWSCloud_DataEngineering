-- Tabela Fato de Locações
CREATE VIEW FatoLocacao AS
SELECT 
    l.idLocacao,
    l.qtdDiaria,
    l.vlrDiaria,
    l.dataLocacao,
    l.dataEntrega,
    c.idCliente,
    ca.idCarro,
    cb.idCombustivel,
    v.idVendedor
FROM 
    Locacao l
JOIN 
    Cliente c ON l.idCliente = c.idCliente
JOIN 
    Carro ca ON l.idCarro = ca.idCarro
JOIN 
    Combustivel cb ON l.idCombustivel = cb.idCombustivel
JOIN 
    Vendedor v ON l.idVendedor = v.idVendedor;

-- Dimensão Cliente
CREATE VIEW DimCliente AS
SELECT 
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM 
    Cliente;

-- Dimensão Carro
CREATE VIEW DimCarro AS
SELECT 
    idCarro,
    kmCarro,
    chassiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro
FROM 
    Carro;

-- Dimensão Combustivel
CREATE VIEW DimCombustivel AS
SELECT 
    idCombustivel,
    tipoCombustivel
FROM 
    Combustivel;

-- Dimensão Vendedor
CREATE VIEW DimVendedor AS
SELECT 
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
FROM 
    Vendedor;
