#7 - Você está estudando o tempo necessário para ler uma enciclopédia que possui um número total de páginas informado pelo usuário.
#Sabendo que você lê 12 páginas por hora, desenvolva um programa em Python que:
#1.	Solicite ao usuário o número total de páginas da enciclopédia.
#2.	Calcule o tempo total necessário para ler todas as páginas em horas, minutos e segundos.
#3.	Apresente o resultado do tempo de leitura em horas, minutos e segundos formatados.
#Regras:
#Considere que 1 hora tem 3600 segundos e 1 minuto tem 60 segundos.
#O programa deve dividir o tempo total de leitura em horas inteiras, minutos inteiros e os segundos restantes.
#Entrada: 

#Número de páginas da enciclopédia: 500

#Saída:

#Tempo horas: 41
#Tempo minutos: 40
#Tempo segundos: 0

qpag = int(input("Entre com o número de páginas da enciclopédia: "))

totals = qpag * 12 # Total de páginas * 12 páginas por hora = Total de Páginas por segundo
qh = totals // 3600 # Total de Páginas por segundo / 3600 porque 1hr = 3600s
r = totals % 3600 # Resto do Total de Páginas por segundo
qm = r // 60 # Quantidade de Minutos 
qs = r % 60 # Quantidade de Segundos

print("Tempo horas:", qh)
print("Tempo minutos:", qm)
print("Tempo segundos:", qs)
