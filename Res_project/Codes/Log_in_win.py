from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Log_in_win(object):
    def setupUi(self, Log_in_win):
        Log_in_win.setObjectName("Log_in_win")
        Log_in_win.resize(828, 359)
        self.log_in_win = QtWidgets.QWidget(Log_in_win)
        self.log_in_win.setObjectName("log_in_win")

        self.Entry_Message = QtWidgets.QLabel(self.log_in_win)
        self.Entry_Message.setGeometry(QtCore.QRect(240, 40, 531, 91))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Entry_Message.setFont(font)
        self.Entry_Message.setMidLineWidth(0)
        self.Entry_Message.setObjectName("Entry_Message")

        self.welcome_lbl = QtWidgets.QLabel(self.log_in_win)
        self.welcome_lbl.setGeometry(QtCore.QRect(360, 150, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(20)
        self.welcome_lbl.setFont(font)
        self.welcome_lbl.setObjectName("welcome_lbl")

        self.admin_btn = QtWidgets.QPushButton(self.log_in_win)
        self.admin_btn.setGeometry(QtCore.QRect(210, 240, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(14)
        self.admin_btn.setFont(font)
        self.admin_btn.setObjectName("admin_btn")

        self.user_btn = QtWidgets.QPushButton(self.log_in_win)
        self.user_btn.setGeometry(QtCore.QRect(490, 240, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(14)
        self.user_btn.setFont(font)
        self.user_btn.setObjectName("user_btn")
        
        Log_in_win.setCentralWidget(self.log_in_win)

        self.retranslateUi(Log_in_win)
        QtCore.QMetaObject.connectSlotsByName(Log_in_win)

    def retranslateUi(self, Log_in_win):
        _translate = QtCore.QCoreApplication.translate
        Log_in_win.setWindowTitle(_translate("Log_in_win", "Log in"))
        self.Entry_Message.setText(_translate("Log_in_win", "Welcome To Our Restaurant"))
        self.welcome_lbl.setText(_translate("Log_in_win", "Log in As : "))
        self.admin_btn.setText(_translate("Log_in_win", "ADMIN"))
        self.user_btn.setText(_translate("Log_in_win", "USER"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Log_in_win = QtWidgets.QMainWindow()
    ui = Ui_Log_in_win()
    ui.setupUi(Log_in_win)
    Log_in_win.show()
    sys.exit(app.exec_())
