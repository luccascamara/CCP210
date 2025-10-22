#20 - Deve-se anotar as medidas (em milímetros) dos diâmetros de 10 peças produzidas em um torno. 
#(Como obter o valor médio dessas medidas que estão entre 50mm e 100mm (inclusive 50mm e 100mm)?)

#Obs.: Utilize duas casas decimais depois da vírgula.
#Tela: Apresente na tela com os seguintes valores de entrada:
#50, 62.8, 25, 32.8, 39.99, 51.1, 65.84, 79.54, 99, 49.99
#Saída: A média é 68.05

# Inicializa a variável 'soma' com 0 para armazenar a soma dos diâmetros válidos.
soma = 0

# Inicializa a variável 'cont' com 0 para contar o número de diâmetros válidos.
cont = 0

# Inicia um loop que irá iterar 10 vezes (de 1 a 10).
for a in range(1, 11):
    # Solicita ao usuário que insira uma medida do diâmetro e converte o valor para ponto flutuante.
    diam = float(input("Entre medida do diâmetro: "))
    
    # Verifica se o diâmetro inserido é maior ou igual a 50.
    if diam >= 50:
        # Se for válido (>= 50), adiciona o valor à soma.
        soma = soma + diam
        # Incrementa o contador de diâmetros válidos.
        cont = cont + 1
    else:
        # Caso contrário, ignora o diâmetro (define diam como 0, embora esta linha não seja usada posteriormente).
        diam = 0

# Calcula a média dividindo a soma total dos diâmetros válidos pelo número de valores válidos.
med = soma / cont

# Exibe a média com duas casas decimais.
print("A média é %.2f" % med)
