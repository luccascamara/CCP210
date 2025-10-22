a = float(input("Valor a: "))
b = float(input("Valor b: ")) 
c = float(input("Valor c: "))
if a >= b and a >= c:
    maior=a
if b >= a and b >= c:
    maior=b
if c >= a and c >= b: 
    maior=c
print("O maior valor é: ", maior)