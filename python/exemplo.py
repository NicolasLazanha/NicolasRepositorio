class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def apresentar(self):
        print(f"meu nome é {self.nome}")
        print(f"tenho {self.vida} de vida")

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome}!")
        alvo.vida -= self.ataque
        print(f"{alvo.nome} perdeu {self.ataque} de vida")
        self.vida -= alvo.ataque
        print(f"{self.nome} perdeu {alvo.ataque} de vida")

    def curar(self):
        self.vida += 20
        print(f"{self.nome} recuperou 20 de vida")

    def status(self):
        print(f"nome: {self.nome}")
        print(f"vida: {self.vida}")
        print(f"ataque: {self.ataque}")


        
    


jogador = Personagem("Exu", 100, 20)
monstro = Personagem("Goblin", 60, 10)
dragao = Personagem("Dragão", 200, 30)

jogador.apresentar()
monstro.apresentar()

while monstro.vida >= 1:
    acao = int(input("1 = atacar, 2 = curar, 3 = status: "))
    if acao == 1:
        jogador.atacar(monstro)

        print(f"exu esta com {jogador.vida}")
        print(f"goblin esta com {monstro.vida}")
    elif acao == 2:

        jogador.curar()

        print(f"exu se curou e esta com {jogador.vida}")

    else:
        jogador.status()

print("\nvoce venceu o goblin, e aparece um dragao!")

if monstro.vida <= 0:
    while dragao.vida >= 1:
        acao = int(input("1 = atacar, 2 = curar, 3 = status: "))
        if acao == 1:
            jogador.atacar(dragao)

            print(f"exu esta com {jogador.vida}")
            print(f"dragao2 esta com {dragao.vida}")
        elif acao == 2:

            jogador.curar()

            print(f"exu se curou e esta com {jogador.vida}")

        else:
            jogador.status()







