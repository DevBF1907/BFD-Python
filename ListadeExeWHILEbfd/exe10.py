saldo = 500

while saldo > 0:
    compra = float(input("digite o valor da compra: "))

    if compra > saldo:
        print(f"tais liso ja saldo: {saldo} ")
        break
    else:
        saldo -= compra
        print(f"compra na saldo: {saldo} ")

