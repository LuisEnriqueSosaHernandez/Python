from tkinter import *
def estado():
    #print("sirve")
    s=select.get()
    if s==1:
        messagebox.showinfo(title="Tu diagnostico",message="Hoy te sientes excelente "+str(s))
    elif s==2:
        messagebox.showinfo(title="Tu diagnostico",message="Hoy te sientes muy bien "+str(s))
    elif s==3:
        messagebox.showinfo(title="Tu diagnostico",message="Hoy te sientes bien "+str(s))
    elif s==4:
        messagebox.showinfo(title="Tu diagnostico",message="Hoy te sientes mal "+str(s))
    elif s==5:
        messagebox.showinfo(title="Tu diagnostico",message="Hoy te sientes pesimo "+str(s))
ventana=Tk()
ventana.geometry("700x300+0+0")
ventana.title("Ejemplo de Radiobutton")
#Creando radioButton
lblAnimo=Label(ventana,text="Como te sientes hoy?").place(x=100,y=70)
select=IntVar()
rdBAnimo=Radiobutton(ventana,text="Excelente",value=1,
                     variable=select,command=estado).place(x=100,y=100)
rdBAnimoMB=Radiobutton(ventana,text="Muy Bien",value=2,
                       variable=select,command=estado).place(x=100,y=120)
rdBAnimoB=Radiobutton(ventana,text="Bien",value=3,
                      variable=select,command=estado).place(x=100,y=140)
rdBAnimoM=Radiobutton(ventana,text="Mal",value=4,
                      variable=select,command=estado).place(x=100,y=160)
rdBAnimoP=Radiobutton(ventana,text="Pesimo",value=5,
                      variable=select,command=estado).place(x=100,y=180)
ventana.mainloop()
