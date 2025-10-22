#33 - No algoritmo a seguir todas as variáveis são do tipo inteiro. 
#Simule sua execução supondo como entrada para n como valor 541.  
#Marque no quadro de resposta a alternativa que contém a resposta para as variáveis a, soma e d.

#leia n
#a ← n div 100;
#b ← (n mod 100) div 10;
#c ← (n mod 100) mod 10;
#inv ← c * 100 + b * 10 + a;
#soma ← n + inv;
#a ← (soma div 100);
#b ← ((soma mod 100) div 10) * 2;
#c ← ((soma mod 100) mod 10) * 3;
#d ← (a + b + c) m

n = int(input("leia n: "))
a = n // 100
b = (n % 100) // 10
c = (n % 100) % 10
inv = (c * 100) + (b * 10) + a
soma = n + inv
a = soma // 100
b = ((soma % 100) // 10) * 2
c = ((soma % 100) % 10) * 3
d = (a + b + c) % 10
print("Valor de A:", a)
print("Valor da soma:", soma)
print("Valor de D:", d)
