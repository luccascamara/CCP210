x = int(input("Digite a distância total: "))
y = int(input("Digite o total de combustível gasto: "))


def divisao(x, y):
    if y == 0:  
        return "Erro: O total de combustível gasto não pode ser zero."
    return x / y

z = divisao(x, y)

print("O total é:", z)
