import requests

def sendData(json_data):
    url = ""

    response = requests.get(url) # tmp, get o post?
    if response.status_code == 200:
        print("Invio completato -- RSC: ", response.status_code)
        return True
    else:
        print("Errore durante la chiamata API -- RSC: ", response.status_code)
        return False
