import oracledb
import json
import Utilities as Utils
import requests

import os
from dotenv import load_dotenv

load_dotenv("Pass.ENV")

pwd = os.getenv('PASSWORD')
hst = os.getenv('HOST')
usr = os.getenv('USER')

def callAPI(json_data):
    url = ""

    

try:
    connection = oracledb.connect(
        user= usr, 
        password = pwd, 
        host= hst, 
        port="1521",
        service_name="mgdwh"
    )

    cursor = connection.cursor()

    cursor.execute(Utils.getQuery(0)) 
    res = cursor.fetchall()

    field_names = [i[0] for i in cursor.description]

    my_dict = [dict(zip(field_names, x)) for x in res]

    jsone = json.dumps(my_dict)
    # Data.json
    with open("Data.json", "w") as file:
        file.write(jsone)
    # END Data.json

except oracledb.DatabaseError as e:
    print(f">> Errore durante la connesione al Database: {e}")


finally:
    if connection:
        cursor.close()
        connection.close()