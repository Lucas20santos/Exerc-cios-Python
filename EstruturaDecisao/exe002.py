# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Digite um número: "))


resultado = "positivo" if num > 0 else "negativo" if num < 0 else "nulo"

print(f"O número é: {resultado}")
