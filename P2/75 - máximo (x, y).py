'''75 - Escreva uma função que retorne o maior de dois números. A função deve se chamar máximo (x, y).'''


def maximo(x, y):
    if x > y:
        print("x:", x)
    else:
        print("y:", y)

x = int(input("Digite x: "))
y = int(input("Digite y: "))
maximo(x, y)
