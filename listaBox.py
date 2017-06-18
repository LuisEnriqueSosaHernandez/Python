from tkinter import *
#Funcion para agregar elementos a la lista
def agrega():
    #print("Si agrega")
    lstMaterias.insert(END,entrada.get())
ventana=Tk()
ventana.geometry("700x600+0+0")
ventana.title("Ejemplo de Listas")
lblMaterias=Label(ventana,text="Materia:").place(x=100,y=100)
#Creando una lista
lstMaterias=Listbox(ventana,width=50)
lstMaterias.insert(0,"Programacion Basica")
lstMaterias.insert(1,"Programacion Orientada a objetos")
lstMaterias.insert(2,"Sistemas Operatoivos")
lstMaterias.insert(3,"Topicos Avanzados de Programacion")
#Eliminando un elemento de la lista
#lstMaterias.delete(0,1)
#lstMaterias.delete(2)
lstMaterias.place(x=100,y=120)
lblMat=Label(ventana,text="Materia:").place(x=100,y=20)
entrada=StringVar()
txtMateria=Entry(ventana,textvariable=entrada,width=40).place(x=150,y=20)
btnAgregar=Button(ventana,text="Agregar",height=2,
                  width=20,command=agrega).place(x=400,y=20)
ventana.mainloop()
