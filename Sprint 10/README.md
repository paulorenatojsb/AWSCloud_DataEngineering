# README SPRINT 10 - Desafio Etapa 5 - Dashboard no AWS QuickSight

## 1. Visão Geral

Este projeto é a última etapa do desafio para construção de um Data Lake para Filmes e Séries, onde o foco final é o consumo dos dados para extrair insights e apresentar análises através de um dashboard no AWS QuickSight. O objetivo desta entrega é utilizar como fonte de dados as tabelas da camada **Refined** do data lake – acessíveis via AWS Athena – para construir visualizações que respondam a questões estratégicas sobre a produção e desempenho dos filmes.

## 2. Objetivo do Desafio

O desafio está dividido em 5 entregas, e nesta entrega final, o foco foi:

- **Consumo dos Dados:**  
  Após as etapas de ingestão, armazenamento e processamento dos dados (usando arquivos CSV e dados da API do TMDB), a última fase foi extrair insights e construir um dashboard analítico.

- **Dashboard no AWS QuickSight:**  
  Criar um dashboard no QuickSight utilizando exclusivamente as tabelas da camada Refined. O datasource deve ser configurado via AWS Athena.

## 3. Arquitetura do Data Lake

O Data Lake deste desafio segue as seguintes camadas:
- **Raw:** Armazenamento dos arquivos originais (CSV e JSON da API do TMDB).
- **Trusted:** Dados processados e validados.
- **Refined:** Tabelas refinadas com modelo dimensional, organizadas para consumo analítico.

### Tabelas Refinadas Utilizadas

Neste projeto, utilizamos 4 tabelas refinadas:
- **DimGenero:**  
  - `genero_id` (string)
- **DimMidia:**  
  - `midia_id` (bigint)  
  - `titulo` (string)  
  - `original_language` (string)
- **DimTempo:**  
  - `data_lancamento` (date)  
  - `ano` (int)  
  - `mes` (int)  
  - `dia` (int)  
  - `tempo_id` (int)
- **FatoMidia:**  
  - `midia_id` (bigint)  
  - `titulo` (string)  
  - `data_lancamento` (string)  
  - `popularity` (double)  
  - `genre_ids` (array<bigint>)  
  - `imdb_id` (string)  
  - `original_language` (string)  
  - `data` (date)

> **Nota:** As tabelas foram geradas a partir de um pipeline em Apache Spark no AWS Glue que ingeriu, processou e transformou os dados dos arquivos brutos e Trusted para a camada Refined.

## 4. Perguntas e Análises para o Dashboard

O dashboard respondeu as seguintes seis questões, focando apenas nos filmes dos gêneros **Crime** e **Guerra** (utilizando os IDs 80 e 10752 do TMDB):

1. **Tendência de Produção ao Longo dos Anos:**  
   - *Objetivo:* Verificar a evolução do número de lançamentos por ano.

2. **Popularidade Média dos Filmes:**  
   - *Objetivo:* Comparar a popularidade média dos filmes de Crime e Guerra por ano.

3. **Distribuição dos Idiomas Originais:**  
   - *Objetivo:* Analisar os idiomas predominantes dos filmes.

4. **Distribuição da Popularidade por Categoria (Box Plot):**  
   - *Objetivo:* Visualizar a dispersão dos valores de popularidade para os filmes.

5. **Ranking dos Filmes Mais Populares:**  
   - *Objetivo:* Exibir os top 10 filmes com maior popularidade dentro dos gêneros Crime e Guerra.

6. **Sazonalidade dos Lançamentos (Por Mês):**  
   - *Objetivo:* Analisar a distribuição dos lançamentos ao longo dos meses para identificar padrões sazonais.

## 5. Criação do Dataset e Configuração do QuickSight

### Conexão com Athena
- Configurei o datasource do QuickSight para utilizar o AWS Athena, apontando para o database que contém as tabelas **Refined**.
- Usei as tabelas Refined como fonte única de dados para o dashboard.

### Criação de Campos Calculados (Exemplos)
- **Agrupamento por Década:**  
  Criei um campo calculado para agrupar os filmes por década, usando o campo `{tempo_ano}` da dimensão de tempo.
- **Agrupamento de Meses (Nome dos Meses):**  
  Criei um campo calculado para transformar os números (1 a 12) nos nomes dos meses:
  ```sql
  ifelse(
    {mes} = 1, 'Janeiro',
    {mes} = 2, 'Fevereiro',
    {mes} = 3, 'Março',
    {mes} = 4, 'Abril',
    {mes} = 5, 'Maio',
    {mes} = 6, 'Junho',
    {mes} = 7, 'Julho',
    {mes} = 8, 'Agosto',
    {mes} = 9, 'Setembro',
    {mes} = 10, 'Outubro',
    {mes} = 11, 'Novembro',
    {mes} = 12, 'Dezembro',
    'Outro'
  )
  ```
- **Filtragem de Gêneros Crime/Guerra:**  
  Criei um campo calculado para identificar se um filme pertence a Crime ou Guerra, por exemplo:
  ```sql
  ifelse(
    contains(toString({genre_ids}), '80') OR contains(toString({genre_ids}), '10752'),
    'Crime/Guerra',
    'Outros'
  )
  ```
  Apliquei esse filtro no visual para focar apenas nos filmes de Crime e Guerra.

## 6. Construção dos Visuais

- **Visual 1 – Tendência de Produção:**  
  Gráfico de linhas com o eixo X configurado com o campo `ano` (da DimTempo) e o eixo Y com a contagem de filmes (FatoMidia).
  
- **Visual 2 – Popularidade Média:**  
  Gráfico de linhas com o eixo X como `ano` e o eixo Y como a média do campo `popularity` (da FatoMidia).

- **Visual 3 – Distribuição dos Idiomas:**  
  Gráfico de nuvem de palavras com o campo `original_language` (usando um campo calculado para converter códigos para nomes) e a contagem de filmes.

- **Visual 4 – Distribuição da Popularidade (Box Plot):**  
  Box plot utilizando um campo calculado de agrupamento (por categoria) para exibir a dispersão do campo `popularity`.

- **Visual 5 – Ranking dos Filmes Mais Populares:**  
  Gráfico de barras horizontal ou tabela ordenada para exibir os 10 filmes com maior `popularity`.

- **Visual 6 – Sazonalidade dos Lançamentos:**  
  Gráfico Pizza configurado com o `mes` (campo calculado com o nome do mês).

## 7. Considerações Finais

- **Narrativa dos Dados:**  
  O dashboard apresenta uma visão agregada e de alto nível dos filmes de Crime e Guerra, permitindo identificar tendências históricas, padrões sazonais e desempenho de filmes.
  
- **Flexibilidade e Interatividade:**  
  Apesar de a entrega ter sido realizada no formato PDF, no QuickSight pode-se utilizar os filtros interativos para permitir que os usuários explorem os dados (por exemplo, filtrar por década, mês ou idioma).

- **Data Source Único:**  
  Garanta que o QuickSight use as tabelas da camada Refined como única fonte de dados, e configure o Athena como o datasource para facilitar a consulta e atualização dos dados.

---

Este README.md descreve o objetivo do desafio, o que foi realizado em termos de ingestão, processamento e criação do modelo dimensional (Refined) e demonstra o processo de construçãod de um dashboard analítico no QuickSight para responder às seis questões definidas.
```