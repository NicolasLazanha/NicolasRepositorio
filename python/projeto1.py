import tkinter as tk
import random
from tkinter import ttk


jogador = {
    "nome": "nicolas",
    "vida": 100,
    'ataque': 20
    }


monstro = {
    "nome": "Goblin",
    "vida": 100,
    'ataque': 25
    }


def atualizar():
    texto_jogador.config(
        text=f"vida de {jogador['nome']}: {jogador['vida']}"
    )
    texto_monstro.config(
        text=f"vida de {monstro['nome']}: {monstro['vida']}"
    )

    barra_vida_P['value'] = jogador["vida"]
    barra_vida_M['value'] = monstro["vida"]
def atacar():

    if jogador["vida"] <= 0 or monstro["vida"] <=0:
        return

    dano = random.randint(5, jogador["ataque"])
    monstro["vida"] -= dano
    if dano > 17:
        mensagem =f"critico! voce causou {dano} de dano!"
    elif dano < 7:
        mensagem = f"droga! voce causou {dano} de dano!"
    else:
        mensagem = f"voce causou {dano} de dano!"

    if monstro["vida"] > 0:

        dano_monstro = random.randint(5, monstro["ataque"])
        jogador["vida"] -= dano_monstro

        mensagem += f"\nO monstro causou {dano_monstro} de dano"

    if jogador["vida"] <= 0:
        mensagem = "voce perdeu"
        texto_mensagem.config(bg="red", fg="white")

    elif monstro["vida"] <= 0:
        mensagem = "voce venceu"
        texto_mensagem.config(bg="green", fg="white")

    texto_mensagem.config(text=mensagem)

    atualizar()

def fugir():
    texto_mensagem.config(text="voce fugiu da batalha")
    texto_mensagem.config(bg="gray")


janela = tk.Tk()
janela.title("meu rpg")
janela.geometry("350x350")

titulo = tk.Label(
    janela,
    text="batalha rpg",
    font=("arial", 20)
)

titulo.pack(pady=15)

texto_jogador = tk.Label(janela)
texto_jogador.pack(pady=20)

texto_monstro = tk.Label(janela)
texto_monstro.pack(pady=10)

texto_mensagem = tk.Label(
    janela,
    text="um gobllin apareceu",
    font=("Arial", 11)
)
texto_mensagem.pack(pady=20)

botao_atacar = tk.Button(
    janela,
    text="atacar", bg="blue", fg="white",
    command=atacar
)
botao_atacar.pack(pady=5)

botao_fugir = tk.Button(
    janela,
    text="fugir", bg="blue", fg="white",
    command=fugir
)
botao_fugir.pack(pady=5)


barra_vida_P = ttk.Progressbar(janela, length=300, maximum=jogador['vida'],)
barra_vida_P.place(x=120, y=80)


barra_vida_M = ttk.Progressbar(janela, length=300, maximum=monstro['vida'],)
barra_vida_M.pack(pady=5)




atualizar()

janela.mainloop()

