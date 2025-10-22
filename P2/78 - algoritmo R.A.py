#Simule a execução do algoritmo acima, considere para a entrada no valor de x o primeiro algarismo do número de matrícula
#ou o dígito do número de matrícula. Indique a resposta para o valor final das variáveis w e c.


x = int(input("Digite o valor de x: "))
y = 1
w = 0
c = 1

while (c <= x):
    t = c // y
    y = y + 1
    q = c % y
    w = w + t + q
    c = c + 4

print("Valor de w:", w)
print("Valor de c:", c)

#Resposta: 10, 13