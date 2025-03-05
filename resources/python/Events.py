import resources.python.Utilities as Utils
import resources.python.APIcalls as APIcalls
import datetime



def Invia(DataInizio, DataFine, Checked):

    dataOggi = datetime.datetime.today().strftime('%d/%m/%Y')

    if (DataInizio <= dataOggi and Checked == 0) or  (Checked == 1 and (DataInizio < DataFine and DataFine <= dataOggi and DataFine != DataInizio)):
        DBconnection = Utils.DBconnection() 
        queryResults = Utils.execQuery(Checked, DBconnection, [DataInizio, DataFine])
        Json = Utils.toJSON(queryResults)

        with open("data.json", "w") as file :
            file.write(Json)
        return True
    else:
        return False
    