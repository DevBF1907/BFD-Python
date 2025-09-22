def soma(*numeros):
    return sum(numeros)

def som(*numeros):
    c = 0
    for n in numeros:
        c += n
    return c



def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
       return "Error: Não pode dividir por zero"
    else:
        return a / b