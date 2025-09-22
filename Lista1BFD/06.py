
nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    situacao = "APROVADO!"
elif 5 <= nota < 7:
    situacao = "em REPOSIÇÃO!"
else:
    situacao = "REPROVADO!"


print(f"{nome} está {situacao}")
