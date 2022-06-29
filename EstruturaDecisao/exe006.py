# Faça um Programa que leia três números e mostre o maior deles.
#
# nesse exercício será pedido para o usuário digite três números inteiros não podendo ser de outra classes
# para isso usarei o try e exception

## Tratamento do dados

while True:
    try:
        n1 = int(input("Informe um número inteiro: "))
        break
    except:
        print("Digite novamente")
while True:
    try:
        n2 = int(input("Informe um número inteiro: "))
        break
    except:
        print("Digite novamente")
while True:
    try:
        n3 = int(input("Informe um número inteiro: "))
        break
    except:
        print("Digite novamente")


def Maior(*num):
    maior = num[0]
    for x in num:
        if x > maior:
            maior = x
    return maior

print(Maior(n1, n2, n3))
