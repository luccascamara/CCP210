peso=[]
altura=[]
IMC=[]
for i in range (5):
    peso.append(float(input("digite o peso da pessoa %d:" %(i+1))))
    altura.append(float(input("digite o altura da pessoa %d:" %(i+1))))
for j in range (5):
    IMC.append(peso[j]/(altura[j]**2)）
for j in range (5):
    print ("peso=", peso[j],"altura=",altura[j],"IMC=%.2f" %IMC[j])
    