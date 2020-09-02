from tkinter import *
from tkinter import messagebox


# ------------------------- Main Window -----------------------
vP = Tk()
vP.geometry("800x600")
vP.title("Analizador de Metadatos MD47")
vP.iconbitmap("JTNEGRO.ico")
vP.resizable(0, 0)
# ------------------------- End Main Window --------------------

# ------------------------- Main Frame -------------------------
mF = Frame()
mF.pack()
mF.config(width="800", height="600")
# ------------------------- End Main Frame ---------------------


# ------------------------- Message Box ------------------------
def about():
    messagebox.showinfo("Acerca de...","El Analizador de Metadatos MD47 es una aplicación que permite "
                        +"ver los metadatos ocultos en muchos de tus archivos de uso "
                        +"diario. Este es el proyecto final de gradación para el "
                        +"Máster Universitario en Ciberseguridad de la Universidad "
                        +"de Alcalá de Henares, España, periodo 2019-2020, "
                        +"estudiante Ing. Julio Chinchilla Moya.")
# ------------------------- End Main Frame ---------------------


# ------------------------- Menu bar ---------------------------
menuBar = Menu(vP)
vP.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Select New")
fileMenu.add_separator()
fileMenu.add_command(label="Save Result")
fileMenu.add_command(label="Clear Results")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

metaDataMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Metadata", menu=metaDataMenu)
metaDataMenu.add_command(label="Analyze")
metaDataMenu.add_command(label="Clean")

wordListMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Word-List", menu=wordListMenu)
wordListMenu.add_command(label="Edit")
wordListMenu.add_command(label="Update")

aboutMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="About", command=about)
# ------------------------- End Menu bar ----------------------


# ------------------------- End Window -------------------------
vP.mainloop()
