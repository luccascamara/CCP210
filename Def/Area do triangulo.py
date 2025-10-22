def area(x,y):
    A=(x*y)/2
    return A
a = float(input("Digite o valor da altura do triângulo: "))
b = float(input("Digite o valor da base do triângulo: "))
at = area(a,b)
print("O valor da área do triângulo é: %.2f" %at)
