def media(A, B, C):
    M = (A + B * 2 + C * 3) / 6
    if M >= 5:
        print("Aprovado")
    else:
        print("Reprovado")
    return M


N1 = float(input("Entre com a nota 1: "))
N2 = float(input("Entre com a nota 2: "))
N3 = float(input("Entre com a nota 3: "))


M = media(N1, N2, N3)
print(f"A média do aluno é: {M:.2f}")

