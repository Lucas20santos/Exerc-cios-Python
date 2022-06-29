# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada 
# por aluno e apresentar:
# 
# * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# * A mensagem "Reprovado", se a média for menor do que sete;
# * A mensagem "Aprovado com Distinção", se a média for igual a dez.

# Primeira maneira

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno:: "))

media = (nota1 + nota2) / 2

#### Maneira 1
resultado = "Aprovado com Distinçaõ" if media == 10 else "Aprovado" if media >= 7 else "Reprovado"

print(f"A media foi {media} e o aluno está {resultado}!")

#### Maneira 2

if media == 10:
    resultado = "aprovado com Distinção"
elif media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"A media foi {media} e o aluno está {resultado}!")
