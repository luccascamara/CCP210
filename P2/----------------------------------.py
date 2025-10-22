qtot = 0
q140 = 0
while True:
    veloc = int(input("Digite a velocidade: "))
    if (veloc == 0):
        break
    qtot = qtot + 1
    if (veloc > 140):
        q140 = q140 + 1
perc = q140 / qtot * 100
print("Percentual de multas acima de 140 km/h:", perc, "%")
