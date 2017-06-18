from tkinter import*
def lenguajes():
    c=selC.get()
    cc=selCC.get()
    java=selJava.get()
    ruby=selRuby.get()
    php=selPhp.get()
    python=selPython.get()
    print("Valor de C..",c)
    print("Valor de C++..",cc)
    print("Valor de java..",java)
    print("Valor de ruby..",ruby)
    print("Valor de php..",php)
    print("Valor de python..",python)
    global cadena
    cadena=""
    if c==1:
        cadena+="C,"
    if cc==1:
        cadena+="C++,"
    if java==1:
        cadena+="Java,"
    if ruby==1:
        cadena+="Ruby,"
    if php==1:
        cadena+="Php,"
    if python==1:
        cadena+="Python"
    #Enviando los lenguajes seleccionados
    if(cadena==""):
        messagebox.showinfo(title="Lenguajes seleccionados",message="No conoces nada")
    else:
          messagebox.showinfo(title="Lenguajes seleccionados",message=" Conoces "+cadena)

ventana=Tk()
ventana.geometry("700x300+200+50")
ventana.title("Ejemplo de checkbutton")
lblPregunta=Label(ventana,text="Que lenguajes de programacion conoces?"
                  ).place(x=100,y=40)
#creando los checkbutton
selC=IntVar()
selCC=IntVar()
selJava=IntVar()
selRuby=IntVar()
selPhp=IntVar()
selPython=IntVar()
chkC=Checkbutton(ventana,text="C",variable=selC,onvalue=1,offvalue=0
                 ).place(x=100,y=60)
chkCC=Checkbutton(ventana,text="C++",variable=selCC,onvalue=1,offvalue=0
                 ).place(x=100,y=80)
chkJava=Checkbutton(ventana,text="Java",variable=selJava,onvalue=1,offvalue=0
                 ).place(x=100,y=100)
chkRuby=Checkbutton(ventana,text="Ruby",variable=selRuby,onvalue=1,offvalue=0
                 ).place(x=100,y=120)
chkPhp=Checkbutton(ventana,text="Php",variable=selPhp,onvalue=1,offvalue=0
                 ).place(x=100,y=140)
chkPython=Checkbutton(ventana,text="Python",variable=selPython,onvalue=1,offvalue=0
                 ).place(x=100,y=160)
btnLenguajes=Button(ventana,text="Cuales seleccione?",command=lenguajes
                    ).place(x=100,y=220)

ventana.mainloop()
