from PyQt5 import QtCore, QtWidgets


class Settings(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Settings, self).__init__(parent)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.gray)
        self.setPalette(palette)

        formLayout = QtWidgets.QFormLayout()
        formLayout.setFormAlignment(QtCore.Qt.AlignLeft)
        hbox = QtWidgets.QHBoxLayout()
        digitalRadio = QtWidgets.QRadioButton("Digital")
        analogRadio = QtWidgets.QRadioButton("Analog")
        analogRadio.clicked.connect(parent.settings.setValue("default/digital", 0))
        digitalRadio.clicked.connect(parent.settings.setValue("default/digital", 1))

        digitalRadio.setAutoExclusive(True)
        analogRadio.setAutoExclusive(True)
        digitalRadio.setChecked(True)

        hbox.addWidget(digitalRadio)
        hbox.addWidget(analogRadio)
        hbox.addStretch()

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(parent.displayDefault)
        buttonBox.rejected.connect(parent.displayDefault)
        buttonLayout = QtWidgets.QVBoxLayout()
        buttonLayout.addWidget(buttonBox)

        formLayout.addRow(QtWidgets.QLabel("Clock Type:"), hbox)
        formLayout.addRow(buttonLayout)

        self.setLayout(formLayout)

        # layoutRadio.setFormAlignment(QtCore.Qt.AlignCenter)
        # name.setMinimumSize(QtCore.QSize(500, 21))
