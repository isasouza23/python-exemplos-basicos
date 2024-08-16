# Reset contador e limite de tentativas
i = 1
while i <= 3:
    user = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    # Checagem
    if user != "Gisele" and senha != "1234":
        i += 1
        print("Usuário ou Senha incorretos!")
        print(" ")
    else:
        print(" ")
        print(f"Bem-vindo, {user}!")
        break # encerra ao inserir senha correta
else:
    print(f"Você excedeu todas as: {i-1} tentativas!!")