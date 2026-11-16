import random

opcoes = ["pedra", "papel", "tesoura"]


while True:
    print("/=n === PEDRA, PAPEL E TESOURA ===")
    placar_jogador = 0 
    placar_computador = 0 

    for rodada in range(1, 4):
        print(f"/n --- rodada {rodada} ---")
        jogador = input("escolha pedra, papel ou tesoura:").lower()

        if jogador not in opcoes:
            print("escolha invalida")
            continue

        computador = random.choice(opcoes)
        print(f"o computador escolheu: {computador}")
        print(f"voce escolheu: {jogador}")

        if jogador == computador:
            print('empate')

        elif (
            (jogador == "pedra" and computador == "tesoura") or
            (jogador == "papel" and computador == "pedra") or
            (jogador == "tesoura" and computador == "papel")
        ):
            print("você venceu a rodada")
            placar_jogador += 1

        else:
            print("o computador venceu a rodada")
            placar_computador += 1

        print(f"Placar: Você {placar_jogador} x {placar_computador} Computador")

    print("/n=== FIM DO  JOGO ===")

    if placar_jogador > placar_computador:
        print ("Você ganhou!!")

    elif placar_computador > placar_jogador:
        print ("Vitoria do computador!!")

    else:
        print("Empate.")

        jogar_novamente = input("/nQuer jogar novamente? (sim/não): ").lower()

    if jogar_novamente != "sim":
        print("Obrigado por jogar!")
        break

