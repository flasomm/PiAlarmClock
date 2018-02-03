from PyQt5 import QtCore
import time


class Alarm(QtCore.QThread):

    def __init__(self, millis):
        super(Alarm, self).__init__()
        self.millis = int(millis)
        print('millis', millis)
        self.keep_running = True

    def run(self):
        print("Alarm Start")
        # QtCore.QTimer().singleShot(self.millis, self.times_up)
        try:
            while self.keep_running:
                current_ms = int(round(time.time() * 1000))
                print('millis', self.millis)
                print('current', current_ms)
                if current_ms == self.millis:
                    print("ALARM NOW!")
                    self.times_up()
                    return
        except:
            return

    def times_up(self):
        print("Alarm stop")
        self.keep_running = False
        self.terminate()
