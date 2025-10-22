v = int(input("Digite a vazão da bomba: "))
c = int(input("Digite a capacidade do reservatório: "))
Ts=c//v
Qh=Ts//3600
R=Ts%3600
Qm=R//60
Qs=R%60
print("Horas: ", Qh)
print("Minutos: ", Qm)
print("Segundos: ", Qs)