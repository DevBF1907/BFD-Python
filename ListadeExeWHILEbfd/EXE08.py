
quantidadenotas = 0
totalnotas = 0
while True:
    notas = float(input("digite a nota e -1 para sair: "))

    if notas == -1:
        break
    else:
        totalnotas += notas
        quantidadenotas += 1


media = totalnotas / quantidadenotas
print(media)