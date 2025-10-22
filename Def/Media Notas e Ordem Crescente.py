def ordemcrescente(a,b):
    if a<b:
        t=a
        h=b
    else:
        t=b
        h=a
    return t,h
def media(c,d):
    m=((c*2)+(d*4))/6
    return m
x = float(input("Digite o valor da primeira nota: "))
y = float(input("Digite o valor da segunda nota: "))
menor,maior=ordemcrescente(x,y)
media=media(menor,maior)
print("A média do aluno é: %.2f" %media)