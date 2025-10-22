#26 - PROBLEMA DA ÁREA DO POLÍGONO
#Implemente o algoritmo que calcula a área de um polígono simples dado pelo número de vértices e suas coordenadas.
#Exemplo de entrada e saída:
#PROBLEMA DA ÁREA DO POLÍGONO  
#Entre com a quantidade de vértices do polígono: 5  
#Entre coordenada x: 0  
#Entre coordenada y: 0  
#Entre coordenada x: 0  
#Entre coordenada y: 1  
#Entre coordenada x: 1  
#Entre coordenada y: 2  
#Entre coordenada x: 2  
#Entre coordenada y: 2  
#Entre coordenada x: 2  
#Entre coordenada y: 0  
#Área do polígono = 3.00  

# Inicialização das listas para armazenar as coordenadas dos vértices
x = []  # Lista para armazenar as coordenadas x dos vértices
y = []  # Lista para armazenar as coordenadas y dos vértices
soma = 0  # Variável para acumular a soma parcial usada no cálculo da área

print("PROBLEMA DA ÁREA DO POLÍGONO") # Impressão inicial do título do problema

# Solicita ao usuário o número de vértices do polígono
qv = int(input("Entre com a quantidade de vértices do polígono: "))

# Laço para coletar as coordenadas dos vértices
for i in range(0, qv, 1):  # Para cada vértice do polígono
    # Solicita e armazena as coordenadas x e y
    x.append(int(input("Entre coordenada x: ")))  # Adiciona o valor de x à lista x
    y.append(int(input("Entre coordenada y: ")))  # Adiciona o valor de y à lista y

# Laço para calcular a soma parcial dos produtos cruzados dos vértices consecutivos
for i in range(0, qv-1, 1):  # Itera sobre os vértices, excluindo o último
    # Soma parcial baseada na fórmula do determinante (produto cruzado)
    soma = soma + (x[i] + x[i+1]) * (y[i] - y[i+1])

# Adiciona a última parte da fórmula, que conecta o último vértice ao primeiro
soma = soma + (x[qv-1] + x[0]) * (y[qv-1] - y[0])
area = soma / 2 # Divide a soma total por 2 para calcular a área do polígono

print("Área do polígono = %.2f" % area) # Exibe a área do polígono com 2 casas decimais
