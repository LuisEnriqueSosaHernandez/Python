from tkinter import *
#creacion ventana
ventana=Tk()
#Tamanio
ventana.geometry("500x300+100+100")
#titulo
ventana.title("Ventana con etiquetas(Labels)")
#etiquetas
#agregar etiquetas a ventana
#lblUsuario=Label(text="Usuario:").place(x=100,y=20)#.pack()
#lblUsuario2=Label(text="kiquesasuke").place(x=110,y=20)#.pack()
lblUsuario=Label(text="Usuario:",fg="Green",background="Yellow").grid(row=0,column=0)#,sticky=W#E)
lblUsuario2=Label(text="kiquesasuke",fg="Gray").grid(row=0,column=1)
lblNom=Label(text="Nombre:",fg="Green").grid(row=1,column=0)
lblNombre=Label(text="Luis Enrique",fg="Purple").grid(row=1,column=1)
#agregar etiquetas a ventana
#lblUsuario.pack()
#lblUsuario2.pack()
ventana.mainloop()
