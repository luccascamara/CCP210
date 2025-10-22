#54 – Múltiplos de 5:

a = int(input("Digite um número para a: "))
b = int(input("Digite um número para b: "))
if a > b:
    print("Números Incorretos")
else:
    soma = a + b
    multiplos = 0
    if a % 5 == 0:
        multiplos += 1
    if b % 5 == 0:
        multiplos += 1
    while b > a + 1:
        b -= 1
        soma = soma + b
        if soma % 5 == 0:
            multiplos += 1

    print("soma dos números inteiros: %d" % soma)
    print("quantidade de números múltiplos de 5: %d" % multiplos)
