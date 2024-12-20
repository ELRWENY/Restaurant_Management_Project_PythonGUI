from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User_Order_Win(object):
    def setupUi(self, User_Order_Win):
        User_Order_Win.setObjectName("User_Order_Win")
        User_Order_Win.resize(586, 600)

        self.user_order_win = QtWidgets.QWidget(User_Order_Win)
        self.user_order_win.setObjectName("user_order_win")

        self.ords_lbl = QtWidgets.QLabel(self.user_order_win)
        self.ords_lbl.setGeometry(QtCore.QRect(190, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.ords_lbl.setFont(font)
        self.ords_lbl.setObjectName("ords_lbl")

        self.ord_nm_lbl = QtWidgets.QLabel(self.user_order_win)
        self.ord_nm_lbl.setGeometry(QtCore.QRect(50, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.ord_nm_lbl.setFont(font)
        self.ord_nm_lbl.setObjectName("ord_nm_lbl")

        self.ord_qnt_lbl = QtWidgets.QLabel(self.user_order_win)
        self.ord_qnt_lbl.setGeometry(QtCore.QRect(370, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.ord_qnt_lbl.setFont(font)
        self.ord_qnt_lbl.setObjectName("ord_qnt_lbl")

        self.dsh_nm_lbl = QtWidgets.QLabel(self.user_order_win)
        self.dsh_nm_lbl.setGeometry(QtCore.QRect(50, 120, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.dsh_nm_lbl.setFont(font)
        self.dsh_nm_lbl.setObjectName("dsh_nm_lbl")

        self.dsh_qnt_lbl = QtWidgets.QLabel(self.user_order_win)
        self.dsh_qnt_lbl.setGeometry(QtCore.QRect(370, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dsh_qnt_lbl.setFont(font)
        self.dsh_qnt_lbl.setObjectName("dsh_qnt_lbl")

        self.tot_pric_lbl = QtWidgets.QLabel(self.user_order_win)
        self.tot_pric_lbl.setGeometry(QtCore.QRect(20, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        self.tot_pric_lbl.setFont(font)
        self.tot_pric_lbl.setObjectName("tot_pric_lbl")

        self.tot_pric = QtWidgets.QLabel(self.user_order_win)
        self.tot_pric.setGeometry(QtCore.QRect(160, 530, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.tot_pric.setFont(font)
        self.tot_pric.setObjectName("tot_pric")
        
        self.conf_ord_btn = QtWidgets.QPushButton(self.user_order_win)
        self.conf_ord_btn.setGeometry(QtCore.QRect(410, 500, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        self.conf_ord_btn.setFont(font)
        self.conf_ord_btn.setObjectName("conf_ord_btn")

        self.bck_btn = QtWidgets.QPushButton(self.user_order_win)
        self.bck_btn.setGeometry(QtCore.QRect(410, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        self.bck_btn.setFont(font)
        self.bck_btn.setObjectName("bck_btn")
        
        User_Order_Win.setCentralWidget(self.user_order_win)

        self.retranslateUi(User_Order_Win)
        QtCore.QMetaObject.connectSlotsByName(User_Order_Win)

    def retranslateUi(self, User_Order_Win):
        _translate = QtCore.QCoreApplication.translate
        User_Order_Win.setWindowTitle(_translate("User_Order_Win", "MainWindow"))
        self.ords_lbl.setText(_translate("User_Order_Win", "Orders"))
        self.ord_nm_lbl.setText(_translate("User_Order_Win", "Name"))
        self.ord_qnt_lbl.setText(_translate("User_Order_Win", "Quantity"))
        self.dsh_nm_lbl.setText(_translate("User_Order_Win", "Dish"))
        self.dsh_qnt_lbl.setText(_translate("User_Order_Win", "1"))
        self.tot_pric_lbl.setText(_translate("User_Order_Win", "Total Price :"))
        self.tot_pric.setText(_translate("User_Order_Win", "0.0"))
        self.conf_ord_btn.setText(_translate("User_Order_Win", "Confirm"))
        self.bck_btn.setText(_translate("User_Order_Win", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User_Order_Win = QtWidgets.QMainWindow()
    ui = Ui_User_Order_Win()
    ui.setupUi(User_Order_Win)
    User_Order_Win.show()
    sys.exit(app.exec_())
