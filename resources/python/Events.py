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

        PDV_List = ""
        with open("PDV_presenze.txt", "r") as f:
            PDV_List = f.read().split(" ")

        print(PDV_List)

        for cod_result in queryResults:
            
            index = next((i for i, d in enumerate(cod_result) if str(d[1]) in PDV_List), None)

            if index is not None:
                Json = Utils.toJSON(cod_result, data_inizio, data_fine)
                
                #APIcalls.sendData(Json)

        return True
    else:
        return False
    