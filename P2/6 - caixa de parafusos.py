#Uma empresa precisa embalar parafusos em três tipos de caixas:
#Caixas Grandes com capacidade para 250 parafusos, Caixas Médias com capacidade para 50 parafusos 
#e Caixas Pequenas com capacidade para 10 parafusos. O custo de cada caixa é diferente:
#uma Caixa Grande custa R$ 8,50, uma Caixa Média custa R$ 3,20 e uma Caixa Pequena custa R$ 1,80.
#Dado o número total de parafusos, seu objetivo é determinar a quantidade de cada tipo de caixa necessária para embalar 
#todos os parafusos, o número de parafusos restantes (se houver), e o custo total das caixas utilizadas.
#Escreva um programa que receba como entrada o número total de parafusos e exiba:
#A quantidade de Caixas Grandes, Caixas Médias e Caixas Pequenas necessárias.
#O número de parafusos que restarem sem embalagem.
#O Custo Total das caixas utilizadas.
#Exemplo de entrada e saída:
#Entrada: 1864

total = int(input("Quantidade total de parafusos:")) #Total = 1864

cg = total // 250 # Caixa Grande 1864/250 = 7 + resto
restocg = total % 250 # Descobrindo o resto = 114

cm = restocg // 50 # Caixa Média 114/50 = 2 + resto2
r2 = restocg % 50 # Descobrindo o resto = 14

cp= r2 // 10 # Caixa Pequena 14/10 = 1 + resto3
resto = r2 % 10 # Descobrindo o resto = 4

custo = (cg * 8.50) + (cm * 3.20) + (cp * 1.80)

print("Caixas Grandes:", cg)
print("Caixas Médias:", cm)
print("Caixas Pequenas:", cp)
print("Número de parafusos restantes:", resto)
print("Custo Total: R$ %.2f" % custo)

# A %250 / %50 / %10 é usada para descobrir o resto de uma divisão.