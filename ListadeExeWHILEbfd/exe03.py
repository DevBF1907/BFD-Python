


while True:
    v1 = float(input("valor 1: "))
    v2 = float(input("valor 2: "))

    if v2 == 0:
        print("Erro: digite número diferente de 0")
    else:
        div = v1 / v2
        print(f"O resultado da divisão é: {div} ")


    resp = input("Quer continuar? [S/N] ")
    if  resp.lower() == "n":
        break





