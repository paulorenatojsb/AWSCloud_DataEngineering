#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

# ------------------------------------------------------------------
# 1) Recebe parâmetros do job
#    O valor 'glue_job_csv' deve ser definido no Glue Console
#    quando criar o job (Job name).
# ------------------------------------------------------------------
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_paths = [
    "s3://data-lake-paulorenato/Raw/Local/CSV/Movies/2025/01/07/movies.csv",
    "s3://data-lake-paulorenato/Raw/Local/CSV/Series/2025/01/07/series.csv"
]

output_path = "s3://data-lake-paulorenato/trusted/"

# ------------------------------------------------------------------
# 3) Leitura dos arquivos CSV da Raw
# ------------------------------------------------------------------
df_csv = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(raw)

# Exemplo de exibição do Schema
df_csv.printSchema()

# Exibe algumas linhas
df_csv.show(5)

# ------------------------------------------------------------------
# 4) Escrita em formato Parquet, modo overwrite
# ------------------------------------------------------------------
df_csv.write \
    .mode("overwrite") \
    .parquet(trusted)

# Encerra o job
job.commit()