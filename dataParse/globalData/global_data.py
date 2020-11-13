import pandas as pd
import pyodbc
import os

csv_path = "E:/Programming/Projects/COVID-19-Windows/covidData/COVID-19/csse_covid_19_data/csse_covid_19_time_series/"

global_cases = pd.read_csv(csv_path + "time_series_covid19_confirmed_global.csv")

server = 'localhost'
database = 'covid19'
username = 'zsmith'
password = os.environ['DBPASSWD']

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

province = global_cases.columns[0]
country = global_cases.columns[1]
latitude = global_cases.columns[2]
longitude = global_cases.columns[3]

province_vals = global_cases[province]
country_vals = global_cases[country]
latitude_vals = global_cases[latitude]
longitude_vals = global_cases[longitude]

sql = "INSERT INTO global (Province, Country, Latitude, Longitude) VALUES (?, ?, ?, ?)"

province_arr = []

for item in province_vals:
    if item != item:
        province_arr.append(None)
    else:
        province_arr.append(item)

data_arr = list(zip(province_arr, country_vals, latitude_vals, longitude_vals))

for item in data_arr:
    with cursor.execute(sql, item):
        print("Success")