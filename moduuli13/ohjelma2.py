#!/usr/bin/env python3
from flask import Flask, request
import mysql.connector

con = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='metropolia',
    password='metropolia',
    autocommit=True
)


app = Flask(__name__)
@app.route('/kenttä/<icao>')
def handle(icao):

    cur = con.cursor()
    query = "SELECT ident, name, municipality FROM airport WHERE ident=%s"
    cur.execute(query, (icao,))
    (icao2, name, municipality) = cur.fetchone()

    ret = {
        "ICAO" : icao2,
        "Name" : name,
        "Municipality": municipality
    }
    return ret

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
