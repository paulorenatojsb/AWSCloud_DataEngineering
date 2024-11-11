CREATE TABLE `Cliente` (
  `idCliente` INT PRIMARY KEY,
  `nomeCliente` VARCHAR,
  `cidadeCliente` VARCHAR,
  `estadoCliente` VARCHAR,
  `paisCliente` VARCHAR
);

CREATE TABLE `Carro` (
  `idCarro` INT PRIMARY KEY,
  `kmCarro` INT,
  `chassiCarro` VARCHAR,
  `marcaCarro` VARCHAR,
  `modeloCarro` VARCHAR,
  `anoCarro` INT
);

CREATE TABLE `Combustivel` (
  `idCombustivel` INT PRIMARY KEY,
  `tipoCombustivel` VARCHAR
);

CREATE TABLE `Vendedor` (
  `idVendedor` INT PRIMARY KEY,
  `nomeVendedor` VARCHAR,
  `sexoVendedor` SMALLINT,
  `estadoVendedor` VARCHAR
);

CREATE TABLE `Locacao` (
  `idLocacao` INT PRIMARY KEY,
  `idCliente` INT,
  `idCarro` INT,
  `idCombustivel` INT,
  `idVendedor` INT,
  `dataLocacao` DATETIME,
  `horaLocacao` TIME,
  `qtdDiaria` INT,
  `vlrDiaria` DECIMAL(18,2),
  `dataEntrega` DATE,
  `horaEntrega` TIME
);

ALTER TABLE `Locacao` ADD FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`);

ALTER TABLE `Locacao` ADD FOREIGN KEY (`idCarro`) REFERENCES `Carro` (`idCarro`);

ALTER TABLE `Locacao` ADD FOREIGN KEY (`idCombustivel`) REFERENCES `Combustivel` (`idCombustivel`);

ALTER TABLE `Locacao` ADD FOREIGN KEY (`idVendedor`) REFERENCES `Vendedor` (`idVendedor`);
