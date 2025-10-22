#22 - O número 3025 tem a seguinte característica:
#0 + 25 = 55 e 55² = 3025.
#Ou, colocado de forma genérica, um número XYZW pode ter a seguinte característica:
#(XY) + (ZW) = RS e (RS)² = XYZW.
#Como verificar se um número inteiro positivo de quatro algarismos apresenta esta característica.
#Se sim, classificar o número como TIPO I.
#Se (XY) + (ZW) = RS e (RS)² > XYZW então classificar o número como TIPO II.
#Se (XY) + (ZW) = RS e (RS)² < XYZW então classificar o número como TIPO III.
#Fazer uma verificação na entrada de dados para assegurar que o número tem quatro algarismos e apresentar na saída uma das mensagens:
#“TIPO I” ou “TIPO II” ou “TIPO III”.
#Construir e utilizar uma função que tenha como parâmetro de entrada um número inteiro positivo de quatro algarismos 
#e como retorno o quadrado da soma descrita acima, ou seja: se a entrada for 3025, devolve para o programa principal o valor 3025, 
#ou se a entrada for 1521, devolve para o programa principal o valor 1296.
#O código abaixo apresenta a descrição da função calc, mas está incompleto.

def calc(num):
    # Verifica se o número possui exatamente 4 algarismos
    if num > 1000 or num < 9999:  # Correção: Deve ser `1000 <= num <= 9999`
        a = num // 100  # Divide o número para obter os dois primeiros dígitos (XY)
        b = num % 100   # Obtém os dois últimos dígitos (ZW)
        c = a + b       # Soma XY + ZW
        d = c * c       # Calcula o quadrado da soma (c^2)

        # Verifica o tipo do número conforme as condições dadas
        if d == num:     # Se o quadrado for igual ao número, é Tipo I
            return "Tipo I"
        if d > num:      # Se o quadrado for maior que o número, é Tipo II
            return "Tipo II"
        if d < num:      # Se o quadrado for menor que o número, é Tipo III
            return "Tipo III"

# Solicita ao usuário que insira um número de 4 algarismos
n = int(input("Entre número de 4 algarismos: "))

# Garante que o número digitado esteja dentro do intervalo permitido (4 algarismos)
while n < 1000 or n > 9999:
    n = int(input("Entre número de 4 algarismos: "))

# Calcula e imprime o tipo do número usando a função calc
print(calc(n))
