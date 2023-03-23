from tkinter import*
from PIL import ImageTk,Image
root= Tk()

ventanaprincipal=Frame(root,bg="#20ff50")
ventanaprincipal.grid()
contras=StringVar()
confirmo=StringVar()


def contraseñas():
    if contras.get()==confirmo.get():
        print("SESION INICIADA")
        ventanaprincipal.config(bg="#00ff00")
        

        
    else:
        print("CONTRASEÑA INCORRECTA")


img=Image.open("kenini.ico")#variable q contiene el nombre de la imagen
imagenmusica=img.resize((150,150))
imag=ImageTk.PhotoImage(imagenmusica)
mititulo=Label(ventanaprincipal,image=imag)
mititulo.grid(row=1,column=1,padx=10,pady=20,columnspan=2,rowspan=2)

titulo=Label(ventanaprincipal,text="LOG IN",font=("roboto",20))
titulo.grid(row=3,column=1,columnspan=2)


NAME=Label(ventanaprincipal,text="NOMBRE:",font=("roboto",15)).grid(row=4,column=1,padx=30,pady=30)
textonombre=Entry(ventanaprincipal,font=("roboto",15)).grid(row=4,column=2,padx=30,pady=15)
CONTRA=Label(ventanaprincipal,text="CONTRASEÑA:",font=("roboto",15)).grid(row=5,column=1,padx=15,pady=30)
textocontra=Entry(ventanaprincipal,font=("roboto",15),textvariable=contras).grid(row=5,column=2,padx=30,pady=15)
CONFIRM=Label(ventanaprincipal,text="CONFIRMAR CONTRASEÑA:",font=("roboto",15)).grid(row=6,column=1,padx=15,pady=30)
textoconfir=Entry(ventanaprincipal,font=("roboto",15),textvariable=confirmo).grid(row=6,column=2,padx=30,pady=15)
control1=IntVar()
HOMBRE=Checkbutton(ventanaprincipal, text="HOMBRE",variable=control1,font=("roboto",15))
HOMBRE.grid(row=7,column=1)
control2=IntVar()
MUJER=Checkbutton(ventanaprincipal, text="MUJER",variable=control2,font=("roboto",15))
MUJER.grid(row=7,column=2)
control3=IntVar()
ACEPTO=Checkbutton(ventanaprincipal, text="ACEPTO TERMINOS",variable=control3,font=("roboto",15))
ACEPTO.grid(row=8,column=1,columnspan=2)
INICIAR=Button(ventanaprincipal,text="INICIAR",command=contraseñas,width=20,height=2).grid(row=9,column=1,columnspan=2)


root.mainloop()