import random

numeroSecreto = random.randint(1,10)
tentativas = 0
while True:
        numero = int(input("digite um numero: "))
        tentativas += 1
        if numero == numeroSecreto:
            print(f"Parabéns vc acertou o número secreto {numero } em {tentativas} tentativas " )
            break
        elif numero < numeroSecreto:
            print("Número secreto é maior")
        else:
            print("Número secreto é menor")