'''62 - "Faça um programa que leia um vetor X[10]. Substitua, a seguir, todos os valores nulos ou negativos do vetor por 1. Em seguida, mostre o vetor XXX.
Entrada:
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.
Saída:
Para cada posição do vetor, escreva 'X[i] = c', onde iii é a posição do vetor XXX e ccc é o valor armazenado naquela posição."'''

lista = []
for i in range(10):
    x = int(input(""))
    if x <= 0:
        x = 1
        lista.append(x)
    else:
        lista.append(x)

print("X[0] = ", lista[0])
print("X[1] = ", lista[1])
print("X[2] = ", lista[2])
print("X[3] = ", lista[3])
print("X[4] = ", lista[4])
print("X[5] = ", lista[5])
print("X[6] = ", lista[6])
print("X[7] = ", lista[7])
print("X[8] = ", lista[8])
print("X[9] = ", lista[9])
