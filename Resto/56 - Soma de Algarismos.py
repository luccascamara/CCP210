#56 - Soma de Algarismos:

número = int(input("Digite um número com 3 algarismos: "))
pn = número // 100
resto = número % 100
sn = resto // 10
tn = resto % 10
soma = pn + sn + tn
print("Soma dos algarismos:", soma)
