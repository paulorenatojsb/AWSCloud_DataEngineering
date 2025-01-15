import boto3
import os
from datetime import datetime

# Configurações AWS
aws_access_key = 'SEU_ACCESS_KEY'
aws_secret_key = 'SEU_SECRET_KEY'
aws_session_token = 'SEU_SESSION_TOKEN'
region_name = 'us-east-1'
bucket_name = 'data-lake-paulorenato'

# Diretório com os arquivos CSV
local_dir = '/app'

# Inicializa o cliente S3
s3_client = boto3.client('s3',
                         aws_access_key_id='INSIRA SUA CHAVE DE ACESSO',
                         aws_secret_access_key='INSIRA SUA CHAVE DE ACESSO SECRETA',
                         aws_session_token='INSIRA SEU TOKEN DE SESSÃO',
                         region_name='us-east-1')

# Data atual para estrutura de pastas
today = datetime.now()
date_path = today.strftime('%Y/%m/%d')

# Upload de arquivos
def upload_files(local_dir, bucket_name):
    for file_name in os.listdir(local_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(local_dir, file_name)
            s3_key = f"Raw/Local/CSV/{file_name.split('.')[0].capitalize()}/{date_path}/{file_name}"
            
            print(f"Carregando {file_name} para s3://{bucket_name}/{s3_key}")
            s3_client.upload_file(file_path, bucket_name, s3_key)
            print(f"{file_name} carregado com sucesso!")

upload_files(local_dir, bucket_name)