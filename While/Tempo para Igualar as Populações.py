A = 100000 
B = 250000 
t = 0
while A <= B:
    A=A+A*0.03
    B=B+B*0.02
    t=t+1
print("Serão necessários: ", t)
    