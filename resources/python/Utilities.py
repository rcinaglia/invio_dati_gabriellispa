import os
from dotenv import load_dotenv
import oracledb
import json
import resources.python.Utilities as Utils


def getQuery(query, fileName = "queris.sql"):
    with open(fileName, "r") as file:
        queriesString = file.read()

    queries = queriesString.split(';')
    return queries[query]


def DBconnection():

    try:
        load_dotenv("Pass.ENV")

        pwd = os.getenv('PASSWORD')
        hst = os.getenv('HOST')
        usr = os.getenv('USER')
        pt = os.getenv('PORT')
        sn = os.getenv('SERVICENAME')

        connection = oracledb.connect(
            user= usr, 
            password = pwd, 
            host= hst, 
            port=pt,
            service_name=sn
        )

        return connection
    
    except:
        print("errore di connession al db")
        return 0


def execQuery(nQuery, DBconnection, date):

    cursor = DBconnection.cursor()

    if nQuery == 0:
        cursor.execute(Utils.getQuery(nQuery), DataIniziale = date[0], DataFinale = date[1]) 
    else:
        cursor.execute(Utils.getQuery(nQuery), DataSingola = date[0]) 

    results = cursor.fetchall()

    cursor.close()
    DBconnection.close()

    return results



def toJSON(results):
    
    start = 540 
    end = 555

    ExpenseCenter = []
    days = []

    for row in results:

        day = row[0].split(" ")[0]
        expenseCenter = str(row[1]) + "-" + str(row[3])
        tickets = 0
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

    return json.dumps(Final)








