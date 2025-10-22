#29-Conhecendo-se o valor total do pedido e o número de produtos adquiridos,
#calcular e exibir o valor a ser pago considerando as seguintes condições:
#•	Pedidos acima de R$ 200,00 com um único produto recebem desconto de 8% e frete grátis;
#•	Pedidos acima de R$ 200,00 com mais de um produto, recebem desconto de 8% e pagam frete de R$ 7,00;
#•	Pedidos que custam entre R$ 150,00 e R$ 200,00 (inclusive) recebem desconto de 7% e pagam frete de R$ 15,00;
#•	Demais situações não recebem desconto e pagam frete de R$ 15,00.
#Copie e cole o código em Python e a Tela de Execução no quadro de resposta.

x = (int(input("Digite o valor total de pedidos:" )))
y = (int(input("Digite o número de produtos adquiridos: ")))

if x > 200 and y == 1:
    frete = 0
    desconto = 0.08

if x > 200 and y > 1:
    frete = 7
    desconto = 0.08

if x > 150 and x <= 200:
    frete = 15
    desconto = 0.07

else: 
    frete = 15
    desconto = 0

d = (x*desconto)
f = frete
vf = (x-d+f)

print("O valor do desconto:", desconto)
print("O valor do frete é:", frete)
print("O valor final é:", vf)

