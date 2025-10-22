nota = float(input("Digite a nota do aluno: "))
while nota < 0 or nota > 10 :
    nota = float(input("Nota fora do intervalo! Digite a nota do aluno novamente: "))
print("Nota aceita!")