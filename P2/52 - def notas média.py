#52 – Notas: média

def ordemcrescente(A, B, C):
    if A > B:
        aux = A
        A = B
        B = aux
    if A > C:
        aux = A
        A = C
        C = aux
    if B > C:
        aux = B
        B = C
        C = aux
    return A, B, C

N1 = float(input("Entre com a nota 1: "))
N2 = float(input("Entre com a nota 2: "))
N3 = float(input("Entre com a nota 3: "))

X, Y, Z = ordemcrescente(N1, N2, N3)
mf = (3 * X + 7 * Z) / 10

print("Média Final: %.2f" % mf)
