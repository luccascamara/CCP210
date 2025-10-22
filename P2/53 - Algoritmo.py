#53 – Algoritmo:

n = int(input("Digite um valor para n: "))
a = n // 100
b = (n % 100) // 10
c = (n % 100) % 10
inv = c * 100 + b * 10 + a
soma = n + inv
a = (soma // 100)
b = ((soma % 100) // 10) * 2
c = ((soma % 100) % 10) * 3
d = (a + b + c) % 10

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
