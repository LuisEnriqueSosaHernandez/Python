#Declarar una lista
#nombre_lista=[valor1,valor2,valorn]
#Creando dos listas,calif y datos
calif=[89,78,87,88,100]
datos=["Javier","Sanchez Perez",20,"El capulin #33","jav@gmail.com",True]
#Mostrando las listas
print("Mostrando la lista calificaciones:")
print(calif)
print("Mostrando la lista datos:")
print(datos)
print(calif[4])
calif[2]=[]
print(calif)
calif[2]=77
print(calif)
#calif[:]=[]
#print("Borrando la lista",calif)
print("La lista calif contiene",len(calif),"elementos")
print("La lista datos contiene",len(datos),"elementos")
#Anidando listas
anidada=["Itver","Veracruz","Mexico",datos,calif]
print("Mostrando la lista anidada")
print(anidada)
print("Datos de la escuela")
print(anidada[0:3])
print("Datos del alumno")
print(anidada[3])
print("Calificaciones del alumno")
print(anidada[4])

