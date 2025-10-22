from math import*
def função(y):
    if y >= 2:
        f=srqt(y)
    elif y > -2 and y < 2:
        f=y
    else:
        f=y**2
    return f
x = int(input("Digite o valor de x: "))
F=funçao(x)
print("O valor da função de F(x) é: ", F)

    