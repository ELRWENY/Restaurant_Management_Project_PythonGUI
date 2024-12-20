from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User_Win(object):
    def setupUi(self, User_Win):
        User_Win.setObjectName("User_Win")
        User_Win.resize(497, 353)
        self.user_win = QtWidgets.QWidget(User_Win)
        self.user_win.setObjectName("user_win")

        self.user_wel_lbl = QtWidgets.QLabel(self.user_win)
        self.user_wel_lbl.setGeometry(QtCore.QRect(30, 20, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(26)
        self.user_wel_lbl.setFont(font)
        self.user_wel_lbl.setObjectName("user_wel_lbl")

        self.usr_nm_lbl = QtWidgets.QLabel(self.user_win)
        self.usr_nm_lbl.setGeometry(QtCore.QRect(20, 140, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.usr_nm_lbl.setFont(font)
        self.usr_nm_lbl.setObjectName("usr_nm_lbl")

        self.usr_pho_lbl = QtWidgets.QLabel(self.user_win)
        self.usr_pho_lbl.setGeometry(QtCore.QRect(20, 190, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.usr_pho_lbl.setFont(font)
        self.usr_pho_lbl.setObjectName("usr_pho_lbl")

        self.usr_nm_in = QtWidgets.QLineEdit(self.user_win)
        self.usr_nm_in.setGeometry(QtCore.QRect(230, 140, 221, 31))
        self.usr_nm_in.setObjectName("usr_nm_in")

        self.usr_pho_in = QtWidgets.QLineEdit(self.user_win)
        self.usr_pho_in.setGeometry(QtCore.QRect(230, 190, 221, 31))
        self.usr_pho_in.setObjectName("usr_pho_in")

        self.cont_btn = QtWidgets.QPushButton(self.user_win)
        self.cont_btn.setGeometry(QtCore.QRect(315, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.cont_btn.setFont(font)
        self.cont_btn.setObjectName("cont_btn")

        self.bck_btn = QtWidgets.QPushButton(self.user_win)
        self.bck_btn.setGeometry(QtCore.QRect(55, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.bck_btn.setFont(font)
        self.bck_btn.setObjectName("bck_btn")
        
        User_Win.setCentralWidget(self.user_win)

        self.retranslateUi(User_Win)
        QtCore.QMetaObject.connectSlotsByName(User_Win)

    def retranslateUi(self, User_Win):
        _translate = QtCore.QCoreApplication.translate
        User_Win.setWindowTitle(_translate("User_Win", "User data"))
        self.user_wel_lbl.setText(_translate("User_Win", "For Best Service, PLz Enter Your Data"))
        self.usr_nm_lbl.setText(_translate("User_Win", "Name : "))
        self.usr_pho_lbl.setText(_translate("User_Win", "Phone Number : "))
        self.usr_nm_in.setPlaceholderText(_translate("User_Win", "Name"))
        self.usr_pho_in.setPlaceholderText(_translate("User_Win", "eg : +20123456789 (11 number )"))
        self.cont_btn.setText(_translate("User_Win", "Continue"))
        self.bck_btn.setText(_translate("User_Win", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User_Win = QtWidgets.QMainWindow()
    ui = Ui_User_Win()
    ui.setupUi(User_Win)
    User_Win.show()
    sys.exit(app.exec_())
