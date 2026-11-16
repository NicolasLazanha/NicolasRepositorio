import tkinter as tk


botao = 0
text = [
    "    Ola.   ",
    "Meu nome\né Nicolas.",
    "Tenho\n 14 anos.",
    "E é isso."
]

janela = tk.Tk()
janela.title("apresentação")
janela.geometry("400x400")

def atualizar_texto():
    titulo1.config(text=text[botao])

def ir():
    global botao
    if botao < len(text):
        botao += 1
        atualizar_texto()
def volta():
    global botao
    if botao > 0:
        botao -= 1
        atualizar_texto()

botao_ir = tk.Button(
    janela, bg="blue", fg="white", text="avançar", width=10,
    command= ir,
    font=("Arial", 16, "bold")
)
botao_ir.pack(pady=40)
botao_ir.place(x= 230, y=300)



botao_volta = tk.Button(
    janela, bg="blue", fg="white", text="voltar", width=10,
    command= volta,
    font=("Arial", 16, "bold")
)
botao_volta.pack(pady=20)
botao_volta.place(x= 30, y=300)


titulo1 = tk.Label(
    janela,
    text=text[botao],
    font=("Arial", 32, "bold")
)
titulo1.pack(pady=20)
titulo1.place(x=100, y=100)

janela.mainloop()
