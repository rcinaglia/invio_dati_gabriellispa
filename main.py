import oracledb
import json
import Utilities as Utils

import tkinter as tk
import ttkbootstrap as tb
from PIL import Image, ImageTk

import os
from dotenv import load_dotenv



#-------LOAD DB CREDENTIALS---------
load_dotenv("Pass.ENV")

pwd = os.getenv('PASSWORD')
hst = os.getenv('HOST')
usr = os.getenv('USER')
pt = os.getenv('PORT')
sn = os.getenv('SERVICENAME')



app = tb.Window(themename ="darkly")
app.resizable(False, False)

app.geometry("400x500")
app.title("Invio dati")
app.iconbitmap("Gabrielli.ico")


def EnableFinishDate():
    if State.get() == 1:
        date2.grid()
    else:
        date2.grid_remove()

img = Image.open("Gabrielli.png")
img = img.resize((250, 150))

img = ImageTk.PhotoImage(img)
panel = tk.Label(app, image = img)
panel.pack()


Frame = tb.Frame(app)

Frame.rowconfigure(1, minsize=45)

Testo = tb.Label(Frame, text="Data di inizio")
Testo.grid(column=0, row=0, padx=(0, 10))
date = tb.DateEntry(Frame, bootstyle="dark")

date.button.place(y = -0.5, x = 100)
date.grid(column=1, row=0, pady=5)

State = tk.IntVar()
Check = tb.Checkbutton(Frame, text='Data di fine', style='Roundtoggle.Toolbutton',  variable=State,  command=EnableFinishDate)
Check.grid(column=0, row=1, pady=5, padx=(0, 10))

date2 = tb.DateEntry(Frame, bootstyle="dark")
date2.button.place(y = -0.5, x = 100)

date2.grid(column=1, row=1, pady=5)
date2.grid_remove()


Frame.pack(padx=10, pady=10)


Button = tb.Button(app, text="Invia", bootstyle="dark", command=lambda: print("ciao"), width=20)
Button.pack(pady=20)


#-------DB CONNECTION---------
connection = oracledb.connect(
    user= usr, 
    password = pwd, 
    host= hst, 
    port=pt,
    service_name=sn
)

cursor = connection.cursor()

cursor.execute(Utils.getQuery(0), DataIniziale="20-02-2025", DataFinale="21-02-2025") 
res = cursor.fetchall()




#-------LOAD DB CREDENTIALS---------



start = 540 
end = 555

ExpenseCenter = []
days = []

for row in res:

    day = row[1].split(" ")[0]
    expenseCenter = str(row[2]) + "-" + str(row[0])
    tickets = row[5]
    sales = row[4]

    Steps = [{"start": start, "end": end, "sales": sales, "tickets": tickets}]

    index = next((i for i, d in enumerate(days) if d["day"] == day), None)


    if index is not None:
        ExpenseCenter = {"expenseCenter": expenseCenter ,"steps": Steps}
        days[index]["expenseCenters"].append(ExpenseCenter)
    else:
        ExpenseCenter = {"expenseCenter": expenseCenter ,"steps": Steps}
        days.append({"day": day, "expenseCenters" : [ExpenseCenter]})


    
    


Final = {"days" : days, "start":start, "end":end}



FinalJson = json.dumps(Final)
with open("Data.json", "w") as file:
    file.write(FinalJson)

print("fatto")


cursor.close()
connection.close()
app.mainloop()
