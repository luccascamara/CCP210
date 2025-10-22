c="S"
while (c=="S") or (c=="s"):
    soma=0
    cont=1
    while cont<=5:
        num=int(input("digite um número"))
        soma=soma+num
        cont=cont+1
    print("A soma dos números = %d" %soma)
c=input("Digite S para continuar ou N para encerrar: ")
