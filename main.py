import tkinter as tk
import ttkbootstrap as tb
from PIL import Image, ImageTk
from ttkbootstrap.dialogs import Messagebox

import resources.python.Events as E

#-----Variables-------
windowSizeX = 400
windowSizeY = 500
appName = "ciao"



#-------GUI---------


app = tb.Window(themename ="darkly")

app.geometry(str(windowSizeX) + "x" + str(windowSizeY))
app.resizable(False, False)
app.title(appName)
app.iconbitmap("resources/assets/Gabrielli.ico")


img = Image.open("resources/assets/Gabrielli.png")
img = img.resize((300, 150))
img = ImageTk.PhotoImage(img)
panel = tk.Label(app, image = img)
panel.pack()

Frame = tb.Frame(app)
Frame.rowconfigure(1, minsize=45)

Testo = tb.Label(Frame, text="Giorno")
Testo.grid(column=0, row=0, padx=(0, 10))

dataInizio = tb.DateEntry(Frame, bootstyle="primary")
dataInizio.grid(column=1, row=0, pady=5)
dataInizio.button.place(y = -0.5, x = 105)

def Checked():
    if State.get() == 1:
        dataFine.grid()
        Testo.config(text="Data di inizio")
    else:
        Testo.config(text="Giorno")
        dataFine.grid_remove()

State = tk.IntVar()
enableDataFine = tb.Checkbutton(Frame, text='Data di fine', style='Roundtoggle.Toolbutton',  variable = State,  command= Checked)
enableDataFine.grid(column=0, row=1, pady=5, padx=(0, 10))


dataVar = tk.StringVar()
dataFine = tb.DateEntry(Frame, bootstyle="primary")
dataFine.button.place(y = -0.5, x = 105)
dataFine.grid(column=1, row=1)
dataFine.grid_remove()

Frame.pack(padx=10, pady=10)


def invio():
    if not E.Invia(dataInizio.entry.get(), dataFine.entry.get(), State.get()):
        Messagebox.show_error(message="Inserire una data valida", title="Errore")

Button = tb.Button(app, text="Invia dati", bootstyle="primary-outline", command= invio, width=20)
Button.pack(pady=20)


app.mainloop()
