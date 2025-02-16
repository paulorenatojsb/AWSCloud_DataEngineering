import sys
from pyspark.context import SparkContext
from pyspark.sql.functions import col, lit, split, explode, trim
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job

# Captura dos argumentos do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializa os contextos Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura dos dados da camada Trusted
trusted_input_path = "s3://data-lake-paulorenato/trusted/"
df_trusted = spark.read.parquet(trusted_input_path)

# Exibe as colunas lidas para debug
print("Colunas iniciais:", df_trusted.columns)

# Identifica se o DataFrame possui a coluna única com os dados concatenados (coluna cujo nome contém o delimitador '|')
data_col = None
for col_name in df_trusted.columns:
    if "|" in col_name:
        data_col = col_name
        break

if data_col is not None:
    df_trusted = df_trusted.withColumn("split_cols", split(col(data_col), "\\|"))
    df_trusted = df_trusted.select(
         col("split_cols").getItem(0).alias("id"),
         col("split_cols").getItem(1).alias("tituloPincipal"),
         col("split_cols").getItem(2).alias("tituloOriginal"),
         col("split_cols").getItem(3).alias("anoLancamento"),
         col("split_cols").getItem(4).alias("tempoMinutos"),
         col("split_cols").getItem(5).alias("genero"),
         col("split_cols").getItem(6).alias("notaMedia"),
         col("split_cols").getItem(7).alias("numeroVotos"),
         col("split_cols").getItem(8).alias("generoArtista"),
         col("split_cols").getItem(9).alias("personagem"),
         col("split_cols").getItem(10).alias("nomeArtista"),
         col("split_cols").getItem(11).alias("anoNascimento"),
         col("split_cols").getItem(12).alias("anoFalecimento"),
         col("split_cols").getItem(13).alias("profissao"),
         col("split_cols").getItem(14).alias("titulosMaisConhecidos")
    )
else:
    print("Não foi encontrada uma coluna com delimitador '|'. Verifique o schema dos dados.")

# Exibe o schema após a separação para confirmar
df_trusted.printSchema()

# Transformações para a camada Refined
# DimTempo: utilizando "anoLancamento"
df_dimtempo = df_trusted.select(col("anoLancamento").alias("ano")).distinct() \
    .withColumn("tempo_id", col("ano")) \
    .withColumn("mes", lit(1)) \
    .withColumn("dia", lit(1))

# DimMidia: informações dos títulos (filmes/séries)
df_dimmidia = df_trusted.select(
    col("id").alias("id_original"),
    col("tituloPincipal").alias("tituloPrincipal"),
    col("tituloOriginal"),
    col("tempoMinutos"),
    lit("Movie/Series").alias("tipoMidia")
).withColumn("midia_id", col("id_original").cast("bigint"))

# FatoMidia: métricas e chaves associadas
df_fatomidia = df_trusted.select(
    col("id").alias("id_original"),
    col("notaMedia").cast("double"),
    col("numeroVotos").cast("long"),
    col("anoLancamento")
).join(df_dimmidia.select("midia_id", "id_original"), on="id_original", how="left") \
 .join(df_dimtempo.select(col("tempo_id"), col("ano").alias("ano_dim")), df_trusted["anoLancamento"] == col("ano_dim"), "left") \
 .drop("ano_dim")

# DimArtista: informações dos artistas
df_dimartista = df_trusted.select(
    col("nomeArtista"),
    col("generoArtista"),
    col("anoNascimento"),
    col("anoFalecimento"),
    col("profissao"),
    col("titulosMaisConhecidos")
).distinct().withColumn("artista_id", col("nomeArtista"))

# BridgeMidiaArtista: ligação entre Midia e Artista, com "personagem"
df_bridgemidiaartista = df_trusted.select(
    col("id").alias("id_original"),
    col("nomeArtista"),
    col("personagem")
).join(df_dimmidia.select("midia_id", "id_original"), on="id_original", how="left") \
 .join(df_dimartista.select("artista_id", "nomeArtista"), on="nomeArtista", how="left")

# DimGenero e BridgeMidiaGenero: tratando o campo "genero"
df_genero_exploded = df_trusted.select(
    col("id").alias("id_original"),
    explode(split(col("genero"), ",")).alias("genero_item")
).withColumn("genero_item", trim(col("genero_item")))

df_dimgenero = df_genero_exploded.select(
    col("genero_item").alias("descricaoGenero")
).distinct().withColumn("genero_id", col("descricaoGenero"))

df_bridgemediagenero = df_genero_exploded.join(
    df_dimmidia.select("midia_id", "id_original"),
    on="id_original",
    how="left"
).join(
    df_dimgenero,
    df_genero_exploded["genero_item"] == df_dimgenero["descricaoGenero"],
    "left"
)

# Escrita dos dados transformados na camada Refined (em Parquet)
refined_output_path = "s3://data-lake-paulorenato/refined/"

# Escreve a tabela FatoMidia particionada por anoLancamento
df_fatomidia.write.mode("overwrite") \
    .partitionBy("anoLancamento") \
    .parquet(refined_output_path + "FatoMidia")

# Escreve as demais dimensões e tabelas de ponte
df_dimmidia.write.mode("overwrite") \
    .parquet(refined_output_path + "DimMidia")

df_dimtempo.write.mode("overwrite") \
    .parquet(refined_output_path + "DimTempo")

df_dimartista.write.mode("overwrite") \
    .parquet(refined_output_path + "DimArtista")

df_dimgenero.write.mode("overwrite") \
    .parquet(refined_output_path + "DimGenero")

df_bridgemediagenero.write.mode("overwrite") \
    .parquet(refined_output_path + "BridgeMidiaGenero")

df_bridgemidiaartista.write.mode("overwrite") \
    .parquet(refined_output_path + "BridgeMidiaArtista")

# Encerra a execução do JOB
job.commit()