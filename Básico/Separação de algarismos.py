n = int(input("Digite um número inteiro de 4 algarismos: "))
m=n//1000
rm=n%1000
c=rm//100
rc=rm%100
d=rc//10
u=rc%10
print("Milhar: ", m)
print("Centena: ", c)
print("Dezena: ", d)
print("Unidade: ", u)
