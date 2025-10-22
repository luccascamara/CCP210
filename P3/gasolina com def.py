x = int(input("Digite a quantidade de km percorrido: "))
y = int(input("Digite a quantidade de dias: "))

def total (x,y):
    if y ==0:
        return "Não é possivel calcular sem a quantidade de dias"
    return (x*0.15)+(y*60)

z = total(x, y)

print("O total é:", z)