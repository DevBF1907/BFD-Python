totalM = 0

for i in range(3):

   nota1 = int(input(f"\nDigite a primeira nota do aluno {i+1}:"))
   nota2 = int(input(f"Digite a segunda nota do aluno {i+1}: "))

   media = (nota1 + nota2) / 2
   print("\nmedia do aluno", media)

   totalM  += media


mediaTurma = totalM / 3

print("\nMédia da turma: ", mediaTurma)