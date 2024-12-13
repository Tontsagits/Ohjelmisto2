# Ohjelmisto 2 - Moduuli 13 - Tehtävä 2 - Mikä lentokenttä, backend versio

import mysql.connector
from flask import Flask


app = Flask(__name__)

game_airports = {}

# toimiva URL esim http://127.0.0.1:3000/airport?ident=<ident>
@app.route('/airport')
def airport():
    args = request.args
    ident = str(args.get("ident"))

    return str(ident)


# database connection
def database();
    yhteys = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="rahtipeli",
        user="pilotti",
        password="pilotti12345",
        autocommit=True,
        collation='utf8mb4_unicode_ci'
    )


# Function to get information of any given airport. Function return airport details (Name, city and country)
def get_information(ident: str):
    sql = f"SELECT airport.name, airport.municipality FROM airport WHERE airport.ident = '{ident}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for info in tulos:
        # return ap name, ap municipality, ap country name
        return (info[0], info[1])


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
