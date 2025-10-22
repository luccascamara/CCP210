v = 0 
v140 = 0
while True:
    velocidade = int(input("Digite a velocidade em Km/h: "))
    if velocidade == 0:
        break
    v = v +1
    if velocidade > 140:
        v140=v140+1
porcentagem=(v140/v)*100
print("Porcentagem de multas = %.2f" %porcentagem)