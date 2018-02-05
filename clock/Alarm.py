from PyQt5 import QtCore


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
                    print("ALARM NOW!")
                    self.times_up()
                    return
        except:
            return

    def times_up(self):
        print("Alarm stop")
        self.keep_running = False
        self.stop_alarm.emit(self.stop_alarm, "terminated")
        self.terminate()
