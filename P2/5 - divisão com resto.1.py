#Escreva um programa em Python que solicite ao usuário a entrada de um número inteiro de três dígitos. 
#Em seguida, o programa deve calcular a soma dos algarismos individuais desse número e exibir o resultado.
#Por exemplo, se o usuário digitar o número 253, o programa deve calcular 2 + 5 + 3 = 10 
#e exibir "Resultado da soma dos algarismos: 10".
#O código do programa pode ser estruturado da seguinte forma:
#1.	Leia o número de três dígitos digitado pelo usuário.
#2.	Separe cada algarismo do número (centena, dezena e unidade).
#3.	Calcule a soma dos três algarismos.
#4.	Exiba o resultado da soma.
#Observação: Considere que o número de entrada sempre terá três dígitos (entre 100 e 999).

num = int(input("Digite um número com 3 algarismos: "))

alg = num//100 # Nesse caso o numero 253 é dividido por 100 e o resultado é 2
r = num%100 # o num%100 é responsável por realizar uma divisão com resto
# No caso 253/100 é igual a 2 com 53 de resto.
alg2 = r//10 # R/10 é igual a 5
alg3 = r%10 # R%1o é igual a 3
soma = alg + alg2 + alg3

print("Resultado da soma dos algorismos: ", soma)
