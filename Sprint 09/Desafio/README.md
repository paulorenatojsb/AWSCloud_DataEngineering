# README DESAFIO SPRINT 9 - Desafio de Filmes e Séries – Etapa 4 (Camada Refined)

Este repositório contém todas as instruções para a criação da camada Refined do Data Lake. Nessa camada, os dados já estão transformados e prontos para análise, seguindo um modelo dimensional (esquema estrela). Foram utilizadas ferramentas do AWS Glue para transformar os dados da camada Trusted e um crawler para atualizar o Glue Data Catalog, facilitando a consulta via AWS Athena e a visualização com AWS QuickSight.

---

## Introdução

Este projeto transforma os dados oriundos da camada Trusted (armazenados em arquivos Parquet no bucket S3) para a camada Refined, aplicando um modelo multidimensional (esquema estrela) que organiza as informações para análises e geração de insights. O fluxo de ETL inclui:

- **Leitura dos dados:** Os arquivos Parquet da camada Trusted são lidos, inclusive de subdiretórios.
- **Transformação dos dados:** Os dados são transformados para criar:
  - Tabelas dimensionais: DimMidia, DimTempo, DimArtista e DimGenero.
  - Tabelas de associação (bridge): BridgeMidiaGenero e BridgeMidiaArtista.
  - Tabela fato: FatoMidia, que centraliza as métricas (nota média, número de votos) e as chaves para as dimensões.
- **Escrita dos dados:** Os dados transformados são gravados na camada Refined, em formato Parquet, com particionamento (por exemplo, por ano de lançamento).
- **Atualização do Glue Data Catalog:** Um crawler é configurado para atualizar o catálogo de dados, permitindo consultas via Athena e visualização com QuickSight.

![S3.1](../Evidências/Evidencias%20-%20Sprint%209%20-%20Desafio%20(4).png)

![S3.2](../Evidências/Evidencias%20-%20Sprint%209%20-%20Desafio%20(5).png)

![S3.3](../Evidências/Evidencias%20-%20Sprint%209%20-%20Desafio%20(6).png)

---

## Modelagem de Dados

O modelo de dados adotado é baseado em um esquema estrela, composto por:

- **FatoMidia**: Tabela fato que armazena métricas (como `notaMedia` e `numeroVotos`) e chaves que referenciam as dimensões.
- **DimMidia**: Representa os títulos (filmes/séries) com informações como `tituloPrincipal`, `tituloOriginal`, `tempoMinutos` e `tipoMidia`.
- **DimTempo**: Dimensão temporal, extraída do campo `anoLancamento`.
- **DimArtista**: Armazena informações sobre os artistas (ex.: nome, gênero, datas de nascimento/falecimento, profissão, etc.).
- **DimGenero**: Lista os gêneros associados aos títulos.
- **BridgeMidiaGenero**: Tabela de associação entre Midia e Gênero.
- **BridgeMidiaArtista**: Tabela de associação entre Midia e Artista, incluindo o campo `personagem`.

### Diagrama - Modelo Dimensional

![Modelo Dimensional](../Desafio/Modelo%20Dimensional%20-%20Desafio%20-%20Sprint%209.png)

---

## Código do Job AWS Glue

O job AWS Glue foi desenvolvido em Python e utiliza o Apache Spark para ler os dados da camada Trusted, realizar as transformações necessárias e gravar os dados na camada Refined. Abaixo um exemplo do código:

