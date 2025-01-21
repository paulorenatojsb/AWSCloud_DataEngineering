# README DESAFIO SPRINT 7 - Desafio de Filmes e Séries – Etapa 2

Este repositório contém o código-fonte e documentação referente à **Etapa 2** do Desafio de Filmes e Séries: **Ingestão de dados do TMDB** e gravação na RAW Zone do Data Lake (S3).

---

## 1. Visão Geral

O objetivo desta etapa é **coletar dados adicionais** de filmes e séries a partir da API do TMDB, com foco nos gêneros de Crime e Guerra, e **armazenar esses dados** em formato JSON no **Amazon S3**, na camada **RAW**, seguindo as boas práticas de organização de arquivos e chunking (máximo de 100 registros por arquivo).

**Principais atividades** realizadas:

1. **Configuração** de um script Python para consumir a API do TMDB.  
2. **Coleta de Filmes** e **Séries** por gênero (Crime, War/War & Politics).  
3. **Enriquecimento** opcional com IMDb ID (endpoint `/external_ids`).  
4. **Upload** para a AWS, rodando como função **Lambda** (ou local, usando `boto3`), seguindo o padrão:
s3://data-lake-paulorenato/Raw/TMDB/JSON//<Filmes ou Series>/<YYYY>/<MM>/<DD>/<arquivo.json>
5. **Documentação** do processo.

---

## 2. Detalhes Técnicos

### 2.1. Estrutura de Código

- **`lambda_function.py`**: principal arquivo que contém a função `lambda_handler(event, context)` (handler da AWS Lambda).  
- Faz chamadas aos endpoints `/discover/movie`, `/discover/tv` (TMDB) para coletar dados de **Crime** e **Guerra** (War).  
- Utiliza funções auxiliares para pegar IMDb ID (endpoint `/external_ids`).  
- Ao final, grava no **S3**, em blocos de até 100 registros.

### 2.2. Dependências

- **Python** 3.9 (ou compatível).
- **Bibliotecas**:
- `requests` para requisições HTTP à API TMDB.
- `boto3` para interação com o Amazon S3.
- **Credenciais**:
- **TMDB API Key** para autenticar as chamadas na API do TMDB.
- **Credenciais AWS** (IAM Role, Access Key + Secret Key, etc.) para acesso ao S3.

### 2.3. Principais Endpoints do TMDB

- **Filmes**: `/discover/movie?with_genres=80,10752` (Crime, War)  
- **Séries**: `/discover/tv?with_genres=80,10768` (Crime, War & Politics)  
- **IMDb ID** (opcional):  
- `/movie/{movie_id}/external_ids`  
- `/tv/{tv_id}/external_ids`

---

## 3. Passo a Passo Realizado

1. **Preparação do Ambiente**  
- Configuração local ou criação de função Lambda na AWS.  
- Instalação das libs: `pip install requests boto3`.  
- Definição de variáveis de ambiente ou hardcode temporário para `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `API_KEY` do TMDB (teste/desenvolvimento).

2. **Coleta e Ingestão**  
1. **Descoberta de Filmes** (`discover_movies`):  
   - Iteração sobre páginas de 1 até `MAX_PAGES_MOVIES`.  
   - Para cada filme, opcionalmente obter `imdb_id` via `/movie/{id}/external_ids`.  
2. **Descoberta de Séries** (`discover_tv`):  
   - Iteração sobre páginas de 1 até `MAX_PAGES_TV`.  
   - Para cada série, opcionalmente obter `imdb_id` via `/tv/{id}/external_ids`.  
3. **Armazenamento** em listas (`all_movies`, `all_tv`).  
4. **Chunking** (100 registros por arquivo) e **upload** para S3:
   ```
   s3://data-lake-paulorenato/Raw/TMDB/JSON/Filmes/<YYYY>/<MM>/<DD>/*.json
   s3://data-lake-paulorenato/Raw/TMDB/JSON/Series/<YYYY>/<MM>/<DD>/*.json
   ```

3. **Execução na AWS Lambda**  
- A função `lambda_handler(event, context)` orquestra todo o processo.  
- Aumento do **Timeout** (para 15 ou 30 segundos) na Lambda, evitando erros de time-out.  
- Verificação dos **logs** no CloudWatch e dos arquivos no S3.

4. **Validação e Evidências**  

Script `tmdb_ingest.py` criado
![Evidencia 1](../Evidências/Desafio%20S7%20-%20evidencias%20(3).png)

Execução Local do Script
![Evidencia 2](../Evidências/Desafio%20S7%20-%20evidencias%20(1).png)

Arquivos Processados e Incluidos no Bucket S3
![Evidencia 3](../Evidências/Desafio%20S7%20-%20evidencias%20(2).png)

Código "deployado" no AWS Lambda
![Evidencia 4](../Evidências/Desafio%20S7%20-%20evidencias%20(4).png)

Função criada no AWS Lambda
![Evidencia 5](../Evidências/Desafio%20S7%20-%20evidencias%20(5).png)

Função Lambda executada com sucesso
![Evidencia 6](../Evidências/Desafio%20S7%20-%20evidencias%20(6).png)

---

## 4. Perguntas a Responder na Próxima Fase

### Análise Descritiva
1. Quais são os atores e diretores mais frequentes em filmes de Crime e Guerra?
2. Qual é a duração média dos filmes de Crime e Guerra em comparação com outros gêneros?

### Análise Preditiva
1. Com base nos dados históricos, qual será a tendência de produção de filmes de Crime e Guerra nos próximos 5 anos?
2. Como a duração do filme pode influenciar seu sucesso (medido pelo numeroVotos) em filmes de Crime e Guerra?

### Análise Diagnóstica
1. Como a escolha do elenco afeta o desempenho de filmes de Crime e Guerra?
2. Qual é o impacto do tempo de duração (tempoMinutos) na notaMedia de filmes de Crime e Guerra?

Essas questões servirão como base para a fase de análise e tratamento dos dados.

---

## 5. Conclusão e Próximos Passos

- Esta **Entrega 2** finaliza a ingestão bruta de dados de Filmes e Séries diretamente da API do TMDB, armazenando em **formato JSON** na camada **Raw** do Data Lake.  
- Os próximos passos incluem o **tratamento** (limpeza, padronização) e a **análise** (responder às perguntas com as fontes combinadas).