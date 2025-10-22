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
num2 = int(input("Digite o sgundo número: "))

if num1 ==0 or num2 ==0:
    print("Erro: O número não pode ser zero, tente novamente com outro número.")
else: 
    soma = num1 + num2
    sub = num1 - num2
    quoc = num1 * num2
    div = num1 / num2
    
    print("O Resultado da Soma é:", soma)
    print("O Resultado da Subtração é:", sub)
    print("O Resultado do Quociente é:", quoc)
    print("O Resultado da Divisão é:", div)


    
    