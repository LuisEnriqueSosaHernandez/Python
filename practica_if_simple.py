print("Escribe tus ingresos mensuales: ")
ingresos=input()
ingresos=float(ingresos)
print("Escribe tus egresos")
egresos=input()
egresos=float(egresos)
efectivo=ingresos-egresos
#print("Tienes: ",efectivo," Pesos en efectivo")
#Evaluando al efectivo
if(efectivo<0):
    print("Tienes: ",efectivo," Pesos y estas en numeros rojos")
    print("Como es que sobrevives?")
    
if(efectivo==0):
    print("Tienes: ",efectivo," Pesos, ponte a trabajar mas")
if(efectivo>0 and efectivo<=100):
     print("Tienes: ",efectivo," Pesos, parece que te va bien")
if(efectivo>100 and efectivo<10000):
     print("Tienes: ",efectivo," Pesos, Pareces que vives bien")
if(efectivo>=10000):
     print("Tienes: ",efectivo," Pesos, Tu si vives como debe de ser")
