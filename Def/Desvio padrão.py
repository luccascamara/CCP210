from math import * 
def desvio(qp,v):
    soma=0
    for k in range (0, qp, 1) :
        soma=soma+v[k]
    med=soma/qp
    soma=0
    for k in range (0, qp, 1) :
        soma=soma+(v[k]-med)**2
    desv=sqrt(soma/qp)
    return desv

vet=[]
quant=int(input("Entre quantidade de peças: "))
for i in range(0,quant,1):
    x=float(input("Entre com a medida %d: " %(i+1)))
    vet.append(x)
dp=desvio(quant, vet) ; #linha de chamada 
print ("O desvio padrao é:", format (dp,".2f") )