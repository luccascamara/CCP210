#70 – Função Ordem Crescente:

def ordemdecrescente(a, b):
    if a > b:
        t = a
        h = b
    else:
        t = b
        h = a
    return t, h

def diferença(c, d):
    j = c - d
    return j

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
maior, menor = ordemdecrescente(n1, n2)
print("Ordem decrescente:", (maior, menor))
diferença = diferença(maior, menor)
print("A diferença é: %.2f" % diferença)
