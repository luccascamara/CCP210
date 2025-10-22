def entrada():
    media=[]
    print ("Digite 4 notas:")
    for i in range (9):
        acum = 0
        print ("Notas do aluno %d" %(i+1))
        for i in range (4):
            n = float (input())
            while n<0 or n>10:
                print ("Nota fora do intervalo, digite novamente")
                n = float (input())
            acum=acum+n
        m = acum/4
        media.append(m)
    return(media)
def aprovados(media):
    ct = 0
    for i in range(9):
        if media[i] >= 7.0:
            ct=ct+1
    return ct
def saida (ap,media):
    print (media) 
    print ("Qtde aprovados:", ap) #principal 
md=entrada()
ap = aprovados(md)
saida(ap.md)