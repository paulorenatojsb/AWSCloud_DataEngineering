# README SPRINT 8 - 

---

## EXERCÍCIO 5 - TMDB (Copiado da Sprint 7)

### 1. Objetivos
- Criar um **processo de extração** de dados da **API do TMDB** usando **serviços da AWS**.

### 2. Atividades

#### 2.1. Etapa 2 - Testando as credenciais e a biblioteca
- Depois de obter sua **chave de API** do TMDB, faça **solicitações** à API no formato:
https://api.themoviedb.org/3/{endpoint}?api_key={SUA_CHAVE_DE_API}&{parametros_opcionais}

yaml
Copiar
- **endpoint**: por exemplo, `movie/{movie_id}`, `tv/{tv_id}`, etc.  
- **parametros_opcionais**: por ex. `language=pt-BR` para obter informações em português.

