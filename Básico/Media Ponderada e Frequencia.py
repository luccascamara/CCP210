P1 = float(input("Digite a nota da P1: "))
P2 = float(input("Digite a nota da P2: "))
T1 = float(input("Digite a nota da T1: "))
T2 = float(input("Digite a nota da T2: "))
TA = int(input("Digite o total de aulas: "))
TP = int(input("Digite o total de aulas assistidas: "))
media=(3*P1+5*P2+T1+T2)/10
frequencia=(TP/TA)*100
print("Média do aluno = %.2f" %media)
print("Frequência do aluno: %.2f" %frequencia)