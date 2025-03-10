import resources.python.Utilities as Utils
import resources.python.APIcalls as APIcalls
import datetime
import time
from ttkbootstrap.dialogs import Messagebox

def Invia(DataInizioSTR, DataFineSTR, Checked, APIprogress):


    

    filename = datetime.datetime.now().strftime('%d-%m-%Y')
    path = "logs/" + str(filename) + ".txt"

    data_inizio = datetime.datetime.strptime(DataInizioSTR, '%d/%m/%Y')
    data_fine = datetime.datetime.strptime(DataFineSTR, '%d/%m/%Y')
    data_oggi = datetime.datetime.today()
    

    if (data_inizio <= data_oggi and Checked == 0) or (Checked == 1 and (data_inizio < data_fine and data_fine < data_oggi)):
        DBconnection = Utils.DBconnection()
  

        queryResults = Utils.execQuery(Checked, DBconnection, [DataInizioSTR, DataFineSTR])

        PDV_List = ""
        with open("PDV_presenze.txt", "r") as f:
            PDV_List = f.read().split(" ")

        Amount = len(PDV_List)
        counter = 0

        
        APIprogress.grid(columnspan=2, pady=(10, 0), row=4) 

        if PDV_List == []:
                with open(path, "a") as errorLog:
                    errorLog.write(str(datetime.datetime.now()) + "\n")
                    errorLog.write(">> PDV LIST VUOTA \n")
                Messagebox.show_warning(title="PDV LIST VUOTA", message="Lista punti vendita vuota. Aggiungerne di nuovi")
                APIprogress.grid_remove()
        else:
            for cod_result in queryResults:

                index = next((i for i, d in enumerate(cod_result) if str(d[1]) in PDV_List), None)


                if index is not None:
                    Json = Utils.toJSON(cod_result, data_inizio, data_fine)
                    
                    if APIcalls.sendData(Json):
                        APIprogress.config(text="Inviati " + str(counter) + " di " + str(Amount) + " possibili")  
                        APIprogress.update()
                    else:
                        break
                        
                    counter += 1
            


                


        return True
    else:
        return False
    