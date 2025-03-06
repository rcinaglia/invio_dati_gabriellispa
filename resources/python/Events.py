import resources.python.Utilities as Utils
import resources.python.APIcalls as APIcalls
import datetime

def Invia(DataInizioSTR, DataFineSTR, Checked):

    data_inizio = datetime.datetime.strptime(DataInizioSTR, '%d/%m/%Y')
    data_fine = datetime.datetime.strptime(DataFineSTR, '%d/%m/%Y')
    data_oggi = datetime.datetime.today()
    

    if (data_inizio <= data_oggi and Checked == 0) or (Checked == 1 and (data_inizio < data_fine and data_fine < data_oggi)):
        DBconnection = Utils.DBconnection() 


        queryResults = Utils.execQuery(Checked, DBconnection, [DataInizioSTR, DataFineSTR])

        for cod_result in queryResults:

            print(cod_result[0][1])

            Json = Utils.toJSON(cod_result, data_inizio, data_fine)

            with open("resources/JSONs/" + str(cod_result[0][1]) + ".json", "w") as file :
                file.write(Json)


        return True
    else:
        return False
    