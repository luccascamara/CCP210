def multiplicacao_por_soma_sucessiva(a, b):
    # Determina o menor número de iterações para a soma sucessiva
    multiplicando = a if abs(a) <= abs(b) else b
    multiplicador = b if multiplicando == a else a

    resultado = 0

    # Realiza a soma sucessiva
    for _ in range(abs(multiplicando)):
        resultado += multiplicador

    # Ajusta o sinal do resultado se necessário
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        resultado = -resultado

    return resultado

# Leitura dos números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Cálculo e exibição do resultado
resultado = multiplicacao_por_soma_sucessiva(numero1, numero2)
print(f"O resultado de {numero1} x {numero2} é {resultado}.")
