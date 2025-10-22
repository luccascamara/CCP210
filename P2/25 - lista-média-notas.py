#25 - Faça um programa que peça as três notas (entre 0 e 10) de 4 alunos, 
#calcule e armazene numa lista a média aritmética de cada aluno.
#Imprima a média aritmética de cada aluno e o número de alunos com média maior ou igual a 7.0

#Digite 3 notas:
#Notas do aluno 1:
#1
#2
#3
#Notas do aluno 2:
#5
#5
#6
#Notas do aluno 3:
#2
#2
#7
#Notas do aluno 4:
#10
#7
#4
#[3.0, 5.0, 5.0, 7.0]
#Qtde aprovados: 1

medias = [] # Inicializa uma lista vazia para armazenar as médias dos alunos
aprov = 0 # Inicializa o contador de aprovados (alunos com média >= 7.0) como 0

print("Digite 3 notas: ") # Exibe uma mensagem para orientar o usuário a inserir as notas

# Laço de repetição para iterar sobre os 4 alunos (range(4) gera valores de 0 a 3)
for i in range(4):
    # Exibe qual aluno está sendo processado (i+1 ajusta o índice para começar do 1)
    print("Notas do aluno %d: " % (i+1))
    
    # Solicita as três notas do aluno e converte as entradas de texto para números decimais
    nota1 = float(input())  # Primeira nota
    nota2 = float(input())  # Segunda nota
    nota3 = float(input())  # Terceira nota
    
    # Calcula a média aritmética das três notas
    media = (nota1 + nota2 + nota3) / 3
    
    # Adiciona a média calculada à lista de médias
    medias.append(media)

# Imprime a lista de médias de todos os alunos
print(medias)

# Outro laço para verificar quantos alunos têm média maior ou igual a 7.0
for i in range(0, 4):
    # Verifica se a média do aluno atual é maior ou igual a 7.0
    if (medias[i] >= 7):
        # Incrementa o contador de aprovados
        aprov = aprov + 1

# Imprime a quantidade total de alunos aprovados
print("Qtde aprovados: ", aprov)