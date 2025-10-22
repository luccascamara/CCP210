def media (n1, n2, n3):
    soma=n1+n2+n3
    return soma/3
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
res=media(n1,n2,n3)
print("A média é: %.2f" %res)