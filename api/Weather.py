import urllib.parse
import urllib.request
import json
import datetime
import os


class Weather:

    def __init__(self):
        self.baseurl = "https://query.yahooapis.com/v1/public/yql?"
        self.yql_query = "select * from weather.forecast where woeid=615702 and u='c'"

    def format_speech(self, data):
        location = data['channel']['location']['city']
        sunrise = data['channel']['astronomy']['sunrise']
        sunset = data['channel']['astronomy']['sunset']
        temp = data['channel']['item']['condition']['temp']
        condition = data['channel']['item']['condition']['code']
        wind = data['channel']['wind']['speed']
        humidity = data['channel']['atmosphere']['humidity']

        codes = json.load(open(os.path.dirname(os.path.realpath(__file__)) + '/weather-codes.json', encoding='utf8'))
        sunrise = datetime.datetime.strptime(sunrise, "%I:%M %p")
        sunset = datetime.datetime.strptime(sunset, "%I:%M %p")
        res = """La température aujourd'hui à %s est de %s degrés celsius.
                Conditions %s.
                Le vent souffle à %10.0f kilomètres heure.
                Humidité %10.0f pourcent.
                Lever du soleil à %s, coucher à %s""" % (
            location, temp, codes[condition], float(wind), float(humidity),
            sunrise.strftime("%H heure %M"), sunset.strftime("%H heure %M")
        )
        print(res)
        return res

    def infos(self):
        yql_url = self.baseurl + urllib.parse.urlencode({'q': self.yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        return self.format_speech(data['query']['results'])
