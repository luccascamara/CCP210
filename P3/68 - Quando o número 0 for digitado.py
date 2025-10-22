'''68 - Escreva um programa que leia números digitados pelo usuário. 
O programa deve ler os números até que 0 (zero) seja digitado. Quando o número 0 for digitado, o programa deve exibir:
- A quantidade de números que foram digitados;
- A somatória destes números;
- A média aritmética.'''


soma = 0
k = 0

while True:
    n = float(input("Digite um número: "))
    if n == 0:
        break
    soma = soma + n
    k = k + 1

media = soma / k

print("Média: %.2f" % media)
print("Soma:", soma)
print("Quantidade de números:", k)
