a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
r=a%b
while r>0:
    a=b
    b=r
    r=a%b
print("MDC=", b)