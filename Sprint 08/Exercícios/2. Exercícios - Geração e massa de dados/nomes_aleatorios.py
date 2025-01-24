import random
import names
import os

def etapa3():
    # Definições iniciais:
    random.seed(40)
    qtd_nomes_unicos = 3000
    qtd_nomes_aleatorios = 100000

    # Gera nomes únicos
    aux = []
    for _ in range(qtd_nomes_unicos):
        aux.append(names.get_full_name())

    # Gera lista final de nomes
    dados = []
    for _ in range(qtd_nomes_aleatorios):
        dados.append(random.choice(aux))

    # Caminho completo onde você quer salvar o arquivo
    caminho_arquivo = r"C:\Users\Administrador\.vscode\CompassAcademy-1\CompassAcademy\Sprint 08\Exercícios\2. Exercícios - Geração e massa de dados\names_aleatorios.txt"
    
    # Garante que o diretório existe (opcional, mas recomendado)
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

    # Escreve os dados no arquivo
    print(f"Gravando {qtd_nomes_aleatorios} nomes em {caminho_arquivo}...")
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        for nome in dados:
            f.write(nome + "\n")

    print("Processo concluido.")

if __name__ == "__main__":
    etapa3()