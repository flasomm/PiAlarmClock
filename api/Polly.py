import os
from boto3 import client


class Polly:

    def __init__(self, text):
        self.text = "Bonjour Monsieur Sommavilla. {}".format(text)

    def say(self):
        polly = client("polly", 'eu-west-1')
        response = polly.synthesize_speech(
            Text=self.text,
            OutputFormat="mp3",
            VoiceId="Mathieu")

        with open("../mp3/wakeup.mp3", 'wb') as f:
            f.write(response['AudioStream'].read())
            f.close()

        os.system('mplayer ../mp3/wakeup.mp3')
