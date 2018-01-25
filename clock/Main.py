import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from clock.DigitalClock import DigitalClock
from clock.AnalogClock import AnalogClock
from clock.Settings import Settings


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.settings = QtCore.QSettings('../settings.ini', QtCore.QSettings.IniFormat)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(palette)
        self.setGeometry(600, 600, 600, 500)
        self.move(600, 300)
        self.setWindowTitle('RaspberryClock')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.displayDefault()
        self.show()

    def displayDefault(self):
        mainWidget = MainWidget(self)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.addWidget(mainWidget)
        self.setCentralWidget(widget)

    def displaySettings(self):
        settings = Settings(self)
        self.setCentralWidget(settings)


class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.__controls()
        self.__layout()

    def __controls(self):
        self.settingsButton = QtWidgets.QPushButton("Settings")
        buttonStyle = 'QPushButton {background-color: #000; color: #71F94C; border: 1px solid #71F94C; padding: 2px;}'
        self.settingsButton.setStyleSheet(buttonStyle)
        self.settingsButton.clicked.connect(self.parent().displaySettings)
        self.digitalClock = DigitalClock()
        self.analogClock = AnalogClock()

    def __layout(self):
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.settingsButton)

        if self.parent().settings.value("default/digital") == "1":
            self.vbox.addWidget(self.digitalClock)
        else:
            self.vbox.addWidget(self.analogClock)

        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
