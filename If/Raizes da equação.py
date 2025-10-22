from math import*
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
if a!=0:
    delta=(b**2)-(4*a*c)
    if delta>0: 
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print("As raizes são", x1,x2)
    elif delta==0:
        x1=-b/(2*a)
        print("A raíz é: ", x1)
    else: 
        print("Não há raízes reais")
else:
    print("Não é uma equação de segundo grau")