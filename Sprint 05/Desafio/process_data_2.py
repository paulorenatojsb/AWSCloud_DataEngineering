import boto3
import pandas as pd
from io import StringIO

# Initialize the S3 client
s3_client = boto3.client('s3',
                          aws_access_key_id='ASIAXEVXYO4ZAY5NKPYI', 
                          aws_secret_access_key='OXbZ7CTGitaIkmvvVA4JCjMWpvSHNpXUQMFOHJLe',
                          aws_session_token='IQoJb3JpZ2luX2VjEBoaCXVzLWVhc3QtMSJIMEYCIQDOwfUZ9ovzLCqz1H377yaH7Del4LzMQEIpYB05mKSCkAIhAKz++KxXLSJXGAUEOuZBzBMO3fDuDR8n6NlCEDAB956eKqQDCOL//////////wEQABoMNDkxMDg1Mzk1NzYyIgzP1TmN1N5Z4cCVxNUq+AKII5kx/xU/wzMbmrGeioEL/UiUHCLTK5CHRzwCSX6kUvu0sSwFsaxJkLDh5U7BmsmmfN7Yr3TjpIKlCdmpJ68qUIgOa06pZDWeRcGgd8TiZ9Kaa4zwRgGDP8VFrp5zm8Uj4KDHLLlThab68OpImODOBig+Dy7mpqgl+h6UVZ1qnJXzXv+XAT8eqWgxgISN5Ty2HAg1wtWQy5tem2NscB9geO/UXey4dmsTpmNi2oUT3ZSn/rKycI2sc5rCD6gYZKv2RQ9GqH5SOqVu61lZ590PqFlNzL0v28M/baqHVtPHEnZKgnO+UnfNTCmHVX51SuD87HGxIS1xMab/Cj7OC7SashdKVwnngx9Tk+IZboGBNb3FHa34KbBR6tdtS9YMOAMz/Q+FybFlVJ1KGx6LgfMjqqv+MXlEtyKcVyrO8p16gl4ZEbTREzOvtES1tN2fVOkuLUu567KAuCwMrdO1BV6lckSU7DPC2grPpVc5qmrNRgkvIFb+YWhnMPORqLsGOqUBbx0INpghbcx9IkULfnkoicTTqljdxzDRTfY8qhbB11K/DwY55cfLTvmR1EbonwLbockjZF5TG7hZWQnVRwD/kaqxA67TnZxY09q7ZGpjkDBEb0dRjkdPhTm9GgQkRoqGa46oif77I2CaFP/0R+O7MOxrCp6A3Ye4CUcIiygJY5crvFn3VGamYYyzZvkdbqqNQlGw6sd9qvwTHluAhpW4pxiP74XP',
                          region_name='us-east-1')

# Configurações do S3
bucket_name = "desafio-compass"
file_name = "chegadas_2023.csv"
output_file_name = r"C:/Users/Administrador/CompassAcademy/Sprint 05/chegadas_2023_processado.csv"

try:
    # Baixar o arquivo do S3
    print("Baixando o arquivo do S3...")
    s3_client.download_file(bucket_name, file_name, output_file_name)
    print(f"Arquivo '{file_name}' baixado com sucesso.")

    # Carregar o arquivo CSV com a codificação correta
    print("Carregando o arquivo CSV...")
    df = pd.read_csv(output_file_name, encoding='latin1', sep=';')  # Substitua ',' pelo delimitador correto

    # 4.1 Filtrar com dois operadores lógicos
    filtered_df = df[(df['Chegadas'] > 0) & (df['ano'] == 2023)]
    print("\nFiltragem com dois operadores lógicos:")
    print(filtered_df.head())

    # 4.2 Funções de agregação
    aggregation_result = df['Chegadas'].agg(['sum', 'mean'])
    print("\nResultados de agregação:")
    print(aggregation_result)

    # 4.3 Função condicional
    df['Categoria Chegadas'] = df['Chegadas'].apply(lambda x: 'Muitas' if x > 100 else 'Poucas')
    print("\nColuna condicional adicionada:")
    print(df[['Chegadas', 'Categoria Chegadas']].head())

    # 4.4 Função de conversão
    df['Chegadas_str'] = df['Chegadas'].astype(str)
    print("\nColuna convertida para string:")
    print(df[['Chegadas_str']].head())

    # 4.5 Função de data
    df['ano_mes'] = df['ano'].astype(str) + '-' + df['cod mes'].astype(str)
    print("\nColuna de ano e mês combinados:")
    print(df[['ano', 'cod mes', 'ano_mes']].head())

    # 4.6 Função de string
    df['UF_minúscula'] = df['UF'].str.lower()
    print("\nColuna 'UF' modificada para minúsculas:")
    print(df[['UF', 'UF_minúscula']].head())

    # Salvar o DataFrame processado em S3
    output = StringIO()
    df.to_csv(output, index=False, sep=';')
    output.seek(0)

    print("Salvando arquivo processado no S3...")
    s3_client.put_object(Bucket=bucket_name, Key="chegadas_2023_processado.csv", Body=output.getvalue())
    print(f"\nArquivo processado salvo no bucket '{bucket_name}' como 'chegadas_2023_processado.csv'.")

except UnicodeDecodeError as ude:
    print(f"Erro de codificação: {ude}. Verifique a codificação do arquivo ou altere o 'encoding' para outro valor (e.g., 'latin1').")
except Exception as e:
    print(f"Ocorreu um erro: {e}")