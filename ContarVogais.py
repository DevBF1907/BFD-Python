frase = input("\nDigite uma frase: ")

vogais = "aeiouAEIOU"

cont = 0

for i in frase:
    if i in vogais:
        cont += 1



print("\nTotal de vogais:", cont)


