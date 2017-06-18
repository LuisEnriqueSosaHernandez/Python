print("Ingrese el nombre del empleado")
nombre=input()
print("Ingrese la horas trabajadas esta semana ", nombre,":")
horas=input()
horas=int(horas)
print("Cuanto se paga por hora")
precioH=input()
precioH=float(precioH)
if(horas<=40):
    pago=horas*precioH
    print("El sueldo final de: ",nombre," Es $", pago)
elif(horas>40 and horas<=50):
    extrasDobles=horas-40
    print("Horas Extras dobles: ",extrasDobles)
    pago=40*precioH
    print("Sueldo Base: $",pago)
    pagoDoble=extrasDobles*precioH*2
    print("Pago de horas extras dobles: $",pagoDoble)
    pagoFinal=pago+pagoDoble
    print("El sueldo final para: ",nombre," es: ",pagoFinal)
elif(horas>50 and horas<=60):
    extrasTriples=horas-50
    print("Horas extra dobles: 10")
    print("Horas extra triples: ",extrasTriples)
    pago=40*precioH
    print("Sueldo Base: $",pago)
    pagoDoble=10*precioH*2
    print("Pago de horas extras dobles: $",pagoDoble)
    pagoTriple=extrasTriples*precioH*3
    print("Pago de horas extras triples: $",pagoTriple)
    pagoFinal=pago+pagoDoble+pagoTriple
    print("El sueldo final para: ",nombre," es: ",pagoFinal)
else:
    
    print("Horeas extra Dobles 10")
    print("Horeas extra Triples 10")
    pago=40*precioH
    print("Sueldo Base: $",pago)
    pagoDoble=10*precioH*2
    print("Pago de horas extras dobles: $",pagoDoble)
    pagoTriple=10*precioH*3
    print("Pago de horas extras triples: $",pagoTriple)
    print("Incentivo por trabajar mas de 60 horas:2000")
    pagoFinal=pago+pagoDoble+pagoTriple+2000
    print("El sueldo final para: ",nombre," es: ",pagoFinal)
    





















    
    
