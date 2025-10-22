s = float(input("Digite o valor do salário: "))
t = int(input("Digite o tempo de trabalho: "))
if t>=5:
    bonus=s*0.2
if t<5:
    bonus=s*0.1
print("O bônus é de: %.2f" %bonus)