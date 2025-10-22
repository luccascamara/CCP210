'''73 - Considere o seguinte problema:
"Conhecendo-se o valor total do pedido e o número de produtos adquiridos, 
calcular e exibir o valor a ser pago considerando as seguintes condições:
•	Pedidos acima de R$ 200,00 com um único produto recebem desconto de 8% e frete grátis;
•	Pedidos acima de R$ 200,00 com mais de um produto, recebem desconto de 8% e pagam frete de R$ 7,00;
•	Pedidos que custam entre R$ 15,00 e R$ 200,00 (inclusive) recebem desconto de 7% e pagam frete de R$ 15,00;
•	Demais situações não recebem desconto e pagam frete de R$ 15,00."'''

x = int(input("Digite o número de produtos: "))
y = float(input("Digite o valor total do pedido: "))

if y > 200 and x == 1:
    desconto = 0.08
    frete = 0
elif y > 200 and x > 1:
    desconto = 0.08
    frete = 7
elif y >= 15 and y <= 200:
    desconto = 0.07
    frete = 15
else:
    desconto = 0
    frete = 15

desconto = y * desconto
valor = y - desconto + frete

print("O valor a ser pago é:", valor)
