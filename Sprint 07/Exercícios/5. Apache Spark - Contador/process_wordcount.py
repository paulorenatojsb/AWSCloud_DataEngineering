from pyspark.sql import SparkSession

# Inicializa a sessão do Spark
spark = SparkSession.builder.appName("Contador").getOrCreate()

# Exemplo de dados
data = [("a", 1), ("b", 1), ("a", 1), ("c", 1), ("b", 1)]
columns = ["letra", "valor"]

# Criação de um DataFrame
df = spark.createDataFrame(data, schema=columns)

# Contagem de ocorrências
resultado = df.groupBy("letra").count()

# Salva o resultado no arquivo especificado
output_path = r"C:\Users\Administrador\.vscode\CompassAcademy-1\CompassAcademy\Sprint 07\Exercícios\5. Apache Spark - Contador\output.txt"
resultado.write.csv(output_path, header=True)

print(f"Resultado salvo em: {output_path}")