'''74 - Escreva um programa que, dado um número inteiro positivo, 
calcular e exibir a quantidade de números pares até o número digitado.'''

x = int(input("Digite um número inteiro: "))
count = 0

while x > 0:
    if x % 2 == 0:
        x -= 2
        count += 1
    else:
        x -= 1

print("Quantidade de números pares:", count)
