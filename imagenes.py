from tkinter import *
ventana=Tk()
ventana.geometry("700x700+0+0")
ventana.config(bg="yellow")
ventana.title("Imagenes")
#Creamos la imagen
imagenL=PhotoImage(file="pizza.GIF")
lblImagen=Label(ventana,image=imagenL).place(x=100,y=100)
fondo=PhotoImage(file="estrellitas.gif")
lblFondo=Label(ventana,image=fondo).place(x=0,y=0)
ventana.mainloop()
