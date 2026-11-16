#funcao para perguntar qual calculo quer fazer  (escolhe o calculo)
#escolha os numeros.
#printar o resultado


def escolha():
    
    escolha = input("qual operação voce quer fazer?\n a = adicao\n s = subtracao\n d = divisao\n m (qualquer outra letra) = multiplicacao\n")
    h = float(input("insira o numero h: "))
    b = float(input("insira o numero b: "))


    if escolha == 'a':
        print(soma(h, b))

    elif escolha == 's':
        print(subtracao(h, b))

    elif escolha == 'd':
        print(divisa(h, b))

    else:
        print(vezes(h, b))



def soma(h, b):
    return(h+ b)

print(soma)




def subtracao(h, b):
    return(h- b)

print(subtracao)




def vezes(h, b):
    return(h* b)

print(vezes)




def divisa(h, b):
    return(h/ b)

print(divisa)

escolha()