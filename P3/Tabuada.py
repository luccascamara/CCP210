# Solicita ao usuário um número para a tabuada
numero = int(input("Digite um número para ver a sua tabuada: "))

# Imprime a tabuada do número
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):  # Gera os números de 1 a 10
    print(f"{numero} x {i} = {numero * i}")
