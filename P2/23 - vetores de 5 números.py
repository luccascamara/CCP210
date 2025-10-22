#23 - Faça um programa que leia dois vetores de 5 números 
#e armazene num vetor de mesmo tamanho a soma de cada elemento dos dois vetores.
#Exibir os três vetores.

# Inicializa três listas vazias: uma para o primeiro vetor, outra para o segundo e uma para armazenar as somas.
num1 = []  # Lista para armazenar os números do vetor 1
num2 = []  # Lista para armazenar os números do vetor 2
soma = []  # Lista para armazenar as somas dos elementos dos dois vetores

# Solicita ao usuário os números do primeiro vetor.
print("Digite 5 números inteiros do vetor 1:")
for i in range(5):  # Laço que se repete 5 vezes para receber 5 números
    x = int(input())  # Lê um número inteiro do usuário
    num1.append(x)  # Adiciona o número lido à lista 'num1'

# Solicita ao usuário os números do segundo vetor.
print("Digite 5 números inteiros do vetor 2:")
for i in range(5):  # Laço que se repete 5 vezes para receber 5 números
    y = int(input())  # Lê um número inteiro do usuário
    num2.append(y)  # Adiciona o número lido à lista 'num2'

# Calcula a soma dos elementos correspondentes dos dois vetores.
for i in range(5):  # Laço que se repete 5 vezes para percorrer os elementos de ambas as listas
    soma.append(num1[i] + num2[i])  # Soma os elementos de 'num1' e 'num2' no mesmo índice e adiciona à lista 'soma'

# Exibe os três vetores.
print(num1)  # Imprime o vetor 1
print(num2)  # Imprime o vetor 2
print(soma)  # Imprime o vetor com as somas
