'''41 - A média aritmética ponderada Xp de um conjunto de números x1, x2,x3,…,xn cuja importância relativa ("peso") 
é respectivamente p1,p2,p3,…,pn é calculada da seguinte maneira:'''

'''xp = p1x1 + p2x2 + p3x3 + ... pnxn // p1 + p2 + p3 + ... pn'''

'''Como obter a média aritmética ponderada de, no máximo, 50 números, conhecendo-se a quantidade de números que serão considerados, os números e seus respectivos pesos?
O código abaixo dá a solução deste problema, mas está incompleto.
- A quantidade de números que serão considerados é armazenada na variável n, os números são guardados na lista N de 50 componentes e os pesos de cada número são guardados na lista P de 50 componentes.
- Na variável auxiliar numerador é armazenado o cálculo do numerador da média aritmética ponderada conforme definição.
- Na variável auxiliar den é armazenado o resultado do denominador da média aritmética ponderada conforme definição.
- A média ponderada é armazenada na variável zp.
Complete as lacunas de 1 a 4.
Principal
Entrada:
Ne P tipo float; n tipo int
Saída:
zp tipo float'''

N = []
P = []
n = int(input("Insira quantos números serão considerados: "))
den = 0
numerador = 0

for i in range(0, n, 1):
    N.append(float(input("Digite o número %d: " % (i + 1))))
    P.append(float(input("Digite o peso %d: " % (i + 1))))

for j in range(0, n, 1):
    numerador = numerador + N[j] * P[j]

for k in range(0, n, 1):
    den = den + P[k]

xp = numerador / den
print("A média ponderada é %.2f" % xp)
