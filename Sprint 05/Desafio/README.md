# Sprint 05 - Desafio AWS S3 + Script Python

## Objetivo

O objetivo deste desafio foi praticar conhecimentos de nuvem AWS aprendidos durante a sprint, com foco em manipulação de arquivos no serviço S3 e análise de dados utilizando Python.

---

## Preparação

Para que o desafio pudesse ser bem executado, foi configurado AWS CLI com `aws configure` via Power Shell, além da instalação das bibliotecas `boto3` e `pandas`.

- As Credenciais (`aws_access_key_id`, `aws_secret_access_key`, `aws_session_token`) foram adicionadas para autenticação no arquivo `credentials` localizado em `C:\Users\Administrador\.aws`.

---

### 1. Manipulação de Arquivos no S3

#### **1.1. Criação do Bucket**

Realizei a criação do Bucket diretamente via console AWS.

- Nome do bucket: `desafio-compass`.
- Região: `us-east-1`.

![Evidencia1](../Evidências/Evidencia%20Desafio%20SP5%20(2).png)

#### **1.2. Upload do Arquivo Original**

- Arquivo enviado: `chegadas_2023.csv`.
- Ferramenta: Script Python utilizando `boto3`.

![Evidencia2](../Evidências/Evidencia%20Desafio%20SP5.png)

#### **1.3. Download do Arquivo**

- O arquivo foi baixado do bucket S3 para o ambiente local para processamento.

```python
s3_client.download_file(bucket_name, file_name, output_file_name)
```

---

### 2. Processamento dos Dados

Os dados foram carregados no formato `.csv` e processados utilizando a biblioteca `pandas` para atender às exigências do desafio.

#### **2.1. Operações Realizadas**

1. **Filtragem com Dois Operadores Lógicos:**
   - Filtrar dados onde `Chegadas > 0` e `ano == 2023`.

2. **Funções de Agregação:**
   - Soma e média da coluna `Chegadas`.

3. **Função Condicional:**
   - Criada a coluna `Categoria Chegadas` para categorizar dados como `Muitas` ou `Poucas`.

4. **Função de Conversão:**
   - Convertida a coluna `Chegadas` para string.

5. **Função de Data:**
   - Criada a coluna `ano_mes` combinando ano e mês.

6. **Função de String:**
   - Coluna `UF` convertida para letras minúsculas.

#### **2.2. Consolidação dos Resultados**

- Todas as operações foram consolidadas em um único DataFrame.
- Salvo em um arquivo CSV: `resultados_aggregados.csv`.

![Evidencia3](../Evidências/Evidencia%20Desafio%20SP5%20(3).png)

---

### 4. Upload do Arquivo Processado

O arquivo processado foi enviado de volta para o bucket S3:

```python
s3_client.put_object(Bucket=bucket_name, Key="resultados_aggregados.csv", Body=output.getvalue())
```

![Evidencia4](../Evidências/Evidencia%20Desafio%20SP5%20(4).png)

---

## Resultados Obtidos

- Arquivo processado disponível no bucket S3:
  - **Nome do arquivo:** `resultados_aggregados.csv`.
- As operações de filtragem, agregação, conversão, e manipulação foram realizadas com sucesso e os resultados consolidados no arquivo gerado.

---

## Scripts Utilizados

### **upload_to_s3.py**

Script para upload inicial do arquivo `chegadas_2023.csv` para o bucket S3.

### **process_data_3.py**

Script para download, processamento, e reupload do arquivo processado para o bucket S3.

---

## Conclusão

Este desafio permitiu aplicar práticas de manipulação de dados e uso de serviços AWS, consolidando o conhecimento em análise de dados e automação com Python.