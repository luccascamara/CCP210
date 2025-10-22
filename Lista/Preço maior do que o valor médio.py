loja=[]
soma=0
for i in range (0,10,1) :
    p=float(input("digite o preço da loja %d:" %(i+1)))
    loja.append(p) 
    soma=soma+loja[i]
prmedio=soma/10
quant=0
for i in range (0,10,1):
    if loja[i] > prmedio:
        quant=quant+1
print ("valor do preço médio: %.2f" %prmedio)
print ("%d lojas compreços acima do médio" %quant)