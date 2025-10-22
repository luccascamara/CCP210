#1 - Escreva um programa em Python que solicite ao usuário a entrada de dois números inteiros. O programa deve então calcular 
#e exibir:
#1.	A soma dos dois números.
#2.	A subtração do primeiro número pelo segundo.
#3.	O produto dos dois números.
#4.	O quociente da divisão do primeiro número pelo segundo.
#Observação: Caso o segundo número seja zero, o programa deve exibir uma mensagem indicando que a divisão não é possível.
#Utilize as variáveis num1 e num2 para armazenar os valores digitados pelo usuário. 
#Em seguida, atribua os resultados dos cálculos às variáveis A (soma), sub (subtração), produto (multiplicação) e quoc (divisão). 
#Exiba os resultados com mensagens apropriadas, como mostrado na imagem acima.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))



soma = num1 + num2
sub = num1 - num2
produto = num1 * num2
quoc = num1 / num2

print("O resultado da soma é:", soma)
print("O resultado da subtração é:", sub)
print("O resultado do produto é:", produto)
print("O resultado do quociente é:", quoc)
