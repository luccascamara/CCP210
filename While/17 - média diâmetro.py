#17 - Foram anotadas as medidas dos diâmetros de várias peças produzidas em um torno. Como obter o valor médio dessas medidas?
#Não é conhecida previamente a quantidade de peças observadas.
#Suponha que após a digitação da medida da última peça observada será digitado o valor zero (o zero indica fim da entrada de dados).
#Exemplo:

#Entrada:
#Digite o valor do diâmetro: 33
#Digite o valor do diâmetro: 34
#Digite o valor do diâmetro: 35.5
#Digite o valor do diâmetro: 34.5
#Digite o valor do diâmetro: 0

#Saída:
#Média dos diâmetros = 34.25

k = 0 # Contador de peças. Ele armazena a quantidade de diâmetros informados.
soma = 0 # Variável que acumula o valor total da soma dos diâmetros digitados.
while True: # Cria um laço infinito para repetir a entrada de valores 
# até que o usuário digite 0, que encerre o Loop.
    d = float(input("Digite o valor do diâmetro: "))
    if d == 0: # Indica quando d = 0, interrompe o codigo
        break
    soma = soma + d # Soma cumulativa de todos os diâmetros digitados até o momento.
    k = k + 1 # Incrementa o contador de peças para cada valor digitado, exceto o 0.

media = soma / k
print("Média dos diâmetros = %.2f" % media)