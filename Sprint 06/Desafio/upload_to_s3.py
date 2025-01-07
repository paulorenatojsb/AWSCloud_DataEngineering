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
                         aws_access_key_id='ASIAXEVXYO4ZMRTBIXNX',
                         aws_secret_access_key='e4wAhRteGen7hhtk6nlXBViNfKuz32LQm+F3hFPr',
                         aws_session_token='IQoJb3JpZ2luX2VjEHgaCXVzLWVhc3QtMSJGMEQCIGY9mTXRQrQQeuEuV0fJDP12oidtd1eGH0BiWumyKy+XAiB51NpEdO0w5OA/koYHNe8/mHRlucRrD8BekGsolHa3HSqbAwhhEAAaDDQ5MTA4NTM5NTc2MiIMnZCpoDSLwgmtZQFoKvgCAeL+u442SqPwxb2lXN7bNDM19RkR2PmUWpQemc0F8RKLWYIZBF6g7+cpujNJKZjtWh3cPBtNPGjaD7VS+AYBikM2wXftJ45IFW/SyFz7lmh952XkBacu5sE3SgDHZ6zIWyf9dskQoS8pL63TAHC4Ten4du6m5ZphgRiKk/SWRtrUcIuBqOuSCEeyPIrhRkj5gWukS4qz7cNVF3sYDsc/6erZxpM7AQLlXCHmSU4p4RE5RNgJ0UYiGE9dSpAVQ2rn1iRAIjvUtfui0Fy7EsYyY/AkEWf10Jns1N1dWy2dHSizcdxCoVs/rr/6zu8BCctdx5HUb9UOyrmQznn0TV7/ALeeLB5rVQIMdf4cW2LqCBYyuOyIfpyeEJ6f04vC8clmbMXJsE3DdzISmngUG2P05aIctO0ywHdVkc9+omSvhzBI72Oopb7+cKW02pCIjckaK39erUiIQ3JWn/necMdsbpeS/HXuO2Ms/hMHkqnZbRyh2usJal/4oDDxlPW7BjqnAXhVV9hukAJEhgZabredC2sA4mfurJTzr3zYEn0wI0o5Ksb4fPf4U1cBRsYl2bwWtIM4eXufbxEn4i+M/SfjpX7kvnMbEjnFkUapk7p1YCVkqnM75twaJQittx6P/GhSopgy4JCT/e34r0GeVQN3ghTmDcQznPCHj4tEeqGZ4kv545McVcV2gKuZTyJIc1y05d5QxMxKonf7xjxrPPKcPPWWPChN1xeB',
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