# README SPRINT 8 - Exercícios de Apache, PySpark Trilha AWS Youtube e Desafio Final Entrega 3

## 1. Trilha de Videos AWS (Youtube)
![Evidencia 1](../Sprint%2008/Certificados/Trilha%20%20Youtube%20AWS%20-%20Concluida.png)

## 2. Exercícios – Geração e Massa de Dados

### 2.1 Objetivos
Este repositório contém scripts em Python para geração de dados (inteiros, nomes de animais e nomes de pessoas) que serão processados nas próximas atividades, utilizando o framework Apache Spark. 

Ao final destes exercícios, você terá:
- Uma lista de números inteiros aleatórios;
- Uma lista de animais ordenada e armazenada em formato CSV;
- Um dataset de nomes de pessoas gerado de forma aleatória, pronto para uso posterior em análises ou processamento distribuído.

### 2.2 Instruções Gerais
1. **Desenvolva o código localmente**, usando o editor de sua preferência (VSCode, PyCharm, etc.).
2. **Faça commit** dos arquivos no seu repositório GitHub para avaliação do monitor(a).
3. Certifique-se de incluir todos os **artefatos** (códigos e evidências) correspondentes às etapas abaixo.

### 3.3 Etapas
#### 3.3.1 Etapa 1
- Declare e inicialize **uma lista com 250 inteiros aleatórios** (pode usar `random.randint`).
- Use o **método `reverse()`** para inverter a lista.
- **Imprima** o resultado invertido no console.

```python
import random

random.seed(42)  # Exemplo de seed (opcional)
lista_inteiros = [random.randint(0, 100) for _ in range(250)]
lista_inteiros.reverse()
print(lista_inteiros)
```

#### 3.3.2 Etapa 2
- Declare e inicialize **uma lista com 20 nomes de animais**.
- **Ordene** os nomes em ordem crescente.
- **Imprima** cada nome (podendo usar `for` ou list comprehension).
- **Salve** estes nomes em um arquivo CSV (um nome por linha).

```python
animais = ["gato", "cachorro", "elefante", ...]  # total de 20
animais.sort()
for animal in animais:
    print(animal)

with open("animais.csv", "w", encoding="utf-8") as f:
    for animal in animais:
        f.write(animal + "\n")
```

#### 3.3.3 Etapa 3

##### Passo 1: Instalar Biblioteca `names`
Instale a biblioteca `names` para gerar nomes:
```bash
pip install names
```

##### Passo 2: Importar Bibliotecas
No script Python, importe:
```python
import random
import names
import time
import os
```

##### Passo 3: Definir Parâmetros
Defina a semente de aleatoriedade e a quantidade de nomes:
```python
random.seed(48)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000
```
> *Observação*: Os valores acima são só exemplos. Ajuste de acordo com a atividade (o enunciado indica 3.000 nomes únicos e 10.600.000 aleatórios).

##### Passo 4: Gerar os Nomes Aleatórios
1. Gere uma lista de **nomes únicos** com `names.get_full_name()`.
2. Gere a lista final de dados, escolhendo aleatoriamente de `aux`.

**Exemplo**:
```python
aux = []
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))
```

##### Passo 5: Gerar Arquivo com Todos os Nomes
Grave todos os nomes em um arquivo texto (um por linha):
```python
with open("names_aleatorios.txt", "w", encoding="utf-8") as f:
    for nome in dados:
        f.write(nome + "\n")
```

##### Passo 6: Verificar o Conteúdo
Abra o arquivo `names_aleatorios.txt` em um editor de texto para conferir.

---

### 2.4 Observações Importantes

**Uso de Seeds**:  
   - `random.seed` garante reprodutibilidade: a cada execução, a mesma sequência de números (ou nomes) será gerada.

---

## 3. Exercícios – Apache Spark

### 3.1 Objetivo
Neste repositório, você encontrará scripts em **PySpark** para praticar manipulação de DataFrames, consultas SQL e transformações usando o framework **Apache Spark**. O foco é utilizar o arquivo **`names_aleatorios.txt`** (com milhões de nomes) e enriquecer esse dataset com novas colunas (Escolaridade, País, AnoNascimento), exercitando operações típicas de ETL com Spark.

### 3.2 Preparação
1. **Arquivo de entrada**:  
   - Copie o arquivo `names_aleatorios.txt` (gerado nos exercícios anteriores) para o diretório do projeto.
2. **Instale o PySpark** (se estiver executando localmente):
   ```bash
   pip install pyspark
   ```
