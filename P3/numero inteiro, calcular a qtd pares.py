# Solicita ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Calcula os números pares até o número digitado
    # Inclui o próprio número se ele for par
    quantidade_pares = (numero // 2) + 1

    # Exibe o resultado
    print(f"A quantidade de números pares até {numero} é: {quantidade_pares}")
