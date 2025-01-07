# Base Image
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copiar os arquivos para o container
COPY . /app

# Instalar dependências
RUN pip install boto3 pandas

# Comando para execução do script
CMD ["python", "upload_to_s3.py"]