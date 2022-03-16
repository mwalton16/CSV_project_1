import csv
from datetime import datetime


open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")
header_row = next(csv_file)
print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []


for i in csv_file:

    highs.append(int(i[5]))
    lows.append(int(i[6]))
    date_i = datetime.strptime(i[2], "%Y-%m-%d")
    dates.append(date_i)
print(highs)

print(dates)
import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, color="red")
plt.plot(dates, lows, color="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily High Temperatures, Sitka, Alaska, July, 2018", fontsize=16)
plt.xlabel("Month of July")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
fig.autofmt_xdate()
plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, color="red")
plt.title("Highs")
plt.subplot(2, 1, 2)
plt.plot(dates, lows, color="blue")
plt.title("Lows")
plt.suptitle("Highs and Lows of Sitka, Alaska, 2018")
plt.show()
