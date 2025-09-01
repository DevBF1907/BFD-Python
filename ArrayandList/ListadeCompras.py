compras = []

while True:

    compra = input("Compras: ")

    if compra.lower() == "sair":
        break
    else:
        compras.append(compra)




print(compras)