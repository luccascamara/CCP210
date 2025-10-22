'''69 - Conhecendo-se a base e a altura de um retângulo, calcular e exibir a área, perímetro e a diagonal. 
Construir e utilizar uma função que tenha como parâmetros de entrada a base e a altura e como parâmetros de
 entrada/saída a área e o perímetro. Construir e utilizar outra função que tenha como parâmetros de entrada a base e a altura 
 e como parâmetro de saída a diagonal.'''

from math import *

def contas(base, altura):
    area = base * altura
    perimetro = 2 * base + 2 * altura
    diagonal = sqrt(base**2 + altura**2)
    print("Área:", area)
    print("Perímetro:", perimetro)
    print("Diagonal:", diagonal)

base = int(input("Digite a base do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
contas(base, altura)
