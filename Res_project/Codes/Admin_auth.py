from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_auth(object):
    def setupUi(self, Admin_auth):
        Admin_auth.setObjectName("Admin_auth")
        Admin_auth.resize(509, 298)
        self.Admin_auth_2 = QtWidgets.QWidget(Admin_auth)
        self.Admin_auth_2.setObjectName("Admin_auth_2")

        self.Ad_det_lbl = QtWidgets.QLabel(self.Admin_auth_2)
        self.Ad_det_lbl.setGeometry(QtCore.QRect(80, 10, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(26)
        self.Ad_det_lbl.setFont(font)
        self.Ad_det_lbl.setObjectName("Ad_det_lbl")

        self.Ad_nm_lbl = QtWidgets.QLabel(self.Admin_auth_2)
        self.Ad_nm_lbl.setGeometry(QtCore.QRect(30, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        self.Ad_nm_lbl.setFont(font)
        self.Ad_nm_lbl.setObjectName("Ad_nm_lbl")

        self.Ad_pass_lbl = QtWidgets.QLabel(self.Admin_auth_2)
        self.Ad_pass_lbl.setGeometry(QtCore.QRect(30, 160, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        self.Ad_pass_lbl.setFont(font)
        self.Ad_pass_lbl.setObjectName("Ad_pass_lbl")

        self.Ad_nm_in = QtWidgets.QLineEdit(self.Admin_auth_2)
        self.Ad_nm_in.setGeometry(QtCore.QRect(150, 100, 151, 31))
        self.Ad_nm_in.setObjectName("Ad_nm_in")

        self.Ad_pass_in = QtWidgets.QLineEdit(self.Admin_auth_2)
        self.Ad_pass_in.setGeometry(QtCore.QRect(150, 150, 151, 31))
        self.Ad_pass_in.setObjectName("Ad_pass_in")

        self.submit_ad_data = QtWidgets.QPushButton(self.Admin_auth_2)
        self.submit_ad_data.setGeometry(QtCore.QRect(360, 230, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.submit_ad_data.setFont(font)
        self.submit_ad_data.setObjectName("submit_ad_data")

        self.cancel_ad_input = QtWidgets.QPushButton(self.Admin_auth_2)
        self.cancel_ad_input.setGeometry(QtCore.QRect(20, 230, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        self.cancel_ad_input.setFont(font)
        self.cancel_ad_input.setObjectName("cancel_ad_input")

        Admin_auth.setCentralWidget(self.Admin_auth_2)
        self.retranslateUi(Admin_auth)
        QtCore.QMetaObject.connectSlotsByName(Admin_auth)

    def retranslateUi(self, Admin_auth):
        _translate = QtCore.QCoreApplication.translate
        Admin_auth.setWindowTitle(_translate("Admin_auth", "Admin autharity"))
        self.Ad_det_lbl.setText(_translate("Admin_auth", "Please Enter Your Details "))
        self.Ad_nm_lbl.setText(_translate("Admin_auth", "Name :"))
        self.Ad_pass_lbl.setText(_translate("Admin_auth", "Password :"))
        self.submit_ad_data.setText(_translate("Admin_auth", "Enter"))
        self.cancel_ad_input.setText(_translate("Admin_auth", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_auth = QtWidgets.QMainWindow()
    ui = Ui_Admin_auth()
    ui.setupUi(Admin_auth)
    Admin_auth.show()
    sys.exit(app.exec_())
