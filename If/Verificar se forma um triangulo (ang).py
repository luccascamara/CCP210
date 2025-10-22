x = float(input("Valor do lado x: "))
y = float(input("Valor do lado y: "))
z = float(input("Valor do lado z: "))
if x < y + z and y < x + z and z < z + y:
    if x == y == z:
        print("Triângulo equilátero")
    if x == y or x == z or y == z:
        print("Triângulo isosceles")
    if x != y != z:
        print("Triângulo escaleno")
else:
    print("Não formam um triângulo")