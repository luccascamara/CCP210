#19 - "Faça um programa que leia um valor n inteiro e positivo, calcule e mostre o valor de S, conforme a fórmula a seguir:
 
#S = 1 + 2/3 + 3/5 + 4/7 + ... + n/2n/1


# Solicita ao usuário o número de parcelas (n), que deve ser um número inteiro e positivo
n = int(input("Digite o número de parcelas:"))

# Inicializa a variável soma com 0 para acumular o valor da soma das parcelas
soma = 0

# Itera de 1 até n (inclusive), calculando cada parcela da fórmula
for i in range(1, n+1):
    # Adiciona a parcela correspondente (i / (2 * i - 1)) à variável soma
    soma = soma + i / (2 * i - 1)

# Exibe o resultado da soma, formatando o número com 5 casas decimais
print("A soma das %d primeiras parcelas é %.5f" % (n, soma))
