cadena="hola como estas"
cadena2="1234"
#Devuelve la cadena con el primer caracter en mayuscula y todo lo demas en minscula
print(cadena.capitalize())
#centra la cadena de texto con los espacios indicados
print(cadena.center(30))
#Tamanio de una cadena
print(len(cadena))
#Devuelve el numero de veces que se encuentra una cadena en otra
print(cadena.count("o",0,len(cadena)))
#Devuelve true si todos los caracteres son alfanumericos
print(cadena.isalnum())
#Devuelve tru si todos son numericos
print(cadena2.isdigit())
#true si todos los caracteres estan en minusculas
print(cadena.islower())
#true si todos los caracteres estan en mayusuculas
print(cadena.isupper())
#Convierte una cadena en minuscula
print(cadena.lower())
#Convierte una cadena en mayuscula
print(cadena.upper())
#Reemplaza una cadena por otra
print(cadena.replace("como estas","que pedo uvu"))
#extraer determinado numero de cadenas
print(cadena[2])
print(cadena[2:14])

