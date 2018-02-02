import time
import os
import threading


class Alarm(threading.Thread):

    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if now.tm_hour == self.hours and now.tm_min == self.minutes:
                    print("ALARM NOW!")
                    #os.popen("bensound-dubstep.mp3")
                    return
            time.sleep(60)
        except:
            return

    def just_die(self):
        self.keep_running = False
