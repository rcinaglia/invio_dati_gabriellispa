import requests
import os
from dotenv import load_dotenv
import datetime

def sendData(json_data):
    filename = datetime.datetime.now().strftime()
    path = "logs/" + str(filename, '%d-%m-%Y') + ".txt"
    API_KEY = os.getenv('TOKEN')
    try:
        url = "https://magazzinigabrielli.staffroster.com//wsrest/v1/sales?type=1"
        payload = json_data
        headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print("** Chiamata API andata a buon fine **")
        if(response.status_code == 201):
            print(">> Dati inseriti correttamente")
            print("RSC:", response.status_code)
        else:
            with open(path, "a") as errorLog: 
                errorLog.write(">> Errore durante l'inserimento")
                errorLog.write("RSC:", response.status_code)
                errorLog.write("Message: ", response.json()['message'])
    except:
        with open(path, "a") as errorLog: 
            errorLog.write("** Non è stato possibile effettuare la chiamata all'API **")


