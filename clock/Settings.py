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

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
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

    def init_alarm(self):
        alarm_activated = int(self.parent().settings.value("alarm/activated")) != 0
        self.activate_alarm_radio.setChecked(alarm_activated)
        ms = int(self.parent().settings.value("alarm/time"))
        secs = (ms / 1000) % 60
        mins = (ms / (1000 * 60)) % 60
        hours = (ms / (1000 * 60 * 60)) % 24

        return QtWidgets.QTimeEdit(QtCore.QTime(hours, mins, secs))

    def set_alarm(self, alarm):
        self.activate_alarm_radio.setChecked(False)
        alarm_delay = QtCore.QTime(0, 0, 0).msecsTo(alarm.time())
        self.parent().settings.setValue("alarm/time", alarm_delay)
        self.parent().settings.setValue("alarm/activated", 0)

    def activate_alarm(self):
        if self.activate_alarm_radio.isChecked():
            alarm_delay = self.parent().settings.value("alarm/time")
            self.parent().settings.setValue("alarm/activated", 1)
            self.parent().start_alarm(alarm_delay)
