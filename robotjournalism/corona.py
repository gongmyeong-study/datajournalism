from urllib import request
import json


class Corona:
    def __init__(self, city=None):
        self.city = city

    def get_confirmed_globally(self):
        url = "https://api.covid19api.com/world/total"
        return self._api_request(url)

    def get_confirmed_globally_monthly(self, start, end):
        url = "https://api.covid19api.com/world?from={}T00:00:00Z&to={}T00:00:00Z".format(start, end)
        return self._api_request(url)

    def get_confirmed_by_country(self, country):
        url = "https://api.covid19api.com/country/{}".format(country)
        return self._api_request(url)

    def _api_request(self, url):
        response = request.urlopen(url)
        res = json.loads(response.read().decode("utf-8"))
        response.close()
        return res
