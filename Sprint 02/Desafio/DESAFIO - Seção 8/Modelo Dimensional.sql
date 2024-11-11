CREATE TABLE `DimCliente` (
  `idCliente` INT PRIMARY KEY,
  `nomeCliente` VARCHAR,
  `cidadeCliente` VARCHAR,
  `estadoCliente` VARCHAR,
  `paisCliente` VARCHAR
);

CREATE TABLE `DimCarro` (
  `idCarro` INT PRIMARY KEY,
  `kmCarro` INT,
  `chassiCarro` VARCHAR,
  `marcaCarro` VARCHAR,
  `modeloCarro` VARCHAR,
  `anoCarro` INT
);

CREATE TABLE `DimVendedor` (
  `idVendedor` INT PRIMARY KEY,
  `nomeVendedor` VARCHAR,
  `sexoVendedor` SMALLINT,
  `estadoVendedor` VARCHAR
);

CREATE TABLE `FatoLocacao` (
  `idLocacao` INT PRIMARY KEY,
  `idCliente` INT,
  `idCarro` INT,
  `idVendedor` INT,
  `dataLocacao` DATETIME,
  `horaLocacao` TIME,
  `qtdDiaria` INT,
  `vlrDiaria` DECIMAL(18,2),
  `dataEntrega` DATE,
  `horaEntrega` TIME
);

ALTER TABLE `FatoLocacao` ADD FOREIGN KEY (`idCliente`) REFERENCES `DimCliente` (`idCliente`);

ALTER TABLE `FatoLocacao` ADD FOREIGN KEY (`idCarro`) REFERENCES `DimCarro` (`idCarro`);

ALTER TABLE `FatoLocacao` ADD FOREIGN KEY (`idVendedor`) REFERENCES `DimVendedor` (`idVendedor`);
