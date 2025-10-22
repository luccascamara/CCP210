#24 - "As temperaturas em n pontos de uma cidade foram armazenadas em uma lista. 
#Faça um programa que leia as temperaturas em n pontos de uma cidade e que imprima a média das temperaturas 
#e uma lista de pontos da cidade com temperaturas superiores à temperatura média da cidade, em ordem crescente."
#Digite o número de pontos: 8
#Digite a temperatura 1: -10
#Digite a temperatura 2: -8
#Digite a temperatura 3: 0
#Digite a temperatura 4: 1
#Digite a temperatura 5: 2
#Digite a temperatura 6: 5
#Digite a temperatura 7: -2
#Digite a temperatura 8: -4
#Temperatura média: -2.00
#[3, 4, 5, 6]

# Inicialização de listas e variáveis
temp = []  # Lista para armazenar as temperaturas de cada ponto
soma = 0  # Variável para armazenar a soma das temperaturas
cidade = []  # Lista para armazenar os índices dos pontos com temperaturas acima da média
media1 = []  # Lista para armazenar as temperaturas acima da média

# Solicita ao usuário o número de pontos a serem considerados
n = int(input("Digite o número de pontos: "))

# Loop para coletar as temperaturas dos pontos
for i in range(0, n):
    t = float(input("Digite a temperatura %d: " % (i + 1)))  # Lê a temperatura como número decimal
    temp.append(t)  # Adiciona a temperatura à lista 'temp'
    soma = soma + temp[i]  # Soma a temperatura ao total acumulado

# Calcula a média das temperaturas
media = soma / n
# Exibe a temperatura média com duas casas decimais
print("Temperatura média: %.2f" % media)

# Loop para identificar pontos com temperaturas acima da média
for i in range(0, n):
    if temp[i] > media:  # Verifica se a temperatura do ponto atual é maior que a média
        media1.append(temp[i])  # Adiciona a temperatura à lista 'media1'
        media1.sort()  # Organiza as temperaturas acima da média em ordem crescente
        cidade.append(i + 1)  # Adiciona o índice do ponto à lista 'cidade' (considerando 1 como o primeiro ponto)
        cidade.sort()  # Organiza os índices dos pontos em ordem crescente

# Exibe os índices dos pontos com temperaturas acima da média
print(cidade)
