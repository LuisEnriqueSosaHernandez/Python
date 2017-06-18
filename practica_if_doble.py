print("Ingrese el nombre del empleado")
nombre=input()
print("Ingrese la horas trabajadas esta semana ", nombre,":")
horas=input()
horas=int(horas)
print("Cuanto se paga por hora")
precioH=input()
precioH=float(precioH)
#Evaluando el salario
if(horas<=40):
    pago=horas*precioH
    print("El sueldo Final de ",nombre,"Es: $",pago)
else:
    extras=horas-40
    pago=40*precioH
    pago+=extras*precioH*2
    print("El sueldo Final de ",nombre,"Es: $",pago)
