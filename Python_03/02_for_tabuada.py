# Tabuada

while True:
    print("")
    num = int(input("Informe um número: "))
    print("")
    print(f"Tabuada do {num} ")


    # Gerar Tabuada usando laço for 
    for i in range (1, 11):
        result = num * i
        print(f"{num} * {i} = {result}")
        i += 1

    # Perguta se quer continuar
    continuar = input("\nDeseja calcular outra tabuada (s/n): ?")
    if continuar.lower() != 's':
        print("Encerrando o programa.")
        break