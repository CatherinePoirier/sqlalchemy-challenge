# SQLAlchemy Homework - Surfs Up!

## Step 1 - Climate Analysis and Exploration

* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.

I chose the end date to be largest date in the data set and the start date is one year before the. The dt.date and 
dt.timedelta methods were used in this calculation.



* Design a query to retrieve the last 12 months of precipitation data. * Select only the `date` and `prcp` values.
After analysing the data, session.query was used to come up with the Precipitation for the last year.


* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by `date`.* Plot the results using the DataFrame `plot` method.

The bar graph was saved as percipitationHW.png

* Use Pandas to print the summary statistics for the precipitation data.
I used the handy df.describe() to get this info.


### Station Analysis

* Design a query to calculate the total number of stations.
Used func.count
There are 9 stations in the dataset.


* Design a query to find the most active stations.
  * List the stations and observation counts in descending order.

[('USC00519281', 2772),
 ('USC00519397', 2724),
 ('USC00513117', 2709),
 ('USC00519523', 2669),
 ('USC00516128', 2612),
 ('USC00514830', 2202),
 ('USC00511918', 1979),
 ('USC00517948', 1372),
 ('USC00518838', 511)]

  * Which station has the highest number of observations?

The most active station is USC00519281


* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
  * Filter by the station with the highest number of observations.
  * Plot the results as a histogram with `bins=12`.

The lowest temp for Station USC00519281 is [[(54.0,)]]
The highest temp for Station USC00519281 is [[(85.0,)]]
The average temp for Station USC00519281 is [(71.66378066378067,)]
The Histogram is Saved in (Images/station-histogramHW.png)

- - -

## Step 2 - Climate App



* Use Flask to create your routes.

  * Home page.
  * List all routes that are available.
/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/start
/api/v1.0/start/end


* `/api/v1.0/precipitation* Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
  * Return the JSON representation of your dictionary.

 http://localhost:5000/api/v1.0/precipitation

* `/api/v1.0/stations  * Return a JSON list of stations from the dataset.

Got to http://localhost:5000/api/v1.0/stations

* `/api/v1.0/tobs` * Query the dates and temperature observations of the most active station for the last year of data.
  * Return a JSON list of temperature observations (TOBS) for the previous year.

Got to http://localhost:5000/api/v1.0/tobs
  


* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

Go to http://localhost:5000/api/v1.0/  then type in a start date in the format of 4 digit year-month-day example 2016-09-04 
then type in an in the same format. Use "/" as a divider between the two. The min date you can use is 2010-0101 and the max date is 8/23/2017.
example  http://localhost:5000/api/v1.0/2015-12-5/2016-02-15

 format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.




