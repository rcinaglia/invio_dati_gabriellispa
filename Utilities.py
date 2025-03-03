def getQuery(query, fileName = "Query.sql"):
    with open(fileName, "r") as file:
        queriesString = file.read()

    queries = queriesString.split(';')
    return queries[query]