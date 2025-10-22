Temp=[-10, -8, 0, 1, 2, 5, -2, -4]
Max=max(Temp)
Min=min(Temp)
soma=0
K=0
i=0
tamanho=len(Temp)
while i<tamanho:
    soma=soma+Temp[i]
    K=K+1
    i=i+1
media=soma/K
print ("A maior temperatura é: ",Max) 
print ("A menor temperatura é: ",Min)
print ("A média das temperatudas é: %.2f" %media)