import pandas as pd
import os
import pyodbc
from sqlalchemy import create_engine

csv_path = "E:/Programming/Projects/COVID-19-Windows/"

deaths = pd.read_csv(csv_path + "deaths.csv")
cases = pd.read_csv(csv_path + "cases.csv")
global_cases = pd.read_csv(csv_path + "global_cases.csv")
global_deaths = pd.read_csv(csv_path + "global_deaths.csv")

del deaths['Unnamed: 0']
del cases['Unnamed: 0']
del global_cases['Unnamed: 0']
del global_deaths['Unnamed: 0']

engine = create_engine(f"mssql+pyodbc://zsmith:{os.environ['DBPASSWD']}@localhost/covid19?driver=ODBC+Driver+17+for+SQL+Server")

deaths.to_sql('deaths', engine, if_exists='replace', index=True, index_label=None, method=None)
cases.to_sql('cases', engine, if_exists='replace', index=True, index_label=None, method=None)
global_deaths.to_sql('global_deaths', engine, if_exists='replace', index=True, index_label=None, method=None)
global_cases.to_sql('global_cases', engine, if_exists='replace', index=True, index_label=None, method=None)