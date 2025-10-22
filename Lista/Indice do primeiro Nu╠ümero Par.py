lista = [25, 15, 20, 30, 5, 100]
tamanho = len(lista)
indice = 0
par=0 
indicePrimeiroPar = -1
while indice < tamanho:
    if lista[indice]%2 == 0:
             par = 1
             indicePrimeiroPar = indice
             break
    indice = indice + 1
if par ==1:
    print('O primeiro par aparece na posição de índice', indicePrimeiroPar)
else:
    print ('Não encontrei um número par na sequência')
print ('fim')