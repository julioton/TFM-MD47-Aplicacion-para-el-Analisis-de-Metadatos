from tkinter import *
from core.menu import MenuFunctions
from core.main import MainMethods

# ------------------------- Definitions -----------------------
title = "Analizador de Metadatos MD47"
tSelectFile = "Seleccione un Archivo para iniciar..."

cPrimary = "#00838f"
cDark = "#005662"
cLight = "#4fb3bf"
tPrimary = "#ffffff"
tDark = "#ffffff"
tLight = "#000000"
cWhite = "#ffffff"
cBlack = "#000000"
cLightGray = "#e0e0e0"
cDarkGray = "#616161"

file = ""

# ------------------------- Local Methods Definitions -----------------------
def selectFile():
    fileSelected = MainMethods.browse_file()
    if fileSelected == "":
        MenuFunctions.errorFileEmpty()
        #buttonSelect.config(text="Select")
        lblBottom.config(text=tSelectFile)
    else:
        tSF = "File: "+fileSelected
        file = fileSelected
        lblBottom.config(text=tSF)
        #buttonSelect.config(text="Clear")

def exitApp():
    if MenuFunctions.exitApp():
        vP.quit()

# ------------------------- Main Window -----------------------
vP = Tk()
vP.geometry("800x600")
vP.title(title)
vP.iconbitmap("img/JTNEGRO.ico")
vP.resizable(0, 0)
# ------------------------- Main Frame -------------------------
mF = Frame()
mF.config(width="800", height="600", bg=cLightGray)
mF.pack()
# ------------------------- Menu bar ---------------------------
menuBar = Menu(vP)
vP.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Select New", command=selectFile)
fileMenu.add_separator()
fileMenu.add_command(label="Save Result")
fileMenu.add_command(label="Clear Results")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitApp)

metaDataMenu = Menu(menuBar, tearoff=0)
metaDataMenu.add_command(label="Analyze")
metaDataMenu.add_command(label="Clean")

wordListMenu = Menu(menuBar, tearoff=0)
wordListMenu.add_command(label="Edit")
wordListMenu.add_command(label="Update")

aboutMenu = Menu(menuBar, tearoff=0)
aboutMenu.add_command(command=MenuFunctions.about)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Metadata", menu=metaDataMenu)
menuBar.add_cascade(label="Word-List", menu=wordListMenu)
menuBar.add_cascade(label="About", menu=aboutMenu)
# ------------------------- End Menu bar ----------------------

# ------------------------- Label Title  ----------------------
lblTitle = Label(mF, text=title.upper())
lblTitle.place(relx=.5, y=20, anchor="center")
lblTitle.config(fon=("Verdana", 24), fg=tPrimary, bg=cPrimary, width="60", height="4")

# ------------------------- Text Result  ----------------------
textResult = Text(mF, width=60, height=20, relief=FLAT)
textResult.place(relx=.5, rely=.4, anchor="center")
textResult.config(fon=("Verdana", 16), fg=cBlack, bg=cWhite)
#textResult.insert(INSERT, "Hello World")
#textResult.config(state=DISABLED)

# ------------------------- Actions Buttons  ----------------------
buttonSelect = Button(mF, text="Selecionar", command=selectFile)
buttonSelect.place(relx=.4, rely=.75)
buttonSelect.config(fon=("Verdana", 20), fg="green", highlightbackground=cLightGray, bg=cLightGray,
                    width="10", height="2", bd=0)

buttonAnalize = Button(mF, text="Analizar")
buttonAnalize.place(relx=.6, rely=.75)
buttonAnalize.config(fon=("Verdana", 20), fg="blue", highlightbackground=cLightGray, bg=cLightGray,
                    width="10", height="2", bd=0)

buttonClean = Button(mF, text="Limpiar")
buttonClean.place(relx=.8, rely=.75)
buttonClean.config(fon=("Verdana", 20), fg="red", highlightbackground=cLightGray, bg=cLightGray,
                    width="10", height="2", bd=0)

# ------------------------- Label Bottom  ----------------------
lblBottom = Label(mF, text=tSelectFile)
lblBottom.place(relx=.5, rely=0.95, anchor="center")
lblBottom.config(fon=("Verdana", 18), fg=cWhite, bg=cLight, width="90", height="3")






# ------------------------- End Window -------------------------
vP.mainloop()
