velocidade = int(input("Informe a velocidade: "))

# Uso do if no ternario
alerta = "Alta velocidade! Multado. " if velocidade > 60 else  "Dentro do limite de velocidade. "

#Exibição
print(alerta)