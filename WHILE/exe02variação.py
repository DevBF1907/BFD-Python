v1 = float(input("valor 1: "))
v2 = float(input("valor 2: "))

while v2 == 0:
    print("Error: o valor da segunda variavel não pode ser  0")
    v2 = float(input("valor 2: "))


div = v1 / v2

print(f"O resultado da divisão é: {div}")
