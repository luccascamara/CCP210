d = 0
c = 0
while True:
    codigo = int(input("Digite o codigo: "))
    if codigo == 0:
        break
    if codigo == 1:
        d=d+1
    if codigo == 2:
        c=c+1
saldo=c-d
print("Total de débitos = ", d)
print("Total de créditos = ", c)
print("Saldo = ", saldo)