# Desafio da Sprint 4 - Containers Docker com Python

## **Objetivo**
O objetivo deste desafio foi praticar os principais conceitos de Docker **Docker** e a continuação dos conceitos de **Python**. Nele eu aprendi a criar imagens no Docker, executar contêineres e automatizar a execução de scripts Python.

---

## **Desafio**
O desafio está dividido em 3 etapas principais.

---

## **Etapa 1 - Criar uma imagem para o `carguru.py`**

### **Objetivo**
Criar uma imagem Docker que execute o script **carguru.py**.

### 📘 **Conteúdo do Dockerfile**
```dockerfile
# Usando a imagem base do Python no Docker
FROM python:3.9

# Copiando o arquivo carguru.py para o contêiner
COPY carguru.py /app/carguru.py

# Definindo o diretório de trabalho
WORKDIR /app

# Comando padrão para executar o script
CMD ["python", "carguru.py"]
```
![Evidencia2](../Evidências/Desafio/Sprint%204%20-%20Desafio%20Evidencias%20(3).png)

### 📘 **Conteúdo do carguru.py**
```python
import random

carros = ['Chevrolet Onix', 'Chevrolet Celta', 'Fiat Uno', 'Fiat Argo', 'Ford Ka', 'Ford Fiesta', 'Volkswagen Gol', 'Volkswagen Voyage']
random_carros = random.choice(carros)

print('Você deve dirigir um ' + random_carros)
```
![Evidencia1](../Evidências/Desafio/Sprint%204%20-%20Desafio%20Evidencias%20(1).png)

---

### 🛠️ **Comandos para execução**

1. **Construir a imagem Docker:**
   ```bash
   docker build -t carguru-image -f Dockerfile .
   ```

2. **Executar o contêiner:**
   ```bash
   docker run carguru-image
   ```

![Evidencia7](../Evidências/Desafio/Sprint4-Desafio%20(1).png)

---

## 🚀 **Etapa 2 - Reutilizar contêineres**

### ❓ **Pergunta**
É possível reutilizar contêineres?

### ✅ **Resposta**
Sim, é possível reutilizar contêineres. 

### 🛠️ **Comandos para reutilizar um contêiner**

1. **Verificar quais contêineres estão parados**:
   ```bash
   docker ps -a
   ```

2. **Iniciar um contêiner parado**:
   ```bash
   docker start <container_id>
   ```

3. **Acessar o terminal do contêiner**:
   ```bash
   docker attach <container_id>
   ```
![Evidencia3](../Evidências/Desafio/Sprint4-Desafio%20(4).png)

4. **Justificativa**
- Contêineres Docker não são destruídos automaticamente ao serem parados, a menos que você adicione a flag `--rm` no comando `docker run`.
- Se o contêiner for reutilizado, ele mantém o estado em que parou.

---

## 🚀 **Etapa 3 - Criar o contêiner `mascarar-dados`**

### 📝 **Objetivo**
Criar um contêiner interativo que permita ao usuário inserir palavras e gerar o **hash SHA-1** dessas palavras.

### 📘 **Conteúdo do Dockerfile**
```dockerfile
# Usar uma imagem base de Python
FROM python:3.9-slim

# Copiar o script para o contêiner
COPY mascarar_dados.py /app/mascarar_dados.py

# Definir o diretório de trabalho
WORKDIR /app

# Comando padrão para executar o script
CMD ["python", "mascarar_dados.py"]
```

![Evidencia4](../Evidências/Desafio/Sprint%204%20-%20Desafio%20Evidencias%20(4).png)

### 📘 **Conteúdo do mascarar_dados.py**
```python
import hashlib

while True:
    user_input = input("Digite uma string para mascarar (ou 'sair' para encerrar): ")
    if user_input.lower() == "sair":
        print("Encerrando...")
        break
    sha1_hash = hashlib.sha1(user_input.encode()).hexdigest()
    print(f"Hash SHA-1: {sha1_hash}")
```

![Evidencia5](../Evidências/Desafio/Sprint%204%20-%20Desafio%20Evidencias%20(2).png)

---

### 🛠️ **Comandos para execução**

1. **Construir a imagem Docker**:
   ```bash
   docker build -t mascarar-dados -f Dockerfile .
   ```

2. **Executar o contêiner** (permitir entrada de dados interativamente):
   ```bash
   docker run -it mascarar-dados
   ```

3. **Interação no contêiner**:
   ```
   Digite uma string para mascarar (ou 'sair' para encerrar): Duster
   Hash SHA-1: a53f2fdb583f8e7f9d660334b9e2f3f1c1655df6

   Digite uma string para mascarar (ou 'sair' para encerrar): mudar@123
   Hash SHA-1: f43c6d2c7d5bc7c060cc6c83641b1d2f80a8bb9b

   Digite uma string para mascarar (ou 'sair' para encerrar): sair
   Encerrando...
   ```
![Evidencia6](../Evidências/Desafio/Sprint4-Desafio%20(3).png)
---

## 🛠️ **Comandos úteis para Docker**

| **Comando**                    | **Descrição**                                      |
|-------------------------------|---------------------------------------------------|
| `docker build -t image-name .` | Cria a imagem Docker no diretório atual            |
| `docker run image-name`         | Executa o contêiner de uma imagem Docker           |
| `docker ps`                    | Lista os contêineres em execução                   |
| `docker ps -a`                 | Lista todos os contêineres (ativos e parados)      |
| `docker stop <container_id>`   | Para um contêiner ativo                            |
| `docker rm <container_id>`     | Remove um contêiner parado                         |
| `docker images`                | Lista todas as imagens Docker no sistema          |
| `docker rmi <image_id>`        | Remove uma imagem Docker                           |

---

## 📋 **Resolução dos questionamentos**
### **Etapa 2: Reutilização de contêineres**
- **É possível reutilizar contêineres?**
  ✅ Sim.

- **Comando para reutilizar um contêiner:**
  ```bash
  docker start <container_id>
  ```

- **Justificativa**:
  O contêiner Docker pode ser reutilizado desde que ele não seja removido. Usar o comando `docker start` permite que ele retome do estado anterior.