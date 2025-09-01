numeros = [3,5,6,7,8,0]


print("Tamanho: ",len(numeros))
print("Soma: ", sum(numeros))
print("Maior: ", max(numeros))
print("Menor: ", min(numeros))
print("Ordenado: ", sorted(numeros))

numeros.append(10)
print("Lista de numeros ", numeros)


numeros = []

# Adicionando 5 números com append
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# Mostrando a lista original
print("\n📋 Lista original:", numeros)

# ➕ Usando insert (insere 999 na posição 2)
numeros.insert(2, 999)
print("Após insert(2, 999):", numeros)

# ➖ Usando remove (remove o número 999)
numeros.remove(999)
print("Após remove(999):", numeros)

# ❌ Usando pop (remove o último item)
ultimo = numeros.pop()
print("Após pop():", numeros)
print("Número removido com pop():", ultimo)

# 🔢 Maior e menor número
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

# 🔄 Ordenando com sort()
numeros.sort()
print("Após sort():", numeros)

# 🔁 Invertendo com reverse()
numeros.reverse()
print("Após reverse():", numeros)

# ➕ Soma dos elementos
print("Soma dos números:", sum(numeros))

# 📏 Tamanho da lista
print("Tamanho da lista:", len(numeros))

# 🔍 Verificando se um número está na lista
valor = int(input("\nDigite um número para verificar se está na lista: "))
if valor in numeros:
    print(f"O número {valor} está na lista!")
else:
    print(f"O número {valor} NÃO está na lista!")