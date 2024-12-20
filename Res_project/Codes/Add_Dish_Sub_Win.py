from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Adding_Dish(object):
    def setupUi(self, Adding_Dish):
        Adding_Dish.setObjectName("Adding_Dish")
        Adding_Dish.resize(376, 80)

        self.centralwidget = QtWidgets.QWidget(Adding_Dish)
        self.centralwidget.setObjectName("centralwidget")

        self.add_dsh_lbl = QtWidgets.QLabel(self.centralwidget)
        self.add_dsh_lbl.setGeometry(QtCore.QRect(40, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.add_dsh_lbl.setFont(font)
        self.add_dsh_lbl.setObjectName("add_dsh_lbl")

        self.add_dsh_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.add_dsh_progress.setGeometry(QtCore.QRect(190, 20, 141, 23))
        self.add_dsh_progress.setProperty("value", 0)
        self.add_dsh_progress.setTextVisible(True)
        self.add_dsh_progress.setOrientation(QtCore.Qt.Horizontal)
        self.add_dsh_progress.setInvertedAppearance(False)
        self.add_dsh_progress.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.add_dsh_progress.setObjectName("add_dsh_progress")
        
        # self.conf_add_dsh_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.conf_add_dsh_btn.setGeometry(QtCore.QRect(130, 70, 101, 31))
        # self.conf_add_dsh_btn.setObjectName("conf_add_dsh_btn")
        Adding_Dish.setCentralWidget(self.centralwidget)

        self.retranslateUi(Adding_Dish)
        QtCore.QMetaObject.connectSlotsByName(Adding_Dish)

    def retranslateUi(self, Adding_Dish):
        _translate = QtCore.QCoreApplication.translate
        Adding_Dish.setWindowTitle(_translate("Adding_Dish", "Processing"))
        self.add_dsh_lbl.setText(_translate("Adding_Dish", "processing..."))
        # self.conf_add_dsh_btn.setText(_translate("Adding_Dish", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Adding_Dish = QtWidgets.QMainWindow()
    ui = Ui_Adding_Dish()
    ui.setupUi(Adding_Dish)
    Adding_Dish.show()
    sys.exit(app.exec_())
