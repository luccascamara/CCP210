def principal():
    # Área Polígono
    x = []
    y = []
    soma = LACUNA 1

    print("PROBLEMA DA ÁREA DO POLÍGONO")
    qv = int(input("Entre com a quantidade de vértices do polígono: "))

    for i in range(LACUNA 2):
        x.append(int(input("Entre coordenada x: ")))
        y.append(int(input("Entre coordenada y: ")))

    for i in range(0, qv - 1):
        soma = soma + LACUNA 3

    soma = soma + (x[qv - 1] * y[0]) - (x[0] * y[qv - 1])
    area = LACUNA 4

    print("Área do polígono = %.2f" % area)

#Resposta:
#Observe o algoritmo e preencha as LACUNAS:
#•	LACUNA 1: 0
#•	LACUNA 2: 0, qv - 1
#•	LACUNA 3: (x[i] + x[i+1]) * (y[i] - y[i+1])
#•	LACUNA 4: soma / 2
