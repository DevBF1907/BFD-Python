numeros=[]

for i in range(3):
    numero = int(input(f"digite o numero {i+1}: "))
    numeros.append(numero)

print("lista de numeros ", numeros)
print("a soma dos numeros: ", sum(numeros))