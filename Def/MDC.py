def mdc(a,b):
    while a%b != 0 :
        a,b = b, a%b
    return b
x = int(input("Digite um número inteiro: "))
y = int(input("Digite um número inteiro: "))
print("O mdc é: ", mdc(x,y))