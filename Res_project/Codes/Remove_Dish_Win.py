from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Remove_Dish(object):
    def setupUi(self, Remove_Dish):
        Remove_Dish.setObjectName("Remove_Dish")
        Remove_Dish.resize(569, 149)
        self.remove_dish = QtWidgets.QWidget(Remove_Dish)
        self.remove_dish.setObjectName("remove_dish")

        self.rmv_dsh_id_lbl = QtWidgets.QLabel(self.remove_dish)
        self.rmv_dsh_id_lbl.setGeometry(QtCore.QRect(10, 60, 240, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.rmv_dsh_id_lbl.setFont(font)
        self.rmv_dsh_id_lbl.setObjectName("rmv_dsh_id_lbl")

        self.rmv_dsh_cmbx = QtWidgets.QComboBox(self.remove_dish)
        self.rmv_dsh_cmbx.setGeometry(QtCore.QRect(250, 60, 120, 41))
        self.rmv_dsh_cmbx.setObjectName("rmv_dsh_cmbx")

        self.rmv_dsh_btn = QtWidgets.QPushButton(self.remove_dish)
        self.rmv_dsh_btn.setGeometry(QtCore.QRect(410, 30, 140, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.rmv_dsh_btn.setFont(font)
        self.rmv_dsh_btn.setObjectName("rmv_dsh_btn")
        
        self.cnl_dsh_rmv_btn = QtWidgets.QPushButton(self.remove_dish)
        self.cnl_dsh_rmv_btn.setGeometry(QtCore.QRect(410, 90, 140, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.cnl_dsh_rmv_btn.setFont(font)
        self.cnl_dsh_rmv_btn.setObjectName("cnl_dsh_rmv_btn")
        Remove_Dish.setCentralWidget(self.remove_dish)

        self.retranslateUi(Remove_Dish)
        QtCore.QMetaObject.connectSlotsByName(Remove_Dish)

    def retranslateUi(self, Remove_Dish):
        _translate = QtCore.QCoreApplication.translate
        Remove_Dish.setWindowTitle(_translate("Remove_Dish", "Remove dish"))
        self.rmv_dsh_id_lbl.setText(_translate("Remove_Dish", "Choose Dish Name : "))
        self.rmv_dsh_btn.setText(_translate("Remove_Dish", "Remove Dish"))
        self.cnl_dsh_rmv_btn.setText(_translate("Remove_Dish", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Remove_Dish = QtWidgets.QMainWindow()
    ui = Ui_Remove_Dish()
    ui.setupUi(Remove_Dish)
    Remove_Dish.show()
    sys.exit(app.exec_())
