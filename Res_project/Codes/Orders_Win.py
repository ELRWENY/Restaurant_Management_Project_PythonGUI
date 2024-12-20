from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Orders_Win(object):
    def setupUi(self, Orders_Win):
        Orders_Win.setObjectName("Orders_Win")
        Orders_Win.resize(600, 650)
        self.orders_win = QtWidgets.QWidget(Orders_Win)
        self.orders_win.setObjectName("orders_win")

        self.ord_win_lbl = QtWidgets.QLabel(self.orders_win)
        self.ord_win_lbl.setGeometry(QtCore.QRect(257, 20, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.ord_win_lbl.setFont(font)
        self.ord_win_lbl.setObjectName("ord_win_lbl")

        self.ord_id_lbl = QtWidgets.QLabel(self.orders_win)
        self.ord_id_lbl.setGeometry(QtCore.QRect(30, 110, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.ord_id_lbl.setFont(font)
        self.ord_id_lbl.setObjectName("ord_id_lbl")

        self.tmp_id_lbl = QtWidgets.QLabel(self.orders_win)
        self.tmp_id_lbl.setGeometry(QtCore.QRect(50, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.tmp_id_lbl.setFont(font)
        self.tmp_id_lbl.setObjectName("ord_id_lbl")

        self.ord_nm_lbl = QtWidgets.QLabel(self.orders_win)
        self.ord_nm_lbl.setGeometry(QtCore.QRect(200, 110, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.ord_nm_lbl.setFont(font)
        self.ord_nm_lbl.setObjectName("ord_nm_lbl")

        self.tmp_nm_lbl = QtWidgets.QLabel(self.orders_win)
        self.tmp_nm_lbl.setGeometry(QtCore.QRect(200, 150, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.tmp_nm_lbl.setFont(font)
        self.tmp_nm_lbl.setObjectName("ord_nm_lbl")
        
        self.ord_dtls_lbl = QtWidgets.QLabel(self.orders_win)
        self.ord_dtls_lbl.setGeometry(QtCore.QRect(450, 110, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.ord_dtls_lbl.setFont(font)
        self.ord_dtls_lbl.setObjectName("ord_dtls_lbl")

        self.dtls_btn = QtWidgets.QPushButton(self.orders_win)
        self.dtls_btn.setGeometry(QtCore.QRect(435, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        self.dtls_btn.setFont(font)
        self.dtls_btn.setObjectName("bck_btn")

        self.bck_btn = QtWidgets.QPushButton(self.orders_win)
        self.bck_btn.setGeometry(QtCore.QRect(225, 550, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        self.bck_btn.setFont(font)
        self.bck_btn.setObjectName("bck_btn")

        Orders_Win.setCentralWidget(self.orders_win)
        self.retranslateUi(Orders_Win)
        QtCore.QMetaObject.connectSlotsByName(Orders_Win)

    def retranslateUi(self, Orders_Win):
        _translate = QtCore.QCoreApplication.translate
        Orders_Win.setWindowTitle(_translate("Orders_Win", "Orders"))
        self.ord_win_lbl.setText(_translate("Orders_Win", "Orders"))
        self.ord_id_lbl.setText(_translate("Orders_Win", "Order ID :-"))
        self.tmp_id_lbl.setText(_translate("Orders_Win", "ID"))
        self.ord_nm_lbl.setText(_translate("Orders_Win", "Order Owner :-"))
        self.tmp_nm_lbl.setText(_translate("Orders_Win", "Owner Name"))
        self.ord_dtls_lbl.setText(_translate("Orders_Win", "Details :-"))
        self.dtls_btn.setText(_translate("Orders_Win", "Details"))
        self.bck_btn.setText(_translate("Orders_Win", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Orders_Win = QtWidgets.QMainWindow()
    ui = Ui_Orders_Win()
    ui.setupUi(Orders_Win)
    Orders_Win.show()
    sys.exit(app.exec_())
