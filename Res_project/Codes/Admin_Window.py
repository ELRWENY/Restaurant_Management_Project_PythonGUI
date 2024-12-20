
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin_Win(object):
    def setupUi(self, Admin_Win):
        Admin_Win.setObjectName("Admin_Win")
        Admin_Win.resize(621, 475)
        self.Admin_Win_2 = QtWidgets.QWidget(Admin_Win)
        self.Admin_Win_2.setObjectName("Admin_Win_2")

        self.Ad_wel_lbl = QtWidgets.QLabel(self.Admin_Win_2)
        self.Ad_wel_lbl.setGeometry(QtCore.QRect(200, 40, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(26)
        self.Ad_wel_lbl.setFont(font)
        self.Ad_wel_lbl.setObjectName("Ad_wel_lbl")

        self.add_dish_btn = QtWidgets.QPushButton(self.Admin_Win_2)
        self.add_dish_btn.setGeometry(QtCore.QRect(30, 130, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.add_dish_btn.setFont(font)
        self.add_dish_btn.setObjectName("add_dish_btn")
        
        self.rmv_dish_btn = QtWidgets.QPushButton(self.Admin_Win_2)
        self.rmv_dish_btn.setGeometry(QtCore.QRect(30, 340, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.rmv_dish_btn.setFont(font)
        self.rmv_dish_btn.setObjectName("rmv_dish_btn")

        self.updte_dish_btn = QtWidgets.QPushButton(self.Admin_Win_2)
        self.updte_dish_btn.setGeometry(QtCore.QRect(30, 270, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.updte_dish_btn.setFont(font)
        self.updte_dish_btn.setObjectName("updte_dish_btn")

        self.print_ordrs_btn = QtWidgets.QPushButton(self.Admin_Win_2)
        self.print_ordrs_btn.setGeometry(QtCore.QRect(30, 200, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.print_ordrs_btn.setFont(font)
        self.print_ordrs_btn.setObjectName("print_ordrs_btn")

        self.ext_btn = QtWidgets.QPushButton(self.Admin_Win_2)
        self.ext_btn.setGeometry(QtCore.QRect(30, 410, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.ext_btn.setFont(font)
        self.ext_btn.setObjectName("ext_btn")
        
        Admin_Win.setCentralWidget(self.Admin_Win_2)

        self.retranslateUi(Admin_Win)
        QtCore.QMetaObject.connectSlotsByName(Admin_Win)

    def retranslateUi(self, Admin_Win):
        _translate = QtCore.QCoreApplication.translate
        Admin_Win.setWindowTitle(_translate("Admin_Win", "Admin"))
        self.Ad_wel_lbl.setText(_translate("Admin_Win", "Welcome , "))
        self.add_dish_btn.setText(_translate("Admin_Win", "Add New Dish"))
        self.rmv_dish_btn.setText(_translate("Admin_Win", "Show Current Orders"))
        self.updte_dish_btn.setText(_translate("Admin_Win", "Update Dish"))
        self.print_ordrs_btn.setText(_translate("Admin_Win", "Remove Dish"))
        self.ext_btn.setText(_translate("Admin_Win", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_Win = QtWidgets.QMainWindow()
    ui = Ui_Admin_Win()
    ui.setupUi(Admin_Win)
    Admin_Win.show()
    sys.exit(app.exec_())
