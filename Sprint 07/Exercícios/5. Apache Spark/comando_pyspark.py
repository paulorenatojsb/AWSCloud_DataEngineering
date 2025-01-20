# 1. Ler o arquivo README.md em um RDD
lines = sc.textFile("README.md")

# 2. Separar (split) cada linha em palavras
words = lines.flatMap(lambda line: line.split())

# 3. Mapear cada palavra para uma tupla (palavra, 1)
pairs = words.map(lambda w: (w, 1))

# 4. Reduzir (somar) as ocorrências
wordCounts = pairs.reduceByKey(lambda a, b: a + b)

# 5. Coletar o resultado
resultado = wordCounts.collect()

# 6. Exibir
for word, count in resultado:
    print(word, count)

#Para ver as palavras mais frequentes primeiro:
wordCountsSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey(False)
wordCountsSorted.collect()