# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/ShutterWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShutterWidget(object):
    def setupUi(self, ShutterWidget):
        ShutterWidget.setObjectName("ShutterWidget")
        ShutterWidget.resize(392, 132)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShutterWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ShutterWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.statusHardware = QtWidgets.QLineEdit(ShutterWidget)
        self.statusHardware.setEnabled(False)
        self.statusHardware.setReadOnly(True)
        self.statusHardware.setObjectName("statusHardware")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.statusHardware)
        self.label_2 = QtWidgets.QLabel(ShutterWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(ShutterWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openShutter = QtWidgets.QPushButton(ShutterWidget)
        self.openShutter.setObjectName("openShutter")
        self.horizontalLayout.addWidget(self.openShutter)
        self.closeShutter = QtWidgets.QPushButton(ShutterWidget)
        self.closeShutter.setObjectName("closeShutter")
        self.horizontalLayout.addWidget(self.closeShutter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.quit = QtWidgets.QPushButton(ShutterWidget)
        self.quit.setObjectName("quit")
        self.verticalLayout.addWidget(self.quit)

        self.retranslateUi(ShutterWidget)
        self.quit.clicked.connect(ShutterWidget.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ShutterWidget)

    def retranslateUi(self, ShutterWidget):
        _translate = QtCore.QCoreApplication.translate
        ShutterWidget.setWindowTitle(_translate("ShutterWidget", "Form"))
        self.label.setText(_translate("ShutterWidget", "Status Hardware"))
        self.statusHardware.setText(_translate("ShutterWidget", "unknown"))
        self.label_2.setText(_translate("ShutterWidget", "Status Shutter"))
        self.lineEdit.setText(_translate("ShutterWidget", "unknown"))
        self.openShutter.setText(_translate("ShutterWidget", "Open"))
        self.closeShutter.setText(_translate("ShutterWidget", "Close"))
        self.quit.setText(_translate("ShutterWidget", "Quit"))
