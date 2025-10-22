'''66 - Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média M=(N1+N2∗2+N3∗3)/6M = (N1 + N2*2 + N3*3)/6M=(N1+N2∗2+N3∗3)/6 alcançada pelo aluno e apresentar:
a) A mensagem "Aprovado", se a média for maior ou igual a 5, com a respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor do que 5, com a respectiva média alcançada.'''



x = float(input("Digite a 1ª nota: "))
y = float(input("Digite a 2ª nota: "))
z = float(input("Digite a 3ª nota: "))

media = (x + y*2 + z*3) / 6

if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")
