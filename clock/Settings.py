from PyQt5 import QtCore, QtWidgets


class Settings(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Settings, self).__init__(parent)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.gray)
        self.setPalette(palette)

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(parent.displayDefault)
        buttonBox.rejected.connect(parent.displayDefault)

        formGroupBox = QtWidgets.QGroupBox("Settings")
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(formGroupBox)
        mainLayout.addWidget(buttonBox)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(QtWidgets.QLabel("Name:"), 1, 0)
        layout.addWidget(QtWidgets.QLineEdit(), 1, 1)
        layout.addWidget(QtWidgets.QLabel("Country:"), 2, 0)
        layout.addWidget(QtWidgets.QComboBox(), 2, 1)
        layout.addWidget(QtWidgets.QLabel("Age:"), 3, 0)
        layout.addWidget(QtWidgets.QSpinBox(), 3, 1)
        layout.setColumnStretch(1, 100)
        layout.setColumnStretch(2, 10)
        layout.setColumnStretch(3, 10)
        formGroupBox.setLayout(layout)
        self.setLayout(mainLayout)

