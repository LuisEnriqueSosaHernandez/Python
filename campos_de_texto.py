from tkinter import*
ventana=Tk()
ventana.geometry("500x300+100+100")
ventana.title("Ejemplo con campos de texto")
lblUsuario=Label(text="Usuario:",font=("Agency FB",14)).place(x=10,y=10)
#CREANDO UN CAMPO DE TEXTO
entradaU=StringVar()
entradaU.set("LESH")
txtUsuario=Entry(ventana,textvariable=entradaU).place(x=70,y=20)
lblUsuario=Label(text="Nombre:",font=("Agency FB",14)).place(x=10,y=50)
entradaN=StringVar()
entradaN.set("Luis Enrique Sosa Hernandez")
txtNombre=Entry(ventana,textvariable=entradaN).place(x=70,y=60)

ventana.mainloop()
