import boto3

s3_client = boto3.client('s3',
                         aws_access_key_id='INSIRA SUA CHAVE DE ACESSO',
                         aws_secret_access_key='INSIRA SUA CHAVE DE ACESSO SECRETA',
                         aws_session_token='INSIRA SEU TOKEN DE SESSÃO',
                        region_name='us-east-1')

# Configuração
bucket_name = "desafio-compass"
file_name = "chegadas_2023.csv"
file_path = "C:/Users/Administrador/CompassAcademy/Sprint 05/chegadas_2023.csv"  # Substitua pelo caminho correto do arquivo local

# Fazer upload do arquivo para o bucket
s3_client.upload_file(file_path, bucket_name, file_name)
print(f"Arquivo '{file_name}' carregado com sucesso no bucket '{bucket_name}'.")