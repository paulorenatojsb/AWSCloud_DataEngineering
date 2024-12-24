import boto3

s3_client = boto3.client('s3',
                        aws_access_key_id="ASIAXEVXYO4ZAY5NKPYI", 
                        aws_secret_access_key="OXbZ7CTGitaIkmvvVA4JCjMWpvSHNpXUQMFOHJLe",
                        aws_session_token="IQoJb3JpZ2luX2VjEBoaCXVzLWVhc3QtMSJIMEYCIQDOwfUZ9ovzLCqz1H377yaH7Del4LzMQEIpYB05mKSCkAIhAKz++KxXLSJXGAUEOuZBzBMO3fDuDR8n6NlCEDAB956eKqQDCOL//////////wEQABoMNDkxMDg1Mzk1NzYyIgzP1TmN1N5Z4cCVxNUq+AKII5kx/xU/wzMbmrGeioEL/UiUHCLTK5CHRzwCSX6kUvu0sSwFsaxJkLDh5U7BmsmmfN7Yr3TjpIKlCdmpJ68qUIgOa06pZDWeRcGgd8TiZ9Kaa4zwRgGDP8VFrp5zm8Uj4KDHLLlThab68OpImODOBig+Dy7mpqgl+h6UVZ1qnJXzXv+XAT8eqWgxgISN5Ty2HAg1wtWQy5tem2NscB9geO/UXey4dmsTpmNi2oUT3ZSn/rKycI2sc5rCD6gYZKv2RQ9GqH5SOqVu61lZ590PqFlNzL0v28M/baqHVtPHEnZKgnO+UnfNTCmHVX51SuD87HGxIS1xMab/Cj7OC7SashdKVwnngx9Tk+IZboGBNb3FHa34KbBR6tdtS9YMOAMz/Q+FybFlVJ1KGx6LgfMjqqv+MXlEtyKcVyrO8p16gl4ZEbTREzOvtES1tN2fVOkuLUu567KAuCwMrdO1BV6lckSU7DPC2grPpVc5qmrNRgkvIFb+YWhnMPORqLsGOqUBbx0INpghbcx9IkULfnkoicTTqljdxzDRTfY8qhbB11K/DwY55cfLTvmR1EbonwLbockjZF5TG7hZWQnVRwD/kaqxA67TnZxY09q7ZGpjkDBEb0dRjkdPhTm9GgQkRoqGa46oif77I2CaFP/0R+O7MOxrCp6A3Ye4CUcIiygJY5crvFn3VGamYYyzZvkdbqqNQlGw6sd9qvwTHluAhpW4pxiP74XP",
                        region_name='us-east-1')

# Configuração
bucket_name = "desafio-compass"
file_name = "chegadas_2023.csv"
file_path = "C:/Users/Administrador/CompassAcademy/Sprint 05/chegadas_2023.csv"  # Substitua pelo caminho correto do arquivo local

# Fazer upload do arquivo para o bucket
s3_client.upload_file(file_path, bucket_name, file_name)
print(f"Arquivo '{file_name}' carregado com sucesso no bucket '{bucket_name}'.")