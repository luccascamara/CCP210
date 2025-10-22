# Lê os 10 valores inteiros do vetor X
X = []
for i in range(10):
    valor = int(input())  # Entrada de um valor inteiro
    if valor <= 0:  # Verifica se o valor é nulo ou negativo
        valor = 1  # Substitui por 1
    X.append(valor)  # Adiciona o valor processado ao vetor

# Mostra o vetor X com o formato "X[i] = x"
for i in range(10):
    print(f"X[{i}] = {X[i]}")
