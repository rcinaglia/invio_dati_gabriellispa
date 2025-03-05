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

cursor.execute(Utils.getQuery(0), DataIniziale="21-02-2025", DataFinale="23-02-2025") 
res = cursor.fetchall()




#-------LOAD DB CREDENTIALS---------



start = 540 
end = 555

ExpenseCenter = []
days = []

for row in res:

    day = row[1].split(" ")[0]
    expenseCenter = str(row[2]) + "-" + str(row[0])
    tickets = row[5]
    sales = row[4]

    Steps = [{"start": start, "end": end, "sales": sales, "tickets": tickets}]

    index = next((i for i, d in enumerate(days) if d["day"] == day), None)


    if index is not None:
        ExpenseCenter = {"expenseCenter": expenseCenter ,"steps": Steps}
        days[index]["expenseCenters"].append(ExpenseCenter)
    else:
        ExpenseCenter = {"expenseCenter": expenseCenter ,"steps": Steps}
        days.append({"day": day, "expenseCenters" : [ExpenseCenter]})


    
    


Final = {"days" : days, "start":start, "end":end}



FinalJson = json.dumps(Final)
with open("Data.json", "w") as file:
    file.write(FinalJson)




cursor.close()
connection.close()
