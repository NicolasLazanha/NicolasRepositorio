import tkinter as tk
import random
# Dados do jogador
jogador = {
    "nome": "Nicolas",
    "vida_max": 100,
    "vida": 100,
    "ataque": 20,
    "nivel": 1,
    "xp": 0,
}
# Dados iniciais do monstro
monstro = {
    "nome": "Goblin",
    "vida_max": 100,
    "vida": 100,
    "ataque": 25,
    "nivel": 1,
}
# Função para atualizar barras gráficas de vida e textos
def atualizar():
    texto_jogador.config(
        text=f"{jogador['nome']} (Nível {jogador['nivel']}) - Vida: {jogador['vida']}/{jogador['vida_max']}"
    )
    texto_monstro.config(
        text=f"{monstro['nome']} (Nível {monstro['nivel']}) - Vida: {monstro['vida']}/{monstro['vida_max']}"
    )
    barra_vida_jogador['value'] = jogador['vida']
    barra_vida_monstro['value'] = monstro['vida']
def fim_batalha(vencedor):
    if vencedor == "jogador":
        texto_mensagem.config(text="Você venceu! Parabéns!", bg="green", fg="white")
        ganhxp = random.randint(10, 20)
        jogador['xp'] += ganhxp
        texto_mensagem.config(text=f"Você venceu! Ganhou {ganhxp} XP!", bg="green", fg="white")
        checar_nivel()
    elif vencedor == "monstro":
        texto_mensagem.config(text="Você perdeu! Tente novamente.", bg="red", fg="white")
    else:
        texto_mensagem.config(text="Você fugiu da batalha.", bg="gray", fg="black")
    botao_atacar.config(state="disabled")
    botao_fugir.config(state="disabled")
    botao_reiniciar.pack(pady=10)
def checar_nivel():
    # Exemplo simples: a cada 50 XP, sobe um nível, aumenta vida e ataque
    while jogador['xp'] >= 50:
        jogador['nivel'] += 1
        jogador['xp'] -= 50
        jogador['vida_max'] += 20
        jogador['ataque'] += 5
        jogador['vida'] = jogador['vida_max']  # cura ao subir nível
        texto_mensagem.config(text=f"Você subiu para o nível {jogador['nivel']}! Vida e ataque aumentaram!", bg="blue", fg="white")
def atacar():
    if jogador["vida"] <= 0 or monstro["vida"] <= 0:
        return
    # Chance de acerto (85%)
    if random.random() > 0.85:
        mensagem = "Você errou o ataque!"
    else:
        dano = random.randint(5, jogador["ataque"])
        # Chance de crítico 20%
        if random.random() < 0.2:
            dano *= 2
            critico = True
        else:
            critico = False
        monstro["vida"] -= dano
        monstro["vida"] = max(monstro["vida"], 0)
        mensagem = f"Você causou {dano} de dano!" + (" CRÍTICO!" if critico else "")
    if monstro["vida"] > 0:
        # Monstro responde ataque
        if random.random() > 0.85:  # monstro erra ataque
            mensagem += "\nO monstro errou o ataque!"
        else:
            dano_monstro = random.randint(5, monstro["ataque"])
            jogador["vida"] -= dano_monstro
            jogador["vida"] = max(jogador["vida"], 0)
            mensagem += f"\nO monstro causou {dano_monstro} de dano."
    if jogador["vida"] <= 0:
        fim_batalha("monstro")
    elif monstro["vida"] <= 0:
        fim_batalha("jogador")
    texto_mensagem.config(text=mensagem)
    atualizar()
def fugir():
    fim_batalha("fugiu")
def reiniciar():
    jogador['vida'] = jogador['vida_max']
    monstro['vida'] = monstro['vida_max']
    texto_mensagem.config(text="Um Goblin apareceu!", bg="SystemButtonFace", fg="black")
    botao_atacar.config(state="normal")
    botao_fugir.config(state="normal")
    botao_reiniciar.pack_forget()
    atualizar()
# Interface gráfica
janela = tk.Tk()
janela.title("Meu RPG")
janela.geometry("400x400")
titulo = tk.Label(janela, text="Batalha RPG", font=("Arial", 20))
titulo.pack(pady=15)
# Barras de vida gráficas
from tkinter import ttk
barra_vida_jogador = ttk.Progressbar(janela, length=300, maximum=jogador['vida_max'])
barra_vida_jogador.pack(pady=5)
texto_jogador = tk.Label(janela)
texto_jogador.pack(pady=5)
barra_vida_monstro = ttk.Progressbar(janela, length=300, maximum=monstro['vida_max'])
barra_vida_monstro.pack(pady=5)
texto_monstro = tk.Label(janela)
texto_monstro.pack(pady=5)
texto_mensagem = tk.Label(janela, text="Um Goblin apareceu", font=("Arial", 11))
texto_mensagem.pack(pady=20)
botao_atacar = tk.Button(janela, text="Atacar", bg="blue", fg="white", command=atacar)
botao_atacar.pack(pady=5)
botao_fugir = tk.Button(janela, text="Fugir", bg="blue", fg="white", command=fugir)
botao_fugir.pack(pady=5)
botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", bg="green", fg="white", command=reiniciar)
atualizar()
janela.mainloop()