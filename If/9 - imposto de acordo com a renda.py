#9 - Escreva um programa em Python para calcular o imposto de renda devido por uma pessoa física, 
#com base no salário mensal informado. Para isso, utilize a tabela abaixo como referência:

#{"Faixa salarial (R$)": "Até 1.499,15", "Alíquota (%)": 0, "Dedução (R$)": 0},
#  {"Faixa salarial (R$)": "De 1.499,16 até 2.246,75", "Alíquota (%)": 7.5, "Dedução (R$)": 112.43},
#  {"Faixa salarial (R$)": "De 2.246,76 até 2.995,70", "Alíquota (%)": 15.0, "Dedução (R$)": 280.94},
# {"Faixa salarial (R$)": "De 2.995,71 até 3.743,19", "Alíquota (%)": 22.5, "Dedução (R$)": 505.62},
# {"Faixa salarial (R$)": "Acima de 3.743,19", "Alíquota (%)": 27.5, "Dedução (R$)": 692.78},


#Imposto = (salário*alíquota/100)-dedução

salario = float(input("Entre com o salário: R$"))
if (salario < 1499.15):
    Imposto = 0

if (salario>=1499.16)and(salario <=2246.75):
    Imposto = (salario*7.5/100)-112.43

if (salario>=2246.76)and(salario <=2995.70):
    Imposto = (salario*15.0/100)-280.94

if (salario>=2995.71)and(salario <=3743.19):
    Imposto = (salario*22.5/100)-505.62
    
if (salario>3743.19):
    Imposto = (salario*27.5/100)-692.78

print("Imposto: R$ %.2f" % Imposto) 
# %.2f no print significa duas casas depois da virgula.