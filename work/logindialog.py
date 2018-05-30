# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from urllib import request
from exceptions import LoginError, FieldsError
import sys


class Ui_dialogLogin(object):

    def setupUi(self, dialogLogin):
        dialogLogin.setObjectName("dialogLogin")
        dialogLogin.resize(498, 250)
        dialogLogin.setMinimumSize(QtCore.QSize(498, 250))
        dialogLogin.setMaximumSize(QtCore.QSize(498, 250))
        self.formLayoutWidget = QtWidgets.QWidget(dialogLogin)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 461, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.lbllurl = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbllurl.setMinimumSize(QtCore.QSize(100, 20))
        self.lbllurl.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbllurl.setFont(font)
        self.lbllurl.setTextFormat(QtCore.Qt.AutoText)
        self.lbllurl.setObjectName("lbllurl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbllurl)
        self.tbloginURL = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbloginURL.sizePolicy().hasHeightForWidth())
        self.tbloginURL.setSizePolicy(sizePolicy)
        self.tbloginURL.setMinimumSize(QtCore.QSize(320, 25))
        self.tbloginURL.setMaximumSize(QtCore.QSize(320, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbloginURL.setFont(font)
        self.tbloginURL.setMouseTracking(True)
        self.tbloginURL.setTabletTracking(True)
        self.tbloginURL.setToolTipDuration(1)
        self.tbloginURL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbloginURL.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.tbloginURL.setText("")
        self.tbloginURL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tbloginURL.setObjectName("tbloginURL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tbloginURL)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tbuser = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbuser.sizePolicy().hasHeightForWidth())
        self.tbuser.setSizePolicy(sizePolicy)
        self.tbuser.setMinimumSize(QtCore.QSize(320, 25))
        self.tbuser.setMaximumSize(QtCore.QSize(320, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbuser.setFont(font)
        self.tbuser.setMouseTracking(True)
        self.tbuser.setTabletTracking(True)
        self.tbuser.setToolTipDuration(1)
        self.tbuser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbuser.setText("")
        self.tbuser.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tbuser.setObjectName("tbuser")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tbuser)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.tbpass = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbpass.sizePolicy().hasHeightForWidth())
        self.tbpass.setSizePolicy(sizePolicy)
        self.tbpass.setMinimumSize(QtCore.QSize(320, 25))
        self.tbpass.setMaximumSize(QtCore.QSize(320, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbpass.setFont(font)
        self.tbpass.setMouseTracking(True)
        self.tbpass.setTabletTracking(True)
        self.tbpass.setToolTipDuration(1)
        self.tbpass.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbpass.setText("")
        self.tbpass.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tbpass.setObjectName("tbpass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tbpass)
        self.label3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label3)
        self.tbredirectURL = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbredirectURL.sizePolicy().hasHeightForWidth())
        self.tbredirectURL.setSizePolicy(sizePolicy)
        self.tbredirectURL.setMinimumSize(QtCore.QSize(320, 25))
        self.tbredirectURL.setMaximumSize(QtCore.QSize(320, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tbredirectURL.setFont(font)
        self.tbredirectURL.setMouseTracking(True)
        self.tbredirectURL.setTabletTracking(True)
        self.tbredirectURL.setToolTipDuration(1)
        self.tbredirectURL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tbredirectURL.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.tbredirectURL.setText("")
        self.tbredirectURL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tbredirectURL.setObjectName("tbredirectURL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tbredirectURL)
        self.lblstate = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblstate.setFont(font)
        self.lblstate.setStyleSheet("color:red;")
        self.lblstate.setText("")
        self.lblstate.setObjectName("lblstate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lblstate)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.retranslateUi(dialogLogin)
        #app.aboutToQuit.connect(lambda: self.closeEvent(self.actionExit))
        QtCore.QMetaObject.connectSlotsByName(dialogLogin)

    def retranslateUi(self, dialogLogin):
        _translate = QtCore.QCoreApplication.translate
        dialogLogin.setWindowTitle(_translate("dialogLogin", "Enter Login Credentials"))
        self.lbllurl.setText(_translate("dialogLogin", "Login URL"))
        self.tbloginURL.setToolTip(_translate("dialogLogin", "Root website URL"))
        self.tbloginURL.setWhatsThis(_translate("dialogLogin", "Login Page URL"))
        self.tbloginURL.setAccessibleName(_translate("dialogLogin", "tbLoginURL"))
        self.tbloginURL.setPlaceholderText(_translate("dialogLogin", "e.g. http://www.example.com/login.php"))
        self.label.setText(_translate("dialogLogin", "Username/Email"))
        self.tbuser.setToolTip(_translate("dialogLogin", "User Credentials"))
        self.tbuser.setWhatsThis(_translate("dialogLogin", "User Credentials"))
        self.tbuser.setAccessibleName(_translate("dialogLogin", "tbuser"))
        self.tbuser.setPlaceholderText(_translate("dialogLogin", "e.g. Admin"))
        self.label_3.setText(_translate("dialogLogin", "Password"))
        self.tbpass.setToolTip(_translate("dialogLogin", "Root website URL"))
        self.tbpass.setWhatsThis(_translate("dialogLogin", "Target website URL"))
        self.tbpass.setAccessibleName(_translate("dialogLogin", "tbBaseURL"))
        self.tbpass.setPlaceholderText(_translate("dialogLogin", "e.g. P@$$W0RD"))
        self.label3.setText(_translate("dialogLogin", "Redirect URL"))
        self.tbredirectURL.setToolTip(_translate("dialogLogin", "Root website URL"))
        self.tbredirectURL.setWhatsThis(_translate("dialogLogin", "Target website URL"))
        self.tbredirectURL.setAccessibleName(_translate("dialogLogin", "tbBaseURL"))
        self.tbredirectURL.setPlaceholderText(_translate("dialogLogin", "e.g. http://www.example.com/main.php"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogLogin = QtWidgets.QDialog()
    ui = Ui_dialogLogin()
    ui.setupUi(dialogLogin)
    dialogLogin.show()
    sys.exit(app.exec_())
