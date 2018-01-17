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
        self.needlesColor = QtGui.QColor(84, 189, 55)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(palette)

        self.hourHand = QtGui.QPolygon([
            QtCore.QPoint(0, 0),
            QtCore.QPoint(0, -50)
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
        pen.setWidth(3)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        pen.setJoinStyle(QtCore.Qt.RoundJoin)
        pen.setColor(self.needlesColor)
        painter.setPen(pen)

        self.paint_needle(painter, 0.5 * (60 * time.hour() + time.minute()), self.hourHand)
        self.paint_needle(painter, 6.0 * time.minute(), self.minuteHand)

        painter.save()
        pen.setColor(self.color)
        pen.setWidth(1)
        painter.setPen(pen)

        self.paint_needle(painter, 6.0 * time.second(), self.secondHand)

        for j in range(0, 60):
            if (j % 5) != 0:
                painter.drawLine(94, 0, 96, 0)
            painter.rotate(6.0)
        painter.restore()

        painter.save()
        pen.setWidth(3)
        painter.setPen(pen)

        for i in range(0, 12):
            painter.drawLine(92, 0, 96, 0)
            painter.rotate(30.0)
        painter.restore()

        painter.save()
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self.color)
        painter.drawEllipse(-3, -3, 6, 6)
        painter.restore()
        painter.end()
