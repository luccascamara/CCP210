'''44- Considere o seguinte problema: Dado um número inteiro positivo n, 
calcular e exibir o valor da soma S: S = 1/n + (2/n-1) + (3/n-2) + ... + n/1 O programa não pode permitir a entrada de dados inválidos, 
ou seja, um valor de n menor ou igual a zero.'''

n = -1
while n <= 0:
    n = int(input("Digite o número de parcelas: "))
soma = 0
den = n

for k in range(1, n + 1, 1):  # SE VOCÊ QUISER REPETIR UM BLOCO 20 VEZES VOCÊ
    soma = soma + k / den    # # PODE ALTERAR AQUI
    den = den - 1
print("soma = %.2f" % soma)
