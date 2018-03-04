import urllib.parse
import urllib.request
import json


class Weather:

    def __init__(self):
        self.baseurl = "https://query.yahooapis.com/v1/public/yql?"
        self.yql_query = "select * from weather.forecast where woeid=615702"

    def infos(self):
        yql_url = self.baseurl + urllib.parse.urlencode({'q': self.yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        print(data['query']['results'])
        return data
