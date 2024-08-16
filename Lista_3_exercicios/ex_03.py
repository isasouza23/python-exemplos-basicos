# Solicita as 4 notas ao usuário
notas = []
for i in range(4):
    while True:
        nota = float(input(f"Digite a nota {i+1} (entre 0 e 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")

# Calcula a média
media = sum(notas) / len(notas)

# Exibe a média final
print(f"A média final é: {media:.2f}")
