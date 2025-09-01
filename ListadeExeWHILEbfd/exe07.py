contPares = 0
contImpares = 0

while True:
    numero = int(input("digite um numero e digite -1 para parar: "))

    if numero == -1:
        break
    elif numero % 2 == 0:
        contPares += 1
    else:
        contImpares += 1

print(f"Números pares: {contPares} Números impare : {contImpares}")