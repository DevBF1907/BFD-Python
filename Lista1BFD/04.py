print("== Quiz de Conhecimentos Gerais ==")
pontuacao = 0


print("1) Capital do Brasil?")
print("1- São Paulo  2- Brasília  3- Rio de Janeiro")
resp = int(input("Sua resposta: "))
if resp == 2:
    pontuacao += 1


print("2) Planeta conhecido como planeta vermelho?")
print("1- Marte  2- Júpiter  3- Vênus")
resp = int(input("Sua resposta: "))
if resp == 1:
    pontuacao += 1


print("3) Quem escreveu Dom Quixote?")
print("1- Machado de Assis  2- Cervantes  3- Shakespeare")
resp = int(input("Sua resposta: "))
if resp == 2:
    pontuacao += 1


print("4) Qual o maior oceano?")
print("1- Atlântico  2- Pacífico  3- Índico")
resp = int(input("Sua resposta: "))
if resp == 2:
    pontuacao += 1


print("5) Qual a cor da clorofila?")
print("1- Verde  2- Azul  3- Amarela")
resp = int(input("Sua resposta: "))
if resp == 1:
    pontuacao += 1


print(f"Pontuação final: {pontuacao}/5")

if pontuacao == 5:
    print("Gênio!")
elif 3 <= pontuacao <= 4:
    print("Mandou bem!")
elif 1 <= pontuacao <= 2:
    print("Precisa estudar mais")
else:
    print("Zerou o quiz")
