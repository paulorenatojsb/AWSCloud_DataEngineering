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
local_dir = "C:/Users/Administrador/.vscode/CompassAcademy-1/CompassAcademy/Sprint 06/Desafio/filmes_series"

# Inicializa o cliente S3
s3_client = boto3.client('s3',
                         aws_access_key_id='awASIAXEVXYO4ZBRBZLTUZ',
                         aws_secret_access_key='eoJHSt7VtVXKPFI7jfnGCXG6tkLhBigb7zLEsrvj',
                         aws_session_token='IQoJb3JpZ2luX2VjEGoaCXVzLWVhc3QtMSJIMEYCIQCO8jS+3cFNt57CO8pQLhAMuh2neRkGjvhAw89DxH/YBgIhALmkO/Zl8sKbn5p4P4dpXOu1kW7s8yjEDMOYEnnOlmi1KpsDCFMQABoMNDkxMDg1Mzk1NzYyIgwSohNaBFd3MDJCN9Eq+ALdND+8TQb/Nr/Lon21eZtibiIDIVdGSMpqj2fulkf/6GsFIIRFXjX1ciXBxlnVLmtYtF5QplEt29+au8gfb5LDlJ6pGt6G99s4sshyxGm5d0qiN22ZxsquX59LBYKifl5SbEB+mg/jyGCRj7Q8UepSeQTSOc0bbQMrtXZZ3fXWRVWUSwJhxc6R+ryQ4o2cBRkPJvFjRVXjqbjKBhZMGJaHzZYkc1pXqAUtVH9DzKJJHLBMaNSiVjT9od+WrJ71tCofOpeykcauju+Tr6KDwSfxpcXklOOVpA5G4Gykk1m1yJkjaR27Icmf8RuXLAHGLAxp9siwHaRSW6qMrZdGyNqepCP9/0kOf5zv4Aei3wvaQWMi0xiHZCqEZcTdvsVWMAnh+xvRPhjrCn98qk0jfuUv2PqTS1n2f5UkIfK9RdjhHf6EM9tzpVt9W7lC+4ZKrYlsx4r6jF2WGVe0VZ8G+kBwFAsE5v9z3IdBnl1kZRfU+IxFRgZDlZIZMOKQ8rsGOqUBpAGhNt/9jLc82rg5DUL9yQ4JG+VsFJCe7kYvOyvrAE+cASmDDPjPOLkIR3uHRYrKZhvPu+RKQwseS5u17D4PX4XRoMqNhf/PwTIBzNeOmplNmYlZhvOZTCaXmpwrMthtIk6+Kk3F6Hz+Gjtvaj5UhfujCgqLyuLjZZwQYbFCQ5bYM2q9YM6GCZuyLUb0wTGmFnICLdHvIPmLN0KXpiI2f3miIOje',
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