#58 - Considere o seguinte problema:
#Dado o valor de n (n ≥ 1 e n ≤ 60), como obter o valor da soma S da série a seguir:

#S = 60/6 + 59/12 + 58/18 + ... + 1/6*n


n = int(input("Digite o valor de n: "))
d = 6
s = 0
num = 60.0
for i in range(1, n + 1, 1):
    m = num / d
    s = s + m
    d = d + 6
    num = num - 1
print("soma=%.2f" % s)
