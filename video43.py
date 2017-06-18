from tkinter import *
def saluda():
    messagebox.showinfo("Saludando con messagebox",message="Hola")
ventana=Tk()
ventana.geometry("700x300+0+0")
ventana.title("Ejemplo de Imagen en un boton y messagebox")
#Imagen en el boton
imgBoton=PhotoImage(file="platano.gif")
btnSaludar=Button(ventana,text="Saludar",image=imgBoton,
                  command=saluda,height=40,width=100).place(x=100,y=100)

ventana.mainloop()
