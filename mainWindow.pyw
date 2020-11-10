from tkinter import *
from core.menu import MenuFunctions
from core.main import MainMethods
from core.definitions import *

file = ""
file_prop = {}
file_meta = {}


# ------------------------- Local Methods Definitions -----------------------

def select_file(fileSelected=False):
    if not fileSelected:
        fileSelected = MainMethods.browse_file()
        textResult.insert(INSERT, tWelcome + '\n')
    if fileSelected == "":
        MenuFunctions.error_file_empty()
        lblBottom.config(text=tdSelectFile)
        textResult.delete(1.0, END)
        textResult.insert(INSERT, tWelcome + '\n')
    else:
        textResult.delete(1.0, END)
        textResult.insert(INSERT, tWelcome + '\n')
        if MainMethods.check_file_ext(fileSelected):
            global file
            global file_prop
            global file_meta
            textResult.delete(1.0, END)
            tSF = tFile + ": " + str(fileSelected)
            file = fileSelected
            lblBottom.config(text=tSF)
            file_prop = MainMethods.get_file_properties(fileSelected)
            MainMethods.print_results(textResult, file_prop)
            file_meta = MainMethods.get_metadata(fileSelected, file_prop)
            MainMethods.print_results(textResult, file_meta)
        else:
            MenuFunctions.error_file_empty()
            # buttonSelect.config(text="Select")
            lblBottom.config(text=tdSelectFile)
            textResult.delete(1.0, END)


def clean_file():
    if file_prop:
        lblBottom.config(text=tdActionCleaning)
        textResult.delete(1.0, END)
        textResult.insert(INSERT, tdActionCleaning + '\n')
        file_clean = MainMethods.clean_metadata(file_prop["File Name"], file_prop["Extension"])
        if file_clean:
            textResult.insert(INSERT, tdActionCleaningOK + '\n')
            select_file(file_clean)
            MenuFunctions.info_file_clean()
        else:
            textResult.insert(INSERT, tdActionCleaningFailed + '\n')
            MenuFunctions.info_file_clean_failed()
    else:
        MenuFunctions.error_file_empty()
        # buttonSelect.config(text="Select")
        lblBottom.config(text=tdSelectFile)
        textResult.delete(1.0, END)
        textResult.insert(INSERT, tWelcome + '\n')


def exit_app():
    if MenuFunctions.exit_app():
        vP.quit()


# ------------------------- Main Window -----------------------
vP = Tk()
vP.geometry("800x600")
vP.title(title)
vP.iconbitmap(tIconBitMap)
vP.resizable(0, 0)
# ------------------------- Main Frame -------------------------
mF = Frame()
mF.config(width="800", height="600", bg=cLightGray)
mF.pack()
# ------------------------- Menu bar ---------------------------
menuBar = Menu(vP)
vP.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label=tSelect, command=select_file)
fileMenu.add_separator()
fileMenu.add_command(label=tSave)
fileMenu.add_command(label=tClean)
fileMenu.add_separator()
fileMenu.add_command(label=tExit, command=exit_app)

metaDataMenu = Menu(menuBar, tearoff=0)
metaDataMenu.add_command(label=tAnalyze)
metaDataMenu.add_command(label=tClean)

wordListMenu = Menu(menuBar, tearoff=0)
wordListMenu.add_command(label=tEdit)
wordListMenu.add_command(label=tUpdate)

aboutMenu = Menu(menuBar, tearoff=0)
aboutMenu.add_command(command=MenuFunctions.about)

menuBar.add_cascade(label=tFile, menu=fileMenu)
menuBar.add_cascade(label=tMetadata, menu=metaDataMenu)
menuBar.add_cascade(label=tWordList, menu=wordListMenu)
menuBar.add_cascade(label=tAbout, menu=aboutMenu)
# ------------------------- End Menu bar ----------------------

# ------------------------- Label Title  ----------------------
lblTitle = Label(mF, text=title.upper())
lblTitle.place(relx=.5, y=20, anchor="center")
lblTitle.config(fon=("Verdana", 24), fg=tPrimary, bg=cPrimary, width="60", height="4")

# ------------------------- Text Result  ----------------------
textResult = Text(mF, width=60, height=20, relief=FLAT)
textResult.place(relx=.5, rely=.4, anchor="center")
textResult.config(fon=("Verdana", 16), fg=cBlack, bg=cWhite)
# textResult.insert(INSERT, "Hello World")
# textResult.config(state=DISABLED)

# ------------------------- Actions Buttons  ----------------------
buttonSelect = Button(mF, text=tSelect, command=select_file)
buttonSelect.place(relx=.6, rely=.75)
buttonSelect.config(fon=("Verdana", 20), fg="green", highlightbackground=cLightGray, bg=cLightGray,
                    width="10", height="2", bd=0)
'''
buttonAnalyze = Button(mF, text=tAnalyze)
buttonAnalyze.place(relx=.6, rely=.75)
buttonAnalyze.config(fon=("Verdana", 20), fg="blue", highlightbackground=cLightGray, bg=cLightGray,
                     width="10", height="2", bd=0)
'''
buttonClean = Button(mF, text=tClean, command=clean_file)
buttonClean.place(relx=.8, rely=.75)
buttonClean.config(fon=("Verdana", 20), fg="red", highlightbackground=cLightGray, bg=cLightGray,
                   width="10", height="2", bd=0)

# ------------------------- Label Bottom  ----------------------
lblBottom = Label(mF, text=tdSelectFile)
lblBottom.place(relx=.5, rely=0.95, anchor="center")
lblBottom.config(fon=("Verdana", 18), fg=cWhite, bg=cLight, width="90", height="3")

# ------------------------- End Window -------------------------


textResult.insert(INSERT, tWelcome + '\n')

vP.mainloop()

