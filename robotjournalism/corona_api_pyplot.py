import datetime
import json
from matplotlib import pyplot as plt
from urllib import request


class Corona:
    """
    Corana class using APIs
    Please refer to https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest
    """

    def __init__(self, city):
        # constructor
        self.city = city

    def get_confirmed_globally(self):
        url = 'https://api.covid19api.com/world/total'
        response = request.urlopen(url)
        result = json.loads(response.read().decode('utf-8'))
        response.close()
        return result

    def get_confirmed_monthly(self, start, end):
        url = f'https://api.covid19api.com/world?from={start}T00:00:00Z&to={end}T00:00:00Z'
        response = request.urlopen(url)
        result = json.loads(response.read().decode('utf-8'))
        response.close()
        return result


corona = Corona("Seoul")
# total_result = corona.get_confirmed_globally()

start = datetime.datetime(2020, 6, 1)
end = datetime.datetime(2020, 7, 1)
dates = []
index_day = start
while index_day != end:
    dates.append(index_day.strftime('%m-%d'))
    index_day = index_day + datetime.timedelta(days=1)

monthly_result = corona.get_confirmed_monthly(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))

daily_confirmed = []
daily_death = []
for daily_result in monthly_result:
    daily_confirmed.append(daily_result['NewConfirmed'])
    daily_death.append(daily_result['NewDeaths'])

plt.plot(dates, daily_confirmed)
plt.xlabel('Day')
plt.ylabel('New Confirmed')
plt.xticks(dates[::3])
plt.show()
