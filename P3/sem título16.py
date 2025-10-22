def calcular_soma():
    # Solicitar entrada do usuário
    n = int(input("Digite um número inteiro positivo: "))
    
    # Verificar se o número é válido
    if n <= 0:
        print("Valor inválido. O número deve ser maior que zero.")
        return

    # Calcular a soma
    soma = 0
    for i in range(1, n + 1):
        soma += i / (n - (i - 1))
    
    # Exibir o resultado
    print(f"O valor da soma S é: {soma:.4f}")

# Chamar a função
calcular_soma()
