#Desenvolva um programa em Python que leia dois números inteiros digitados pelo usuário. 
#O programa deve calcular e exibir o quociente e o resto da divisão do primeiro número pelo segundo. 
#Utilize as variáveis num1 e num2 para armazenar os números digitados pelo usuário. 
#Em seguida, realize a divisão inteira e a operação de módulo para calcular o quociente e o resto, respectivamente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

A = num1//num2
B = num1%num2

print("Quociente:", A) # Resposta da Divisão
print("Resto: ", B) 
