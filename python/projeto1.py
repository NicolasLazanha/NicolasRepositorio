import tkinter as tk
import random
jogador = {
    "nome": "nicolas",
    "vida": 100,
    'ataque': 20
    }

monstro = {
    "nome": "Goblin",
    "vida": 50,
    'ataque': 10
    }

def atualizar():
    texto_jogador.config(
        text=f"vida de {jogador['nome']}: {jogador["vida"]}"
    )
    texto_monstro.config(
        text=f"vida de {monstro['nome']}: {monstro["vida"]}"
    )


def atacar():

    if jogador["vida"] <= 0 or monstro["vida"] <=0:
        return

    dano = random.randint(5, jogador["ataque"])
    monstro["vida"] -= dano

    mensagem = f"voce causou {dano} de dano!"

    if monstro["vida"] > 0:

        dano_monstro = random.randint(1, monstro["ataque"])
        jogador["vida"] -= dano_monstro

    mensagem += f"\nO monstro causou {dano_monstro} de dano"

    if jogador["vida"] <= 0:
        mensagem = "voce perdeu"

    elif monstro["vida"] <= 0:
        mensagem = "voce venceu"

    texto_mensagem.config(text=mensagem)

    atualizar()

def fugir():
    texto_mensagem.config(text="voce fugiu da batalha")


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
    text="atacar",
    command=atacar
)
botao_atacar.pack(pady=5)

botao_fugir = tk.Button(
    janela,
    text="fugir",
    command=fugir
)
botao_fugir.pack(pady=5)

atualizar()

janela.mainloop()

