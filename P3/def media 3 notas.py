def media(N1, N2, N3):
    M = (N1 + N2 * 2 + N3 * 3) / 6
    if M >= 5:
        print("Aprovado")
    else:
        print("Reprovado")
    return M

N1 = float(input("Entre com a nota 1: "))
N2 = float(input("Entre com a nota 2: "))
N3 = float(input("Entre com a nota 3: "))


M = media(N1, N2, N3)

# Exibe a média final
print("Média Final: %.2f" % M)
