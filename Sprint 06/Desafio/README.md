# Desafio de Filmes e Séries - Data Lake

## 1. Objetivo

O objetivo deste desafio é praticar a combinação de conhecimentos adquiridos no Programa, aplicando diferentes conceitos e tecnologias para resolver um problema completo. Minha tarefa é construir um Data Lake, passando por todas as etapas de ingestão, armazenamento, processamento e consumo de dados.

## 2. Entregáveis

- **Código-fonte**: Todo o código, comentários, evidências e demais artefatos desenvolvidos para resolver o desafio estarão comitados no Git, de forma organizada.
  
- **Código Python**: O código desenvolvido estará comentado, explicando a lógica implementada, especialmente em relação ao processo de ingestão de dados.

- **DockerFile**: Incluirá as instruções necessárias para a criação do ambiente Docker.

- **Arquivos Python (.py)**: O código Python estará pronto para ser executado, com os módulos necessários para a execução do desafio.

## 3. Preparação

- Realizei o download do arquivo **Filmes e Series.zip**, necessário para a ingestão dos dados.

## 4. Desafio

Este desafio está dividido em cinco entregas, sendo a **Entrega 1** a primeira etapa do processo completo de construção de um Data Lake para Filmes e Séries. A proposta é trabalhar com dados provenientes de arquivos CSV e da API do TMDB, utilizando boas práticas de armazenamento e processamento.

### Descrição Geral do Desafio

O desafio consiste na construção de um **Data Lake** dividido em várias camadas, com as etapas de ingestão, armazenamento, processamento e consumo de dados. A primeira camada do Data Lake será populada com dados provenientes de arquivos CSV, enquanto a segunda camada será processada e catalogada. Na terceira camada, os dados serão consumidos para análise e visualização.

As etapas principais são:

1. **Ingestão de dados**: Carregar os dados em formato CSV e dados de APIs do TMDB para o Data Lake.
  
2. **Processamento de dados**: Padronizar o formato de armazenamento e catalogar os dados em tabelas.
  
3. **Criação do modelo dimensional**: Definir o modelo de dados dimensional para análise e processamento com Apache Spark.
  
4. **Consumo de dados**: Criar dashboards analíticos para responder às perguntas de análise definidas.

### Questões para Análise e Criação de Dashboard

O tema para o desafio final da minha Squad ficou definido como **Filmes e Séries de Crime/Guerra**, e após análise exploratória, minhas perguntas são questão serão:

### Análise Descritiva
1. Quais são os atores e diretores mais frequentes em filmes de Crime e Guerra?
2. Qual é a duração média dos filmes de Crime e Guerra em comparação com outros gêneros?

### Análise Preditiva
1. Com base nos dados históricos, qual será a tendência de produção de filmes de Crime e Guerra nos próximos 5 anos?
2. Como a duração do filme pode influenciar seu sucesso (medido pelo numeroVotos) em filmes de Crime e Guerra?

### Análise Diagnóstica
1. Como a escolha do elenco afeta o desempenho de filmes de Crime e Guerra?
1. Qual é o impacto do tempo de duração (tempoMinutos) na notaMedia de filmes de Crime e Guerra?

## 4.1. Entrega 1

### Objetivo

Nesta etapa, a ingestão de dados foi feita utilizando um processo **Batch**, onde os arquivos CSV foram carregados para a AWS S3, mais especificamente para a zona **RAW** do Data Lake.

### Tarefas

1. **Desenvolver o código Python**:
   - Utilizar a biblioteca `boto3` para carregar os dados para a AWS S3.

2. **Estrutura de Armazenamento no S3**:
   - A estrutura de gravação no S3 seguiu o padrão:
     ```
     <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento>\<arquivo>
     ```
   - Exemplo:
     ```
     s3://data-lake-paulorenato/raw/local/csv/movies/2022/05/02/movies.csv
     s3://data-lake-paulorenato/raw/local/csv/series/2022/05/02/series.csv
     ```

3. **Criar um container Docker**:
   - O código Python foi executado dentro de um container Docker.
   - Criei um volume para armazenar os arquivos CSV localmente e vincular esse volume ao Docker para execução do processo.

4. **Execução local do Docker**:
   - Executei o container Docker localmente para realizar a carga dos dados no bucket S3.

A entrega da etapa 1 consistiu na implementação do código Python, a configuração do Docker para o ambiente de execução e a realização da ingestão dos dados para o S3.