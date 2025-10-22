c = int(input("Consumo de água: "))
if (c <= 20) and (c >= 20):
    base=c*1.60
if (c>20) and (c<=50):
    base=32+(c-20)*2.90
if (c>50):
    base=119+(c-50)*4.2
if base<=100:
    conta=base*0.95
else:
    conta=100+(base-100)*1.10
print("Valor da tarifa =R$ %.2f" %conta)