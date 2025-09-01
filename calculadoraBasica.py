try:
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))

    print("\nSOMA = 1"
      "\nSUBTRAÇÃO = 2"
      "\nMULTIPLICAÇÃO = 3"
      "\nDIVISÃO = 4\n")

    ope = int(input("ESCOLHA DENTRE ESSAS OPÇÕES: "))


    match ope:
        case 1:
            print(n1 + n2)
        case 2:
            print(n1 - n2)
        case 3:
            print(n1 * n2)
        case 4:
            if n2!=0:
                print(n1 / n2)
            else:
                print("Não pode dividir por zero")
except ValueError:
        print("Erro: Digite apenas números")
