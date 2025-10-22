#28 – Simule a execução do algoritmo abaixo, supondo que as entradas sejam: 
#a = 10, b = 9, c = 6 e d = 5.

a = 10
b = 9
c = 6
d = 5
e = 0
f = 0
g = 0

if a > b or a > c:
    g  = a

elif b>d or b<c:
    g = d
else:
    g = c
    
if a>=b :
    f = b
    b = a
    a = f

if a>b and c<d:
    e = e + 1
else:
    e = e + 2   

if b == c:
    f = f + 2
    g = g + 2

if c!=a:
    g = g + 3
    e = e + 3
    f = f + 3

print(e)
print (e+f)
