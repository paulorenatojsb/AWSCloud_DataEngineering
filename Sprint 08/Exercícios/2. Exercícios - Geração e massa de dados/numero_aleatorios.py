import random

def etapa1():
    # Define uma semente para manter resultados reproduzíveis (opcional)
    random.seed(40)
    
    # Gera uma lista com 250 inteiros aleatórios entre 0 e 100
    lista_inteiros = [random.randint(0, 100) for _ in range(250)]
    
    print("Lista original:")
    print(lista_inteiros)
    
    # Inverte a lista
    lista_inteiros.reverse()
    
    print("\nLista invertida:")
    print(lista_inteiros)

if __name__ == "__main__":
    etapa1()