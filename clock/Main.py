import sys
import configparser
from PyQt5 import QtCore, QtWidgets, QtGui
from clock.DigitalClock import DigitalClock
from clock.AnalogClock import AnalogClock


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(palette)
        self.setGeometry(600, 600, 600, 500)
        self.move(600, 300)
        self.setWindowTitle('RaspberryClock')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.mainWidget = MainWidget(self)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.addWidget(self.mainWidget)
        self.setCentralWidget(widget)


class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.config = configparser.ConfigParser()
        self.config.read_file(open('../settings.ini'))
        self.__controls()
        self.__layout()

    def __controls(self):
        self.settingsButton = QtWidgets.QPushButton("Settings")
        self.digitalClock = DigitalClock()
        self.analogClock = AnalogClock()

    def __layout(self):
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        self.hbox.addStretch(1)
        self.hbox.addWidget(self.settingsButton)

        if self.config['default']['digital'] == "1":
            self.vbox.addWidget(self.digitalClock)
        else:
            self.vbox.addWidget(self.analogClock)

        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
