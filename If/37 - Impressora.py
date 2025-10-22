#37 - Uma impressora tem capacidade para imprimir 5 páginas de texto por minuto. 
#Conhecendo a quantidade de páginas de uma enciclopédia que essa impressora deve imprimir, como calcular o tempo necessário para realizar essa impressão?
#Exemplo:
#Entre com o número de páginas da enciclopédia: 2497
#Tempo horas: 8
#Tempo minutos: 19
#Tempo segundos: 24

qpag = int(input("entre com o número de páginas da enciclopédia: "))
qm = qpag // 5
qs = int((((qpag % 5) / 5) * 60))
if (qm >= 60):
    qh = qm // 60
    qm = (qm % 60)
else:
    qh = 0

print("tempo em horas: ", qh)
print("tempo em minutos: ", qm)
print("tempo em segundos: ", qs)
