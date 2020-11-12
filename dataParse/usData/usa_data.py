import pandas as pd
import os
import pyodbc

csv_path = "E:/Programming/Projects/COVID-19-Windows/covidData/COVID-19/csse_covid_19_data/csse_covid_19_time_series/"

us_deaths = pd.read_csv(csv_path + "time_series_covid19_deaths_US.csv")

server = 'localhost'
database = 'covid19'
username = 'zsmith'
password = ''

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

uid = us_deaths.columns[0]  # int or float
county = us_deaths.columns[5]  # string. will need to account for null values
province_state = us_deaths.columns[6]  # string
latitude = us_deaths.columns[8]  # float
longitude = us_deaths.columns[9]  # float
population = us_deaths.columns[11]  # int

# want to grab every item in columns except for last row since last row is NaN
# Last row also doesn't have useful info
county_vals = us_deaths[county][:-1]
province_state_vals = us_deaths[province_state][:-1]
latitude_vals = us_deaths[latitude][:-1]
longitude_vals = us_deaths[longitude][:-1]
population_vals = us_deaths[population][:-1]

# cursor.execute("CREATE TABLE [covid19].[dbo].[usa] (UID INT IDENTITY (1,1) PRIMARY KEY, County nvarchar(50), State nvarchar(50), Latitude FLOAT, Longitude FLOAT, Population INT);")

sql = "INSERT INTO usa (County, State, Latitude, Longitude, Population) VALUES (?, ?, ?, ?, ?)"

county_arr = []

for item in county_vals:
    if item != item:
        county_arr.append(None)
    else:
        county_arr.append(item)

data_arr = list(zip(county_arr, province_state_vals,
                    latitude_vals, longitude_vals, population_vals))

for item in data_arr:
    with cursor.execute(sql, item):
        print("Success")

# for item in data_arr:
#     cursor.execute(sql, item)
# cursor.execute(sql, data_arr)