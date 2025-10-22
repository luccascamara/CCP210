#55 -Reservatório de Água (Cálculo de tempo através de capacidade e vazão):

C = int(input("Digite a capacidade do reservatório: "))
V = int(input("Digite a vazão da bomba: "))

Ts = C // V
Qh = Ts // 3600
R = Ts % 3600
Qm = R // 60
Qs = R % 60

print("Horas para abastecer o reservatório:", Qh)
print("Minutos para abastecer o reservatório:", Qm)
print("Segundos para abastecer o reservatório:", Qs)
