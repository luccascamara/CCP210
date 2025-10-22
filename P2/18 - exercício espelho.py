#18 - Obter o espelho de um valor inteiro positivo conhecido.
#Observação: entenda-se espelho como o valor obtido pela leitura invertida do valor.

#Exemplos:
#- O espelho de 3629 é 9263.
#- O espelho de 301 é 103.
#- O espelho de 2000 é 2.
#- O espelho de 5 é 5.
#O algoritmo incompleto a seguir deve representar um método de resolução do problema.








valor = int(input("Digite o valor: "))  # Entrada do número inteiro
esp = 0                                # Variável que armazenará o espelho do número

while valor != 0:                      # Enquanto o número ainda tiver dígitos:
    d = valor % 10                     # Obtém o último dígito do número (resto da divisão por 10)
    esp = esp * 10 + d                 # Adiciona o dígito ao espelho, "deslocando" os anteriores
    valor = valor // 10                # Remove o último dígito do número (divisão inteira por 10)

print("Resultado:", esp)               # Exibe o valor invertido (espelho)
