from flask import Flask, jsonify
import datetime as dt  
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"available routes<br/>" 
        f"/api/v1.0/precipitation<br/>" 
        f"/api/v1.0/stations<br/>" 
        f"/api/v1.0/tobs<br/>" 
        f"/api/v1.0/startdate/<start><br/>" 
        f"/api/v1.0/interval/<start>/<end>"

    )
@app.route("/api/v1.0/precipitation")
def rainy(): 
    return()

if __name__ == '__main__':
    app.run(debug=True)