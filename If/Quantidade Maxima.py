A = int(input("Digite a quantidade do tipo A: "))
B = int(input("Digite a quantidade do tipo B: "))
C = int(input("Digite a quantidade dp tipo C: "))
QA=A//2
QB=B//3
QC=C//7 
QM=QA
if QB<QM:
    QM=QB
if QC<QM: 
    QM=QC 
print("Quantidade máxima: ", QM)