#Raízes reais de uma equação

from math import *

a = int(input("Termo a: "))
b = int(input("Termo b: "))
c = int(input("Termo c: "))

if a != 0:
    delta = b**2 - (4 * a * c)
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print("%.2f e %.2f" % (x1, x2))
    elif delta == 0:
        x1 = -b / (2 * a)
        print("%.2f" % x1)
    else:
        print("A equação não tem raízes reais")
else:
    print("Não é uma equação do segundo grau")
