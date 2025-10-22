'''67 - Desenvolva um programa que receba a quantidade de alunos de uma turma e as médias de cada aluno.
 O programa deve verificar se o número de alunos é válido (maior que 0) e calcular a média da turma. Para cada aluno, 
 exiba uma mensagem indicando se ele foi "APROVADO" (média maior ou igual a 6) ou "REPROVADO" (média menor que 6). 
 Por fim, mostre a média geral da turma formatada com duas casas decimais.
Regras:
- Se a quantidade de alunos for menor ou igual a zero,
 exiba a mensagem "NÃO HOUVE PROCESSAMENTO" e solicite novamente o número de alunos.
- Para cada aluno, insira sua média.
- Exiba uma mensagem individual de aprovação ou reprovação para cada média informada.
- Calcule e mostre a média geral da turma.'''


n = int(input("Digite a quantidade de alunos: "))
k = 0
while n <= 0:
    print("NÃO HOUVE PROCESSAMENTO")
    n = int(input("Digite a quantidade de alunos: "))
    
for i in range(1, n + 1, 1):
    m = float(input("Digite a média: "))
    k = k + m
    if m >= 6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    elif m < 6:
        print("VOCÊ ESTÁ REPROVADO")

media = k / n
print("Média da turma: %.2f" % media)
