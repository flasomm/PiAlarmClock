import sys
import os
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
        self.setWindowTitle('RaspberryClock')
        self.setGeometry(600, 600, 600, 500)
        self.move(600, 300)
        self.display_default()
        self.show()

    def display_default(self):
        main_widget = MainWidget(self)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.addWidget(main_widget)
        self.setCentralWidget(widget)

    def display_settings(self):
        settings = Settings(self)
        self.setCentralWidget(settings)


class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.__controls()
        self.__layout()

    def __controls(self):
        self.settings_button = QtWidgets.QPushButton("Settings")
        button_style = 'QPushButton {background-color: #000; color: #71F94C; border: 1px solid #71F94C; padding: 2px;}'
        self.settings_button.setStyleSheet(button_style)
        self.settings_button.clicked.connect(self.parent().display_settings)
        self.digital_clock = DigitalClock()
        self.analog_clock = AnalogClock()

    def __layout(self):
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.settings_button)

        if int(self.parent().settings.value("default/digital")) == 1:
            self.vbox.addWidget(self.digital_clock)
        else:
            self.vbox.addWidget(self.analog_clock)

        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    icon_path = os.path.abspath(os.path.join(os.path.dirname(sys.modules[__name__].__file__), os.pardir))
    app.setWindowIcon(QtGui.QIcon(os.path.join(icon_path, 'clock.png')))
    main = Main()
    sys.exit(app.exec_())
