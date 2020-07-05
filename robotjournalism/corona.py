from urllib import request
import json
from pprint import pprint

class Corona:

    def __init__(self, city):
        self.city = city

    def get_confirmed_globally(self):

        url = "https://api.covid19api.com/world/total"

        result = self.__api_Request(url)

        return result

    def get_confirmed_globally_monthly(self, start, end):

        #  start =  "2020-06-01"
        #  end =  "2020-07-01"

        url = "https://api.covid19api.com/world?from={}T00:00:00Z&to={}T00:00:00Z".format(start, end)

        result = self.__api_Request(url)

        return result

    def get_confirmed_by_country(self, country, start, end):

        url = "https://api.covid19api.com/country/{}/status/confirmed?from={}T00:00:00Z&to={}T00:00:00Z".format(country, start, end)

        result = self.__api_Request(url)

        return result

    def __api_Request(self, url):
        response = request.urlopen(url)
        result = json.loads(response.read().decode("utf-8"))
        response.close()

        return result

corona = Corona("seoul")

print(corona.city)

result = corona.get_confirmed_by_country('south-korea', "2020-06-01", "2020-07-01")

pprint(result)

for day in result:
    new_confirmed = day['Cases']
    print(new_confirmed)

