import hashlib

while True:
    user_input = input("Digite uma string para mascarar (ou 'sair' para encerrar): ")
    if user_input.lower() == "sair":
        print("Encerrando...")
        break
    sha1_hash = hashlib.sha1(user_input.encode()).hexdigest()
    print(f"Hash SHA-1: {sha1_hash}")