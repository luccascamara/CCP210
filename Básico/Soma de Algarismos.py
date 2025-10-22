n = int(input("Digite um número de 3 algarimos: "))
c=n//100
resto=n%100
d=resto//10
u=resto%10
soma=c+d+u
print("Soma = ",soma)