# Desafio de Modelagem de Dados Relacional e Dimensional

## Objetivo

O objetivo deste desafio foi aplicar os conceitos de **NORMALIZAÇÃO e MODELAGEM de DADOS RELACIONAL e DIMENSIONAL** utilizando a **Linguagem SQL**, para que este objetivo fosse alcançado utilizamos o banco [concessionaria.sqlite]() para normalizar uma tabela inicial e, em seguida, criar um modelo dimensional para análise de dados.

## Passo a Passo

### 1. Análise da Tabela Original

Iniciamos com a tabela `tb_locacao`, que contém dados misturados de clientes, carros, combustível, vendedores e locações. Essa tabela inclui dados redundantes, pois várias informações sobre clientes e carros se repetem para cada locação.

**Estrutura Inicial de `tb_locacao`:**

| Campo             | Tipo          |
|-------------------|---------------|
| idLocacao         | INT           |
| idCliente         | INT           |
| nomeCliente       | VARCHAR(100)  |
| cidadeCliente     | VARCHAR(40)   |
| estadoCliente     | VARCHAR(40)   |
| paisCliente       | VARCHAR(40)   |
| idCarro           | INT           |
| kmCarro           | INT           |
| chassiCarro       | VARCHAR(30)   |
| marcaCarro        | VARCHAR(30)   |
| modeloCarro       | VARCHAR(20)   |
| anoCarro          | INT           |
| idCombustivel     | INT           |
| tipoCombustivel   | VARCHAR(20)   |
| dataLocacao       | DATETIME      |
| horaLocacao       | TIME          |
| qtdDiaria         | INT           |
| vlrDiaria         | DECIMAL(18,2) |
| dataEntrega       | DATE          |
| horaEntrega       | TIME          |
| idVendedor        | INT           |
| nomeVendedor      | VARCHAR(15)   |
| sexoVendedor      | SMALLINT      |
| estadoVendedor    | VARCHAR(4)    |

### 2. Normalização da Tabela `tb_locacao`

Para eliminar redundâncias e melhorar a organização, aplicamos as **formas normais** e dividimos `tb_locacao` em tabelas separadas para cada entidade principal:

#### Passos de Normalização:

1. **Primeira Forma Normal (1NF)**:
   - Garantimos que todos os campos contêm valores atômicos e indivisíveis.
   
2. **Segunda Forma Normal (2NF)**:
   - Removemos as dependências parciais, garantindo que cada tabela contém apenas informações relacionadas a uma única entidade. Criamos tabelas independentes para **Cliente**, **Carro**, **Combustivel** e **Vendedor**.

3. **Terceira Forma Normal (3NF)**:
   - Removemos dependências transitivas, assegurando que cada coluna não-chave é dependente apenas da chave primária de sua tabela.

#### Tabelas Resultantes:

- **Cliente**: Informações do cliente (`idCliente`, `nomeCliente`, `cidadeCliente`, `estadoCliente`, `paisCliente`).
- **Carro**: Detalhes do carro (`idCarro`, `kmCarro`, `chassiCarro`, `marcaCarro`, `modeloCarro`, `anoCarro`).
- **Combustivel**: Tipo de combustível (`idCombustivel`, `tipoCombustivel`).
- **Vendedor**: Informações do vendedor (`idVendedor`, `nomeVendedor`, `sexoVendedor`, `estadoVendedor`).
- **Locacao**: Informações específicas da locação (`idLocacao`, `idCliente`, `idCarro`, `idCombustivel`, `idVendedor`, `dataLocacao`, `horaLocacao`, `qtdDiaria`, `vlrDiaria`, `dataEntrega`, `horaEntrega`).

#### Script SQL para o Modelo Relacional:

O script `modelo_relacional.sql` contém as instruções SQL para criar as tabelas normalizadas com suas respectivas chaves primárias e estrangeiras, garantindo a integridade dos dados.

### 3. Criação do Modelo Dimensional

Após a normalização, criamos um **modelo dimensional** baseado no modelo relacional. O objetivo do modelo dimensional é facilitar a análise de dados e consultas analíticas, estruturando as informações em uma tabela **fato** e várias tabelas de **dimensões**.

#### Estrutura do Modelo Dimensional:

1. **Tabela Fato (`FatoLocacao`)**:
   - Representa os eventos de locação e contém métricas como `qtdDiaria` e `vlrDiaria`.
   
2. **Tabelas de Dimensão**:
   - **DimCliente**: Contém dados sobre os clientes.
   - **DimCarro**: Contém dados sobre os carros.
   - **DimCombustivel**: Contém dados sobre os tipos de combustível.
   - **DimVendedor**: Contém dados sobre os vendedores.

#### Script SQL para o Modelo Dimensional:

O script `modelo_dimensional.sql` inclui as instruções SQL para criar a tabela fato e as tabelas de dimensão, com relacionamentos estabelecidos para permitir análises de métricas por cliente, carro, tipo de combustível e vendedor.

### 4. Diagramas

- **Modelo Relacional**: O diagrama `modelo_relacional.png` ilustra a estrutura das tabelas normalizadas e seus relacionamentos.
- **Modelo Dimensional**: O diagrama `modelo_dimensional.png` mostra o modelo dimensional em formato de estrela, com a tabela fato `FatoLocacao` no centro e as dimensões ao redor.

## Arquivos na Pasta Desafio


- `modelo_relacional.sql`: Script SQL do modelo relacional.
- `modelo_relacional.png`: Diagrama do modelo relacional.
- `modelo_dimensional.sql`: Script SQL do modelo dimensional.
- `modelo_dimensional.png`: Diagrama do modelo dimensional.

## Conclusão

Este desafio permitiu aplicar e reforçar conceitos de normalização e modelagem dimensional, essencial para o design de bases de dados otimizadas tanto para operações transacionais quanto para análises. O processo envolveu dividir a tabela original, remover redundâncias e estruturar os dados de maneira que facilite a consulta e análise no futuro.
O repositório Git contém os arquivos organizados da seguinte forma:

