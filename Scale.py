from tkinter import *
def temperatura():
    temper="Estamos a "+str(valor.get())
    messagebox.showinfo(title="Temperatura",message="Estamos a "+temper+" Grados centigrados")
ventana=Tk()
ventana.geometry("700x300+200+50")
ventana.title("Ejemplo de Scale(Slider)")
#Creando el Scale
valor=IntVar()
sclBarra=Scale(ventana,label="Temperaturas C°",orient=HORIZONTAL,
               width=25,from_=-15,to=45,tickinterval=5,
               length=350,variable=valor).place(x=100,y=100)
btnVer=Button(ventana,text="Ver Temperatura",command=temperatura).place(x=235,y=200)
ventana.mainloop()
