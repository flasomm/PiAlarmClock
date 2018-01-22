from PyQt5 import QtCore, QtWidgets


class Settings(QtWidgets.QDialog):

    def __init__(self, parent):
        super(Settings, self).__init__()

        self.formGroupBox = QtWidgets.QGroupBox("Settings")
        self.createFormGroupBox()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.gray)
        self.setPalette(palette)

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(parent.displayDefault)
        buttonBox.rejected.connect(parent.displayDefault)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

    def createFormGroupBox(self):
        self.formGroupBox.setAlignment(QtCore.Qt.AlignLeft)
        layout = QtWidgets.QFormLayout()
        layout.addRow(QtWidgets.QLabel("Name:"), QtWidgets.QLineEdit())
        layout.addRow(QtWidgets.QLabel("Country:"), QtWidgets.QComboBox())
        layout.addRow(QtWidgets.QLabel("Age:"), QtWidgets.QSpinBox())
        self.formGroupBox.setLayout(layout)
