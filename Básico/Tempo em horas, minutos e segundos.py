total= int(input("Tempo do evento em segundos: "))
horas=total//3600
resto1=total%3600
minutos=resto1//60
segundos=resto1%60
print("Tempo do evento em horas: ", horas)
print("Tempo do evento em minutos: ", minutos)
print("Tempo do evento em segundos: ", segundos)