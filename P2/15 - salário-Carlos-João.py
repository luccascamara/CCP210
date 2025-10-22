#15 - Carlos e João decidiram investir parte de seus salários em aplicações financeiras com rendimentos diferentes. 
#Carlos aplica todo o seu salário em uma caderneta de poupança que rende 2% ao mês, 
#enquanto João, que possui um salário equivalente à metade do de Carlos, 
#investe todo o seu dinheiro em um fundo de renda fixa com rendimento de 25% ao mês.
#Escreva um programa em Python que receba o salário inicial de Carlos como entrada 
#e calcule o número de meses necessários para que o montante acumulado por João ultrapasse ou iguale o montante acumulado por Carlos. 
#O programa deve exibir o número de meses necessários para que isso aconteça.
#Considere que os rendimentos sejam compostos mensalmente (ou seja, os juros são aplicados sobre o saldo atualizado a cada mês).

c = float(input('Digite o salário de Carlos: R$ '))

j = c / 2 # Salário de João é a metade do salário de Carlos

# Rendimento mensal de Carlos e João
rendimento_carlos = 0.02  # 2% ao mês
rendimento_joao = 0.25    # 25% ao mês

# Inicializa os meses
meses = 0

# Loop até o valor de João ultrapassar o de Carlos
while j <= c:
    c += c * rendimento_carlos  # Atualiza o valor de Carlos
    j += j * rendimento_joao    # Atualiza o valor de João
    meses += 1

# Exibe o número de meses
print("Tempo necessário: meses", meses)
