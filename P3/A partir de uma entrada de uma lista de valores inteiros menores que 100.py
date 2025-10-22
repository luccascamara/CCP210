# Função para calcular a média dos valores entre 30 e 70 (inclusive)
def calcular_media(lista):
    # Filtrar valores na faixa desejada (30 a 70, inclusive)
    valores_filtrados = [valor for valor in lista if 30 <= valor <= 70]
    
    # Verificar se há valores filtrados
    if len(valores_filtrados) == 0:
        return None  # Retorna None se não houver valores na faixa

    # Calcular a média
    media = sum(valores_filtrados) / len(valores_filtrados)
    return media

# Entrada de dados
print("Digite os valores inteiros menores que 100. Digite 100 para encerrar a entrada.")
lista = []

while True:
    try:
        valor = int(input("Digite um valor: "))
        if valor == 100:  # Condição de parada
            break
        if valor < 100:  # Garantir que o valor é menor que 100
            lista.append(valor)
        else:
            print("O valor deve ser menor que 100. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Calcular a média
media = calcular_media(lista)

# Exibir o resultado
if media is not None:
    print(f"A média dos valores entre 30 e 70 é: {media:.2f}")
else:
    print("Não há valores na faixa entre 30 e 70 na lista fornecida.")
