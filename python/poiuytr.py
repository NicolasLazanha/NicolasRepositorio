import tkinter as tk

botao = 0

textos = [
    "Ola.",
    "Meu nome e Nicolas.",
    "Tenho 14 anos.",
    "E é isso."
]

janela = tk.Tk()
janela.title("Minha apresentação")
janela.geometry("400x400")


def atualizar_texto():
    if botao < 0:
        titulo1.config(text="Não há nada antes do início")
    elif botao >= len(textos):
        titulo1.config(text="Não há mais textos.")
    else:
        titulo1.config(text=textos[botao])


def ir():
    global botao
    if botao < len(textos):
        botao += 1
    atualizar_texto()


def volta():
    global botao
    if botao > 0:
        botao -= 1
    atualizar_texto()


botao_ir = tk.Button(
    janela,
    text="Avançar",
    width=10,
    command=ir
)
botao_ir.pack(pady=20)

botao_volta = tk.Button(
    janela,
    text="Voltar",
    width=10,
    command=volta
)
botao_volta.pack(pady=20)

titulo1 = tk.Label(
    janela,
    text=textos[botao],
    font=("Arial", 16, "bold"),
    wraplength=350
)
titulo1.pack(pady=20)

janela.mainloop()