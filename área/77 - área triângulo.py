'''77 - Escreva uma função que receba a base e a altura de um triângulo e retorne sua área A=base×altura/2'''


def a(base, altura):
    a = base * altura / 2
    print(a)

base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))
a(base, altura)

