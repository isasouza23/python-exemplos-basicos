def verificar_credenciais(nome_usuario, senha):
    usuario_correto = "admin"
    senha_correta = "1234"
    
    if nome_usuario == usuario_correto and senha == senha_correta:
        return True
    else:
        return False

def main():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verifica as credenciais
    if verificar_credenciais(nome_usuario, senha):
        print("Sucesso!")
    else:
        print("Erro.")

if __name__ == "__main__":
    main()