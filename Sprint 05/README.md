# Sprint 5 - AWS Exploration

Este documento descreve as atividades realizadas durante a Sprint 5, com foco no aprendizado e na prática de conceitos relacionados à S3 da Amazon Web Services (AWS).

---

## Objetivo Geral
Explorar e praticar as capacidades dos serviços AWS, incluindo:
- Preparação para certificações AWS.
- Prática de criação e manipulação de buckets no Amazon S3.
- Configuração de hospedagem estática com o Amazon S3.

---

## Atividades Realizadas

### 1. **Curso-padrão de preparação para o exame AWS Certified Cloud Practitioner**

- Estudo teórico e prático dos conceitos fundamentais de AWS.
- Preparação para a certificação **AWS Certified Cloud Practitioner**, abordando tópicos como:
  - Introdução à computação em nuvem.
  - Serviços AWS (EC2, S3, RDS, IAM, entre outros).
  - Práticas de segurança e compliance.
  - Planejamento e monitoramento de custos na nuvem.

[Certificado do Curso](../Sprint%2005/Cerificados/18719_5_6620401_1734929093_AWS%20Skill%20Builder%20Course%20Completion%20Certificate.pdf)

- Realização do Simulado da Prova de Certificação AWS:

![simulado1](../Sprint%2005/Exercícios/Evidencia%20Exercicio%20SP5%20(1).png)
![simulado2](../Sprint%2005/Exercícios/Evidencia%20Exercicio%20SP5%20(2).png)

### 2. **AWS Skill Builder - AWS Cloud Quest: Cloud Practitioner**

- Participação em atividades interativas no **AWS Cloud Quest** para consolidar o aprendizado.
- Solução de desafios em um ambiente gamificado, envolvendo:
  - Criação e gerenciamento de recursos na AWS.
  - Resolução de problemas em cenários fictícios baseados em situações do mundo real.

![Badge AWS Cloud Quest](../Sprint%2005/Cerificados/Evidencia%20-%20Cloud%20Quest%20(2).png)

### 3. **Exercício: Configuração e Hospedagem de Site Estático no Amazon S3**

#### Objetivo
Explorar as capacidades do serviço **AWS S3**, configurando um bucket para atuar como hospedagem de conteúdo estático.

### Etapa 1: Criar um bucket

1. Acesse o AWS Management Console.
2. Pesquise pelo serviço **S3** e abra o console.
3. Clique em **Create bucket**.
4. Insira o nome do bucket, por exemplo, `mycompassbucket`.
5. Escolha a região **US East (N. Virginia) - us-east-1**.
6. Aceite as configurações padrão e clique em **Create**.

### Etapa 2: Habilitar hospedagem de site estático

1. No console S3, selecione o bucket `mycompassbucket`.
2. Navegue até **Properties**.
3. Em **Static website hosting**, clique em **Edit**.
4. Ative a opção **Use this bucket to host a website**.
5. Configure o documento de índice como `index.html`.
6. Opcionalmente, configure um documento de erro como `404.html`.
7. Clique em **Save changes**.

![Evidencia-1](../Sprint%2005/Exercícios/Evidencia%20Exercicio%20SP5%20(3).png)

### Etapa 3: Editar as configurações do Bloqueio de Acesso Público

1. Selecione o bucket `mycompassbucket`.
2. Navegue até **Permissions**.
3. Em **Block public access (bucket settings)**, clique em **Edit**.
4. Desmarque a opção **Block all public access**.
5. Confirme a desativação e clique em **Save changes**.

![Evidencia-2](../Sprint%2005/Exercícios/Evidencia%20Exercicio%20SP5%20(6).png)

### Etapa 4: Adicionar política de bucket

1. Em **Permissions**, role até **Bucket policy** e clique em **Edit**.
2. Adicione a seguinte política:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::mycompassbucket/*"
            ]
        }
    ]
}
```

3. Clique em **Save changes**.

![Evidencia-2](../Sprint%2005/Exercícios/Evidencia%20Exercicio%20SP5%20(4).png)

### Etapa 5: Configurar um documento de índice

1. Crie um arquivo local chamado `index.html` com o seguinte conteúdo:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Meu Site Estático</title>
</head>
<body>
    <h1>Bem-vindo ao meu site hospedado no Amazon S3!</h1>
    <a href="meuarquivo.csv">Baixar arquivo CSV</a>
</body>
</html>
```

2. No console S3, faça upload do `index.html` para o bucket.

![Evidencia-4](../Sprint%2005/Exercícios/Evidencia%20Exercicio%20SP5%20(5).png)

### Etapa 6: Configurar documento de erros

1. Crie um arquivo local chamado `404.html` com o seguinte conteúdo:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Erro 404</title>
</head>
<body>
    <h1>Página não encontrada</h1>
</body>
</html>
```

2. Faça upload do `404.html` para o bucket.

### Etapa 7: Testar o endpoint do site

1. No console S3, acesse **Properties** no bucket.
2. Copie o endpoint do site listado em **Static website hosting**.
3. Abra o endpoint no navegador para verificar o site.

Seguindo estes passos o site está disponível publicamente no endpoint.

![Evidencia-5](../Sprint%2005/Exercícios/Evidencia%20Exercicio%20SP5%20(7).png)

### 4. **Desafio da Sprint 05 (resumo)**

## Principais Etapas

### **1. Configuração**
- Configuração do AWS CLI com `aws configure`.
- Instalação de bibliotecas: `boto3` e `pandas`.
- Configuração de credenciais no arquivo `credentials`.

### **2. Manipulação no S3**
- **Criação do Bucket:** Nome: `desafio-compass`, Região: `us-east-1`.
- **Upload do Arquivo:** Arquivo `chegadas_2023.csv` enviado ao S3 via script Python.
- **Download do Arquivo:** O arquivo foi baixado para processamento local.

### **3. Processamento de Dados**
Operações realizadas utilizando `pandas`:
1. **Filtragem:** Dados com `Chegadas > 0` e `ano == 2023`.
2. **Agregação:** Soma e média da coluna `Chegadas`.
3. **Função Condicional:** Criação de `Categoria Chegadas` (e.g., `Muitas`, `Poucas`).
4. **Conversão:** Conversão de `Chegadas` para string.
5. **Manipulação de Datas:** Coluna `ano_mes` combinando ano e mês.
6. **Função de String:** Coluna `UF` convertida para letras minúsculas.

### **4. Reupload do Arquivo Processado**
- Arquivo `resultados_aggregados.csv` e `chegadas_2023_processado.csv` gerados e enviados de volta para o bucket S3.

---

## Scripts Utilizados
- **upload_to_s3.py:** Envio inicial do arquivo CSV ao S3.
- **process_data_3.py:** Download, processamento, e reupload do arquivo processado.

```

### Aprendizado

- Consolidação de conhecimentos básicos e intermediários de AWS.
- Habilidade em configurar e manipular buckets no Amazon S3.
- Automação de processos com boto3 e pandas.