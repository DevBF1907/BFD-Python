numb = int(input("Digite um número: "))


if numb == 0:
    print("Não pode digitar o número 0")
else:
    if numb > 0:
        print("Número é positivo")
    else:
        print("Número é negativo")
    if numb % 2 == 0:
        print("Numero par")
    else:
        print("Numero impar")

