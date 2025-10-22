alfa = int(input("Digite o ângulo 1: "))
beta = int(input("Digite o ângulo 2: "))
if (alfa+beta<180) and (alfa>0) and (beta>0):
    gama=180-(alfa+beta)
    print("Gama = ", gama)
    if (alfa==90) or (beta==90) or (gama==90):
        print("Triângulo Retângulo")
    elif (alfa>90) or (beta>90) or (gama > 90):
        print("Obtusângulo")
    else:
        print("Acutângulo")
else:
    print("Não formam triângulo")