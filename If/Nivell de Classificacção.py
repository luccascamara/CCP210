p1 = float(input("Digite o valor da P1: "))
p2 = float(input("Digite o valor da P2: "))
p3 = float(input("Digite o valor da P#: "))
contagem = 0
if p1 > 7:
    contagem += 1
if p2 > 7:
    contagem += 1 
if p3 > 7:
    contagem += 1
if contagem >= 2:
    print("O nivel de classificação é A ")
elif contagem == 1:
    print("O nivel de classificação é B ")
else: 
    print("O nivel de classificação é C")