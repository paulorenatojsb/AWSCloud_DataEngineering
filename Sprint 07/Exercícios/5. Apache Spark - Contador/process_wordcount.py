from pyspark import SparkContext

# Inicialize o SparkContext
sc = SparkContext("local", "WordCount")

# Leia o arquivo README.md como RDD
rdd = sc.textFile("README.md")

# Divida as linhas em palavras
words = rdd.flatMap(lambda line: line.split())

# Mapeie as palavras para pares (palavra, 1)
word_pairs = words.map(lambda word: (word, 1))

# Reduza os pares somando as ocorrências
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

# Colete o resultado e exiba
for word, count in word_counts.collect():
    print(f"{word}: {count}")