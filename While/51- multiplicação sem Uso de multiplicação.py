#51 – Multiplicação sem Uso de *:

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

soma = 0
cont = 1
while cont <= a:
    soma = soma + b
    cont = cont + 1

print("O produto de %d x %d é = %d" % (a, b, soma))
