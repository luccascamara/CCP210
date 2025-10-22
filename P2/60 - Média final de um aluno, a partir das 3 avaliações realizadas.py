'''60 - "Calcular e exibir a média final de um aluno, a partir das 3 avaliações realizadas. À menor nota é atribuído peso 3 e à maior nota é atribuído peso 7 (a nota com valor intermediário é descartada).
Construir e utilizar a função auxiliar MaiorMenor que tenha como parâmetros de entrada as três notas - a, b, e c de tipo float, 
e como parâmetros de saída a maior e a menor das notas – max e min de tipo float."
'''


def MaiorMenor(a, b, c):
    notas = []
    maior = max(a, b, c)
    menor = min(a, b, c)
    notas.append(menor)
    notas.append(maior)
    menorNota = notas[0] * 0.3
    maiorNota = notas[1] * 0.7
    print("Maior Nota foi de %.2f, com peso 7 aplicado temos %.2f" % (notas[1], maiorNota))
    print("Menor Nota foi de %.2f, com peso 3 aplicado temos %.2f" % (notas[0], menorNota))

a = float(input("Digite uma nota: "))
b = float(input("Digite uma nota: "))
c = float(input("Digite uma nota: "))
MaiorMenor(a, b, c)

