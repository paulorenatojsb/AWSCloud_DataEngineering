CREATE TABLE `Cliente` (
  `cliente_id` bigserial PRIMARY KEY COMMENT 'Identificador único do cliente',
  `nome` varchar(255) NOT NULL COMMENT 'Nome do cliente',
  `documento_identidade` varchar(255) NOT NULL COMMENT 'Documento de identidade do cliente',
  `telefone` varchar(255) COMMENT 'Telefone do cliente',
  `email` varchar(255) COMMENT 'Email do cliente'
);

CREATE TABLE `Carro` (
  `carro_id` bigserial PRIMARY KEY COMMENT 'Identificador único do carro',
  `modelo` varchar(255) NOT NULL COMMENT 'Modelo do carro',
  `marca` varchar(255) NOT NULL COMMENT 'Marca do carro',
  `ano` int COMMENT 'Ano de fabricação do carro',
  `placa` varchar(255) NOT NULL COMMENT 'Placa do carro',
  `tipo_combustivel_id` bigint COMMENT 'Referência ao tipo de combustível'
);

CREATE TABLE `Combustivel` (
  `tipo_combustivel_id` bigserial PRIMARY KEY COMMENT 'Identificador único do tipo de combustível',
  `descricao` varchar(255) NOT NULL COMMENT 'Descrição do tipo de combustível'
);

CREATE TABLE `Vendedor` (
  `vendedor_id` bigserial PRIMARY KEY COMMENT 'Identificador único do vendedor',
  `nome` varchar(255) NOT NULL COMMENT 'Nome do vendedor',
  `telefone` varchar(255) COMMENT 'Telefone do vendedor',
  `email` varchar(255) COMMENT 'Email do vendedor'
);

CREATE TABLE `Locacao` (
  `locacao_id` bigserial PRIMARY KEY COMMENT 'Identificador único da locação',
  `cliente_id` bigint NOT NULL COMMENT 'Referência ao cliente',
  `carro_id` bigint NOT NULL COMMENT 'Referência ao carro',
  `vendedor_id` bigint NOT NULL COMMENT 'Referência ao vendedor',
  `data_locacao` timestamp NOT NULL COMMENT 'Data da locação',
  `data_devolucao` timestamp COMMENT 'Data da devolução',
  `valor_total` decimal NOT NULL COMMENT 'Valor total da locação'
);

ALTER TABLE `Carro` ADD FOREIGN KEY (`tipo_combustivel_id`) REFERENCES `Combustivel` (`tipo_combustivel_id`);

ALTER TABLE `Locacao` ADD FOREIGN KEY (`cliente_id`) REFERENCES `Cliente` (`cliente_id`);

ALTER TABLE `Locacao` ADD FOREIGN KEY (`carro_id`) REFERENCES `Carro` (`carro_id`);

ALTER TABLE `Locacao` ADD FOREIGN KEY (`vendedor_id`) REFERENCES `Vendedor` (`vendedor_id`);
