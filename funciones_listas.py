lista=["Jose",33,56,7,True,"kiquesasuke@gmail.com"]
print(lista)
#Agrega un elemento al final de la lista
lista.append("Casado")
print(lista)
#Agrega mas de un elemento al final de la lista
lista.extend([56,"Jardin"])
print(lista)
#Inserta un elemento en el indice indicado
lista.insert(0,"LESH")
print(lista)
#Elimina un elemento de la lista indicandole el elemento
lista.remove(True)
print(lista)
#Cuenta los elementos repetidos
print(lista.count("LESH"))
numeros=[2,5,1,34,10,18,2]
print(numeros)
#Metodo de ordenamiento , ordena ascendentemente
numeros.sort()
print(numeros)
#Metodo de ordenamiento , ordena descendentemente
numeros.reverse()
print(numeros)
#Elimina un elemento de la lista en el indice indicado
del numeros[4]
print(numeros)
#Extraer como si fuera una pila
numeros.pop()
print(numeros)
#Extraer con parametro
numeros.pop(0)
print(numeros)

