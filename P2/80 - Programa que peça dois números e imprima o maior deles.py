'''80 - Faça um programa que peça dois números e imprima o maior deles. Caso forem iguais, o programa também deverá apontar.'''




maior = 0
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

if a >= b:
    maior = a
if a <= b:
    maior = b
if a == b:
    print("Os números são iguais")

print("O maior número é: {}".format(maior))
