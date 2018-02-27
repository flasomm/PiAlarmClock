import urllib3, urllib, json


class Weather:

    def __init__(self):
        self.baseurl = "https://query.yahooapis.com/v1/public/yql?"
        self.yql_query = "select wind from weather.forecast where woeid=2460286"

    def infos(self):
        yql_url = self.baseurl + urllib.urlencode({'q': self.yql_query}) + "&format=json"
        result = urllib3.urlopen(yql_url).read()
        return json.loads(result)
        # print data['query']['results']
