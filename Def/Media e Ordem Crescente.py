def ordemcrescente (a,b,c):
    if a>b: 
        a, b = b, a
    if a > c:
        a, c = c, a
    if b>c:
        b, c = c, b
    return a, b, c

def media(a,b,c):
    menor,meio,maior=ordemcrescente(a,b,c)
    media=((menor*3)+(maior*7))/10
    return media 

n1=float(input("Entre com a nota 1: "))
n2=float(input("Entre com a nota 2: "))
n3=float(input("Entre com a nota 3: "))

notasordem = ordemcrescente(n1,n2,n3)
media_final=media(n1,n2,n3)
print("A média final do aluno é: ", media_final)
