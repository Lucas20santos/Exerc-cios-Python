# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Operador Ternário
Maior = num1 if num1 > num2 else num2

print(f"O maior é: {Maior}")

if num1 > num2:
    print(f"O maior é: {num1}")
else:
    print(f"O maior é: {num2}")
