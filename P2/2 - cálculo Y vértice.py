#2 - Escreva um programa em Python que calcule uma função quadrática f(x) = ax²+bx+c. 
# programa deve solicitar ao usuário que insira os valores dos coeficientes a, b, c e então calcular o valor de Y Vértice 
#usando a formula de Y vértice = - Delta/ 4*a. O seu programa deve exibir o valor de Y Vértice com quatro casas decimais. 


print("f(x) = a*x*x + b*x + c")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: ")) 
c = float(input("Digite o valor de c: "))

delta = b * b - 4 * a * c
yv = -delta / (4 * a)


print("O valor do YV é: %.4f" % yv)
# No print acima, foi colocado o termo "%.4f %f" 
# porque no enuciado se pede o YV com 4 casas decimais.
