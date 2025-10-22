def entrada():
    x = float(input())
    return x
def somaImposto(porc,custo):
    porc=(porc/100)+1
    t=custo*porc
    return t
print ("Digite o valor do produto: ")
p=entrada()
print("Digite o valor do imposto: ")
c=entrada()
prodImposto=somaImposto(c,p)
print("O valor do produto com imposto é: %.2f" %prodImposto)
