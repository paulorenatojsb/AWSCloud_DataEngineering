import json
import requests
import boto3
from datetime import datetime

# >>> CREDENCIAIS DESEJADAS (mas cuidado com exposição)
AWS_ACCESS_KEY_ID = "INSIRA SUA CHAVE DE ACESSO"
AWS_SECRET_ACCESS_KEY = "INSIRA SUA CHAVE DE ACESSO SECRETA"
AWS_SESSION_TOKEN = "INSIRA SEU TOKEN DE SESSÃO"
AWS_REGION = "us-east-1"
BUCKET_NAME = "data-lake-paulorenato"

API_KEY = "INSIRA A CHAVE DA SUA API"

MOVIE_GENRES = "80,10752"
TV_GENRES = "80,10768"
MAX_PAGES_MOVIES = 500
MAX_PAGES_TV = 500

def chunker(seq, size=100):
    """Divide uma lista em blocos de até 'size' elementos."""
    for pos in range(0, len(seq), size):
        yield seq[pos:pos+size]

def discover_movies(genres, page):
    """
    Chama o endpoint /discover/movie para coletar filmes de determinados gêneros.
    Retorna o JSON (com 'results', 'page', 'total_pages', etc.) ou None em caso de erro.
    """
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": genres,
        "page": page,
        "language": "en-US"
    }
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"[ERRO] discover_movies - Página {page}: {resp.status_code} - {resp.text}")
        return None

def discover_tv(genres, page):
    """
    Chama o endpoint /discover/tv para coletar séries de determinados gêneros.
    Retorna o JSON (com 'results', 'page', 'total_pages', etc.) ou None em caso de erro.
    """
    url = "https://api.themoviedb.org/3/discover/tv"
    params = {
        "api_key": API_KEY,
        "with_genres": genres,
        "page": page,
        "language": "en-US"
    }
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"[ERRO] discover_tv - Página {page}: {resp.status_code} - {resp.text}")
        return None

def get_movie_imdb_id(tmdb_movie_id):
    """
    Dado um TMDB ID (filme), obtém o IMDb ID via /movie/{movie_id}/external_ids.
    Retorna a string do IMDb ou None se não existir.
    """
    url = f"https://api.themoviedb.org/3/movie/{tmdb_movie_id}/external_ids"
    params = {
        "api_key": API_KEY
    }
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("imdb_id")
    else:
        return None

def get_tv_imdb_id(tmdb_tv_id):
    """
    Dado um TMDB ID (série), obtém o IMDb ID via /tv/{tv_id}/external_ids.
    Retorna a string do IMDb ou None se não existir.
    """
    url = f"https://api.themoviedb.org/3/tv/{tmdb_tv_id}/external_ids"
    params = {
        "api_key": API_KEY
    }
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("imdb_id")
    else:
        return None

def collect_movies(genres, max_pages):
    """
    Percorre as páginas de /discover/movie até 'max_pages'.
    Retorna uma lista com os registros de filmes.
    Cada registro terá:
      - tmdb_id
      - title
      - release_date
      - genre_ids
      - imdb_id
      - popularity
      - original_language
    etc.
    """
    all_movies = []
    page = 1
    while page <= max_pages:
        data = discover_movies(genres, page)
        if not data:
            break

        results = data.get("results", [])
        total_pages = data.get("total_pages", 1)

        for movie in results:
            tmdb_id = movie["id"]
            imdb_id = get_movie_imdb_id(tmdb_id)  
            record = {
                "tmdb_id": tmdb_id,
                "title": movie.get("title"),
                "release_date": movie.get("release_date"),
                "genre_ids": movie.get("genre_ids"),
                "imdb_id": imdb_id,
                "popularity": movie.get("popularity"),
                "original_language": movie.get("original_language")
            }
            all_movies.append(record)

        print(f"[Filmes] Página {page}: {len(results)} registros coletados.")
        page += 1
        if page > total_pages:
            break

    print(f"[Filmes] Total coletado: {len(all_movies)}")
    return all_movies

def collect_tv_shows(genres, max_pages):
    """
    Percorre as páginas de /discover/tv até 'max_pages'.
    Retorna uma lista com os registros de séries.
    Cada registro terá:
      - tmdb_id
      - name (nome da série)
      - first_air_date
      - genre_ids
      - imdb_id (se existir)
      - popularity
      - original_language
    """
    all_tv = []
    page = 1
    while page <= max_pages:
        data = discover_tv(genres, page)
        if not data:
            break

        results = data.get("results", [])
        total_pages = data.get("total_pages", 1)

        for tv_show in results:
            tmdb_id = tv_show["id"]
            imdb_id = get_tv_imdb_id(tmdb_id)  # opcional
            record = {
                "tmdb_id": tmdb_id,
                "name": tv_show.get("name"),
                "first_air_date": tv_show.get("first_air_date"),
                "genre_ids": tv_show.get("genre_ids"),
                "imdb_id": imdb_id,
                "popularity": tv_show.get("popularity"),
                "original_language": tv_show.get("original_language")
            }
            all_tv.append(record)

        print(f"[Séries] Página {page}: {len(results)} registros coletados.")
        page += 1
        if page > total_pages:
            break

    print(f"[Séries] Total coletado: {len(all_tv)}")
    return all_tv

def main():
    # Sessão com credenciais definidas acima
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION
    )
    s3_client = session.client("s3")

    # 1) Coleta filmes
    movies_data = collect_movies(MOVIE_GENRES, MAX_PAGES_MOVIES)

    # 2) Coleta séries
    tv_data = collect_tv_shows(TV_GENRES, MAX_PAGES_TV)

    # 3) Gravar no S3
    now = datetime.utcnow()
    year, month, day = now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")

    # Salva filmes
    i = 1
    for chunk in chunker(movies_data, 100):
        file_name = f"movies_crime_war_part{i}.json"
        s3_key = f"Raw/TMDB/JSON/Filmes/{year}/{month}/{day}/{file_name}"
        body = json.dumps(chunk, indent=2, ensure_ascii=False)
        s3_client.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=body)
        i += 1

    # Salva séries
    j = 1
    for chunk in chunker(tv_data, 100):
        file_name = f"tv_crime_war_part{j}.json"
        s3_key = f"Raw/TMDB/JSON/Series/{year}/{month}/{day}/{file_name}"
        body = json.dumps(chunk, indent=2, ensure_ascii=False)
        s3_client.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=body)
        j += 1

    print("Processo concluído!")

if __name__ == "__main__":
    main()