#32 - "Uma empresa decidiu dar uma gratificação de Natal aos seus funcionários baseada no número de horas extras 
#e no número de horas que o funcionário faltou ao trabalho. 
#O valor do prêmio é obtido pela consulta na tabela a seguir, em M é a quantidade de minutos equivalente à quantidade de horas obtida 
#pela expressão:
#M = (quantidade de horas extras) - 2/3 * (quantidade de horas ausentes)

#premios = 
#">2400": 500,
#"1800 até 2400": 400,
#"<=1800": 100

#Construir e utilizar uma função que tenha como parâmetros de entrada a quantidade de horas extras (HE) 
#e a quantidade de horas que o funcionário faltou (HF) e como parâmetro de saída o valor do prêmio.
#Exemplo da Tela de Execução:
#digite a quantidade de horas extras: 20
#digite a quantidade de horas que faltou: 4
#O valor do prêmio é: 100
#É obrigatório o uso da função def.
#Usar CTRL C para copiar o código e a tela de execução e CTRL V para colar o código e a tela de execução. 
#Usar na Tela de Execução 45 horas extras e 4 horas que faltou.
#É proibido o uso de ALT PrtSc.

def Premios(A,B):
    M = ((A)-2/3*(B))*60
    if M >2400:
        premio = 500
    elif M > 1800 and M < 2400:
        premio = 400
    else:
        premio = 100
    return premio


HE = int(input("Digite as horas extras: "))
HA = int(input("Digite as horas ausentes: "))

P = Premios(HE,HA)
print(P)

#Digite as horas extras: 45
#Digite as horas ausentes: 4
#500
