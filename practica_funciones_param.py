resp="si"
aciertos=0
errores=0
intentos=0;
def sumar(n1,n2):
    print("Cuanto suman",n1,"+",n2,"?")
    global resulUsuario
    resulUsuario=input()
    resulUsuario=float(resulUsuario)
    global resulReal
    resulReal=n1+n2
    if(resulReal==resulUsuario):
        print("Resultado Correcto")
        global aciertos
        aciertos+=1
    else:
        print("Resultado Incorrecto")
        global errores
        errores+=1
    global intentos
    intentos+=1
def resta(n1,n2):
    print("Cuanto restan",n1,"-",n2,"?")
    global resulUsuario
    resulUsuario=input()
    resulUsuario=float(resulUsuario)
    global resulReal
    resulReal=n1-n2
    if(resulReal==resulUsuario):
        print("Resultado Correcto")
        global aciertos
        aciertos+=1
    else:
        print("Resultado Incorrecto")
        global errores
        errores+=1
    global intentos
    intentos+=1
def multiplicar(n1,n2):
    print("Cuanto es el producto de ",n1,"*",n2,"?")
    global resulUsuario
    resulUsuario=input()
    resulUsuario=float(resulUsuario)
    global resulReal
    resulReal=n1*n2
    if(resulReal==resulUsuario):
        print("Resultado Correcto")
        global aciertos
        aciertos+=1
    else:
        print("Resultado Incorrecto")
        global errores
        errores+=1
    global intentos
    intentos+=1
def division(n1,n2):
    print("Cuanto es la division de ",n1,"/",n2,"?")
    global resulUsuario
    resulUsuario=input()
    resulUsuario=float(resulUsuario)
    global resulReal
    resulReal=n1/n2
    if(resulReal==resulUsuario):
        print("Resultado Correcto")
        global aciertos
        aciertos+=1
    else:
        print("Resultado Incorrecto")
        global errores
        errores+=1
    global intentos
    intentos+=1
#Definiendo el diagnostico
def diagnostico(intentos,er):
    global prom
    prom=intentos/2
    if(aciertos>=prom):
        print("Andas bien en Operaciones Aritmeticas")
    else:
        print("Andas mal en Operaciones Aritmeticas")    
def resultados(ac,er):
    print("Resultados Correctos ",ac)
    print("Resultados Incorrectos ",er)
    diagnostico(ac,er)
while(resp!="no"):
    print("Ingrese un numero")
    global num1
    num1=input()
    num1=float(num1)
    print("Ingrese otro numero")
    global num2
    num2=input()
    num2=float(num2)
    #Llamando a la funcion sumar
    sumar(num1,num2)
    resta(num1,num2)
    multiplicar(num1,num2)
    division(num1,num2)
    print("Deseas seguir participando(si/no)?")
    global resp
    resp=input()
    resp.lower()
resultados(aciertos,errores)

    
    
