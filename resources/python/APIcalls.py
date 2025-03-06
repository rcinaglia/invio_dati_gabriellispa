import requests
import os
from dotenv import load_dotenv

def sendData(json_data):
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
            print(">> Errore durante l'inserimento")
            print("RSC:", response.status_code)
            print("Message: ", response.json()['message'])
    except:
        print("** Non è stato possibile effettuare la chiamata allì'API **")


