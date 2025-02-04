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

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_paths = [
    "s3://data-lake-paulorenato/Raw/TMDB/JSON/Filmes/2025/01/21/movies_crime_war_part1.json",
    "s3://data-lake-paulorenato/Raw/TMDB/JSON/Filmes/2025/01/21/movies_crime_war_part2.json",
    "s3://data-lake-paulorenato/Raw/TMDB/JSON/Series/2025/01/21/tv_crime_war_part1.json"
]

output_path = "s3://data-lake-paulorenato/trusted/"

# Lendo todos os arquivos em um único DataFrame
df_json = spark.read \
    .option("multiline", "true") \
    .json(input_paths)

df_json.printSchema()
df_json.show(5)

ingestion_date = datetime.now()
df_json = df_json \
    .withColumn("year_ingest", F.lit(ingestion_date.year)) \
    .withColumn("month_ingest", F.lit(ingestion_date.month)) \
    .withColumn("day_ingest", F.lit(ingestion_date.day))

df_json.write \
    .partitionBy("year_ingest", "month_ingest", "day_ingest") \
    .mode("append") \
    .parquet(output_path)

job.commit()