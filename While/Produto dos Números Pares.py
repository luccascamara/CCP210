p = 1
while True:
    n = int(input("Digite um número inteiro positivo: "))
    if n == 0:
        break 
    if n%2 == 0:
        p=p*n
print("O produto dos números pares é: ", p)