```python
#!/usr/bin/env python
"""
Glue Job para criação da camada Refined a partir dos dados da camada Trusted,
ajustado para o caso em que os dados estejam em uma única coluna com delimitador '|'
e com colunas de partição (day_ingest, month_ingest, year_ingest).

Este job realiza:
  1. Leitura de múltiplos arquivos Parquet do bucket S3.
  2. Verificação se os dados foram lidos como uma única coluna (contendo o cabeçalho completo),
     e, se necessário, separa os campos utilizando o delimitador '|'.
  3. Transformação para criar as dimensões:
       - DimTempo, DimMidia, DimArtista, DimGenero;
     e as tabelas de associação:
       - BridgeMidiaGenero, BridgeMidiaArtista;
     bem como a tabela fato FatoMidia.
  4. Escrita dos dados transformados na camada Refined em formato Parquet, com particionamento.
"""

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

# ------------------------------------------------------------------
# 1. Leitura dos dados da camada Trusted (múltiplos arquivos Parquet)
# ------------------------------------------------------------------
trusted_input_path = "s3://data-lake-paulorenato/trusted/"
df_trusted = spark.read.parquet(trusted_input_path)

print("Colunas iniciais:", df_trusted.columns)

# Identifica se os dados estão em uma única coluna concatenada com delimitador '|'
data_col = None
for col_name in df_trusted.columns:
    if "|" in col_name:
        data_col = col_name
        break

if data_col is not None:
    # Se encontrado, divide os dados em várias colunas
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
    print("Não foi encontrada uma coluna com delimitador '|'.")

# Exibe o schema para confirmação
df_trusted.printSchema()

# ------------------------------------------------------------------
# 2. Transformações para a camada Refined
# ------------------------------------------------------------------

# 2.1 DimTempo: utiliza "anoLancamento" para criar a dimensão de tempo.
df_dimtempo = df_trusted.select(col("anoLancamento").alias("ano")).distinct() \
    .withColumn("tempo_id", col("ano")) \
    .withColumn("mes", lit(1)) \
    .withColumn("dia", lit(1))

# 2.2 DimMidia: extrai informações dos títulos (filmes/séries).
df_dimmidia = df_trusted.select(
    col("id").alias("id_original"),
    col("tituloPincipal").alias("tituloPrincipal"),
    col("tituloOriginal"),
    col("tempoMinutos"),
    lit("Movie/Series").alias("tipoMidia")
).withColumn("midia_id", col("id_original").cast("bigint"))

# 2.3 FatoMidia: centraliza métricas e relaciona as dimensões.
df_fatomidia = df_trusted.select(
    col("id").alias("id_original"),
    col("notaMedia").cast("double"),
    col("numeroVotos").cast("long"),
    col("anoLancamento")
).join(df_dimmidia.select("midia_id", "id_original"), on="id_original", how="left") \
 .join(df_dimtempo.select(col("tempo_id"), col("ano").alias("ano_dim")),
       df_trusted["anoLancamento"] == col("ano_dim"), "left") \
 .drop("ano_dim")

# 2.4 DimArtista: cria a dimensão de artistas.
df_dimartista = df_trusted.select(
    col("nomeArtista"),
    col("generoArtista"),
    col("anoNascimento"),
    col("anoFalecimento"),
    col("profissao"),
    col("titulosMaisConhecidos")
).distinct().withColumn("artista_id", col("nomeArtista"))

# 2.5 BridgeMidiaArtista: associa os títulos aos artistas, incluindo o campo "personagem".
df_bridgemidiaartista = df_trusted.select(
    col("id").alias("id_original"),
    col("nomeArtista"),
    col("personagem")
).join(df_dimmidia.select("midia_id", "id_original"), on="id_original", how="left") \
 .join(df_dimartista.select("artista_id", "nomeArtista"), on="nomeArtista", how="left")

# 2.6 DimGenero e BridgeMidiaGenero: trata o campo "genero", dividindo valores separados por vírgula.
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

# ------------------------------------------------------------------
# 3. Escrita dos dados transformados na camada Refined (formato Parquet)
# ------------------------------------------------------------------
refined_output_path = "s3://data-lake-paulorenato/refined/"

# Escreve a tabela FatoMidia particionada por "anoLancamento"
df_fatomidia.write.mode("overwrite") \
    .partitionBy("anoLancamento") \
    .parquet(refined_output_path + "FatoMidia")

# Escrita das demais dimensões e tabelas de associação
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

job.commit()
```
![JobRun](../Evidências/Evidencias%20-%20Sprint%209%20-%20Desafio%20(1).png)

---

## Configuração e Execução do Crawler

Após a execução do job, é necessário criar e executar um crawler para atualizar o Glue Data Catalog com as novas tabelas e schemas.

### Passos para criação do Crawler:
1. **Acesse o AWS Glue**: No Console da AWS, navegue até o serviço AWS Glue.
2. **Crie um novo crawler**:
   - Clique em **"Add crawler"**.
   - Dê um nome (por exemplo, `Crawler_Refined_Data`) e uma descrição.
3. **Configurar o data store**:
   - Selecione **"S3"** como o data store.
   - Informe o caminho: `s3://data-lake-paulorenato/refined/`
4. **Definir um role IAM**:
   - Escolha um role que possua permissões para acessar o bucket S3 e atualizar o Glue Data Catalog.
5. **Agendamento**:
   - Configure para rodar sob demanda ou agende execuções periódicas, conforme a necessidade.
6. **Configurar o output**:
   - Selecione o database do Glue Data Catalog onde as tabelas serão criadas ou atualizadas.
7. **Revisão e criação**:
   - Revise as configurações e finalize a criação do crawler.
8. **Execução do Crawler**:
   - Execute o crawler para que ele analise os dados na camada Refined e atualize o catálogo com as tabelas e seus schemas.

![Crawler](../Evidências/Evidencias%20-%20Sprint%209%20-%20Desafio%20(2).png)

---

## Validação dos Dados

Após a execução do crawler:
- Utilize o **AWS Athena** para executar consultas nas tabelas do Glue Data Catalog e validar os schemas e dados.
- Configure o **AWS QuickSight** para conectar ao Glue Data Catalog e criar dashboards e relatórios analíticos.

![Athena](../Evidências/Evidencias%20-%20Sprint%209%20-%20Desafio%20(3).png)

---

## Observações Finais

Este repositório documenta todo o processo de criação da camada Refined, desde a modelagem dos dados e desenvolvimento do job AWS Glue até a configuração do crawler para atualização do Glue Data Catalog.
```