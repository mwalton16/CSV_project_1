import csv
from datetime import datetime
import matplotlib.pyplot as plt

### Open Files
open_sitka = open('sitka_weather_2018_simple.csv', "r")
open_dv = open('death_valley_2018_simple.csv')
csv_sitka = csv.reader(open_sitka, delimiter=",")
csv_dv = csv.reader(open_dv,delimiter = ',')

### Create Index Dictionaries and Lists
header_row_sitka = next(csv_sitka)
plot_dict_sitka = {}
header_row_dv = next(csv_dv)
plot_dict_dv = {}
sitka_highs, sitka_lows, dv_highs, dv_lows,dates = [],[],[],[],[]
for index, column_header in enumerate(header_row_sitka):
    plot_dict_sitka[column_header] = index
    plot_dict_dv[column_header] = index

### Data Collection
sitka_high = plot_dict_sitka['TMAX']
sitka_low = plot_dict_sitka['TMIN']
dv_high = plot_dict_dv['TMAX']
dv_low = plot_dict_dv['TMIN']
for i in csv_sitka:
    try:
        date_i = datetime.strptime(i[2], "%Y-%m-%d")
        plot_high_i = int(i[sitka_high])
        plot_low_i = int(i[sitka_low])
        plot_high_i = int(i[dv_high])
        plot_low_i = int(i[dv_low])
        dv_highs.append(plot_high_i)
        dv_lows.append(plot_low_i)
        sitka_highs.append(plot_high_i)
        sitka_lows.append(plot_low_i)
        dates.append(date_i)
    except ValueError:
        print(f"Missing data for {date_i}")

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(dates, sitka_highs, color="red")
plt.plot(dates, sitka_lows, color="blue")
plt.title("Sitka Airport, AK US")
plt.subplot(2, 1, 2)
plt.plot(dates, dv_highs, color="red")
plt.plot(dates, dv_lows, color="blue")
plt.title("Death Valley, CA US")
plt.suptitle("Temperature Comparison Between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")
plt.show()
