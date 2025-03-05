import requests

def sendData(json_data):
    url = ""
    try:
        response = requests.post(url, json=json_data)
        if response.status_code == 200:
            print("Invio completato -- RSC: ", response.status_code)
            print(response.json())
            return True
        else:
            print("Errore durante la chiamata API -- RSC: ", response.status_code)
            return False
    except:
        print("errore")
