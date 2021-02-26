from flask import Flask
from flask import jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt
from sqlalchemy import distinct
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()    #Base is a variable and could be called anything
Base.prepare(engine, reflect=True)
Base.classes.keys()
session=Session(bind=engine)
Measurement=Base.classes.measurement
Station=Base.classes.station


app=Flask(__name__)

#List all routes that are available
@app.route("/")
def home():
   return "/api/v1.0/precipitation<br/>  /api/v1.0/stations<br/>  /api/v1.0/tobs<br/>   /api/v1.0/start<br/>   /api/v1.0/start/end<br/> "


#Convert the query results to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def percipitation():
    #start session here
    last_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prior_year=dt.date(2017,8,23) - dt.timedelta(days=365)
    lastyear_query=session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > prior_year).all()
    x=dict(lastyear_query)
    #close session here
    something_here=jsonify(x)
    return something_here
   

#Return a JSON list of stations from the dataset
#see dictionary defined above
@app.route("/api/v1.0/stations")
def stations():
    active_stations=session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    station_list=dict(active_stations)
    returned=jsonify(station_list)
    return returned

# #Query the dates and temperature observations of the most active station for the last year of data.
# #Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    last_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    prior_year=dt.date(2017,8,23) - dt.timedelta(days=365)
    
    most_lastyear_tobs=session.query(Measurement.tobs, Measurement.date, Measurement.station).filter(Measurement.date > prior_year)\
    .filter(Measurement.station=='USC00519281').all()
    
    tobs = list(np.ravel(most_lastyear_tobs))
    
    tobs_list=jsonify(tobs)
    return tobs_list
    



#/api/v1.0/<start> and /api/v1.0/<start>/<end>
#Return a JSON list of the minimum Ftemperature, the average temperature, and the max temperature for a given start or start-end range.
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start_date>/<end_date>")
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    result=jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all())
    return result
  
if (__name__)=="__main__":
    app.run(debug=True)