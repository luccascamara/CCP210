dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))


total = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos


print("O total em segundos é: ", total)
