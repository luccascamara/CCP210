#30 - Uma parede retangular precisa receber um revestimento de azulejos.
#- Conhecendo-se as dimensões da parede (altura e comprimento) e a dimensão de cada azulejo quadrado (lado).
#- Calcular e exibir quantos azulejos serão necessários para recobrir essa parede.
#- Os azulejos não serão recortados, dessa forma, uma parcela da parede poderá não ser revestida.
#- Determinar também a área da parede que ficará sem revestimento.
#- Todas as medidas (altura/comprimento/lado) são dadas por valores inteiros em centímetros.
#Altura da parede = 200 cm / Comprimento da parede = 250 cm / Lado do azulejo = 45.
#Total de azulejos = 20 / Área não revestida = 9500.

altura = int(input("Digite o valor da altura da parede: "))
comprimento = int(input("Digite o comprimento da parede: "))
lado = int(input("Digite o lado do azulejo: "))

qtdAzulejoAltura = altura // lado
qtdAzulejoComprimento = comprimento // lado
totalAzulejos = qtdAzulejoAltura * qtdAzulejoComprimento

areaRevestida = totalAzulejos * (lado * lado)
areaNaoRevestida = (altura * comprimento) - areaRevestida

print("A quantidade total de azulejos é: {}".format(totalAzulejos))
print("A área da parede não revestida é: {}".format(areaNaoRevestida))

