### Imports
import csv
from datetime import datetime
import matplotlib.pyplot as plt

### Open Files
open_sitka = open('sitka_weather_2018_simple.csv', "r")
open_dv = open('death_valley_2018_simple.csv')
csv_sitka = csv.reader(open_sitka, delimiter=",")
csv_dv = csv.reader(open_dv,delimiter = ',')

### Sitka Max and Min
header_row_sitka = next(csv_sitka)
plot_dict_sitka = {}
for index, column_header in enumerate(header_row_sitka):
    plot_dict_sitka[column_header] = index
sitka_high = plot_dict_sitka['TMAX']
sitka_low = plot_dict_sitka['TMIN']

### Death Valley Max and Min
header_row_dv = next(csv_dv)
plot_dict_dv = {}
for index, column_header in enumerate(header_row_dv):
    plot_dict_dv[column_header] = index
dv_high = plot_dict_dv['TMAX']
dv_low = plot_dict_dv['TMIN']

### Plot Variables
sitka_highs, sitka_lows, dv_highs, dv_lows,dates = [],[],[],[],[]

### Data Generation
for i in csv_sitka:
    try:
        date_i = datetime.strptime(i[2], "%Y-%m-%d")
        plot_high_i = int(i[sitka_high])
        plot_low_i = int(i[sitka_low])
        sitka_highs.append(plot_high_i)
        sitka_lows.append(plot_low_i)
        dates.append(date_i)
    except ValueError:
        print(f"Missing data for {date_i}")

for i in csv_dv:
    try:
        date_i = datetime.strptime(i[2], "%Y-%m-%d")
        plot_high_i = int(i[dv_high])
        plot_low_i = int(i[dv_low])
        dv_highs.append(plot_high_i)
        dv_lows.append(plot_low_i)
    except ValueError:
        print(f"Missing data for {date_i}")

for i in range(len(dates)):
    print(str(sitka_highs[i])+", "+
    str(sitka_lows[i])+", "+str(dv_highs[i])+", "+str(dv_lows[i]))

'''
### Figure Creation

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(dates, highs, color="red")
plt.title("Highs")
plt.subplot(2, 1, 2)
plt.plot(dates, lows, color="blue")
plt.title("Lows")
plt.suptitle("Highs and Lows of Sitka, Alaska, 2018")
plt.show()
'''