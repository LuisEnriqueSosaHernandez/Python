resp="si"
while(resp!="no"):
    print("Ingresa el nombre del alumno")
    nom=input()
    print("Cuantas Calificaciones vas a promediar")
    nCal=int(input())
    suma=0
    for i in range(1,nCal+1):
        print("Ingresa la ",i,"a.Califacion:")
        cal=float(input())
        suma=suma+cal
    promedio=suma/nCal
    #Comprobando si el promedio es aprobatorio o reprobatorio
    if(promedio>=70):
        print("El alumno ",nom+" tiene de promedio ",promedio," Y es aprobatorio")
    else:
        print("El alumno ",nom+" tiene de promedio ",promedio," Y es reprobatorio")
    #preguntado si desea capturar otro alumno
    print("Deseas capturar a otro alumno(si/no)")
    resp=input()
              
        
    
