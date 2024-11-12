# Sprint de SQL e Certificação AWS - Sales Accreditation

## Objetivo da Sprint

Esta sprint teve como foco o aprimoramento das habilidades em SQL, passando por conceitos básicos e avançados, com o uso de bancos de dados fornecidos para prática e aplicação dos comandos aprendidos. Além disso, foi realizada a primeira unidade da certificação **AWS - Sales Accreditation**, com o objetivo de desenvolver uma base sólida de conhecimentos em soluções e serviços AWS.

## Conteúdo da Sprint

### 1. Conceitos de SQL

Durante esta sprint, exploramos uma ampla gama de tópicos em SQL, tanto para operações básicas quanto avançadas. As práticas incluíram o uso de várias consultas e manipulações em bancos de dados relacionais, cobrindo aspectos de modelagem relacional e dimensional.

#### Conteúdos Principais Abordados

- **Consultas Básicas**: Recuperação de dados, filtros com `WHERE`, ordenação com `ORDER BY`, e limites com `LIMIT`.
- **Funções de Agregação**: Uso de funções como `SUM`, `AVG`, `COUNT`, `MAX`, e `MIN` para resumir e analisar dados.
- **Joins**: Trabalhamos com `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` e `FULL JOIN` para combinar dados de diferentes tabelas e entender suas interações.
- **Subconsultas**: Realizamos subconsultas para consultas mais complexas, tanto em cláusulas `SELECT` quanto `WHERE`.
- **Agrupamento e Ordenação**: Utilizamos `GROUP BY` e `HAVING` para organizar dados em grupos e aplicar filtros adicionais.
- **Modelagem Relacional**: Aprendemos a criar um modelo relacional normalizado, eliminando redundâncias e garantindo integridade referencial.
- **Modelagem Dimensional**: Criamos um modelo dimensional, estruturado no formato de **esquema estrela** (Star Schema), com foco em análise de dados.

