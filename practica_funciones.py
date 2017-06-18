def menu():
    print("1.Dolar")
    print("2.Dolar Canandiense")
    print("3.Euro")
    print("4.Libra Esterlina")
    print("5.Centenario")
    print("Cuanto tienes en pesos mexicanos?")
    global pesos
    pesos=float(input())
    print("Que tipo de cambio deseas realizar?")
    global cambio
    cambio=int(input())
    #Evaluando tipo de cambio
    if(cambio==1):
        #Llamando funcion folares
        dolares()
    elif(cambio==2):
        dolaresCanadienses()
    elif(cambio==3):
        Euros()
    elif(cambio==4):
        LibraEsterlina()
    elif(cambio==5):
        Centenario()
    else:
        print("Opcion Incorrecta")
    print("Deseas hacer otro tipo de cambio(si/no)")
    global resp
    resp=input()
    resp=resp.lower()
    otraVez()
       
def dolares():
    print("Cual es el precio del dolar el dia de hoy")
    global precioD
    precioD=float(input())
    global dinerito
    dinerito=pesos/precioD
    print("Tienes ",dinerito," Dolares")
def dolaresCanadienses():
    print("Cual es el precio del dolar Canadiense el dia de hoy")
    global precioDC
    precioDC=float(input())
    global dinerito
    dinerito=pesos/precioDC
    print("Tienes ",dinerito," Dolares Canadienses")
def Euros():
    print("Cual es el precio del Euro el dia de hoy")
    global precioE
    precioE=float(input())
    global dinerito
    dinerito=pesos/precioE
    print("Tienes ",dinerito," Euros")
def LibraEsterlina():
    print("Cual es el precio de la Libra Esterlina el dia de hoy")
    global precioL
    precioL=float(input())
    global dinerito
    dinerito=pesos/precioL
    print("Tienes ",dinerito," Libras Esterlinas")
def Centenario():
    print("Cual es el precio del Centenario el dia de hoy")
    global precioC
    precioC=float(input())
    global dinerito
    dinerito=pesos/precioC
    print("Tienes ",dinerito," Centenarios")
    
    
    
def otraVez():
    while(resp!="no"):
        menu()
#Llamando a la funcion menu
menu()
    
