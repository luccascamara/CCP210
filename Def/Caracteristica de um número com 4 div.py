def caracteristica(y):
    resto=y%100 
    t=y//100 
    d=resto+t
    if ((d**2)==y):
        a=1
    else:
        a=0
    return a
x = int(input("Digite um número de 4 digitos: "))
while x < 1000 or x > 9999:
    print("Número errado!")
    x = int(input("Digite um número de 4 digitos: "))
a=caracteristica(x)
print(a)
