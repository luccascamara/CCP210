'''42 - Obter o espelho de um valor inteiro positivo conhecido.
Observação: entenda-se espelho como o valor obtido pela leitura invertida do valor.
Exemplos:
- O espelho de 3629 é 9263
- O espelho de 301 é 103
- O espelho de 2000 é 2
- O espelho de 5 é 5
'''



valor = int(input("Digite o valor:"))
r = 0
esp = 0

while valor > 0:
    r = valor % 10
    esp = (esp * 10) + r
    valor = valor // 10

print("Resultado:", esp)
