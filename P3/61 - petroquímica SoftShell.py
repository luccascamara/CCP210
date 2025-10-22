'''61- "A equipe de engenharia responsável pela programação da produção da petroquímica SoftShell calculou os componentes dos custos de produção de um determinado solvente.
 O custo fixo calculado resultou R$ 80.000,00 (o custo fixo, em geral, é composto por: 
aquisição de máquinas/equipamentos, contratação/treinamento de pessoal, alocação física do dispositivo de produção, ...). 
O custo variável resultou R$ 6,00 por litro do solvente produzido, ou seja: a produção de cada litro custa R$ 6,00 para a empresa, além da parcela denominada custo fixo (o custo variável, em geral, 
                                                                                                                                                                          é composto por matéria-prima, energia, impostos, embalagens, refugos, ...).
Sabendo-se que cada litro será vendido a R$ 10,00 
e conhecendo-se o valor do lucro que a empresa deseja obter, 
como determinar a quantidade de litros do solvente que deve ser produzida? Suponha que todo o volume produzido será vendido."'''

lucroi = float(input('Digite o lucro que gostaria: R$ '))
lminimo = 20000
litrosf = lminimo + lucroi / 4
print("Litros necessários:", litrosf)
