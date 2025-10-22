#21 - Faça uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for "A", 
#a função deverá calcular a média aritmética das notas do aluno; se for "P", 
#deverá calcular a média ponderada com pesos 5, 3 e 2. A média calculada deve ser devolvida à função principal para, então, 
#ser mostrada.
#Exemplo:

#Digite a primeira nota: 4.5
#Digite a segunda nota: 7.3
#Digite a terceira nota: 5.7
#Digite A ou P para a letra: A
#Média = 5.83

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
letra = input("Digite A ou P para a letra: ")
# Função para calcular a média aritmética
def meda(a, b, c):
    # Calcula a média aritmética somando as notas e dividindo por 3
    m = (a + b + c) / 3
    return m  # Retorna o resultado da média aritmética

# Função para calcular a média ponderada
def medp(a, b, c):
    # Calcula a média ponderada aplicando os pesos 5, 3 e 2 às notas
    p = (a * 5 + b * 3 + c * 2) / 10
    return p  # Retorna o resultado da média ponderada

# Verifica se o usuário escolheu calcular a média aritmética
if letra == 'A':
    # Chama a função 'meda' com as notas fornecidas e atribui o resultado a M
    M = meda(nota1, nota2, nota3)
    # Exibe o resultado formatado com duas casas decimais
    print("Média = %.2f" % M)

# Verifica se o usuário escolheu calcular a média ponderada
elif letra == 'P':
    # Chama a função 'medp' com as notas fornecidas e atribui o resultado a M
    M = medp(nota1, nota2, nota3)
    # Exibe o resultado formatado com duas casas decimais
    print("Média = %.2f" % M)
