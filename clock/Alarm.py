from PyQt5 import QtCore
from api.Weather import Weather
from api.Polly import Polly


class Alarm(QtCore.QThread):
    stop_alarm = QtCore.pyqtSignal()

    def __init__(self, millis):
        super(Alarm, self).__init__()
        self.millis = int(millis)
        self.keep_running = True

    def run(self):
        print("Alarm Start")
        try:
            while self.keep_running:
                current_ms = QtCore.QTime(0, 0, 0).msecsTo(QtCore.QTime.currentTime())
                if self.millis == current_ms:
                    self.times_up()
                    return
        except:
            return

    def times_up(self):
        print("Alarm stop")
        self.keep_running = False
        weather = Weather()
        voice = Polly(weather.infos())
        voice.say()
        self.stop_alarm.emit()
        self.quit()
