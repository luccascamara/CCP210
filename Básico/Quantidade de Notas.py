p = int(input("Digite o preço do produto: "))
notas100=p//100
resto1=p%100
notas50=resto1//50
resto2=resto1%50
notas20=resto2//20
resto3=resto2%20
notas10=resto3//10
resto4=resto3%10
notas5=resto4//5
resto5=resto4%5
notas2=resto5//2
resto6=resto5%2
notas1=resto6
print("Notas de 100: ", notas100)
print("Notas de 50: ", notas50)
print("Notas de 20: ", notas20)
print("Notas de 10: ", notas10)
print("Notas de 5: ", notas5)
print("Notas de 2: ", notas2)
print("Notas de 1: ", notas1)