# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite uma letra: ").upper().strip()[0]

resultado = "Masculino" if letra == "M" else "Feminino"

print(f"{letra} - {resultado}")
