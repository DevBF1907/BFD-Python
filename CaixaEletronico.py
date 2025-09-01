dindin = int(input("Quanto de dinheiros vc tem ? "))

while True:

    print("\nSacar R$ 100,00 = 1 "
          "\nSacar R$ 50,00 = 2 "
          "\nSacar R$ 20,00 = 3 "
          "\nSacar R$ 10,00 = 4 "
          "\nFinalizar = 5 ")
    op = int(input("\nEscolha a opção "))

    match op:
        case 1:

            if dindin >= 100:
                dindin -= 100
                print("Seu Saldo R$ ", dindin)
            else:
                print("Quem ta liso dorme")

        case 2:

            if dindin >= 50:
                dindin -= 50
                print("Seu Saldo R$ ", dindin)
            else:
                print("Quem ta liso dorme")

        case 3:

            if dindin >= 20:
                dindin -= 20
                print("Seu saldo R$ ", dindin)
            else:
                print("Quem ta liso dorme")

        case 4:

            if dindin > 10:
                saldo = dindin - 10
                print("Seu saldo R$ ", dindin)
            else:
                print("Quem ta liso dorme")

        case 5:
          print("Evitando Gastos Saldo: ", dindin)
          break
