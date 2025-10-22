m = float(input("Digite a quantidade de minutos: "))
if m > 400 :
    v=0.15*m
if m <= 400: 
    v=0.18*m
if m <= 200:
    v=0.20*m
print("O valor da conta é %.2f" %v)