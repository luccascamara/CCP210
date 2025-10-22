VC = float(input("Digite o valor registrado na nota: "))
M = int(input("Digite o número correspondente ao mês de licenciamento: "))
meses=12-M
IPVAA=0.4*VC
IPVAP=(meses/12)*IPVAA
print("O valor do IPVA é %.2f" %IPVAP)