#Dado um número inteiro positivo n, calcular e exibir o valor da soma S dos n primeiros termos da série:

#S = 2 + 4/3 + 6/5 + 8/7 + ...

#Para n = 3

#S= 2 + 4/3 + 6/5 = 4.53

#Para n = 4

#S = 2 + 4/3 + 6/5 + 8/7 = 5.68

#O programa não pode permitir a entrada de dados inválidos, ou seja, um valor de n menor ou igual a zero.
#Construir e utilizar uma função soma que tenha como parâmetro de entrada o número de termos da série (variável n) 
#e como parâmetro de saída o valor da soma S.

def soman(n):
    x = 1
    y = 1
    s = 0
    while (y <= n):
        num = x + 1
        den = x
        s = s + (num / den)
        x = x + 2
        y += 1
    return s

n = -1
while (n <= 0):
    n = int(input("Digite o valor de n: "))

print("O valor da soma é: %.2f" % soman(n))
