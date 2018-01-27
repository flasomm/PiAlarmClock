from PyQt5 import QtCore, QtGui, QtWidgets

"""DigitalClock(QtWidgets.QLCDNumber)

Provides a digital clock custom widget.
"""


class DigitalClock(QtWidgets.QLCDNumber):

    def __init__(self):
        super().__init__()

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setNumDigits(8)
        self.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        palette = self.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(113, 249, 76))
        palette.setColor(palette.Light, QtCore.Qt.black)
        palette.setColor(palette.Dark, QtCore.Qt.black)
        self.setPalette(palette)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)

        self.show_time()

    def show_time(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.display(text)
