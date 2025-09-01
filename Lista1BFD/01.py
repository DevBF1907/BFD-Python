vitorias = 0
empates = 0
derrotas = 0

for i in range(1, 6):
    gols_selecao = int(input(f"Gols da Seleção no jogo {i}: "))
    gols_adversario = int(input(f"Gols do adversário no jogo {i}: "))

    if gols_selecao > gols_adversario:
        vitorias += 1
    elif gols_selecao == gols_adversario:
        empates += 1
    else:
        derrotas += 1

print("=== Torneio de Futebol ===")
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
