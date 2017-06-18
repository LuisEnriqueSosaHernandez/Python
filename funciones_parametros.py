def saludar(nombre,an):
    print("Hola",nombre," Hoy te sientes ",an)
def bienvenida(nombre,an):
    print("Hola ",nombre," Bienvenido a la fiesta,Te sientes ",an," Y te vas a sentir mejor")
def despedir(nombre,an):
    print("Adios ",nombre,"Te sientes ",an," Y que termine Ok tu dia")
print("Ingresa tu nombre:")
nombre=input()
print(nombre," Como te sientes hoy?")
animo=input()
saludar(nombre,animo)
bienvenida(nombre,animo)
despedir(nombre,animo)
