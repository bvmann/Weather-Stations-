from flask import Flask, jsonify
import datetime as dt  
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

app = Flask(__name__)

Base = automap_base()
# reflect an existing database into a new model
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

df = session.query(Measurement.date, Measurement.prcp)

date_temp = ({Measurement.date[0]:Measurement.date[1] for  Measurement.date in df})

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
    
    
    
    return jsonify(date_temp)
session.close()

@app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    stations = session.query(Station.station)
    stat = []
    for x in stations:
        stat.append(x)

    return jsonify(stat)
session.close()
@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)
    station_7_=session.query(Measurement.date,Measurement.tobs,Measurement.station).filter(Measurement.station=='USC00519281')
    station7=[]
    for x in station_7_: 
       station7.append(x)
    
    
    return jsonify(station7)

@app.route("/api/v1.0/startdate/<start>")
def start(): 
    session=Session(engine)
    return f"enter your start date "


if __name__ == '__main__':
    app.run(debug=True)