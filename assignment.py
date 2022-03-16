### Imports
import csv
from datetime import datetime
import matplotlib.pyplot as plt

### Open Files
open_sitka = open('sitka_weather_2018_simple.csv', "r")
open_dv = open('death_valley_2018_simple.csv')
csv_sitka = csv.reader(open_sitka, delimiter=",")
csv_dv = csv.reader(open_dv,delimiter = ',')

### Choose Variable to Plot
header_row = next(csv_sitka)
plot_dict = {}
print("What input would you like to use? Options are:")
for index, column_header in enumerate(header_row):
    plot_dict[column_header] = index
    print(column_header)
plot_choice = input()
data_column = plot_dict[plot_choice]
plot_variable_sitka = []
plot_variable_dv = []
dates = []

### Data Generation
for i in csv_sitka:
    try:
        date_i = datetime.strptime(i[2], "%Y-%m-%d")
        plot_var_i = int(i[data_column])
        plot_variable_sitka.append(plot_var_i)
        dates.append(date_i)
    except ValueError:
        print(f"Missing data for {date_i}")
print(plot_variable_sitka)
for i in csv_dv:
    try:
        date_i = datetime.strptime(i[2], "%Y-%m-%d")
        plot_var_i = int(i[data_column])
        plot_variable_dv.append(plot_var_i)
        dates.append(date_i)
    except ValueError:
        print(f"Missing data for {date_i}")

for i in range(len(dates)):
    print(str(i)+', '+str(plot_variable_sitka[i])+", "+str(plot_variable_dv[i]))

### Figure Creation

fig = plt.figure()
