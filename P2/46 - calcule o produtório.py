'''46 - Crie um programa que receba uma sequência de números inteiros positivos 
e calcule o produtório (multiplicação) de todos os números pares inseridos. O programa deve atender às seguintes condições:
- O programa encerra a execução quando o número 0 for digitado.
- Caso o número digitado seja negativo, o programa deve solicitar novamente um número válido (inteiro e positivo).
- O primeiro número digitado pode ser 0, e, nesse caso, o produtório será 0.
- Se nenhum número par for inserido antes de digitar 0, o programa deve retornar o resultado 0.
- O programa deve exibir o resultado do produtório dos números pares ao final da execução.
Exemplo de saída esperada:
•	Entrada: 4, 6, 3, 0
Saída: "O produtório dos números pares é: 24"
•	Entrada: 0
Saída: "O produtório dos números pares é: 0"'''


n = -1  # Valor aleatório de "n" para entrar no WHILE
p = 0  # Valor inicial do produtório consecutivo
k = 0  # Contador para caso o primeiro número digitado seja "0"

while n != 0:  # Verificação de "n" para encerrar a simulação
    n = int(input("Digite o valor inteiro e positivo: "))
    while n < 0:  # Verificação se o valor é válido, se ele é inteiro e positivo
        print("Valor incorreto, apresente valor inteiro e positivo")
        n = int(input("Digite o valor inteiro e positivo: "))

    if n % 2 == 0 and n != 0:  # Se "n" for par e diferente de "0", entra no IF
        if p == 0:  # Verifica se "p" ainda é zero
            p = n  # Se "p" for zero, "p" recebe o valor de "n" para dar procedência às próximas operações
        elif p != 0:  # Se "p" já tiver um valor, basta apenas multiplicá-lo pelo novo "n" e jogar esse novo valor de volta ao "p"
            p = p * n

    if n == 0 and k == 0:  # Se de início colocar-se "0", então "p" não deverá ter nenhum valor.
        p = 0  # Ambos "n" e "k" são comparados para saber se o primeiro valor da simulação foi "0", e "k" também será "0" devido ao contador.
    k = k + 1  # Somente nesse ponto "k" atribui outros valores para sair das condições que podiam implicar nos resultados

print("O produtório dos números pares é: ", p)
