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

        digital_radio.setChecked(int(parent.settings.value("default/digital")) == 1)
        analog_radio.setChecked(int(parent.settings.value("default/digital")) == 0)

        hbox_type.addWidget(digital_radio)
        hbox_type.addWidget(analog_radio)
        hbox_type.addStretch()

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Save)
        button_box.accepted.connect(parent.display_default)
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(button_box)

        hbox_alarm = QtWidgets.QHBoxLayout()

        self.activate_alarm_radio = QtWidgets.QCheckBox("Activate")
        self.activate_alarm_radio.clicked.connect(self.activate_alarm)
        self.alarm = self.init_alarm()
        self.alarm.dateTimeChanged.connect(self.set_alarm)
        hbox_alarm.addWidget(self.alarm)
        hbox_alarm.addWidget(self.activate_alarm_radio)

        form_layout.addRow(QtWidgets.QLabel("Clock Type:"), hbox_type)
        form_layout.addRow(QtWidgets.QLabel("Alarm:"), hbox_alarm)
        form_layout.addRow(button_layout)

        self.setLayout(form_layout)

    def sec_to_hms(self, sec):
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)

        return [h, m, s]

    def init_alarm(self):
        is_checked = int(self.parent().settings.value("alarm/time")) != 0
        self.activate_alarm_radio.setChecked(is_checked)
        hms = [0, 0, 0]
        if is_checked:
            hms = self.sec_to_hms(int(self.parent().settings.value("alarm/time")))

        return QtWidgets.QTimeEdit(QtCore.QTime(hms[0], hms[1], hms[2]))

    def set_alarm(self, data):
        alarm_in_sec, time_diff_sec = 0, 0
        if self.activate_alarm_radio.isChecked():
            current_in_sec = QtCore.QTime(0, 0, 0).secsTo(QtCore.QTime.currentTime())
            alarm_in_sec = QtCore.QTime(0, 0, 0).secsTo(data.time())
            time_diff_sec = alarm_in_sec - current_in_sec
        if time_diff_sec < 0:
            time_diff_sec += 86400  # number of seconds in a day
        self.parent().settings.setValue("alarm/time", alarm_in_sec)
        
        print(self.sec_to_hms(time_diff_sec))

    def activate_alarm(self):
        self.set_alarm(self.alarm)
