#13 - Uma determinada marca de televisores apresenta duas linhas de TVs (série 100 e a série 200). 
#A distância ideal entre o sofá e o televisor depende do tamanho da tela e também da própria série, conforme as tabelas abaixo:

# Série 100

#{"Distância (metros)": "Até 1.4", "Tamanho da Tela (Polegadas)": 32},
#{"Distância (metros)": "De 1.5 a 2.6", "Tamanho da Tela (Polegadas)": 37},
#{"Distância (metros)": "Acima de 2.6", "Tamanho da Tela (Polegadas)": 42},

# Série 200

#{"Distância (metros)": "Até 2.8", "Tamanho da Tela (Polegadas)": 42},
#{"Distância (metros)": "De 2.9 a 3.6", "Tamanho da Tela (Polegadas)": 50},
#{"Distância (metros)": "Acima de 3.6", "Tamanho da Tela (Polegadas)": 61},

#Conhecendo-se a distância e a série pretendida por certo cliente, obtenha o tamanho ideal de sua televisão.

#Digite a distância (m): 3.1 
#Digite a série: 200 
#Tamanho da televisão (pol): 50


D = float(input("Digite a distância (m): "))
S = float(input("Digite a série: "))

if(S == 100):
    if D <= 1.4:
        print("Tamanho da televisão (pol): 32")
    if D > 1.5 and D <= 2.6:
        print("Tamanho da televisão (pol): 37")
    if D >= 2.6:
        print("Tamanho da televisão (pol): 42")

if(S == 200):
    if D <= 2.8:
        print("Tamanho da televisão (pol): 42")
    if D > 2.9 and D <= 3.6:
        print("Tamanho da televisão (pol): 50")
    if D > 3.6:
        print("Tamanho da televisão (pol): 61")
