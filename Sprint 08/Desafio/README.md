# README DESAFIO SPRINT 8 - Desafio de Filmes e Séries – Etapa 3

# Desafio – Entrega 3 (Camada Trusted)

Este **README** descreve como realizar o processamento para criar a **Camada Trusted** de um Data Lake, utilizando **AWS Glue** e **Apache Spark**. Abaixo consta o detalhamento sobre os **scripts**, as **etapas de processamento** e algumas **referências de código** para compreender como cada parte foi implementada.

---

- **`glue_job_csv.py`**: Processa arquivos CSV (dados batch) da camada Raw para a camada Trusted **sem partição**.  
![Evidencia 4](../Evidências/Sprint8%20-%20EvidenciaDesafio%20(2).png)

- **`glue_job_json.py`**: Processa arquivos JSON (dados oriundos da API TMDB) da camada Raw para a camada Trusted, **particionando por data de ingestão** (ano, mês, dia).
![Evidencia 1](../Evidências/Sprint8%20-%20EvidenciaDesafio%20(5).png)

---

## 2. Objetivo

Gerar dados **limpos e padronizados** (Trusted) em formato **Parquet** no S3, permitindo futura consulta via **Athena** ou outras ferramentas analíticas. Essa abordagem segue as boas práticas de Data Lake:

1. **Formato Parquet**: melhora a eficiência de armazenamento e leitura.  
2. **Particionamento**: para dados JSON da API TMDB, facilita a gestão e a performance de consultas (ano/mês/dia).  
3. **Jobs Spark** no **AWS Glue**: orquestração simplificada, sem necessidade de gerenciar servidores.

---

## 3. Preparação

1. **Dados na Raw Zone**:  
   - **CSV**: ex.: `s3://data-lake-paulorenato/Raw/Local/CSV/Movies/2025/01/07/movies.csv`  
   - **JSON**: ex.: `s3://data-lake-paulorenato/Raw/TMDB/JSON/Filmes/2025/01/21/movies_crime_war_part1.json`  

2. **Buckets S3 para Trusted**: `s3://data-lake-paulorenato/trusted/`  
![Evidencia 3](../Evidências/Sprint8%20-%20EvidenciaDesafio%20(4).png)

3. **AWS Glue**:  
   - **Worker type**: `G.1X`  
   - **Number of workers**: `2`  
   - **Job timeout**: `60` minutos (ou menor)

4. **Permissões IAM**:  
   - O **Glue Job** precisa de permissão de `GetObject` e `PutObject` nos buckets S3.  
   - Permissões para atualizar o **Glue Data Catalog** se necessário.

---

## 4. Script `glue_job_csv.py`

![Evidencia 1](../Evidências/Sprint8%20-%20EvidenciaDesafio%20(7).png)

### 4.1. Estrutura

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

# 1) Captura do argumento JOB_NAME
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 2) Caminhos S3 de entrada (Raw) e saída (Trusted)
input_paths = [
    "s3://data-lake-paulorenato/Raw/Local/CSV/Movies/2025/01/07/movies.csv",
    "s3://data-lake-paulorenato/Raw/Local/CSV/Series/2025/01/07/series.csv"
]
output_path = "s3://data-lake-paulorenato/trusted/"

# 3) Leitura do CSV
df_csv = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(input_path)

# 4) Escreve em Parquet (sem particionamento)
df_csv.write \
    .mode("append") \
    .parquet(output_path)

job.commit()
```

### 4.2. Detalhes Técnicos

- **`getResolvedOptions`**: Obtém parâmetros do Glue, incluindo `JOB_NAME`.  
- **`spark.read.csv(input_path)`**: Lê todos os arquivos CSV em `input_path`.  
  - Opções `header="true"` e `inferSchema="true"` podem ser ajustadas conforme o formato real.  
- **`df_csv.write.mode("append").parquet(output_path)`**: converte CSV para Parquet.  
  - `append` para acrescentar dados (sem sobrescrever).  
  - **Sem partição** neste caso, pois se trata de dados batch que não requerem data-based partitioning.

---

## 5. Script `glue_job_json.py`

![Evidencia 2](../Evidências/Sprint8%20-%20EvidenciaDesafio%20(6).png)

### 5.1. Estrutura

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
import pyspark.sql.functions as F

# 1) Inicializa Glue e Spark
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 2) Caminhos S3
input_paths = [
    "s3://data-lake-paulorenato/Raw/TMDB/JSON/Filmes/2025/01/21/movies_crime_war_part1.json",
    "s3://data-lake-paulorenato/Raw/TMDB/JSON/Filmes/2025/01/21/movies_crime_war_part2.json",
    "s3://data-lake-paulorenato/Raw/TMDB/JSON/Series/2025/01/21/tv_crime_war_part1.json"
]

output_path = "s3://data-lake-paulorenato/trusted/"

# 3) Leitura JSON (API TMDB)
df_json = spark.read \
    .option("multiline", "true") \
    .json(input_path)

df_json.printSchema()

# 4) Particionamento por data de ingestão
ingestion_date = datetime.now()
df_json = df_json \
    .withColumn("year_ingest", F.lit(ingestion_date.year)) \
    .withColumn("month_ingest", F.lit(ingestion_date.month)) \
    .withColumn("day_ingest", F.lit(ingestion_date.day))

# 5) Escreve em Parquet, particionado
df_json.write \
    .partitionBy("year_ingest", "month_ingest", "day_ingest") \
    .mode("append") \
    .parquet(output_path)

job.commit()
```

### 5.2. Detalhes Técnicos

- **Leitura de JSON**:
  - `option("multiline", "true")` se cada arquivo JSON tiver arrays ou estruturas complexas em múltiplas linhas.  
- **Colunas de Partição**:
  - `year_ingest`, `month_ingest`, `day_ingest` são criadas dinamicamente usando `datetime.now()`.  
- **`partitionBy`** e `mode("append")`:
  - **append** para incluir os dados acrescentando aos já existentes, sem sobresecrever.

---

## 6. Execução no AWS Glue

1. **Criar um Glue Job** (Spark script editor) para cada script.  
2. **Nome do job**: `glue_job_csv` ou `glue_job_json`.  
3. **Upload** do script: cole o conteúdo do `.py` no editor ou aponte para um local no S3.  
4. **Configurações**:
   - Worker type = `G.1X`  
   - Number of workers = `2`  
   - Job timeout = `60`  
   - IAM Role com acesso S3 (Read/Write)  
5. **Salvar** e **Run** o Job.  
6. Monitorar logs e, ao finalizar, verificar a pasta de saída no S3.

---

## 9. Conclusão

Com estes dois scripts (`glue_job_csv.py` e `glue_job_json.py`), foi possivel separar o processamento da camada Raw para a camada Trusted. O uso de **AWS Glue** simplifica a orquestração e a escalabilidade de jobs Spark. O **formato Parquet** e o **particionamento** otimizam consultas no **Athena** e reduzem custos de análise.