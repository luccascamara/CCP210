def entrada():
    n=int(input("Digite um número positivo maior que zero: "))
    while n<=0:
        print("Número errado! Digite outro número: ")
        n = int(input("Digite um número positivo maior que zero: "))
    return n
def soma(n):
    soma = 0
    while n != 0:
        d=n%10
        soma=soma+d
        n=n//10
    return soma 
x = entrada()
s=soma(x)
print("A soma do dígitos de ", x,"é de: ",s)
