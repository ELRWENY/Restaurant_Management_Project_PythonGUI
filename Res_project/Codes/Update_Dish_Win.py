from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Update_Dish(object):
    def setupUi(self, Update_Dish):
        Update_Dish.setObjectName("Update_Dish")
        Update_Dish.resize(500, 300)

        self.update_dish = QtWidgets.QWidget(Update_Dish)
        self.update_dish.setObjectName("update_dish")

        self.updt_dsh_lbl = QtWidgets.QLabel(self.update_dish)
        self.updt_dsh_lbl.setGeometry(QtCore.QRect(25, 60, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.updt_dsh_lbl.setFont(font)
        self.updt_dsh_lbl.setObjectName("updt_dsh_lbl")

        self.updt_dsh_cmbx = QtWidgets.QComboBox(self.update_dish)
        self.updt_dsh_cmbx.setGeometry(QtCore.QRect(205, 65, 150, 40))
        self.updt_dsh_cmbx.setObjectName("updt_dsh_cmbx")

        self.cur_prc_lbl = QtWidgets.QLabel(self.update_dish)
        self.cur_prc_lbl.setGeometry(QtCore.QRect(385, 60, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.cur_prc_lbl.setFont(font)
        self.cur_prc_lbl.setObjectName("cur_prc_lbl")

        self.new_prc_lbl = QtWidgets.QLabel(self.update_dish)
        self.new_prc_lbl.setGeometry(QtCore.QRect(25, 120, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.new_prc_lbl.setFont(font)
        self.new_prc_lbl.setObjectName("new_prc_lbl")

        self.updt_dsh_spbx = QtWidgets.QSpinBox(self.update_dish)
        self.updt_dsh_spbx.setGeometry(QtCore.QRect(205, 128, 100, 30))
        self.updt_dsh_spbx.setMaximum(1000)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updt_dsh_spbx.setFont(font)
        self.updt_dsh_spbx.setObjectName("updt_dsh_in")

        self.updt_dsh_btn = QtWidgets.QPushButton(self.update_dish)
        self.updt_dsh_btn.setGeometry(QtCore.QRect(300, 200, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.updt_dsh_btn.setFont(font)
        self.updt_dsh_btn.setObjectName("updt_dsh_btn")
        
        self.cnl_updt_dsh_btn = QtWidgets.QPushButton(self.update_dish)
        self.cnl_updt_dsh_btn.setGeometry(QtCore.QRect(40, 200, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.cnl_updt_dsh_btn.setFont(font)
        self.cnl_updt_dsh_btn.setObjectName("cnl_updt_dsh_btn")

        Update_Dish.setCentralWidget(self.update_dish)
        self.retranslateUi(Update_Dish)

    def retranslateUi(self, Update_Dish): 
            _translate = QtCore.QCoreApplication.translate
            Update_Dish.setWindowTitle(_translate("Update_Dish", "Update Dish Price"))
            self.updt_dsh_lbl.setText(_translate("Update_Dish", "Select Dish Name : "))
            self.cur_prc_lbl.setText(_translate("Update_Dish", "  L.E"))
            self.new_prc_lbl.setText(_translate("Update_Dish", "Enter New Price : "))
            self.updt_dsh_btn.setText(_translate("Update_Dish", "Update Dish"))
            self.cnl_updt_dsh_btn.setText(_translate("Update_Dish", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Update_Dish = QtWidgets.QMainWindow()
    ui = Ui_Update_Dish()
    ui.setupUi(Update_Dish)
    Update_Dish.show()
    sys.exit(app.exec_())

