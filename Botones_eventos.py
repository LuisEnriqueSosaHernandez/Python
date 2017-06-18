from tkinter import*
#Definiendo a la funcion encargada de saludar al usuario
def saluda():
    lblSaludar=Label(ventana,text="Hola "+entradaU.get(),
                     font=("Agency FB",14)).place(x=10,y=110)
def despide():
    lblDespide=Label(ventana,text="Adios "+entradaN.get(),
                     font=("Agency FB",14)).place(x=10,y=140)
    

ventana=Tk()
ventana.geometry("500x300+100+100")
ventana.title("Eventos con Botones")
lblUsuario=Label(text="Usuario:",font=("Agency FB",14)).place(x=10,y=10)
#CREANDO UN CAMPO DE TEXTO
entradaU=StringVar()
#entradaU.set("LESH")
txtUsuario=Entry(ventana,textvariable=entradaU).place(x=70,y=20)
lblUsuario=Label(text="Nombre:",font=("Agency FB",14)).place(x=10,y=50)
entradaN=StringVar()
#entradaN.set("Luis Enrique Sosa Hernandez")
txtNombre=Entry(ventana,textvariable=entradaN,width=30).place(x=70,y=60)
# Crear Botones
btnSaludar=Button(ventana,text="Saludar",command=saluda,font=("Agency FB",14),
                  width=10).place(x=300,y=20)
btnDespedir=Button(ventana,text="Despedir",command=despide,font=("Agency FB",14),
                   width=10).place(x=300,y=80)
ventana.mainloop()
