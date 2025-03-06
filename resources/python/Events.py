import resources.python.Utilities as Utils
import resources.python.APIcalls as APIcalls
import datetime



def Invia(DataInizio, DataFine, Checked):

    data_inizio = datetime.datetime.strptime(DataInizio, '%d/%m/%Y')
    data_fine = datetime.datetime.strptime(DataFine, '%d/%m/%Y')
    data_oggi = datetime.datetime.today()
    

    if (data_inizio <= data_oggi and Checked == 0) or (Checked == 1 and (data_inizio < data_fine and data_fine < data_oggi)):
        DBconnection = Utils.DBconnection() 
        queryResults = Utils.execQuery(Checked, DBconnection, [DataInizio, DataFine])
        Json = Utils.toJSON(queryResults)

        with open("data.json", "w") as file :
            file.write(Json)
        return True
    else:
        return False
    