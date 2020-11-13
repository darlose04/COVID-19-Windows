import pandas as pd
import os
import pyodbc
from sqlalchemy import create_engine

csv_path = "E:/Programming/Projects/COVID-19-Windows/"

deaths = pd.read_csv(csv_path + "deaths.csv")
cases = pd.read_csv(csv_path + "cases.csv")

del deaths['Unnamed: 0']
del cases['Unnamed: 0']

engine = create_engine(f"mssql+pyodbc://zsmith:{os.environ['DBPASSWD']}@localhost:1433/covid19")

deaths.to_sql('deaths', engine, if_exists='replace', index=True, index_label=None, method=None)
cases.to_sql('cases', engine, if_exists='replace', index=True, index_label=None, method=None)