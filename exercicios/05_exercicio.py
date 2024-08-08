
# Valores
print("Insira os valore.")
Produto = float(input("Insira o valor do Produto: "))
Comissao = float(input("Insira a porcentagem da comissão: "))

# Calculo
Comissão = (Produto * (Comissao / 100))

# Final
print(f"A sua Comissão é de R${Comissão}")