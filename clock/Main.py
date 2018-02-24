import sys
import os
import signal
from PyQt5 import QtCore, QtWidgets, QtGui
from clock.DigitalClock import DigitalClock
from clock.AnalogClock import AnalogClock
from clock.Settings import Settings
from clock.Alarm import Alarm


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
        self.move(300, 0)
        self.alarm_worker = None
        self.settings_form = None
        self.display_default()
        self.show()

    def display_default(self):
        main_widget = MainWidget(self)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.addWidget(main_widget)
        self.setCentralWidget(widget)

    def display_settings(self):
        self.settings_form = Settings(self)
        self.setCentralWidget(self.settings_form)

    def start_alarm(self, delay):
        self.alarm_worker = Alarm(delay)
        self.alarm_worker.stop_alarm.connect(self.stop_alarm)
        self.alarm_worker.start()

    def stop_alarm(self):
        self.settings.setValue("alarm/activated", 0)

    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit...",
                                                "Are you sure you want to exit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        event.ignore()

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()


class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.digital_clock = DigitalClock()
        self.analog_clock = AnalogClock()
        self.__controls()
        self.__layout()

    def __controls(self):
        self.settings_button = QtWidgets.QPushButton("Settings")
        button_style = 'QPushButton {background-color: #000; color: #71F94C; border: 1px solid #71F94C; padding: 2px;}'
        self.settings_button.setStyleSheet(button_style)
        self.settings_button.clicked.connect(self.parent().display_settings)

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
    font = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)) + '/fonts/DS-DIGIT.TTF'
    QtGui.QFontDatabase.addApplicationFont(font)
    icon_path = os.path.abspath(os.path.join(os.path.dirname(sys.modules[__name__].__file__), os.pardir))
    app.setWindowIcon(QtGui.QIcon(os.path.join(icon_path, 'clock.png')))
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main = Main()
    sys.exit(app.exec_())
