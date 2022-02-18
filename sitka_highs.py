import csv
from multiprocessing.sharedctypes import Value 
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs, lows, dates = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
    
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates,highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title('Highest temperature each day in 2018', fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature(F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

print(highs)