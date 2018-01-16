import sys
import configparser
from time import strftime
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon
from clock.AnalogClock import AnalogClock
from clock.AnalogClock2 import AnalogClock2


class Clock(QWidget):

    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.read_file(open('../settings.ini'))
        self.lcd = None
        self.init_ui()

    def init_ui(self):
        self.setGeometry(600, 600, 600, 500)
        self.move(600, 300)
        self.setWindowTitle('RaspberryClock')
        self.setWindowIcon(QIcon('web.png'))

        settings_button = QPushButton("Settings")
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(settings_button)

        if self.config['default']['digital'] == "1":
            timer = QTimer(self)
            timer.timeout.connect(self._time)
            timer.start(1000)

            self.lcd = QLCDNumber(self)
            self.lcd.setNumDigits(8)
            self.lcd.resize(600, 500)
            self.lcd.display(strftime("%H" + ":" + "%M" + ":" + "%S"))
            vbox.addWidget(self.lcd)

        else:
            analog_clock = AnalogClock()
            vbox.addWidget(analog_clock)

        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.show()

    def _time(self):
        self.lcd.display(strftime("%H" + ":" + "%M" + ":" + "%S"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    sys.exit(app.exec_())
