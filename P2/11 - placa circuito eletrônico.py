#11 - Você trabalha em uma fábrica que monta placas de circuito eletrônico utilizando três tipos diferentes de peças: 
#A, B e C. Cada placa é composta por:

#- 2 unidades do tipo A,
#- 3 unidades do tipo B,
#- 7 unidades do tipo C.

#O objetivo é determinar a quantidade máxima de placas que podem ser produzidas com os estoques disponíveis de cada tipo de peça.

Qa = int(input("Qtde de peças A: "))
Qb = int(input("Qtde de peças B: "))
Qc = int(input("Qtde de peças C: "))

La = Qa // 2
Lb = Qb // 3
Lc = Qc // 7

menor = La
if (Lb < menor):
    menor = Lb
if (Lc < menor):
    menor = Lc

print("A máxima qtde de placas é", menor)
