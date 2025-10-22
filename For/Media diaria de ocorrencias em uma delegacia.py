soma = 0
for dia in range(1,31,1):
    qd=int(input("Quantidade do dia %d:" %dia))
    soma=soma+qd
media=soma/30 
print("Média = %.2f" %media)