from math import*
x = float(input("Valor de x: "))
if x < -2:
    y = sqrt(abs(x+1))
elif (-2 < x) and (x < 2): 
    y = 0
elif x > 2:
    y = sqrt(abs(1-x))
if x == -2 or x == 2:
    print("Não existe função definida")
else:
    print("O valor de y = ", y)