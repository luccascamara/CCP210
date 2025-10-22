'''65 - "Faça um programa, utilizando funções, que receba três números inteiros e positivos e que forneça a soma desses três números.
Para este exercício crie três funções:
- entrada(): retorna um número digitado (fazer a verificação se é positivo);
- calculaSoma(a, b, c): recebe 3 números inteiros e positivos e retorna a soma deles;
- principal: chamada das funções criadas (chama 3 vezes a entrada,
sendo uma para cada número e a função para somar) e depois mostre o resultado."'''

# Função que retorna o número digitado
def entrada():
    x = int(input("Digite o número: "))
    while x <= 0:
        x = int(input("Digite o número: "))
    return x

# Função que faz a soma de 3 números positivos
def calculaSoma(a, b, c):
    d = a + b + c
    return d

# Principal
n1 = entrada()
n2 = entrada()
n3 = entrada()
s = calculaSoma(n1, n2, n3)  # Linha de chamada
print("Soma =", s)
