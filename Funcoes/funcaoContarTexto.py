

def contarTexto(texto):
    vogais = "aeiouAEIOU"
    cont = 0

    for c in texto:
        if c in vogais:
            cont += 1
    return print(f"Contei {cont} vogais")

def contarPalavras(texto):
        palavras = texto.split()
        print(f"As palavras são: {palavras}")
        print(f"Quantidade: {len(palavras)}")




