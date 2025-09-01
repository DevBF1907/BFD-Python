for i in range(5):
    numb = int(input("Enter a number: "))

    if i == 0:
        maior = menor = numb
    else:
        if numb > maior:
            maior = numb
        if numb < menor:
            menor = numb



print("maior = ",maior,"menor = ", menor)
