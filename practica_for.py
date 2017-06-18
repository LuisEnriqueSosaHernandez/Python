print("Programa para calcular Promedio de n calificaciones")
print("Ingrese el nombre del alumno")
nombre=input()
print("Ingrese el numero de materias a promediar")
numCal=input()
numCal=int(numCal)
#Realizando un ciclo para pedir n calificaciones
suma=0
calificacion=0
for i in range(1,numCal+1):
    print("Ingresa la: ",i,"a.Calificacion:")
    calificacion+=float(input())
#Calculando el promedio
calificacion/=numCal
print("El promedio del alumno: ",nombre," es: ",calificacion)
    
    
  
