#34 - Um órgão de defesa ao consumidor analisa um lote com várias dessas caixas.
#Se pelo menos 98% das caixas inspecionadas apresentarem quantidade efetiva maior do que 58 unidades, o lote é aprovado, 
#caso contrário (porcentagem menor do que 98%) o lote é rejeitado. 
#Conhecendo-se as quantidades efetivas das várias caixas inspecionadas, como determinar se o lote deve ser aprovado ou rejeitado? 
#A 'saída' deverá ser uma das mensagens: lote aprovado ou lote rejeitado.
#Não é conhecida previamente a quantidade de caixas inspecionadas. 
#Supor que após o último valor será anotado será digitado o valor zero (zero indica fim da entrada de dados).
#Exemplo da Tela de Execução:
#Entre quantidade 1: 60
#Entre quantidade 2: 60
#Entre quantidade 3: 59
#Entre quantidade 4: 60
#Entre quantidade 5: 60
#Entre quantidade 6: 0
#Porcentagem: 100.0 %
#lote aprovado
#Copie e cole o código e a tela de execução no espaço a seguir com os valores de entrada: 60;60;60;58;60;0."

qtd = 1
x = 1
t = 0
maior = 0
while (qtd > 0):
    qtd = int(input("Entre quantidade %i: " % x))
    x += 1
    t += 1
    if (qtd > 58):
        maior += 1
Porcentagem = ((100 * maior) / (t - 1))
t -= 1
print("Porcentagem: %.2f%%" % Porcentagem)
if (maior >= ((98 * t) / 100)):
    print("lote aprovado")
else:
    print("lote reprovado")
