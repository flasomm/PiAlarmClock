from PyQt5 import QtCore, QtWidgets


class Settings(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Settings, self).__init__(parent)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        self.setPalette(palette)

        form_layout = QtWidgets.QFormLayout()
        form_layout.setFormAlignment(QtCore.Qt.AlignLeft)
        hbox_type = QtWidgets.QHBoxLayout()

        digital_radio = QtWidgets.QRadioButton("Digital")
        analog_radio = QtWidgets.QRadioButton("Analog")
        analog_radio.toggled.connect(lambda: parent.settings.setValue("default/digital", 0))
        digital_radio.toggled.connect(lambda: parent.settings.setValue("default/digital", 1))

        digital_radio.setAutoExclusive(True)
        analog_radio.setAutoExclusive(True)

        digital_radio_checked = True if (int(parent.settings.value("default/digital")) == 1) else False
        analog_radio_checked = True if (int(parent.settings.value("default/digital")) == 0) else False
        digital_radio.setChecked(digital_radio_checked)
        analog_radio.setChecked(analog_radio_checked)

        hbox_type.addWidget(digital_radio)
        hbox_type.addWidget(analog_radio)
        hbox_type.addStretch()

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Save)
        button_box.accepted.connect(parent.display_default)
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(button_box)

        hbox_alarm = QtWidgets.QHBoxLayout()
        time = QtCore.QTime()
        curent_t = time.currentTime()
        self.alarm = QtWidgets.QTimeEdit(curent_t)
        self.alarm.dateTimeChanged.connect(self.set_alarm)
        self.activate_alarm_radio = QtWidgets.QCheckBox("Activate")
        self.activate_alarm_radio.clicked.connect(self.activate_alarm)
        hbox_alarm.addWidget(self.alarm)
        hbox_alarm.addWidget(self.activate_alarm_radio)

        form_layout.addRow(QtWidgets.QLabel("Clock Type:"), hbox_type)
        form_layout.addRow(QtWidgets.QLabel("Alarm:"), hbox_alarm)
        form_layout.addRow(button_layout)

        self.setLayout(form_layout)

        # layoutRadio.setFormAlignment(QtCore.Qt.AlignCenter)
        # name.setMinimumSize(QtCore.QSize(500, 21))

    def activate_alarm(self):
        self.set_alarm(self.alarm)

    def set_alarm(self, data):
        if self.activate_alarm_radio.isChecked():
            current_in_sec = QtCore.QTime(0, 0, 0).secsTo(QtCore.QTime.currentTime())
            alarm_in_sec = QtCore.QTime(0, 0, 0).secsTo(data.time())
            alarm_sec = alarm_in_sec - current_in_sec
            self.parent().settings.setValue("alarm/time", alarm_sec)
            print("alarm", alarm_sec)
        else:
            self.parent().settings.setValue("alarm/time", 0)
