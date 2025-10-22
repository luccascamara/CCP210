#10 - Uma locadora de veículos oferece descontos e cobra multas dependendo da quantidade de dias que um cliente demora para devolver 
#o carro alugado. O programa deve calcular o valor a ser pago pelo cliente, com base nas seguintes regras:

#- Se o carro for devolvido em até 8 dias, o cliente terá um desconto de 2% sobre o valor do aluguel.

#- Se o carro for devolvido entre 9 e 15 dias, não há desconto nem acréscimo no valor do aluguel.

#- Se o carro for devolvido após 15 dias, será cobrada uma multa de 20% sobre o valor do aluguel, 
#acrescida de um adicional de R$ 0,0086 por dia excedente após o 15º dia.

#Requisitos:

#O programa deve solicitar dois valores ao usuário:
#- O valor do aluguel diário (em reais).
#- A quantidade total de dias que o cliente manteve o carro alugado.

aluguel = float(input("Entre aluguel: "))
dia = int(input("Entre dia: "))

if (dia <= 8): 
    valor = aluguel * 0.98
elif (dia >= 9) and (dia <= 15): # elif significa uma multipla escolha de if
    valor = aluguel
else:
    valor = aluguel * 1.2 + aluguel * (dia - 15) * 0.0086

print("Valor a ser pago: R$ ", valor)

