'''39- Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
Exemplo:
Entrada:
Digite a quantia R$ 576
Saída:
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
'''

n = (int((input("Digite a quantia: R$"))))

n100 = n //100
n100r = n % 100

n50 = n100r// 50 
n50r = n100r % 50

n20 = n50r // 20
n20r = n50r % 20

n10 = n20r // 10
n10r = n20r % 10

n5 = n10r // 5
n5r = n10r % 5

n2 = n5r // 2 
n2r = n5r % 2

n1 = n2r // 1
n1r = n2r % 1

print("Quantidade de notas de R$100,00: ", n100)
print("Quantidade de notas de R$50,00: ", n50)
print("Quantidade de notas de R$20,00: ", n20)
print("Quantidade de notas de R$10,00: ", n10)
print("Quantidade de notas de R$5,00: ", n5)
print("Quantidade de notas de R$2,00: ", n2)
print("Quantidade de notas de R$1,00: ", n1)
