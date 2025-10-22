x = float(input("Digite o valor x: "))
y = float(input("Digite o valor y: "))
n = int(input("Digite o número de pontos: "))
v = (x**2/2**2) + (y**2/3**2) == 1
if v == 1:
    print("O ponto está na linha da elipse")
if v < 1:
    print("O valor está dentro da elipse")
if v > 1:
    print("O valor está fora da elipse")