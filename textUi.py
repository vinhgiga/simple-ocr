# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Vinh/AppData/Local/Temp/textUiDQHOur.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextForm(object):
    def setupUi(self, TextForm):
        TextForm.setObjectName("TextForm")
        TextForm.resize(814, 488)
        TextForm.setStyleSheet("QPushButton {\n"
"    font-family: Arial;\n"
"    font-size: 17px;\n"
"    min-width: 26px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 17px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(TextForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLabel(TextForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setText("")
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save_to_file = QtWidgets.QPushButton(TextForm)
        self.pushButton_save_to_file.setObjectName("pushButton_save_to_file")
        self.horizontalLayout.addWidget(self.pushButton_save_to_file)
        self.pushButton_copy_text = QtWidgets.QPushButton(TextForm)
        self.pushButton_copy_text.setObjectName("pushButton_copy_text")
        self.horizontalLayout.addWidget(self.pushButton_copy_text)
        self.pushButton_close = QtWidgets.QPushButton(TextForm)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TextForm)
        QtCore.QMetaObject.connectSlotsByName(TextForm)

    def retranslateUi(self, TextForm):
        _translate = QtCore.QCoreApplication.translate
        TextForm.setWindowTitle(_translate("TextForm", "Văn bản nhận dạng"))
        self.pushButton_save_to_file.setText(_translate("TextForm", "Lưu vào tệp..."))
        self.pushButton_copy_text.setText(_translate("TextForm", "Sao chép vào Clipboard"))
        self.pushButton_close.setText(_translate("TextForm", "Đóng"))
