# Desafio de Modelagem de Dados Relacional e Dimensional

## Objetivo

O objetivo deste desafio foi aplicar os conceitos de **NORMALIZAÇÃO e MODELAGEM de DADOS RELACIONAL e DIMENSIONAL** utilizando a **Linguagem SQL**, para que este objetivo fosse alcançado utilizamos o banco [concessionaria.sqlite](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2002/Desafio/DESAFIO%20-%20Se%C3%A7%C3%A3o%208/concessionaria.sqlite). A partir deste arquivo, inicialmente normalizei a tabela e, em seguida, segui para a criação do relacional e dimensional para análise de dados.

## Passo a Passo

### 1. Análise Inicial

A tabela `tb_locacao` estava com os dados "misturados" em uma única sheet: clientes, carros, combustível, vendedores e locações. Desta forma, muitos dados estavam redundantes, fazendo com que algumas informações se repetissem diversas vezes.

**Modelo Inicial da Tabelam Locação `tb_locacao`:**

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

### 2. Passo a Passo - Normalização da Tabela `tb_locacao`

Para eliminar redundâncias e melhorar a organização, apliquei as **formas normais**, dividindo a `tb_locacao` em tabelas separadas para cada entidade principal. Desta forma, criei tabelas independentes para **Cliente**, **Carro**, **Combustivel** e **Vendedor**.
A Query da normalização está disponivel em [Desafio_normalização.sql](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2002/Desafio/DESAFIO%20-%20Se%C3%A7%C3%A3o%208/Desafio_normaliza%C3%A7%C3%A3o.sql)

#### Formas Normais

1. **Primeira Forma Normal (1NF)**:
   - Garantir que todos os campos contêm valores atômicos e indivisíveis.
2. **Segunda Forma Normal (2NF)**:
   - Remover as dependências parciais, garantindo que cada tabela contém apenas informações relacionadas a uma única entidade. 
3. **Terceira Forma Normal (3NF)**:
   - Remover as dependências transitivas, assegurando que cada coluna não-chave é dependente apenas da chave primária de sua tabela.

#### Tabelas Resultantes:

- **Cliente**: Informações do cliente (`idCliente`, `nomeCliente`, `cidadeCliente`, `estadoCliente`, `paisCliente`).
- **Carro**: Detalhes do carro (`idCarro`, `kmCarro`, `chassiCarro`, `marcaCarro`, `modeloCarro`, `anoCarro`).
- **Combustivel**: Tipo de combustível (`idCombustivel`, `tipoCombustivel`).
- **Vendedor**: Informações do vendedor (`idVendedor`, `nomeVendedor`, `sexoVendedor`, `estadoVendedor`).
- **Locacao**: Informações específicas da locação (`idLocacao`, `idCliente`, `idCarro`, `idCombustivel`, `idVendedor`, `dataLocacao`, `horaLocacao`, `qtdDiaria`, `vlrDiaria`, `dataEntrega`, `horaEntrega`).

[Evidencia da Normalização]()

### 3. Script para o Modelo Relacional:

O script [`Modelo Relacional.sql`](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2002/Desafio/DESAFIO%20-%20Se%C3%A7%C3%A3o%208/Modelo%20Relacional.sql) contém as instruções SQL para criar o Diagrama Relacional, com suas respectivas chaves primárias e estrangeiras, garantindo a integridade dos dados.

![Modelo Relacional_versão final.png](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2002/Desafio/DESAFIO%20-%20Se%C3%A7%C3%A3o%208/Modelo%20Relacional_vers%C3%A3o%20final.png)

O diagrama `Modelo Relacional_versão final.png` ilustra a estrutura das tabelas normalizadas e seus relacionamentos.

### 4. Criação do Modelo Dimensional

Após a normalização, criei um **modelo dimensional** baseado no modelo relacional. O objetivo do modelo dimensional é facilitar a análise de dados e consultas analíticas, estruturando as informações em uma tabela **fato** e várias tabelas de **dimensões**.

#### Estrutura do Modelo Dimensional:

1. **Tabela Fato (`FatoLocacao`)**:
   - Representa os eventos de locação e contém métricas como `qtdDiaria` e `vlrDiaria`.
   
2. **Tabelas de Dimensão**:
   - **DimCliente**: Contém dados sobre os clientes.
   - **DimCarro**: Contém dados sobre os carros.
   - **DimCombustivel**: Contém dados sobre os tipos de combustível.
   - **DimVendedor**: Contém dados sobre os vendedores.

#### Script para o Modelo Dimensional:

O script [`Modelo Dimensional.sql`](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2002/Desafio/DESAFIO%20-%20Se%C3%A7%C3%A3o%208/Modelo%20Relacional.sql) inclui as instruções SQL para criar a tabela fato e as tabelas de dimensão, com relacionamentos estabelecidos para permitir análises de métricas por cliente, carro, tipo de combustível e vendedor.

![Modelo Dimensional_versão final.png](https://github.com/paulorenatojsb/CompassAcademy/blob/main/Sprint%2002/Desafio/DESAFIO%20-%20Se%C3%A7%C3%A3o%208/Modelo%20Dimensional_vers%C3%A3o%20final.png)

O diagrama `Modelo Dimensional_versão final.png` mostra o modelo dimensional em formato de estrela, com a tabela fato `FatoLocacao` no centro e as dimensões ao redor.

## Arquivos na Pasta Desafio

- `concessionaria.sqlite`: Banco de dados utilizado para realizar o desafio..
- `Desafio_normalização.sql`: Script SQL utilizado para a normalização da base de dados.
- `Modelo Relacional.sql`: Script SQL do modelo relacional.
- `Modelo Relacional_versão final.png`: Diagrama do modelo relacional.
- `Modelo Dimensional.sql`: Script SQL do modelo dimensional.
- `Modelo Dimensional_versão final.png`: Diagrama do modelo dimensional.

## Conclusão

Com este desafio pude aplicar e reforçar conceitos fundamentais de SQL (normalização e modelagem dimensional), que são essenciais para o design de bases de dados otimizadas - tanto para operações transacionais quanto para análises. O processo envolveu dividir a tabela original, remover redundâncias e estruturar os dados de maneira que facilite a consulta e análise no futuro.
