# README SPRINT 7 - Pyspark, TMDB e AWS Glue

## Curso: Formação Spark com Pyspark - O Curso Completo

Além do curso teórico **Formação Spark com Pyspark - O Curso Completo** realizado na Sprint, também foram propostos três exercícios principais, cada um abordando diferentes aspectos de **Spark**, **Docker** e **Serviço AWS Glue**. A seguir, apresentamos um resumo das tarefas, objetivos e passos esperados em cada exercício.

---

## EXERCÍCIO 1 - Pyspark

### 1. Objetivo
Desenvolver um **job de processamento** com o framework **Spark** por meio de um **container Docker**.

### 2. Etapas

#### 2.1. Etapa 1
- Realizar o **pull** da imagem [jupyter/all-spark-notebook](https://hub.docker.com/r/jupyter/all-spark-notebook).  

#### 2.2. Etapa 2
- Criar um **container** a partir da imagem acima.
- A imagem contém Spark e **Jupyter Lab**.  
  - Se quiser usar o Jupyter Lab, iniciar o container em **modo interativo** (`-it`).  
  - Mapear a **porta 8888** do container para uma porta local (por ex. `-p 8888:8888`).  
- Copiar o link com prefixo `http://127.0.0.1:8888/lab?token=` para acessar o **Jupyter Lab** no navegador.

#### 2.3. Etapa 3
- Em outro terminal, usar o comando `docker exec` (com flags `-i -t`) para **executar** `pyspark` dentro do container.
- Isso disponibilizará o **terminal interativo** do Spark (Spark Shell em Python).

#### 2.4. Etapa 4
- Usando o **Spark Shell**, escrever e testar comandos para **contar a quantidade de ocorrências** de cada palavra contida no arquivo `README.md` do seu repositório Git.
- Dica: pode-se usar o comando `wget` dentro do container para baixar arquivos da internet.

---

## EXERCÍCIO 2 - TMDB

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

---

## EXERCÍCIO 3 - LAB AWS GLUE

O objetivo era criar um processo de ETL para processar um arquivo CSV usando o AWS Glue e salvar os dados no S3 em formato JSON particionado.

### **Passos**

### **1. Preparar Dados de Origem**
- Faça upload do arquivo `nomes.csv` para o S3 no caminho: `s3://{BUCKET}/lab-glue/input/nomes.csv`.

### **2. Criar Role IAM**
- Crie uma role chamada `AWSGlueServiceRole-Lab4` com as permissões:
  - `AmazonS3FullAccess`
  - `AWSLakeFormationDataAdmin`
  - `AWSGlueConsoleFullAccess`
  - `CloudWatchFullAccess`.

### **3. Configurar o Glue**
- Acesse o Glue e configure:
  - Adicione a role `AWSGlueServiceRole-Lab4`.
  - Habilite acesso total ao S3.
  - Atualize a role padrão do Glue.

### **4. Criar Banco no Lake Formation**
- Crie um banco de dados chamado `glue-lab`.

### **5. Criar Job no Glue**
- Crie um job com as configurações:
  - **Nome:** `job_aws_glue_lab_4`
  - **Role:** `AWSGlueServiceRole-Lab4`
  - **Engine:** Spark
  - **Versão:** Glue 3.0
  - **Workers:** 2
  - **Timeout:** 5 minutos
- **Script:** 
  1. Leia o arquivo `nomes.csv` do S3.
  2. Converta os nomes para maiúsculas.
  3. Agrupe por `ano` e `sexo` e calcule totais.
  4. Salve os dados no S3 em JSON particionado por `sexo` e `ano`.

### **6. Criar Crawler**
- Crie um crawler com:
  - **Nome:** `FrequenciaRegistroNomesCrawler`
  - **Caminho S3:** `s3:///lab-glue/frequencia_registro_nomes_eua/`
  - **Banco de Dados:** `glue-lab`
  - **Frequência:** On Demand.
- Execute o crawler.

### **7. Consultar no Athena**
- No Athena, selecione o banco `glue-lab` e execute:
  ```sql
  SELECT * 
  FROM glue-lab.frequencia_registro_nomes_eua 
  LIMIT 10;

---

## Desafio: Filmes e Séries – Etapa 2

**Resumo**:  
Nesta etapa do Desafio de Filmes e Séries, realizamos a **ingestão de dados** via **API do TMDB** para complementar informações de filmes e séries, salvando os dados brutos em formato JSON na **Raw Zone** do Amazon S3. O desafio envolve tanto o aprendizado em manipulação de APIs externas quanto a gravação segura e organizada dos dados no Data Lake, preparando terreno para análises posteriores.

Detalhamento completo consta no `README.me` do Desafio, que pode ser acesso [clicando aqui](./Desafio/README.md).

---