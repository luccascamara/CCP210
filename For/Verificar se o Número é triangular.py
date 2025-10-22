n = int(input("Digite um número: "))
T = False
for i in range (1,n,1):
    if i*(i+1)*(i+2) == n:
        T = True 
        break
if T == True :
    print("O número é triangular")
else:
    print("Não é triangular")
    