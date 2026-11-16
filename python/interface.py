import tkinter as tk



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

def fazer_soma():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = soma(n1, n2)

    resultado.config(text="resultado: " + str(valor))

def fazer_subtracao():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = subtracao(n1, n2)

    resultado.config(text="resultado: " + str(valor))

def fazer_multiplicacao():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = vezes(n1, n2)

    resultado.config(text="resultado: " + str(valor))

def fazer_divisao():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = divisa(n1, n2)

    resultado.config(text="resultado: " + str(valor))


janela = tk.Tk()

janela.config(bg="gray")

janela.title("Calculadora")

tk.Label(janela, bg="gray", fg="white", text="primeiro numero").pack()
numero1 = tk.Entry(janela)
numero1.pack()

tk.Label(janela, bg="gray", fg="white", text="segundo numero").pack()
numero2 = tk.Entry(janela)
numero2.pack()

tk.Button(janela, text="soma" , bg="blue", fg="white", command=fazer_soma).pack()
tk.Button(janela, text="subtracao" , bg="blue", fg="white",  command=fazer_subtracao).pack()
tk.Button(janela, text="multiplicacao" , bg="blue", fg="white", command=fazer_multiplicacao).pack()
tk.Button(janela, text="divisao" , bg="blue", fg="white", command=fazer_divisao).pack()

resultado = tk.Label(janela, bg="gray", text="resultado")
resultado.pack(padx=75, pady=50)
janela.mainloop()

