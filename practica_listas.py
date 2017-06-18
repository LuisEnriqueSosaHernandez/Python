def capturar():
    global lista
    lista=[]
    print("Cuantos elementos tendra la lista?")
    n=int(input())
    for i in range(0,n):
        print("Ingresa el elemento del indice ",i)
        elemento=input()
        lista.insert(i,elemento)
def mostrar():
    print(lista)
def agregar():
    print("Ingresa el elemento que desea agregar:")
    elemento=input()
    print("Ingresa el indice:")
    indice=int(input())
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud or indice<0):
        print("El indice debe estar entre 0 y :",longitud)
    else:
        lista.insert(indice,elemento)
        print("Elemento agregado")
def eliminar():
    print("Ingresa el indice del elemento a eliminar:")
    indice=int(input())
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud-1 or indice<0):
        print("El indice debe estar entre 0 y :",longitud-1)
    else:
        del lista[indice]
        print("Elemento eliminado")
def modificar():
    print("Ingresa el indice del elemento que desea modificar:")
    indice=int(input())
    print("Ingrese el nuevo valor del elemento")
    elemento=input()
    longitud=len(lista)
    longitud=int(longitud)
    if(indice>longitud-1 or indice<0):
        print("El indice debe estar entre 0 y :",longitud-1)
    else:
         lista[indice]=elemento
         print("Elemento modificado")
def principal():
    opcion="1"
    while(opcion!="6"):
        print("Manipulacion de una lista")
        print("1.Capturar una lista")
        print("2.Mostrar lista")
        print("3.Agregar elemento a la lista")
        print("4.Eliminar elemento")
        print("5.Modificar elemento")
        print("6.Salir")
        print("Elige una opcion")
        opcion=input()
        if(opcion=="1"):
            capturar()
        elif(opcion=="2"):
            mostrar()
        elif(opcion=="3"):
            agregar()
        elif(opcion=="4"):
            eliminar()
        elif(opcion=="5"):
            modificar()
        elif(opcion=="6"):
            print("Programa terminado")
        else:
            print("Opcion incorrecta")
principal()
            
        
            
            
