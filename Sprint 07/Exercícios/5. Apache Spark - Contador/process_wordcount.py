from pyspark.sql.functions import explode, split, lower, trim, col

# Leia o arquivo README.md
df = spark.read.text("README.md")

# Divida o texto em palavras, converta para minúsculas e remova espaços em branco
words_df = df.select(explode(split(lower(trim(col("value"))), "\\s+")).alias("word"))

# Conte as ocorrências de cada palavra
word_counts = words_df.groupBy("word").count().orderBy("count", ascending=False)

# Mostre os resultados
word_counts.show()