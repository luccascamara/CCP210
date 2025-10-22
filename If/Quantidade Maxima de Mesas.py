p = int(input("Digite o número de pés: "))
t = int(input("Digite o número de tampos: "))
qp=p//6
qt=t//2
qm=qp
if qm>qt:
    qt=qm 
print("A quantidade máxima é %.2d" %qm)
    