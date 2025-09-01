alu = int(input("\n Quantos alunos? "))
c = 0
nota = 0
while c < alu:
    nota = nota + float(input(f"\n Nota do aluno {c+1}: "))
    c += 1

media = nota / alu
print(media)

