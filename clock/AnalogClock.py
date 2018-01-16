from PyQt5 import QtCore, QtGui, QtWidgets

"""AnalogClock(QtGui.QWidget)

Provides an analog clock custom widget with signals, slots and properties.
The implementation is based on the Analog Clock example provided with both
Qt and PyQt.
"""


class AnalogClock(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        self.color = QtGui.QColor(113, 249, 76)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(palette)

        self.hourHand = QtGui.QPolygon([
            QtCore.QPoint(0, 0),
            QtCore.QPoint(0, -40)
        ])
        self.minuteHand = QtGui.QPolygon([
            QtCore.QPoint(0, 0),
            QtCore.QPoint(0, -70)
        ])
        self.secondHand = QtGui.QPolygon([
            QtCore.QPoint(0, 0),
            QtCore.QPoint(0, -80)
        ])

    def paint_needle(self, painter, angle, needle):
        painter.save()
        painter.rotate(angle)
        painter.drawConvexPolygon(needle)
        painter.restore()

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QtCore.QTime.currentTime()

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        pen = QtGui.QPen()
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(2)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        pen.setColor(self.color)
        painter.setPen(pen)

        self.paint_needle(painter, 30.0 * (time.hour() + time.minute() / 60.0), self.hourHand)

        for i in range(0, 12):
            painter.drawLine(92, 0, 96, 0)
            painter.rotate(30.0)

        self.paint_needle(painter, 6.0 * (time.minute() + time.second() / 60.0), self.minuteHand)

        pen.setWidth(1)
        painter.setPen(pen)

        self.paint_needle(painter, 6.0 * time.second(), self.secondHand)

        for j in range(0, 60):
            if (j % 5) != 0:
                painter.drawLine(94, 0, 96, 0)
            painter.rotate(6.0)

        painter.end()
