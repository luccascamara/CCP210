#16 - Elabore um programa em Python que permita ao usuário inserir uma nota. A nota deve estar no intervalo de 0 a 10. 
#Caso o usuário insira um valor fora desse intervalo, 
#o programa deverá exibir uma mensagem informando que a nota está fora da faixa permitida e solicitará que o usuário 
#insira a nota novamente. O programa deve repetir esse processo até que o usuário forneça uma nota válida.


nota = float(input("Digite sua nota: "))
while (nota<0)or(nota>10):
    print("Nota fora da faixa: ")
    nota = float(input("Digite novamente sua nota: "))