x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))
soma=0
for k in range (1,n+1):
    numerador=x**(2*k)
    denominador=2*k
    soma=soma+(numerador/denominador)
print("A soma das parcelas é ", soma)