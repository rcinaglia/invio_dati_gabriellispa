import oracledb
import json
import Utilities as Utils

import os
from dotenv import load_dotenv

load_dotenv("Pass.ENV")

pwd = os.getenv('PASSWORD')
hst = os.getenv('HOST')
usr = os.getenv('USER')

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

print(res)


firstRow = res[0]
day = firstRow[0].split(" ")[0]



expenseCenter = str(firstRow[1]) + "-" + str(firstRow[2])
start = 540 
end = 555
tickets = firstRow[4]

sales = 0
for row in res:
    sales += row[3]
    

Steps = [{"start": start, "end": end, "sales": sales, "tickets":tickets}]
expenseCenters = [{"expenseCenter": expenseCenter ,"steps": Steps}]

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
