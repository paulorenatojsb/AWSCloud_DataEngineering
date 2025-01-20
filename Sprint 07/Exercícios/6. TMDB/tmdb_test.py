import requests
import pandas as pd
from IPython.display import display

api_key = "SUA_CHAVE_AQUI"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={SUA_CHAVE_AQUI}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data['results']:
    df_temp = {
        'Titulo': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }
    filmes.append(df_temp)

df = pd.DataFrame(filmes)
display(df)