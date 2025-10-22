Z=[]
P=[]
I=[]
for i in range (0,20,1):
    n=int(input("Digite um valor inteiro: "))
    Z.append(n)
    if n%2 == 0:
        P.append(n)
else:
    I.append(n)
print ("A lista geral é: ",Z)
print ("A lista par é: ",P) 
print ("'A lista impar é: ",I)