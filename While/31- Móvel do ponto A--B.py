#31 – Um móvel desloca-se ao longo de uma reta determinada pelos pontos A e B, a partir do ponto A em direção ao ponto B. 
#O movimento é realizado em várias etapas:
#•	na primeira etapa a distância percorrida é x;
#•	na segunda etapa é x/2;
#•	na terceira etapa é x/3; e assim sucessivamente até que o móvel ultrapasse o ponto B.
#"Conhecendo-se a distância entre os pontos A e B e a distância percorrida na primeira etapa do deslocamento, 
#como determinar a quantidade de etapas necessárias para que o ponto B seja ultrapassado?"
#Variáveis:
#•	Entrada: dab e x de tipo real.
#•	Saída: etap de tipo inteiro.
#Exemplo da Tela de Execução:
#Digite a distância ab: 10  
#Digite a distância x: 2  
#Número de etapas: 83  


dab=float(input("Digite a distância ab:"))
x=float(input("digite a distância x:"))

n = 1

etapa = 0
distancia = 0

while distancia < dab:
    distancia = distancia + x/n
    n = n + 1
    etapa = etapa + 1

print("numeros de etapas=",etapa) 
