#14 - "Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor de E, conforme a fórmula a seguir:

#E = 1 + 1/1 + 1/2 + 1/3 + ... 1/N

N = int(input("Digite o valor de N: "))

cont = 1
soma = 1

while cont <= N:
    soma = soma + (1 / cont)
    cont = cont + 1

print("O valor de E = %.4f" % soma)
