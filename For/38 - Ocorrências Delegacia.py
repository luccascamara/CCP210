'''38 - Durante os 30 dias do mês de junho foram anotadas as quantidades diárias de ocorrências numa delegacia. 
Conhecendo-se a série de quantidades anotadas, como determinar a média diária de ocorrências registradas?'''

Soma = 0
for dia in range(1, 31):
    qd = int(input("Digite a quantidade do dia: "))
    Soma = Soma + qd
Média = Soma / 30
print("Média = %.2f" % Média)
