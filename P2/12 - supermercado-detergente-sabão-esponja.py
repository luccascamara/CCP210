#12 - Em um supermercado, o setor de artigos para limpeza deseja oferecer durante uma promoção, 
#um kit de produtos com o preço diferenciado. O kit deve ter quatro unidades de detergente, 
#três de sabão em pó e cinco unidades de esponja. 
#Conhecendo-se as quantidades de unidades disponíveis de cada um desses itens, 
#como determinar a quantidade de kits que poderão ser colocados à venda?
#Considere que todas as quantidades serão expressas por valores inteiros.
#Exemplo:
#Quantidade de detergente: 1555
#Quantidade de sabão em pó: 1910
#Quantidade de esponja: 4810
#Quantidade de kit: 388

dtg = int(input("Quantidade de detergente: "))
sab = int(input("Quantidade de sabão em pó: "))
esp = int(input("Quantidade de esponja: "))

Qd = dtg // 4 
Qsab = sab // 3
Qesp = esp // 5

menor = Qd # Igualou menor = Quantidade de Detergente

if Qsab < menor: # Quant de Sabão for menor que Quant Detergente
    menor = Qsab

if Qesp < menor: # Quant de Esponja for menor que Quant Detergente
    menor = Qesp

print("Quantidade de kit:", menor)
