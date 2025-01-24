def etapa2():
    # Lista de animais
    animais = [
        "cachorro", "gato", "elefante", "girafa", "leopardo",
        "tigre", "zebra", "rinoceronte", "cavalo", "porco",
        "ovelha", "baleia", "golfinho", "macaco", "coelho",
        "pato", "galinha", "urso", "raposa", "canguru"
    ]
    
    # Ordena a lista em ordem alfabética
    animais.sort()

    # Imprime os animais em ordem crescente
    for animal in animais:
        print(animal)

    # Caminho completo onde você quer salvar o arquivo:
    caminho_arquivo = r"C:\Users\Administrador\.vscode\CompassAcademy-1\CompassAcademy\Sprint 08\Exercícios\2. Exercícios - Geração e massa de dados\animais.txt"

    # Cria o arquivo e salva os animais (um por linha)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        for animal in animais:
            f.write(animal + "\n")

if __name__ == "__main__":
    etapa2()