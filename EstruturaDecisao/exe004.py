# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# Primeira maneira

vogais = ['a', 'e', 'i', 'o', 'u']

letra = str(input("Digite uma letra: ")).lower().strip()[0]

isVogal = "Sim" if letra in vogais else "Não"

print(f"A letra digitada é vogal: {isVogal}")

# Segunda maneira


