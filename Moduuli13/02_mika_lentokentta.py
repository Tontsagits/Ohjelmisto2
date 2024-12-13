# Ohjelmisto 2 - Moduuli 13 - Tehtävä 2 - Mikä lentokenttä, backend versio

# imports

import mysql.connector
from flask import Flask, request, Response
import json

# global variables

game_airports = {}

# db connection config
dbconf = {
    'host': 'localhost',
    'port': 3306,
    'database': 'flight_game',
    'user': 'pilotti',
    'password': 'pilotti12345',
    'autocommit': True,
    'collation': 'utf8mb4_unicode_ci'
}

# connection to db
dbconn = mysql.connector.connect(**dbconf)

# request curson from connect
dbcursor = dbconn.cursor()

# setup Flask
app = Flask(__name__)

# functions

# Function to get information of any given airport. Function return airport details (Name, city and country)
def get_ap_info(ident: str):
    sql = f"SELECT airport.name, airport.municipality FROM airport WHERE airport.ident = %s;"
    opt = f'{ident}'
    dbcursor.execute(sql, (opt,))
    # fetchone returns data in tuple format
    # fetchall returns data in list format with items made of tuples
    results = dbcursor.fetchone()
    # return ap name, ap municipality
    # print(results)
    return results

# APIs

# toimiva URL esim http://127.0.0.1:3000/airport?ident=EFHK
@app.route('/airport')
def airport():
    try:
        args = request.args
        ident = args.get("ident")
        result = get_ap_info(ident)
        returncode = 200
        dataout = {
            'status': returncode,
            "ICAO": ident,
            "Name": result[0],
            "Municipality": result[1]
        }
    except ValueError:
        returncode = 400
        dataout = {
            'status': returncode,
            "text": 'Error.'
        }
    jsondataout = json.dumps(dataout)
    return Response(response=jsondataout, status=returncode, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(errorcode):
    vastaus = {
        "status" : errorcode,
        "text" : "Faulty endpoint."
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


# Main

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
