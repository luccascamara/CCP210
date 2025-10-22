l = int(input("Digite a quantidade de livros: "))
A = (0.25*l)+7.5
B = (0.50*l)+2.50
if A > B:
    print("A melhor opção de desconto é a A")
if A < B:
    print("A melhor opção de desconto é a B")
if A == B: 
    print("Ambas as opções de desconto são boas")