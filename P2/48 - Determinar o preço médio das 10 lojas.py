'''"Conhecendo-se uma sequência de 10 valores correspondentes aos preços de um produto em 10 lojas varejistas, 
como determinar em quantas das lojas determinar é superior ao preço médio dessas 10 lojas?"'''

prec = []
soma = 0
for i in range(0, 10, 1):
    p = float(input("Entre com o preço da loja %d: " % (i+1)))
    prec.append(p) # quando ele coloca append ele guarda o que a lista quer
    soma = soma + prec[i]

pm = soma / 10
q = 0

for i in range(0, 10, 1):
    if prec[i] > pm:
        q += 1

print("Quantidade de lojas com preços acima da média:", q)


