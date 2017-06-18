import random
matriz=[[0,0,0],[0,0,0],[0,0,0]]
errores=0
aciertos=0
#print(matriz)
#Ciclo para las oportunidades
for n in range(0,5):
    for i in range(0,3):
        for j in range(0,3):
            numero=random.randrange(0,2)
            matriz[i][j]=numero
    print(matriz)
    print("En que posicion crres que no haya un Hoyo")
    print("Fila...")
    fila=int(input())
    print("Columa...")
    col=int(input())
    #Evaluando
    if(matriz[fila][col]==1):
        print("La libraste, no hay Hoyo!")
        aciertos+=1
    else:
        print("Caiste, hay Hoyo!")
        errores+=1
    #Evaluando si gano
    if(aciertos==3):
        print("!Winner")
        break
    #Evaluando si pierde
    if(errores==3):
        print("!Game Over")
        break
        
    

