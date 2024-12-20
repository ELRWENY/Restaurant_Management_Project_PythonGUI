from PyQt5 import QtWidgets as qtw, QtCore, QtGui  # type: ignore
from Log_in_win import Ui_Log_in_win
from Admin_auth import Ui_Admin_auth
from Admin_Window import Ui_Admin_Win
from Add_Dish_Win import Ui_Add_Dish_Win
from Remove_Dish_Win import Ui_Remove_Dish
from User_Win import Ui_User_Win
from Add_Dish_Sub_Win import Ui_Adding_Dish
from Update_Dish_Win import Ui_Update_Dish
import mysql.connector # type: ignore
import random

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="139271",
    database="restaurant" 
)
c = connection.cursor()

class MainApp:

    def __init__(self):
        self.app = qtw.QApplication([])

        self.log_in_window = qtw.QMainWindow()
        self.admin_auth_window = qtw.QMainWindow()
        self.admin_window = qtw.QMainWindow()
        self.add_dish_window = qtw.QMainWindow()
        self.remove_dish_window = qtw.QMainWindow()
        self.orders_window = qtw.QMainWindow()
        self.menu_window = qtw.QMainWindow()
        self.user_order_window = qtw.QMainWindow()
        self.user_window = qtw.QMainWindow()
        self.add_dish_sub_window = qtw.QMainWindow()
        self.update_dish_window = qtw.QMainWindow()

        self.log_in_ui = Ui_Log_in_win()
        self.log_in_ui.setupUi(self.log_in_window)

        self.admin_auth_ui = Ui_Admin_auth()
        self.admin_auth_ui.setupUi(self.admin_auth_window)

        self.admin_ui = Ui_Admin_Win()
        self.admin_ui.setupUi(self.admin_window)

        self.add_dish_ui = Ui_Add_Dish_Win()
        self.add_dish_ui.setupUi(self.add_dish_window)

        self.remove_dish_ui = Ui_Remove_Dish()
        self.remove_dish_ui.setupUi(self.remove_dish_window)

        self.setup_orders_Ui(self.orders_window)

        self.setup_menu_Ui(self.menu_window)

        self.setup_user_order_Ui(self.user_order_window)

        self.user_ui = Ui_User_Win()
        self.user_ui.setupUi(self.user_window)

        self.add_dish_sub_ui = Ui_Adding_Dish()
        self.add_dish_sub_ui.setupUi(self.add_dish_sub_window)

        self.update_dish_ui = Ui_Update_Dish()
        self.update_dish_ui.setupUi(self.update_dish_window)

        self.connections()

    def connections(self):
        self.log_in_ui.admin_btn.clicked.connect(self.open_admin_auth_window)
        self.log_in_ui.user_btn.clicked.connect(self.open_user_window)

        self.admin_auth_ui.cancel_ad_input.clicked.connect(self.open_log_in_window)
        self.admin_auth_ui.submit_ad_data.clicked.connect(lambda : self.open_admin_window(True))

        self.admin_ui.ext_btn.clicked.connect(self.open_log_in_window)
        self.admin_ui.add_dish_btn.clicked.connect(self.open_add_dish_window)
        self.admin_ui.rmv_dish_btn.clicked.connect(self.open_orders_window)
        self.admin_ui.print_ordrs_btn.clicked.connect(self.open_remove_dish_window)
        self.admin_ui.updte_dish_btn.clicked.connect(self.open_update_dish_window)

        self.add_dish_ui.cnl_dsh_btn.clicked.connect(lambda : self.open_admin_window(False))
        self.add_dish_ui.add_dsh_btn.clicked.connect(self.add_dish_to_db)

        self.remove_dish_ui.cnl_dsh_rmv_btn.clicked.connect(lambda : self.open_admin_window(False))
        self.remove_dish_ui.rmv_dsh_btn.clicked.connect(self.rmv_dish_from_db)

        self.update_dish_ui.cnl_updt_dsh_btn.clicked.connect(lambda : self.open_admin_window(False))
        self.update_dish_ui.updt_dsh_btn.clicked.connect(self.updt_dish_in_db)

        self.user_ui.cont_btn.clicked.connect(self.user_data)
        self.user_ui.bck_btn.clicked.connect(self.open_log_in_window)

