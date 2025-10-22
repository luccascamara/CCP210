def soma(a,b):
    soma=0
    if a>b:
        t=b
        h=a
    else:
        t=a
        h=b
    for k in range (t+1,h,1):
        soma=soma+k
    return soma 
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
s=soma(x,y)
print("A soma do N números existentes entre ",x,"e",y,"é: ", s)

        