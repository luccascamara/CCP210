from math import*
def esfera(b):
    area=4*pi*(b**2)
    volume=(4/3)*pi*(b**3)
    return area, volume 
r = float(input("Digite o valor do raio da esfera: "))
a,v=esfera(r)
print("A área da esfera é %.2f" %a,"e o volume é %.2f" %v)
