-- Tabela Cliente
CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

-- Tabela Carro
CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    chassiCarro VARCHAR(30),
    marcaCarro VARCHAR(30),
    modeloCarro VARCHAR(20),
    anoCarro INT
);

-- Tabela Combustivel
CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

-- Tabela Vendedor
CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(4)
);

-- Tabela Locacao
CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idCombustivel INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);
