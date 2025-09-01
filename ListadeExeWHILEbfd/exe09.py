
totalcompra = 0
while True:
    produto = float(input("digite o valor do item  e 0 para sair: "))

    if produto == 0:
        break
    else:
        totalcompra += produto


print(f"voce gastou R${totalcompra:.2f}")