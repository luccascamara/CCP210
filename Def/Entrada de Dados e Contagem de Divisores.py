def entrada(): 
    n = -1
    while n<=0:
        n=int(input("Digite um número inteiro positivo: "))
    return n
def contdiv(a):
    ndiv = 0
    for cont in range (1,a+1):
        resto=a%cont
        if resto==0:
            ndiv=ndiv+1
    return ndiv
x=entrada()
y=contdiv(x)
print("%d tem %d divisores" %(x,y))
