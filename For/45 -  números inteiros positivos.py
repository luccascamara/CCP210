#45 – Números inteiros Positivos de uma série for:

cont = 0
quant = int(input("Entre com a quantidade de número: "))
for i in range(1, quant + 1):
    n = int(input("Entre um número positivo: "))
    if n % 2 == 1:
        cont = cont + 1

p = (cont / quant) * 100
print("porcentagem de números ímpares = %.2f" % p, "%")
