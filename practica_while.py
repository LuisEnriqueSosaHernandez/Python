print("Ingrese un numero")
num=int(input())
numElevados=0;
while(num!=0):
    numCubo=num*num*num
    print("El numero ",num," elevado al cubo es: ",numCubo)
    numElevados+=1
    print("Ingrese un numero: ")
    num=int(input())
print("La cantidad de numeros elevados al cubo fue: ",numElevados)
