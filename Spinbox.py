from tkinter import *
ventana=Tk()
ventana.geometry("700x600+0+0")
ventana.title("Ejemplo de Listas")
#Creando un Spinbox
lblCalif=Label(ventana,text="Calificaciones en texto:").place(x=20,y=100)
spnCalif=Spinbox(ventana,values=("Reprobado","Setenta",
                                 "Ochenta","Noventa","Cien")).place(x=200,y=100)
lblCalifN=Label(ventana,text="Calificaciones numericas:").place(x=20,y=140)
spnCalifN=Spinbox(ventana,from_=70,to=100).place(x=200,y=140)
ventana.mainloop()
