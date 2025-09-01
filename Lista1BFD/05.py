
pontuacoes = [0, 0, 0]


for avaliador in range(1, 4):
    for candidato in range(3):
        nota = int(input(f"Nota do avaliador {avaliador} para o candidato {candidato + 1}: "))
        pontuacoes[candidato] += nota


print("Pontuação final:")
for i, pontos in enumerate(pontuacoes, start=1):
    print(f"Candidato {i}: {pontos}")


max_pontos = max(pontuacoes)

if pontuacoes.count(max_pontos) > 1:
    print("Empate! Disputa acirrada")
else:
    vencedor = pontuacoes.index(max_pontos) + 1
    print(f"Candidato {vencedor} é o campeão!")
