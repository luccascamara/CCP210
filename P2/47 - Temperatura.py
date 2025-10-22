'''47 - TEMPERATURA (imprimir a maior, a menor e a média da temperatura):'''

temp = [-10, -8, 0, 1.2, 5, -2, -4]
maior = temp[0]
menor = temp[0]
soma = 0

for i in range(0, len(temp), 1):
    if temp[i] >= maior:
        maior = temp[i]
    if temp[i] <= menor:
        menor = temp[i]
    soma = soma + temp[i]

print("Maior temperatura: ", maior)
print("Menor temperatura: ", menor)
print("A média das temperaturas: %.2f" % (soma / len(temp)))
