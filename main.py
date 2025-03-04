import oracledb
import json
import Utilities as Utils

import os
from dotenv import load_dotenv


#-------LOAD DB CREDENTIALS---------
load_dotenv("Pass.ENV")

pwd = os.getenv('PASSWORD')
hst = os.getenv('HOST')
usr = os.getenv('USER')



#-------DB CONNECTION---------
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



start = 540 
end = 555


#-------LOAD DB CREDENTIALS---------

expenseCenters = []


for row in res:
    day = row[1].split(" ")[0]
    expenseCenter = str(row[2]) + "-" + str(row[0])
    tickets = row[4]
    sales = row[3]
    Steps = [{"start": start, "end": end, "sales": sales, "tickets": tickets}]
    expenseCenters.append( {"expenseCenter": expenseCenter ,"steps": Steps} )



days = [{"day": day, "expenseCenters" : expenseCenters}]
Final = {"days" : days, "start":start, "end":end}



FinalJson = json.dumps(Final)
with open("Data.json", "w") as file:
    file.write(FinalJson)


#field_names = [i[0] for i in cursor.description]

#my_dict = [dict(zip(field_names, x)) for x in res]
#
#
#jsone = json.dumps(my_dict)
#
#
#with open("Data.json", "w") as file:
#    file.write(jsone)


cursor.close()
connection.close()
