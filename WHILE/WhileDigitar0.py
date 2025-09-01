numeros = int(input("quantos numeros voce quer digitar ?"))
soma = 0
c = 0
while c < numeros:

    numero = int(input("Digite um número e digite 0 para parar: "))

    if numero == 0:
        break
    else:
        soma += numero

    c += 1


print(f" soma final: {soma}")