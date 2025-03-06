import os
from dotenv import load_dotenv
import oracledb
import json
import datetime
import resources.python.Utilities as Utils


def getQuery(query, fileName = "resources/sql/queries.sql"):
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

    results = []


    if nQuery == 1:
        cursor.execute(Utils.getQuery(nQuery + 2), DataIniziale = date[0], DataFinale = date[1]) 
        pdv_cods = cursor.fetchall()

        for pdv_cod in pdv_cods:
            cursor.execute(Utils.getQuery(nQuery), DataIniziale = date[0], DataFinale = date[1], PDV = pdv_cod[0])
            cod_results = cursor.fetchall()

            results.append(cod_results)

    else:
        cursor.execute(Utils.getQuery(nQuery + 2), DataSingola = date[0]) 
        pdv_cods = cursor.fetchall()

        for pdv_cod in pdv_cods:
            cursor.execute(Utils.getQuery(nQuery), DataSingola = date[0], PDV = pdv_cod[0])
            cod_results = cursor.fetchall()

            results.append(cod_results)


    cursor.close()
    DBconnection.close()

    return results



def toJSON(results, data_inizio, data_fine):
    
    start = 540 
    end = 555

    ExpenseCenter = []
    days = []

    dataMin = data_fine
    dataMax = data_inizio



    for row in results:

        day = row[0]

        data_curr = datetime.datetime.strptime(day, '%d-%m-%Y')

        if data_curr < dataMin:
            dataMin = data_curr
        if data_curr > dataMax:
            dataMax = data_curr

        expenseCenter = str(row[1]) + "-" + str(row[3])
        tickets = 0
        sales = row[4]

        Steps = [{"start": start, "end": end, "sales": sales, "tickets": tickets}]


        index = next((i for i, d in enumerate(days) if d["day"] == day), None)

        ExpenseCenter = {"expenseCenter": expenseCenter ,"steps": Steps}

        if index is not None:
            days[index]["expenseCenters"].append(ExpenseCenter)
        else:
            days.append({"day": day, "expenseCenters" : [ExpenseCenter]})

    
    dataMin = datetime.datetime.strftime(dataMin, '%d-%m-%Y')
    dataMax = datetime.datetime.strftime(dataMax, '%d-%m-%Y')

    Final = {"days" : days, "start":dataMin, "end":dataMax}


    return json.dumps(Final)








