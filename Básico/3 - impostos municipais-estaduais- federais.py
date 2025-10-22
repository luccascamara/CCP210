#3 - Escreva um programa em Python que receba como entrada a arrecadação de impostos de três níveis de governo: 
#municipal, estadual e federal. O programa deve calcular e exibir o percentual que cada um desses valores 
#representa em relação ao total arrecadado.
#Especificações:
#1.	Solicite ao usuário que insira o valor da arrecadação de impostos municipais, estaduais e federais.
#2.	Calcule o total arrecadado somando os três valores.
#3.	Calcule o percentual de cada tipo de imposto em relação ao total.
#4.	Exiba o percentual de cada arrecadação formatado com duas casas decimais.
#Exemplo de Entrada:
#•	Impostos municipais: 2000.00
#•	Impostos estaduais: 3000.00
#•	Impostos federais: 5000.00




m = float(input("Digite a arrecadação de impostos municipais: "))
e = float(input("Digite a arrecadação de impostos estaduais: "))
f = float(input("Digite a arrecadação de impostos federais: "))

T = m + e + f 

pm = m/(T*100)
pe = e/(T*100)
pf = f/(T*100)

print("O total de impostos é: " , T)
print("O total de impostos municipais é: %.4f" %pm)
print("O total de impostos estaduais é: %.4f" %pe)
print("O total de impostos federais é: %.4f" %pf)
#Foi colocado o termo "%.4f %pm/pe/pf" para colocar
# as quatros casas decimais depois da virgula.