def multiplo(a,b):
    if a%b == 0:
       t = True
    else:
        t = False
    return t
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
mult = multiplo(x, y)
print(mult)