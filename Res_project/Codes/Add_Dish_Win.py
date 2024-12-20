from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_Dish_Win(object):
    def setupUi(self, Add_Dish_Win):
        Add_Dish_Win.setObjectName("Add_Dish_Win")
        Add_Dish_Win.resize(507, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Add_Dish_Win.sizePolicy().hasHeightForWidth())
        Add_Dish_Win.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        Add_Dish_Win.setFont(font)
        self.add_dish_win = QtWidgets.QWidget(Add_Dish_Win)
        self.add_dish_win.setObjectName("add_dish_win")

        self.dsh_nm_lbl = QtWidgets.QLabel(self.add_dish_win)
        self.dsh_nm_lbl.setGeometry(QtCore.QRect(50, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.dsh_nm_lbl.setFont(font)
        self.dsh_nm_lbl.setObjectName("dsh_nm_lbl")

        self.dsh_prc_lbl = QtWidgets.QLabel(self.add_dish_win)
        self.dsh_prc_lbl.setGeometry(QtCore.QRect(50, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.dsh_prc_lbl.setFont(font)
        self.dsh_prc_lbl.setObjectName("dsh_prc_lbl")

        self.dsh_nm_in = QtWidgets.QLineEdit(self.add_dish_win)
        self.dsh_nm_in.setGeometry(QtCore.QRect(180, 20, 280, 31))
        self.dsh_nm_in.setObjectName("dsh_nm_in")

        self.dsh_prc_bx = QtWidgets.QSpinBox(self.add_dish_win)
        self.dsh_prc_bx.setGeometry(QtCore.QRect(240, 80, 81, 31))
        self.dsh_prc_bx.setMinimumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dsh_prc_bx.setFont(font)
        self.dsh_prc_bx.setObjectName("dsh_prc_bx")

        self.add_dsh_btn = QtWidgets.QPushButton(self.add_dish_win)
        self.add_dsh_btn.setGeometry(QtCore.QRect(350, 170, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.add_dsh_btn.setFont(font)
        self.add_dsh_btn.setObjectName("add_dsh_btn")
        
        self.cnl_dsh_btn = QtWidgets.QPushButton(self.add_dish_win)
        self.cnl_dsh_btn.setGeometry(QtCore.QRect(40, 170, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.cnl_dsh_btn.setFont(font)
        self.cnl_dsh_btn.setObjectName("cnl_dsh_btn")
        Add_Dish_Win.setCentralWidget(self.add_dish_win)

        self.retranslateUi(Add_Dish_Win)
        QtCore.QMetaObject.connectSlotsByName(Add_Dish_Win)

    def retranslateUi(self, Add_Dish_Win):
        _translate = QtCore.QCoreApplication.translate
        Add_Dish_Win.setWindowTitle(_translate("Add_Dish_Win", "Add dish"))
        self.dsh_nm_lbl.setText(_translate("Add_Dish_Win", "Dish Name : "))
        self.dsh_prc_lbl.setText(_translate("Add_Dish_Win", "Dish Unit Price : "))
        self.dsh_nm_in.setPlaceholderText(_translate("Add_Dish_Win", "Dish Name"))
        self.add_dsh_btn.setText(_translate("Add_Dish_Win", "Add Dish"))
        self.cnl_dsh_btn.setText(_translate("Add_Dish_Win", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Dish_Win = QtWidgets.QMainWindow()
    ui = Ui_Add_Dish_Win()
    ui.setupUi(Add_Dish_Win)
    Add_Dish_Win.show()
    sys.exit(app.exec_())
