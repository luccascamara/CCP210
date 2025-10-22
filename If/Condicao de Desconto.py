PE = float(input("Digite o preço da etiqueta: "))
CP = int(input("Digite a condição de pagamento: "))
if CP == 1:
    PF=PE-(PE*0.10)
if CP == 2:
    PF=PE-(PE*0.05)
if CP == 3:
    PF = PE
if CP == 4:
    PF=PE+(PE*0.10)
if CP > 4:
    print("Condição inválida")
print("Valor final = %.2f" %PF)