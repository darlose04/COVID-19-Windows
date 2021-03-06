import pandas as pd

csv_path = "E:/Programming/Projects/COVID-19-Windows/covidData/csse_covid_19_data/csse_covid_19_time_series/"

us_deaths = pd.read_csv(csv_path + "time_series_covid19_deaths_US.csv")
us_confirmed = pd.read_csv(csv_path + "time_series_covid19_confirmed_US.csv")

death_dates = us_deaths.columns[12:]
confirmed_dates = us_confirmed.columns[12:]

def create_csv(data, dates, csv_name):
    columns = ['UID']
    dataLength = len(data)

    for header in dates:
        columns.append(header)

    uid_arr = []
    increment = 1

    while increment <= dataLength:
        uid_arr.append(increment)
        increment += 1

    col_arr = []
    count = 1

    while count <= dataLength:
        sub_arr = []
        sub_arr.append(uid_arr.pop(0))

        for header in dates:
            sub_arr.append(data[header].pop(count - 1))

        col_arr.append(sub_arr)

        count += 1

    csv = csv_name + '.csv'
    csv_name = pd.DataFrame(col_arr, columns=columns,)
    csv_name.to_csv(csv)

create_csv(us_deaths, death_dates, 'deaths')
create_csv(us_confirmed, confirmed_dates, 'cases')