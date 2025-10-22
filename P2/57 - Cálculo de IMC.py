#57 – Cálculo de IMC:

peso = []
altura = []
IMC = []

for i in range(0, 5, 1):
    peso.append(float(input("Digite o peso da pessoa %d: " % (i + 1))))
    altura.append(float(input("Digite a altura da pessoa %d: " % (i + 1))))

for j in range(0, 5, 1):
    IMC.append(peso[j] / (altura[j] ** 2))

for k in range(0, 5, 1):
    print("peso =", peso[k], "altura =", altura[k], "IMC=%.2f" % IMC[k])
