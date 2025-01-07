# README DESAFIO SPRINT 6 - AWS Certification

Este documento descreve as atividades realizadas durante a Sprint 6, com foco no aprendizado e na prática de conceitos relacionados à S3 da Amazon Web Services (AWS), com utilização dos recursos Athena e Lambda.

---

## Objetivo Geral
Explorar e praticar as capacidades dos serviços AWS, incluindo:
- Preparação para certificações AWS.
- Prática de criação e manipulação de buckets no Amazon S3.
- Configuração de hospedagem estática com o Amazon S3.
- Configuração e utilização dos recursos AWS Athena e AWS Lambda.

---

## Cursos AWS Skills Builder Realizados

### 1. **Noções Básicas de Analytics na AWS - Parte 1 (Português)**

[Certificado do Curso](../Certificados/AWS%20Certificate_Noções%20básicas%20de%20Analytics%20na%20AWS%20–%20Parte%201_Paulo%20Renato%20Braga.pdf)

### 2. **Fundamentos de analytics na AWS – Parte 2**

[Certificado do Curso](../Certificados/AWS%20Certificate_Fundamentos%20de%20analytics%20na%20AWS%20–%20Parte%202_Paulo%20Renato%20Braga.pdf)

### 3. **Serverless Analytics**

[Certificado do Curso](../Certificados/AWS%20Certificate_Serverless%20Analytics%20_Paulo%20Renato%20Braga.pdf)

### 4. **Introduction to Amazon Athena**

[Certificado do Curso](../Certificados/AWS%20Certificate_Introduction%20to%20Amazon%20Athena_Paulo%20Renato%20Braga.pdf)

### 5. **AWS Glue Getting Started**

[Certificado do Curso](../Certificados/AWS%20Certificate_AWS%20Glue%20Getting%20Started_Paulo%20Renato%20Braga.pdf)

### 6. **Amazon EMR Getting Started**

[Certificado do Curso](../Certificados/AWS%20Certificate_Amazon%20EMR%20Getting%20Started_Paulo%20Renato%20Braga.pdf)

### 7. **Getting Started with Amazon Redshift**

[Certificado do Curso](../Certificados/AWS%20Certificate_Getting%20Started%20with%20Amazon%20Redshift_Paulo%20Renato%20Braga.pdf)

### 8. **Best Practices for Data Warehousing with Amazon Redshift**

[Certificado do Curso](../Certificados/AWS%20Certificate_Best%20Practices%20for%20Data%20Warehousing%20with%20Amazon%20Redshift_Paulo%20Renato%20Braga.pdf)

### 9. **Amazon QuickSight - Getting Started**

[Certificado do Curso](../Certificados/AWS%20Certificate_Amazon%20QuickSight%20-%20Getting%20Started_Paulo%20Renato%20Braga.pdf)

---

## **Desafio da Sprint 06 (resumo)**

# Desafio - Data Lake Filmes e Séries

## Objetivo
Construir um Data Lake para filmes e séries, com ingestão, processamento e consumo de dados.

## Entregáveis
- Código com comentários no Git.
- Markdown com explicações e evidências.
- DockerFile e código Python (.py).

## Desafio
1. **Ingestão**: Carregar arquivos CSV para o S3 usando Python e `boto3`.
2. **Processamento**: Padronizar e catalogar os dados.
3. **Modelo Dimensional**: Definir modelo para análise com Apache Spark.
4. **Consumo**: Criar dashboards analíticos.

## Entrega 1
- **Objetivo**: Ingestão de dados CSV para o S3.
- **Tarefas**:
  - Criar código Python para ingestão.
  - Usar Docker para execução e carga no S3.