3. **Configuração do Python**:  
   - Se ocorrer erro de “Cannot run program python.exe” no Windows, crie o arquivo `spark-env.cmd` em `...\pyspark\conf` com o conteúdo:
     ```
     set PYSPARK_PYTHON=<caminho_completo_python.exe>
     ```
   - Referência: [StackOverflow: PySpark Windows Setup](https://stackoverflow.com/questions/45498049/encountered-a-error-that-cant-run-program-on-pyspark)

### 3.3 Etapas
#### 3.3.1 Etapa 1
- Importe as bibliotecas necessárias:
  ```python
  from pyspark.sql import SparkSession
  from pyspark import SparkContext, SQLContext
  ```
- Crie a **SparkSession** e leia o arquivo `names_aleatorios.txt` via `spark.read.csv(...)`, resultando em um `DataFrame (df_nomes)`.  
- Liste algumas linhas com `df_nomes.show(5)`.

#### 3.3.2 Etapa 2
- Como o Spark não infere automaticamente o esquema, renomeie a coluna `_c0` para `"Nomes"`.
- Use `df_nomes.printSchema()` para ver o schema.
- Mostre 10 linhas do dataframe.

#### 3.3.3 Etapa 3
- Adicione uma coluna **Escolaridade** no `df_nomes`, com valores aleatórios entre `Fundamental`, `Medio` e `Superior`.
- Evite `for` ou `while`; utilize funções de coluna PySpark (`rand()`, `when()`, etc.) ou `rand()` + array.

#### 3.3.4 Etapa 4
- Adicione a coluna **Pais**, atribuindo de forma aleatória um dos 13 países da América do Sul.
- Novamente, use funções nativas do Spark para gerar valores aleatórios.

#### 3.3.5 Etapa 5
- Adicione a coluna **AnoNascimento**, com valores aleatórios entre 1945 e 2010.
- Utilize funções de Spark em vez de iterações manuais.

#### 3.3.6 Etapa 6
- Selecione as pessoas que nasceram **neste século** (>= 2001).
- Armazene em outro DataFrame (`df_select`) e mostre 10 linhas.

#### 3.3.7 Etapa 7
- Repita o filtro da Etapa 6 via **Spark SQL**.
  - Crie uma **tempView**: `df_nomes.createOrReplaceTempView("pessoas")`.
  - Use `spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2001").show(10)`.

#### 3.3.8 Etapa 8
- Conte, via **DataFrame.filter(...)**, quantas pessoas são **Millennials** (1980–1994).

#### 3.3.9 Etapa 9
- Repita a contagem de Millennials usando **Spark SQL**.

#### 3.3.10 Etapa 10
- Usando Spark SQL, agrupe por **País** e **Geração** (Baby Boomers, Geração X, Millennials, Geração Z).
- Mostre a quantidade de pessoas de cada país por geração, ordenando por País, Geração e Quantidade.

---

## EXERCÍCIO 5 - TMDB (Copiado da Sprint 7)

### 1. Objetivos
- Criar um **processo de extração** de dados da **API do TMDB** usando **serviços da AWS**.

### 2. Atividades

#### 2.1. Etapa 2 - Testando as credenciais e a biblioteca
- Depois de obter sua **chave de API** do TMDB, faça **solicitações** à API no formato:
https://api.themoviedb.org/3/{endpoint}?api_key={SUA_CHAVE_DE_API}&{parametros_opcionais}

yaml
Copiar
- **endpoint**: por exemplo, `movie/{movie_id}`, `tv/{tv_id}`, etc.  
- **parametros_opcionais**: por ex. `language=pt-BR` para obter informações em português.

## Resumo Desafio – Entrega 3 (Camada Trusted)

### Objetivo
Processar dados da **Raw Zone** e produzir uma **Camada Trusted** em **formato Parquet**, usando **AWS Glue** + **Spark**, para posterior consulta via **Glue Data Catalog** e **AWS Athena**.

### Entregáveis
1. **Scripts PySpark (AWS Glue)**:  
   - `glue_job_csv.py`: processa arquivos CSV (batch) da Raw para Trusted (sem partição).  
   - `glue_job_json.py`: processa dados JSON (API TMDB) da Raw para Trusted (particionado por data de ingestão).  
2. **Arquivo Markdown**: documentação, prints, e motivadores das APIs utilizadas.

### Preparação
- Entender o **Desafio de Filmes e Séries** (Sprint 6).  
- Ter dados na Raw Zone e buckets/pastas no S3 para a Trusted Zone.

### Atividade
- **Formatos**: os dados **Parquet** vão para o S3.  
- **Particionamento**: apenas para dados oriundos da **API TMDB** (JSON).  
- **CSV** não requer partições.  

### Conclusão
Os dados limpos na Trusted Zone podem ser consultados via **Athena** (SQL) ou integrados a outras ferramentas. Essa etapa consolida uma visão confiável do seu **Desafio de Filmes e Séries**, unindo conceitos de Data Lake, AWS Glue e Spark.