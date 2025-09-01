import random


numero_secreto = random.randint(1, 20)


tentativas = 5

for i in range(tentativas):
    palpite = int(input("Adivinhe o número (1 a 20): "))

    if palpite == numero_secreto:
        print("Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")
else:
    print(f"Game over! O número era {numero_secreto}")
