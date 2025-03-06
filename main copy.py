import tkinter as tk
import ttkbootstrap as tb
from PIL import Image, ImageTk
from ttkbootstrap.dialogs import Messagebox
import re
import os

import resources.python.Events as E

#-----Variables-------
windowSizeX = 400
windowSizeY = 500
appName = "Invio dati"



#-------GUI---------

def Checked():
    if State.get() == 1:
        dataFine.grid()
        Testo.config(text="Data di inizio")
    else:
        Testo.config(text="Giorno")
        dataFine.grid_remove()


def invio():    
    Button.config(default="disabled", bootstyle="secondary")

    if not E.Invia(dataInizio.entry.get(), dataFine.entry.get(), State.get(), progressBar):
        Messagebox.show_error(message="Inserire una data valida", title="Errore")
    else:
        Button.config(default="normal", bootstyle="primary")

    


def aggiungiPDV():

    TextContent = PDV_Text.get("1.0", "end")

    if TextContent and not TextContent.isspace():

        delimiter = " "
        TestoList = delimiter.join( re.split('; |,|\n|-| |/|"', TextContent)).split(" ")

        TestoList = list(set(TestoList))

        PDV_List = ""
        with open("PDV_presenze.txt", "r") as f:
            PDV_List = f.read().split(" ")

        with open("PDV_presenze.txt", "a") as f:
            for Testo in TestoList:
                if Testo not in PDV_List:
                    f.write(Testo + " ")


        Flag = tb.Label(tab2, text="ciao")
        Flag.config(text="List updated")
        Flag.pack(pady=10)
        app.after(1000, Flag.destroy)
        

    PDV_Text.delete("1.0", "end")

    

def openLogs():
    os.startfile("logs")



app = tb.Window(themename ="darkly")

app.geometry(str(windowSizeX) + "x" + str(windowSizeY))
app.resizable(False, False)
app.title(appName)
app.iconbitmap("resources/assets/Gabrielli.ico")


Notebook = tb.Notebook(app, bootstyle = "superhero")

tab1 = tb.Frame(Notebook)
tab2 = tb.Frame(Notebook)
tab3 = tb.Frame(Notebook)

Notebook.add(tab1, text="bella")
Notebook.pack(pady=50, padx=30)

PrincipalFrame = tb.Frame(app)




img = Image.open("resources/assets/Gabrielli.png")
img = img.resize((300, 150))
img = ImageTk.PhotoImage(img)
panel = tk.Label(tab1, image = img)
panel.grid(columnspan=2)


tab1.rowconfigure(2, minsize=45)

Testo = tb.Label(tab1, text="Giorno")
Testo.grid(column=0, row=1, padx=(0, 10))

dataInizio = tb.DateEntry(tab1, bootstyle="primary")
dataInizio.grid(column=1, row=1, pady=5)
dataInizio.button.place(y = -0.5, x = 105)


State = tk.IntVar()
enableDataFine = tb.Checkbutton(tab1, text='Data di fine', style='Roundtoggle.Toolbutton',  variable = State,  command= Checked)
enableDataFine.grid(column=0, row=2, pady=5, padx=(0, 10))


dataVar = tk.StringVar()
dataFine = tb.DateEntry(tab1, bootstyle="primary")
dataFine.button.place(y = -0.5, x = 105)
dataFine.grid(column=1, row=2)
dataFine.grid_remove()


Button = tb.Button(tab1, text="Invia dati", bootstyle="primary", command= invio, width=20)
Button.grid(columnspan=2, pady=(10, 0), row=3)

tab1.rowconfigure(4, minsize=25)

progressBar = tb.Progressbar(tab1, orient="horizontal", value=0)

tab1.grid(column=0, row=0)





TestoPDV = tb.Label(tab2, text="Inserire PDV")
TestoPDV.pack(pady=20)

PDV_Text = tb.Text(tab2, height=5, width=30)
PDV_Text.pack()

AddPDV = tb.Button(tab2, text="Aggiungi PDV", bootstyle="secondary", command= aggiungiPDV, width=20)
AddPDV.pack(pady=(25 , 20), padx=50)






tab2.grid(column=2, row=0, padx=(15, 0))





OpenLogs = tb.Button(tab3, text="Open logs", bootstyle="secondary", command= openLogs, width=10)
OpenLogs.grid(row=0, column=0, pady=10)



Notebook.add(tab1, text="Invio")
Notebook.add(tab2, text="Aggiungi PDV")
Notebook.add(tab3, text="Info")


app.mainloop()
