'''76 - Escreva uma função chamada múltiplo(x, y) que receba dois números e retorne 
True se o primeiro for múltiplo do segundo número.'''

def multiplo(x, y):
    if x % y == 0:
        print("True")
    else:
        print("Error")

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
multiplo(x, y)
