'''63 - "Faça um programa que solicita do usuário uma quantidade de dias, horas, minutos e segundos. 
Calcule e imprima o total convertido em somente segundos."'''


d = int(input("Digite a quantidade de dias: "))
h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))

horast = h + (d * 24)
mintotal = m + (horast * 60)
sectotal = s + (mintotal * 60)

print("Total de segundos:", sectotal)
