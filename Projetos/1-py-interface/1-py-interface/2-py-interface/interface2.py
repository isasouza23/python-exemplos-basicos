import tkinter as tk
from tkinter import ttk

# Função para atualizar (nome e escolhas do usuário)
def atualizar_resultado():
    # Obter nome usuário
    nome = caixa_texto.get()

    # Obter preferencia
    preferencia = var_radio.get()

    # Verifivcar tipo de saudação marcada "checkBox"
    if var_check_saudacao.get():
        saudacao = "Olá"
    else:
        saudacao = "Bem-vindo!"

    # Formal
    if var_check_personalizada.get():
        saudacao = f"{saudacao}, caro(a)"
    
    # Obter cor favorita selecionada
    cor_favorita = combo_cor.get()

    # Montar a mensagem final
    mensagem = f"{saudacao} {nome}! Você preferer{preferencia}."
    if cor_favorita:
        mensagem += f"Sua cor favorita é: {cor_favorita}."
    
    # Atuallizar o texto do rotulo com a mensagem
    label_resultado.config(text=mensagem)

def limpar_campos():
    # Limpa todos os campos
    caixa_texto.delete(0, tk.END)
    var_radio.set("Café")
    var_check_saudacao.set(False)
    var_check_personalizada.set(False)
    combo_cor.set("")
    label_resultado.config(text="")

janela = tk.Tk()
janela.title("Interface Avançada")
janela.geometry("400x500")

label_nome = tk.Label(janela, text="Digite seu nome: ")
label_nome.pack(pady=5)
caixa_texto = tk.Entry(janela, width=40)
caixa_texto.pack(pady=5)

label_preferencia = tk.Label(janela, text="Digite sua preferência: ")
label_preferencia.pack(pady=5)
var_radio = tk.StringVar(value="Café")
radio_cafe = tk.Radiobutton(janela, text="Café", variable=var_radio,
                            value="Café")
radio_cha = tk.Radiobutton(janela, text="Chá", variable=var_radio,
                            value="Chá")
radio_suco = tk.Radiobutton(janela, text="Suco", variable=var_radio,
                            value="Suco")
radio_agua = tk.Radiobutton(janela, text="Água", variable=var_radio,
                            value="Agua")
radio_cafe.pack()
radio_cha.pack()
radio_suco.pack()
radio_agua.pack()

var_check_saudacao = tk.BooleanVar()
check_saudacao = tk.Checkbutton(janela, text= "Usar saudação informal",
                                variable= var_check_saudacao)
check_saudacao.pack(pady=5)

var_check_personalizada = tk.BooleanVar()
check_personalizada = tk.Checkbutton(janela, text= "Usar saudação personalizada",
                                     variable= var_check_personalizada)
check_personalizada.pack(pady=5)

label_cor = tk.Label(janela, text="Digite sua cor favorita: ")
label_cor.pack(pady=5)
combo_cor = ttk.Combobox(janela, values=["Vermelho", "Azul", "Verde", "Preto"])
combo_cor.pack(pady=5)

botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_resultado)
botao_atualizar.pack(pady=10)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar_campos)
botao_limpar.pack(pady=10)

# Criar um rótulo para mostrar o resultado "label"
label_resultado = tk.Label(janela, text="", wraplength=350)
label_resultado.pack(pady=10)

janela.mainloop()