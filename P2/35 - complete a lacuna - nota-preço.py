#35 - Considere que esse programa deve representar um método de resolução do seguinte problema:
#A avaliação de mercado para um novo veículo é feita por uma revista, considerando-se três quesitos: preço final, 
#custo de manutenção e aspectos de conforto.
#Para cada quesito é obtida uma pontuação, de 0 até 10 com valores de 0.5 em 0.5, definida pelas respectivas equipes de avaliação.
#A avaliação final é definida como média ponderada dessas três pontuações, atribuindo-se peso 2 para a menor das pontuações 
#e peso 5 para cada uma das outras duas.
#Conhecendo-se as pontuações dos três quesitos como obter o valor da avaliação final? Indique no quadro de respostas o preenchimento adequado de cada lacuna.

# Código incompleto:
pf = float(input("nota preço final:"))
cm = float(input("nota custo manutenção:"))
LACUNA 1 = float(input("nota aspecto de conforto:"))
menor = pf
if cm < menor:
    menor = LACUNA 2
if LACUNA 3:
    menor = ac
media = LACUNA 4
print("media = %.2f" % media)

# LACUNA 1: ac
# LACUNA 2: cm
# LACUNA 3: ac < menor
# LACUNA 4: (2*menor+5*(pf+cm+ac-menor))/12
