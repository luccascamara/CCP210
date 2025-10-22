'''71 - Elabore um programa que mostre o preço de etiqueta de um produto e calcule e mostre o quanto deve ser pago por um produto, 
considerando o preço normal de etiqueta e a escolha da condição de pagamento.
Utilize os códigos da tabela seguinte para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.'''

'''1: {"condicao": "À vista em dinheiro ou cheque", "desconto": "10% de desconto"},
    2: {"condicao": "À vista no cartão de crédito", "desconto": "5% de desconto"},
    3: {"condicao": "Em 2 vezes", "detalhe": "Preço normal de etiqueta sem juros"},
    4: {"condicao": "Em 3 vezes", "detalhe": "Preço normal de etiqueta mais juros de 10%"}'''
    
p = float(input("Digite o preço do produto: "))
c = int(input("Digite o código de pagamento: "))

if c == 1:
    valor = p * 0.9
if c == 2:
    valor = p * 0.95
if c == 3:
    valor = p
if c == 4:
    valor = p * 1.1

print("O valor final é:", valor)

