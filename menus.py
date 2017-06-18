from tkinter import *
def abrir():
    #messagebox.showinfo(title="Eehhh",message="Hiciste click en abrir")
    venAbrir=Tk()
    venAbrir.geometry("400x200+100+100")
    venAbrir.title("Otra Ventana")
    venAbrir.mainloop()
ventana=Tk()
ventana.geometry("600x600+0+0")
ventana.title("Menus")
#crear barra de menus
barraMenu=Menu(ventana)
#crear los menus
mnuArchivo=Menu(barraMenu)
mnuEdicion=Menu(barraMenu)
#crear los comandos de los menus
mnuArchivo.add_command(label="Abrir",command=abrir)
mnuArchivo.add_command(label="Nuevo")
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Guardar")
mnuArchivo.add_command(label="Cerrar")
mnuArchivo.add_command(label="Salir",command=ventana.destroy)
#Otro menu
mnuEdicion.add_command(label="Copiar")
mnuEdicion.add_command(label="Pegar")
mnuEdicion.add_command(label="Deshacer")
mnuEdicion.add_command(label="Rehacer")
#Agregar los menus a la barra de menus
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
barraMenu.add_cascade(label="Edicion",menu=mnuEdicion)
#indicamos que la barra de menus estara en la ventana
ventana.config(menu=barraMenu)
ventana.mainloop()
