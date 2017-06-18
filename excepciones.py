"""
try:
    Codigo donde puede ocurrir una excepcion
    >>>
    >>>
    >>>
except nombre_excepcion
    mensaje de error
"""
#Capturando division entre cero ZeroDivisionError
try:
    print(7/0)
except ZeroDivisionError:
    print("Division entre cero")
#Capturando la excepcion ValueError
try:
    print("Ingresa un numero entero")
    numero=int(input())
except ValueError:
    print("Solo se aceptan numeros")
#Capturando error x
try:
    print("Ingresa un numero con decimales")
    numD=floa(input())
except:
    print("Ha ocurrido un error")
