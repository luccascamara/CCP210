def maximo(a,b):
    if a>b:
        m=a
    else:
        m=b
    return m
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: ")) 
maior=maximo(x,y)       
print("O maior número é: ", maior)