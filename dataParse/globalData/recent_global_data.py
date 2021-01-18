import pandas as pd

csv_path = "E:/Programming/Projects/COVID-19-Windows/covidData/csse_covid_19_data/csse_covid_19_time_series/"

global_cases = pd.read_csv(csv_path + 'time_series_covid19_confirmed_global.csv')
global_deaths = pd.read_csv(csv_path + 'time_series_covid19_deaths_global.csv')

confirmed_dates = global_cases.columns[4:]
death_dates = global_deaths.columns[4:]

def create_csv(data, dates, csv_name):
    columns = ['ID']
    dataLength = len(data)

    for header in dates:
        columns.append(header)

    id_arr = []
    increment = 1

    while increment <= dataLength:
        id_arr.append(increment)
        increment += 1

    col_arr = []
    count = 1

    while count <= dataLength:
        sub_arr = []
        sub_arr.append(id_arr.pop(0))

        for header in dates:
            sub_arr.append(data[header].pop(count - 1))

        col_arr.append(sub_arr)

        count += 1

    csv = csv_name + '.csv'
    csv_name = pd.DataFrame(col_arr, columns=columns,)
    csv_name.to_csv(csv)

create_csv(global_cases, confirmed_dates, 'global_cases')
create_csv(global_deaths, death_dates, 'global_deaths')