A pratica dos conceitos acima foi realizada nos exercícios da propria trilha, e estão disponíveis em: [Exercícios](https://github.com/paulorenatojsb/CompassAcademy/tree/main/Sprint%2002/Exerc%C3%ADcios)

### 2. Bancos de Dados Utilizados

Os exercícios foram realizados em dois bancos de dados fornecidos durante a sprint:

1. **Banco de Dados Biblioteca**: Utilizado para consultas e análises de dados relacionados a autores, livros, editoras e seus relacionamentos. Exploramos queries para listar livros, identificar editoras com maior número de publicações e calcular métricas sobre vendas. [Pasta dos Exercícios - Seção 3](https://github.com/paulorenatojsb/CompassAcademy/tree/main/Sprint%2002/Desafio/Exerc%C3%ADcio%20(Desafio)%20-%20Se%C3%A7%C3%A3o%203) e [Pasta dos Exercícios - Seção 6](https://github.com/paulorenatojsb/CompassAcademy/tree/main/Sprint%2002/Desafio/Exerc%C3%ADcio%20(Desafio)%20-%20Se%C3%A7%C3%A3o%206)

2. **Banco de Dados Loja**: Contém informações sobre vendas, produtos, vendedores e estoque. Este banco foi utilizado para consultas específicas envolvendo operações de vendas, como identificação dos produtos menos vendidos por canal de vendas, cálculo de comissões de vendedores, e análise de desempenho de produtos em diferentes localidades. [Pasta dos Exercícios - Seção 4](https://github.com/paulorenatojsb/CompassAcademy/tree/main/Sprint%2002/Desafio/Exerc%C3%ADcio%20(Desafio)%20-%20Se%C3%A7%C3%A3o%204)

3. **Banco de Dados Concessionaria**: Com dados sobre locações de veículos, clientes, carros, combustíveis e vendedores, esse banco de dados foi usado para exercícios de modelagem relacional e dimensional, além de consultas avançadas para calcular comissões, listar produtos menos vendidos e calcular o gasto médio por estado. [Pasta do Desafio](https://github.com/paulorenatojsb/CompassAcademy/tree/main/Sprint%2002/Desafio/DESAFIO%20-%20Se%C3%A7%C3%A3o%208)

### 3. Modelagem de Dados Relacional e Dimensional

**Modelo Relacional**
A partir dos dados do banco de dados Concessionaria, realizamos a normalização para criar um modelo relacional. 

**Modelo Dimensional**

Com base no modelo relacional, construímos um modelo dimensional para facilitar análises de dados. Esse modelo foi estruturado em um **Star Schema**.

### 4. Primeira Unidade da Certificação AWS - Sales Accreditation

Além dos estudos em SQL, foi concluída a primeira unidade da certificação **AWS - Sales Accreditation**, voltada para o entendimento das soluções e serviços da AWS. Esse módulo cobriu os seguintes tópicos:

- **Conceitos Básicos da AWS**: Visão geral dos serviços oferecidos pela AWS e como eles atendem a diferentes necessidades dos clientes.
- **Soluções AWS para Empresas**: Conhecimento sobre como a AWS ajuda a resolver desafios comuns em diferentes setores.
- **Segurança e Confiabilidade**: Entendimento das práticas de segurança da AWS e dos benefícios para clientes que utilizam a nuvem.

![Badge]

## Estrutura do Repositório

O repositório foi organizado para facilitar o acesso aos scripts SQL, diagramas e documentação da sprint.


Aqui está um modelo de README.md completo para documentar sua sprint:

markdown
Copiar código
# Sprint de SQL e Certificação AWS - Sales Accreditation

## Objetivo da Sprint

Esta sprint teve como foco o aprimoramento das habilidades em SQL, passando por conceitos básicos e avançados, com o uso de bancos de dados fornecidos para prática e aplicação dos comandos aprendidos. Além disso, foi realizada a primeira unidade da certificação **AWS - Sales Accreditation**, com o objetivo de desenvolver uma base sólida de conhecimentos em soluções e serviços AWS.

## Conteúdo da Sprint

### 1. Conceitos de SQL

Durante esta sprint, exploramos uma ampla gama de tópicos em SQL, tanto para operações básicas quanto avançadas. As práticas incluíram o uso de várias consultas e manipulações em bancos de dados relacionais, cobrindo aspectos de modelagem relacional e dimensional.

#### Conteúdos Principais Abordados

- **Consultas Básicas**: Recuperação de dados, filtros com `WHERE`, ordenação com `ORDER BY`, e limites com `LIMIT`.
- **Funções de Agregação**: Uso de funções como `SUM`, `AVG`, `COUNT`, `MAX`, e `MIN` para resumir e analisar dados.
- **Joins**: Trabalhamos com `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` e `FULL JOIN` para combinar dados de diferentes tabelas e entender suas interações.
- **Subconsultas**: Realizamos subconsultas para consultas mais complexas, tanto em cláusulas `SELECT` quanto `WHERE`.
- **Agrupamento e Ordenação**: Utilizamos `GROUP BY` e `HAVING` para organizar dados em grupos e aplicar filtros adicionais.
- **Modelagem Relacional**: Aprendemos a criar um modelo relacional normalizado, eliminando redundâncias e garantindo integridade referencial.
- **Modelagem Dimensional**: Criamos um modelo dimensional, estruturado no formato de **esquema estrela** (Star Schema), com foco em análise de dados.

### 2. Bancos de Dados Utilizados

Os exercícios foram realizados em dois bancos de dados fornecidos durante a sprint:

1. **Banco de Dados Biblioteca**: Utilizado para consultas e análises de dados relacionados a autores, livros, editoras e seus relacionamentos. Exploramos queries para listar livros, identificar editoras com maior número de publicações e calcular métricas sobre vendas.

2. **Banco de Dados Concessionaria**: Com dados sobre locações de veículos, clientes, carros, combustíveis e vendedores, esse banco de dados foi usado para exercícios de modelagem relacional e dimensional, além de consultas avançadas para calcular comissões, listar produtos menos vendidos e calcular o gasto médio por estado.

### 3. Modelagem de Dados Relacional e Dimensional

#### Modelo Relacional

A partir dos dados do banco de dados Concessionaria, realizamos a normalização para criar um modelo relacional. Esse processo resultou em várias tabelas independentes:

- **Cliente**: Tabela com dados dos clientes.
- **Carro**: Informações sobre os carros disponíveis para locação.
- **Combustivel**: Tipos de combustível.
- **Vendedor**: Dados dos vendedores.
- **Locacao**: Registros de locações, conectando clientes, carros, combustível e vendedores.

#### Modelo Dimensional

Com base no modelo relacional, construímos um modelo dimensional para facilitar análises de dados. Esse modelo foi estruturado em um **esquema estrela**:

- **Tabela Fato (`FatoLocacao`)**: Armazena eventos de locação e métricas como `qtdDiaria` e `vlrDiaria`.
- **Tabelas de Dimensão**:
  - **DimCliente**: Informações sobre clientes.
  - **DimCarro**: Detalhes sobre os carros.
  - **DimCombustivel**: Tipos de combustível.
  - **DimVendedor**: Dados sobre os vendedores.

### 4. Exercícios de Consultas Avançadas

Durante a sprint, foram realizados exercícios de consultas avançadas para consolidar o conhecimento:

- **Listar Livros Mais Caros**: Extraímos os 10 livros mais caros, ordenados por valor.
- **Top Editoras**: Consultamos as editoras com o maior número de livros na biblioteca.
- **Produtos Menos Vendidos**: Listamos os 10 produtos menos vendidos por canais específicos (E-commerce e Matriz).
- **Gasto Médio por Estado**: Calculamos o gasto médio de clientes por estado.
- **Consultas de Comissões**: Calculamos a comissão dos vendedores com base no valor das vendas realizadas.

### 5. Primeira Unidade da Certificação AWS - Sales Accreditation

Além dos estudos em SQL, foi concluída a primeira unidade da certificação **AWS - Sales Accreditation**, voltada para o entendimento das soluções e serviços da AWS. Esse módulo cobriu os seguintes tópicos:

- **Conceitos Básicos da AWS**: Visão geral dos serviços oferecidos pela AWS e como eles atendem a diferentes necessidades dos clientes.
- **Soluções AWS para Empresas**: Conhecimento sobre como a AWS ajuda a resolver desafios comuns em diferentes setores.
- **Segurança e Confiabilidade**: Entendimento das práticas de segurança da AWS e dos benefícios para clientes que utilizam a nuvem.

## Estrutura do Repositório

O repositório foi organizado para facilitar o acesso aos scripts SQL, diagramas e documentação da sprint.

Sprint_SQL_AWS/
├── Relacional/
│   ├── modelo_relacional.sql         # Script SQL para criação do modelo relacional
│   └── modelo_relacional.png         # Diagrama visual do modelo relacional
│
├── Dimensional/
│   ├── modelo_dimensional.sql        # Script SQL para criação do modelo dimensional
│   └── modelo_dimensional.png        # Diagrama visual do modelo dimensional
│
├── Consultas_SQL/
│   ├── consultas_basicas.sql         # Script com consultas SQL básicas
│   ├── consultas_avancadas.sql       # Script com consultas SQL avançadas
│   └── consultas_analiticas.sql      # Script com consultas analíticas e de agregação
│
└── AWS_Certificacao/
    └── Sales_Accreditation.md        # Anotações sobre a primeira unidade da certificação AWS - Sales Accreditation

## Passos Realizados na Sprint

1. **Exploração e Normalização do Banco de Dados Concessionaria**:
   - Analisamos a tabela `tb_locacao` original, aplicando normalização para criar o modelo relacional.
   - Definimos chaves primárias e estrangeiras para garantir integridade referencial.
   - Geramos o diagrama `modelo_relacional.png` para visualizar as relações.

2. **Construção do Modelo Dimensional**:
   - Criamos o esquema estrela com `FatoLocacao` e as dimensões (`DimCliente`, `DimCarro`, `DimCombustivel`, `DimVendedor`).
   - Documentamos o modelo no diagrama `modelo_dimensional.png`.

3. **Consultas SQL**:
   - Desenvolvemos e testamos consultas SQL para responder a perguntas específicas e extrair insights dos dados.
   - Exportamos resultados de algumas consultas para CSV conforme as especificações fornecidas.

4. **Certificação AWS - Sales Accreditation**:
   - Concluímos a primeira unidade, compreendendo a oferta de soluções AWS para empresas e a importância da segurança em nuvem.

## Conclusão

Esta sprint proporcionou uma prática completa dos fundamentos e técnicas avançadas de SQL, cobrindo desde a modelagem de dados até consultas analíticas. Também foi dado um primeiro passo na certificação AWS, reforçando a compreensão sobre as soluções em nuvem e seu valor para clientes. Esses conhecimentos são essenciais tanto para gestão de dados quanto para entender a aplicação de tecnologias de nuvem em diferentes contextos.

Este repositório serve como uma referência completa, documentando todas as etapas e resultados da sprint.
