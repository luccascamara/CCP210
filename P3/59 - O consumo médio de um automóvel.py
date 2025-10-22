'''59 - Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) 
e o total de combustível gasto (em litros).
Entrada:
O arquivo de entrada contém dois valores: um valor inteiro XXX representando a distância total percorrida (em Km), 
e um valor real YYY representando o total de combustível gasto, com um dígito após o ponto decimal.
Saída:
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".'''




x = int(input("Digite a distância total percorrida(Km): "))
y = float(input("Digite o total de combustível gasto(L): "))

cm = x / y

print("Consumo médio do automóvel(km/l): %.3f" % cm)