########################################################open_window_functions

    def open_log_in_window(self):
        self.admin_auth_window.close()
        self.admin_window.close()
        self.menu_window.close()
        self.add_dish_sub_window.close()
        self.user_window.close()
        self.log_in_window.show()

#user_windows

    def open_user_window(self):
        self.log_in_window.close()

        self.user_ui.usr_nm_lbl.setText("Name : ")
        self.user_ui.usr_pho_lbl.setText("Phone Number : ")
        self.user_ui.usr_nm_in.setText('')
        self.user_ui.usr_nm_in.setPlaceholderText("Name")
        self.user_ui.usr_pho_in.setText('')
        self.user_ui.usr_pho_in.setPlaceholderText("eg : +20123456789 (11 number )")

        self.user_window.show()

    def open_menu_window(self):

        self.user_window.close()

        for obj in self.menu_win.children():
            obj.deleteLater()

        c.execute('select dish_name, price from Dish')
        dish_num = c.fetchall()

        self.menu_window.resize(800, 220 + len(dish_num) * 50)

        menu_lbl = qtw.QLabel(self.menu_win)
        menu_lbl.setGeometry(QtCore.QRect(20, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        menu_lbl.setFont(font)
        menu_lbl.setText("MENU")
        
        space_btw = 90
        self.order_dict = {}
        for dish_name, price in dish_num:

            dish_name = dish_name[0].upper() + dish_name[1:]

            lbl = qtw.QLabel(self.menu_win)
            lbl.setGeometry(QtCore.QRect(30, space_btw, 200, 41))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(16)
            lbl.setFont(font)
            lbl.setText(f"{dish_name} : {price} L.E")

            spn_bx = qtw.QSpinBox(self.menu_win)
            spn_bx.setGeometry(QtCore.QRect(260, space_btw, 51, 31))
            spn_bx.setMinimum(0)
            spn_bx.setMaximum(100)

            add_btn = qtw.QPushButton(self.menu_win)
            add_btn.setGeometry(QtCore.QRect(350, space_btw, 171, 31))
            font.setPointSize(16)
            add_btn.setFont(font)
            add_btn.setText("Add To Order")
            add_btn.clicked.connect(lambda _, dn=dish_name, sb=spn_bx, pr=price: 
                                    self.add_to_order(dn, sb, pr, self.order_dict))


            rmv_btn = qtw.QPushButton(self.menu_win)
            rmv_btn.setGeometry(QtCore.QRect(560, space_btw, 201, 31)) 
            rmv_btn.setFont(font)
            rmv_btn.setText("Remove From Order")
            rmv_btn.clicked.connect(lambda _, dn=dish_name, sb=spn_bx: 
                                    self.remove_from_order(dn, sb, self.order_dict))

            space_btw += 50
        
        shw_ord_btn = qtw.QPushButton(self.menu_win)
        shw_ord_btn.setGeometry(QtCore.QRect(600, space_btw + 60, 151, 51))
        font.setPointSize(16)
        shw_ord_btn.setFont(font)
        shw_ord_btn.setText("Show Order")
        shw_ord_btn.clicked.connect(lambda : self.open_user_order_window(self.order_dict, False, ''))
        
        cnl_ord_btn = qtw.QPushButton(self.menu_win)
        cnl_ord_btn.setGeometry(QtCore.QRect(70, space_btw + 60, 151, 51))
        cnl_ord_btn.setFont(font)
        cnl_ord_btn.setText("Cancel Order")
        cnl_ord_btn.clicked.connect(self.open_log_in_window)

        self.menu_window.show()

    def add_to_order(self, dish_name, spn_box, price, order_dict):
        quantity = spn_box.value()
        if quantity:
            order_dict[dish_name] = (quantity, price)

    def remove_from_order(self, dish_name, spn_box, order_dict):
        spn_box.setValue(0)
        if dish_name in order_dict:
            del order_dict[dish_name]

    def open_user_order_window(self, order_dict : dict, from_admin : bool, phone_num):

        if self.user_order_window.layout() is not None:
            for child in self.user_order_window.children():
                if isinstance(child, qtw.QWidget):
                    child.deleteLater()

        self.user_order_window.resize(590, 265 + len(order_dict) * 50)

        ords_lbl = qtw.QLabel(self.user_order_window)
        ords_lbl.setGeometry(QtCore.QRect(259, 10, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        ords_lbl.setFont(font)
        ords_lbl.setText("Order")

        ord_nm_lbl = qtw.QLabel(self.user_order_window)
        ord_nm_lbl.setGeometry(QtCore.QRect(80, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        ord_nm_lbl.setFont(font)
        ord_nm_lbl.setText("Name")

        ord_qnt_lbl = qtw.QLabel(self.user_order_window)
        ord_qnt_lbl.setGeometry(QtCore.QRect(400, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        ord_nm_lbl.setFont(font)
        ord_qnt_lbl.setText("Quantity")

        space_btw = 120
        total_price = 0
        for dish_name, (quantity, price) in order_dict.items():

            dsh_nm_lbl = qtw.QLabel(self.user_order_window)
            dsh_nm_lbl.setGeometry(QtCore.QRect(80, space_btw, 220, 41))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(18)
            dsh_nm_lbl.setFont(font)
            dsh_nm_lbl.setText(f"{dish_name}")
            
            dsh_qnt_lbl = qtw.QLabel(self.user_order_window)
            dsh_qnt_lbl.setGeometry(QtCore.QRect(420, space_btw, 71, 41))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(18)
            dsh_qnt_lbl.setFont(font)
            dsh_qnt_lbl.setText(f"{quantity}")

            total_price += price * quantity
            space_btw += 50

        bck_btn = qtw.QPushButton(self.user_order_window)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        bck_btn.setFont(font)
        bck_btn.setText("Back")
        bck_btn.clicked.connect(lambda : self.user_order_window.close())
        
        tot_pric_lbl = qtw.QLabel(self.user_order_window)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        tot_pric_lbl.setFont(font)
        tot_pric_lbl.setText(f"Total Price : {total_price}")

        if not from_admin:
            tot_pric_lbl.setGeometry(QtCore.QRect(20, space_btw + 60, 210, 30))
            bck_btn.setGeometry(QtCore.QRect(410, space_btw + 85, 140, 40))

            conf_ord_btn = qtw.QPushButton(self.user_order_window)
            conf_ord_btn.setGeometry(QtCore.QRect(410, space_btw + 35, 140, 40))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(22)
            conf_ord_btn.setFont(font)
            conf_ord_btn.setText("Confirm")
            conf_ord_btn.clicked.connect(lambda : self.send_order_to_db(total_price, order_dict))


        else:
            tot_pric_lbl.setGeometry(QtCore.QRect(20, space_btw + 30, 210, 30))
            bck_btn.setGeometry(QtCore.QRect(410, space_btw + 60, 140, 40))

            phn_nm_lbl = qtw.QLabel(self.user_order_window)
            phn_nm_lbl.setGeometry(QtCore.QRect(20, space_btw + 60, 400, 30))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(24)
            phn_nm_lbl.setFont(font)
            phn_nm_lbl.setText(f"Phone Number : {phone_num}")

        self.user_order_window.show()

#admin_windows

    def open_admin_auth_window(self):

        self.log_in_window.close()
        self.admin_auth_ui.Ad_det_lbl.setText("Please Enter Your Details")
        self.admin_auth_ui.Ad_nm_in.setText("")
        self.admin_auth_ui.Ad_pass_in.setText("")
        self.admin_auth_ui.Ad_nm_in.setPlaceholderText("User name")
        self.admin_auth_ui.Ad_pass_in.setPlaceholderText("password")
        self.admin_auth_window.show()

    def open_admin_window(self, come_from : bool):
        if not come_from:
            self.add_dish_window.close()
            self.remove_dish_window.close()
            self.add_dish_sub_window.close()
            self.orders_window.close()
            self.update_dish_window.close()

        if come_from and not self.check_ad_auth_in(): # Please Enter Your Details
            self.admin_auth_ui.Ad_det_lbl.setText("  Wrong inputs, try again ")
            return

        admin_name = self.admin_auth_ui.Ad_nm_in.text()
        self.admin_auth_window.close()

        self.admin_ui.Ad_wel_lbl.setText(f'Welcome {admin_name}')
        self.admin_window.show()

    def open_add_dish_window(self):
        self.admin_window.close()

        self.add_dish_ui.dsh_nm_lbl.setText("Dish Name : ")
        self.add_dish_ui.dsh_prc_lbl.setText("Dish Unit Price : ")
        self.add_dish_ui.dsh_nm_in.setText('')
        self.add_dish_ui.dsh_nm_in.setPlaceholderText('Dish Name')
        self.add_dish_ui.dsh_prc_bx.setValue(0)

        self.add_dish_window.show()

    def open_remove_dish_window(self):
        self.admin_window.close()

        font = QtGui.QFont()
        font.setPointSize(26)
        self.remove_dish_ui.rmv_dsh_id_lbl.setFont(font)
        self.remove_dish_ui.rmv_dsh_id_lbl.setText("Enter Dish Name : ")
        self.remove_dish_ui.rmv_dsh_cmbx.clear()

        c.execute('select dish_name from Dish')
        temp_list = c.fetchall()
        dish_nams_list = [row[0].capitalize() for row in temp_list]  
        self.remove_dish_ui.rmv_dsh_cmbx.addItems(dish_nams_list)

        self.remove_dish_window.show()

    def open_update_dish_window(self):
        self.admin_window.close()

        self.update_dish_ui.new_prc_lbl.setText("Enter New Price : ")
        self.update_dish_ui.updt_dsh_spbx.setValue(0)
        self.update_dish_ui.updt_dsh_cmbx.clear()

        c.execute('select dish_name from Dish')
        temp_list = c.fetchall()
        dish_nams_list = [row[0].capitalize() for row in temp_list]  
        self.update_dish_ui.updt_dsh_cmbx.addItems(dish_nams_list)

        self.updt_cur_prc_lbl()
        self.update_dish_ui.updt_dsh_cmbx.currentIndexChanged.connect(self.updt_cur_prc_lbl)

        self.update_dish_window.show()

    def updt_cur_prc_lbl(self):
        dish_name_price = self.update_dish_ui.updt_dsh_cmbx.currentText()
        c.execute('select price from Dish where dish_name = %s', (dish_name_price,))
        dish_name_price = c.fetchall()
        if dish_name_price:
            self.update_dish_ui.cur_prc_lbl.setText(f'{dish_name_price[0][0]} L.E')

    def open_orders_window(self):
        self.admin_window.close()

        if self.orders_window.layout() is not None:
            for child in self.orders_window.children():
                if isinstance(child, qtw.QWidget):
                    child.deleteLater()

        c.execute('select o.order_id, u.phone_num, u.user_name\
                   from Orders o inner join User u\
                   on o.user_id = u.user_id')
        
        orders = c.fetchall()

        self.orders_window.resize(600, 190 + len(orders) * 50)

        ord_win_lbl = qtw.QLabel(self.orders_win)
        ord_win_lbl.setGeometry(QtCore.QRect(257, 20, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        ord_win_lbl.setFont(font)
        ord_win_lbl.setText('Orders')

        ord_id_lbl = qtw.QLabel(self.orders_win)
        ord_id_lbl.setGeometry(QtCore.QRect(30, 110, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        ord_id_lbl.setFont(font)
        ord_id_lbl.setText("Order ID :-")

        ord_nm_lbl = qtw.QLabel(self.orders_win)
        ord_nm_lbl.setGeometry(QtCore.QRect(200, 110, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        ord_nm_lbl.setFont(font)
        ord_nm_lbl.setText("Order Owner :-")

        ord_dtls_lbl = qtw.QLabel(self.orders_win)
        ord_dtls_lbl.setGeometry(QtCore.QRect(450, 110, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        ord_dtls_lbl.setFont(font)
        ord_dtls_lbl.setText("Details :-")

        space_btw = 150
        for order in orders:

            order_id = order[0]
            phone_num = order[1]
            user_name = order[2]

            c.execute(' select d.dish_name, odr.quantity, d.price\
                        from Order_req odr\
                        inner join Dish d on odr.dish_id = d.dish_id\
                        where odr.order_id = %s', (order_id,))
            
            each_order = c.fetchall()

            order_dict = {}
            for dish_name, quantity, price in each_order:
                order_dict[dish_name] = (quantity, price)

            tmp_id_lbl = qtw.QLabel(self.orders_win)
            tmp_id_lbl.setGeometry(QtCore.QRect(50, space_btw, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(18)
            tmp_id_lbl.setFont(font)
            tmp_id_lbl.setText(f'{order_id}')

            tmp_nm_lbl = qtw.QLabel(self.orders_win)
            tmp_nm_lbl.setGeometry(QtCore.QRect(200, space_btw, 210, 30))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(18)
            tmp_nm_lbl.setFont(font)
            tmp_nm_lbl.setText(f'{user_name}')

            dtls_btn = qtw.QPushButton(self.orders_win)
            dtls_btn.setGeometry(QtCore.QRect(435, space_btw, 100, 30))
            font = QtGui.QFont()
            font.setFamily("Rockwell Condensed")
            font.setPointSize(18)
            dtls_btn.setFont(font)
            dtls_btn.setText(f'Details')
            dtls_btn.clicked.connect(lambda _, ordi = order_dict, phnm = phone_num : self.open_user_order_window(ordi, True, phnm))

            space_btw += 40

        bck_btn = qtw.QPushButton(self.orders_win)
        bck_btn.setGeometry(QtCore.QRect(225, space_btw + 20, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        bck_btn.setFont(font)
        bck_btn.setText('Back')
        bck_btn.clicked.connect(lambda : self.open_admin_window(False))

        self.orders_window.show()

    def open_add_dish_sub_window(self, from_admin : bool):
        self.add_dish_window.close()
        self.remove_dish_window.close()
        self.user_order_window.close()
        self.update_dish_window.close()

        self.add_dish_sub_ui.add_dsh_lbl.setText("processing...")
        self.add_dish_sub_window.show()
        
        self.progress_value = random.randint(1, 80) 
        self.add_dish_sub_ui.add_dsh_progress.setProperty("value", self.progress_value)

        self.timer = QtCore.QTimer(self.add_dish_sub_window)
        self.timer.timeout.connect(lambda : self.update_progress(from_admin))
        self.timer.start(1000)

    def update_progress(self, from_admin):
        if self.progress_value >= 100:
            self.timer.stop()
            self.add_dish_sub_window.close()
            self.open_admin_window(False) if from_admin else self.open_log_in_window()              
        else:
            self.progress_value = random.randint(self.progress_value + 1, 100)
            self.add_dish_sub_ui.add_dsh_progress.setProperty("value", self.progress_value)

##############################################################validate_input_functions

    def check_ad_auth_in(self):
        ad_name = self.admin_auth_ui.Ad_nm_in.text()
        ad_pass = self.admin_auth_ui.Ad_pass_in.text()

        query ='SELECT admin_name, admin_password\
                FROM Admin\
                WHERE admin_name = %s AND admin_password = %s'
        
        val = (ad_name, ad_pass)
        c.execute(query, val)
        return c.fetchall()

    def add_dish_to_db(self):
        dish_name = self.add_dish_ui.dsh_nm_in.text()
        dish_price = self.add_dish_ui.dsh_prc_bx.value()

        if not dish_name:
            self.add_dish_ui.dsh_nm_lbl.setText("*Empty input : ")
            self.add_dish_ui.dsh_nm_in.setPlaceholderText("Empty spot")
            return
            
        if not dish_price:
            self.add_dish_ui.dsh_prc_lbl.setText("*Price is Zero! : ")
            return
        
        query = 'select dish_name from Dish\
                 where dish_name = %s'
        val = (dish_name,)
        c.execute(query, val)
        res = c.fetchall()

        if not res: 
            query = 'insert into Dish(dish_name, price)\
                     values(%s, %s)'
            val = (dish_name, dish_price)

            c.execute(query, val)
            connection.commit()


        self.open_add_dish_sub_window(True)

    def rmv_dish_from_db(self):
        dish_name = self.remove_dish_ui.rmv_dsh_cmbx.currentText()

        c.execute('delete from Dish where dish_name = %s', (dish_name,))
        connection.commit()

        self.open_add_dish_sub_window(True)

    def updt_dish_in_db(self):
        dish_name = self.update_dish_ui.updt_dsh_cmbx.currentText()
        new_price = self.update_dish_ui.updt_dsh_spbx.value()

        if not new_price:
            font = QtGui.QFont()
            font.setPointSize(16)
            self.update_dish_ui.new_prc_lbl.setFont(font)
            self.update_dish_ui.new_prc_lbl.setText("*Price is Zero! : ")
            return
        
        query = 'update Dish\
                 set price = %s\
                 where dish_name = %s'
        val = (new_price, dish_name)

        c.execute(query, val)
        connection.commit()

        self.open_add_dish_sub_window(True)

    def send_order_to_db(self, total_price, order_dict):

        c.execute("select max(user_id) from User")
        user_id = c.fetchone()[0]

        c.execute(
            "insert into Orders (user_id, total_price) values (%s, %s)",
            (user_id, total_price)
        )

        order_id = c.lastrowid

        for dish_name, (quantity, price) in order_dict.items():

            c.execute("select dish_id from Dish where dish_name = %s", (dish_name,))
            dish_id = c.fetchone()[0]

            c.execute(
                "insert into Order_req (order_id, dish_id, quantity) values (%s, %s, %s)",
                (order_id, dish_id, quantity)
            )

        connection.commit()
        self.open_add_dish_sub_window(False)

    def user_data(self):

        self.user_ui.usr_nm_lbl.setText("Name : ")
        self.user_ui.usr_pho_lbl.setText("Phone Number : ")

        user_name = self.user_ui.usr_nm_in.text()
        user_phone = self.user_ui.usr_pho_in.text()

        if not user_name:
            self.user_ui.usr_nm_lbl.setText('*Empty input : ')
            return
        
        if len(user_phone) != 11 or not user_phone.isdigit():
            self.user_ui.usr_pho_lbl.setText('*invalid Number : ')
            self.user_ui.usr_pho_in.setText('')
            self.user_ui.usr_pho_in.setPlaceholderText('The Number should be 11 bigits')
            return
        
        self.user_ui.usr_nm_in.setText("")
        self.user_ui.usr_pho_in.setText("")
        self.user_ui.usr_nm_in.setPlaceholderText("Name")
        self.user_ui.usr_pho_in.setPlaceholderText("eg : +20123456789 (11 number )")
        
        query = 'insert into User(phone_num, user_name)\
                 values(%s, %s)'
        val = (user_phone, user_name)

        c.execute(query, val)
        connection.commit()
        self.open_menu_window()

##############################################################dynamic_windows_declaration     

    def setup_menu_Ui(self, Menu_Win):
        
        Menu_Win.setObjectName("Menu_Win")
        Menu_Win.resize(800, 520)

        self.menu_win = qtw.QWidget(Menu_Win)
        self.menu_win.setObjectName("menu_win")
        Menu_Win.setCentralWidget(self.menu_win)
        self.menu_window = Menu_Win

        Menu_Win.setWindowTitle("Menu")

    def setup_user_order_Ui(self, User_order_Win):

        User_order_Win.setObjectName("User_order_Win")
        User_order_Win.resize(586, 600)

        self.user_order_window = qtw.QWidget(User_order_Win)
        self.user_order_window.setObjectName("user_order_window")
        User_order_Win.setCentralWidget(self.user_order_window)
        self.user_order_window = User_order_Win

        User_order_Win.setWindowTitle("Your order")

    def setup_orders_Ui(self, Orders_Win):

        Orders_Win.setObjectName("Orders_Win")
        Orders_Win.resize(600, 650)

        self.orders_win = qtw.QWidget(Orders_Win)
        self.orders_win.setObjectName("orders_win")
        Orders_Win.setCentralWidget(self.orders_win)
        self.orders_win = Orders_Win

        Orders_Win.setWindowTitle("Orders")

##############################################################Run_project_function

    def run(self):
        self.log_in_window.show()
        self.app.exec_()

#############################################################main
if __name__ == "__main__":
    app = MainApp()
    app.run()