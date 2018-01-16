from PyQt5 import QtCore, QtGui, QtWidgets

"""AnalogClock(QtGui.QWidget)

Provides an analog clock custom widget with signals, slots and properties.
The implementation is based on the Analog Clock example provided with both
Qt and PyQt.
"""


class AnalogClock(QtWidgets.QWidget):
    # Emitted when the clock's time changes.
    timeChanged = QtCore.pyqtSignal(QtCore.QTime)

    # Emitted when the clock's time zone changes.
    timeZoneChanged = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.timeZoneOffset = 0

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        self.color = QtGui.QColor(205, 216, 87)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(palette)

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QtCore.QTime.currentTime()
        time = time.addSecs(self.timeZoneOffset * 3600)

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        pen = QtGui.QPen()
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(4)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        pen.setColor(self.color)
        painter.setPen(pen)

        painter.save()
        painter.rotate(30.0 * (time.hour() + time.minute() / 60.0))
        painter.drawLine(0, 0, -35, -35)
        painter.restore()

        for i in range(0, 12):
            painter.drawLine(92, 0, 96, 0)
            painter.rotate(30.0)

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawLine(0, 0, -50, -50)
        painter.restore()

        pen.setWidth(1)
        painter.setPen(pen)

        painter.save()
        painter.rotate(6.0 * time.second())
        painter.drawLine(0, 0, -60, -60)
        painter.restore()

        for j in range(0, 60):
            if (j % 5) != 0:
                painter.drawLine(94, 0, 96, 0)
            painter.rotate(6.0)

        painter.end()

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(100, 100)

    def update_time(self):
        self.timeChanged.emit(QtCore.QTime.currentTime())

    # The timeZone property is implemented using the getTimeZone() getter
    # method, the setTimeZone() setter method, and the resetTimeZone() method.

    # The getter just returns the internal time zone value.
    def get_timezone(self):
        return self.timeZoneOffset

    # The setTimeZone() method is also defined to be a slot. The @pyqtSlot
    # decorator is used to tell PyQt which argument type the method expects,
    # and is especially useful when you want to define slots with the same
    # name that accept different argument types.

    @QtCore.pyqtSlot(int)
    def set_timezone(self, value):
        self.timeZoneOffset = value
        self.timeZoneChanged.emit(value)
        self.update()

    # Qt's property system supports properties that can be reset to their
    # original values. This method enables the timeZone property to be reset.
    def reset_timezone(self):
        self.timeZoneOffset = 0
        self.timeZoneChanged.emit(0)
        self.update()

    # Qt-style properties are defined differently to Python's properties.
    # To declare a property, we call pyqtProperty() to specify the type and,
    # in this case, getter, setter and resetter methods.
    timeZone = QtCore.pyqtProperty(int, get_timezone, set_timezone, reset_timezone)
