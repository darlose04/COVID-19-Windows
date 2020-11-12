import pandas as pd
import os
import pyodbc

csv_path = "E:/Programming/Projects/COVID-19-Windows/covidData/COVID-19/csse_covid_19_data/csse_covid_19_time_series/"

us_deaths = pd.read_csv(csv_path + "time_series_covid19_deaths_US.csv")
