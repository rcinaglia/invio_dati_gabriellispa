import requests
import os
import datetime
from ttkbootstrap.dialogs import Messagebox

def sendData(json_data):
    filename = datetime.datetime.now().strftime('%d-%m-%Y')
    path = "logs/" + str(filename) + ".txt"
    API_KEY = os.getenv('TOKEN')
    try:
        url = "https://magazzinigabrielli.staffroster.com//wsrest/v1/sales?type=1"
        payload = json_data
        headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if(response.status_code == 201):
            print(">> Dati inseriti correttamente")
            print("RSC:", response.status_code)
            return True
        else:
            Messagebox.show_error(title="ERRORE INSERIMENTO DATI", message=f"API RESPONSE CODE: {response.status_code}\nMESSAGE: {response.json()['message']}")
            with open(path, "a") as errorLog: 
                errorLog.write(str(datetime.datetime.now()) + "\n")
                errorLog.write(">> Errore durante l'inserimento \n")
                errorLog.write("RSC: " + str(response.status_code) + "\n")
                errorLog.write("Message: " + str(response.json()['message']) + "\n")
                return False
    except:
        with open(path, "a") as errorLog: 
            errorLog.write(str(datetime.datetime.now()) + "\n")
            errorLog.write("** Non è stato possibile effettuare la chiamata all'API ** \n")
        return False


