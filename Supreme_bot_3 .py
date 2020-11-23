import logging
from threading import Thread
from harvester.server import Harvester
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from all_models import get_info, add_items, add_info, add_drop, add_token, get_token
from captcha import Captcha
from run_bot import Bot


class Example(QListWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Supreme Bot')
        self.setStyleSheet("background-color: black;")
        self.setFixedSize(950, 580)

        self.payment_data_text = QLabel(self)
        self.payment_data_text.setText("Payment data:")
        self.payment_data_text.setFont(QFont('SansSerif', 13))
        self.payment_data_text.setStyleSheet("color: white;")
        self.payment_data_text.move(20, 10)

        self.customer_name_text = QLabel(self)
        self.customer_name_text.setText("Full name:")
        self.customer_name_text.setFont(QFont('SansSerif', 11))
        self.customer_name_text.setStyleSheet("color: white;")
        self.customer_name_text.move(20, 40)

        self.customer_name_info = QLineEdit(self)
        self.customer_name_info.text()
        self.customer_name_info.setStyleSheet("color: white;")
        self.customer_name_info.setFont(QFont('SansSerif', 11))
        self.customer_name_info.move(100, 40)

        self.customer_mail_text = QLabel(self)
        self.customer_mail_text.setText("Email:")
        self.customer_mail_text.setFont(QFont('SansSerif', 11))
        self.customer_mail_text.setStyleSheet("color: white;")
        self.customer_mail_text.move(20, 70)

        self.customer_mail_info = QLineEdit(self)
        self.customer_mail_info.setStyleSheet("color: white;")
        self.customer_mail_info.setFont(QFont('SansSerif', 11))
        self.customer_mail_info.move(100, 70)

        self.customer_tel_text = QLabel(self)
        self.customer_tel_text.setText("Telephone:")
        self.customer_tel_text.setFont(QFont('SansSerif', 11))
        self.customer_tel_text.setStyleSheet("color: white;")
        self.customer_tel_text.move(20, 100)

        self.customer_tel_info = QLineEdit(self)
        self.customer_tel_info.setStyleSheet("color: white;")
        self.customer_tel_info.setFont(QFont('SansSerif', 11))
        self.customer_tel_info.move(100, 100)

        self.customer_address1_text = QLabel(self)
        self.customer_address1_text.setText("Address 1:")
        self.customer_address1_text.setFont(QFont('SansSerif', 11))
        self.customer_address1_text.setStyleSheet("color: white;")
        self.customer_address1_text.move(20, 130)

        self.customer_address1_info = QLineEdit(self)
        self.customer_address1_info.setStyleSheet("color: white;")
        self.customer_address1_info.setFont(QFont('SansSerif', 11))
        self.customer_address1_info.move(100, 130)

        self.customer_address2_text = QLabel(self)
        self.customer_address2_text.setText("Address 2:")
        self.customer_address2_text.setFont(QFont('SansSerif', 11))
        self.customer_address2_text.setStyleSheet("color: white;")
        self.customer_address2_text.move(20, 160)

        self.customer_address2_info = QLineEdit(self)
        self.customer_address2_info.setStyleSheet("color: white;")
        self.customer_address2_info.setFont(QFont('SansSerif', 11))
        self.customer_address2_info.move(100, 160)

        self.customer_city_text = QLabel(self)
        self.customer_city_text.setText("City:")
        self.customer_city_text.setFont(QFont('SansSerif', 11))
        self.customer_city_text.setStyleSheet("color: white;")
        self.customer_city_text.move(20, 190)

        self.customer_city_info = QLineEdit(self)
        self.customer_city_info.setStyleSheet("color: white;")
        self.customer_city_info.setFont(QFont('SansSerif', 11))
        self.customer_city_info.move(100, 190)

        self.customer_postcode_text = QLabel(self)
        self.customer_postcode_text.setText("Postcode:")
        self.customer_postcode_text.setFont(QFont('SansSerif', 11))
        self.customer_postcode_text.setStyleSheet("color: white;")
        self.customer_postcode_text.move(20, 220)

        self.customer_postcode_info = QLineEdit(self)
        self.customer_postcode_info.setStyleSheet("color: white;")
        self.customer_postcode_info.setFont(QFont('SansSerif', 11))
        self.customer_postcode_info.move(100, 220)

        self.customer_country_text = QLabel(self)
        self.customer_country_text.setText("Country:")
        self.customer_country_text.setFont(QFont('SansSerif', 11))
        self.customer_country_text.setStyleSheet("color: white;")
        self.customer_country_text.move(20, 250)

        country = ['UK', 'UK (N. IRELAND)', 'AUSTRIA', 'BELARUS', 'BELGIUM', 'BULGARIA', 'CROATIA', 'CYPRUS',
                   'CZECH REPUBLIC', 'DENMARK', 'ESTONIA', 'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HUNGARY',
                   'ICELAND', 'IRELAND', 'ITALY', 'LATVIA', 'LITHUANIA', 'LUXEMBOURG', 'MALTA', 'MONACO', 'NETHERLANDS',
                   'NORWAY', 'POLAND', 'PORTUGAL', 'ROMANIA', 'RUSSIA', 'SLOVAKIA', 'SLOVENIA', 'SPAIN', 'SWEDEN',
                   'SWITZERLAND', 'TURKEY']

        self.customer_country_info = QComboBox(self)
        self.customer_country_info.addItems(country)
        self.customer_country_info.setStyleSheet("border: 1px solid white; color: white;")
        self.customer_country_info.setFont(QFont('SansSerif', 10))
        self.customer_country_info.move(100, 250)

        self.customer_card_text = QLabel(self)
        self.customer_card_text.setText("Card info:")
        self.customer_card_text.setFont(QFont('SansSerif', 11))
        self.customer_card_text.setStyleSheet("color: white;")
        self.customer_card_text.move(20, 280)

        card_type = ['Visa', 'American Express', 'Mastercard', 'Solo', 'PayPal']
        self.customer_card_info = QComboBox(self)
        self.customer_card_info.addItems(card_type)
        self.customer_card_info.setStyleSheet("border: 1px solid white; color: white;")
        self.customer_card_info.setFont(QFont('SansSerif', 10))
        self.customer_card_info.move(100, 280)

        self.customer_card_number_text = QLabel(self)
        self.customer_card_number_text.setText("Number:")
        self.customer_card_number_text.setFont(QFont('SansSerif', 11))
        self.customer_card_number_text.setStyleSheet("color: white;")
        self.customer_card_number_text.move(20, 310)

        self.customer_card_number_info = QLineEdit(self)
        self.customer_card_number_info.setStyleSheet("color: white;")
        self.customer_card_number_info.setFont(QFont('SansSerif', 11))
        self.customer_card_number_info.move(100, 310)

        self.customer_card_exp_text = QLabel(self)
        self.customer_card_exp_text.setText("Exp date:")
        self.customer_card_exp_text.setFont(QFont('SansSerif', 11))
        self.customer_card_exp_text.setStyleSheet("color: white;")
        self.customer_card_exp_text.move(20, 340)

        month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.customer_card_exp_month_info = QComboBox(self)
        self.customer_card_exp_month_info.addItems(month)
        self.customer_card_exp_month_info.setStyleSheet("border: 1px solid white; color: white;")
        self.customer_card_exp_month_info.setFont(QFont('SansSerif', 10))
        self.customer_card_exp_month_info.resize(40, 19)
        self.customer_card_exp_month_info.move(100, 340)

        year = ['2020', '2021', '2022', '2023', '2024', '2025', '2026',
                '2026', '2027', '2028', '2029', '2030']
        self.customer_card_exp_year_info = QComboBox(self)
        self.customer_card_exp_year_info.addItems(year)
        self.customer_card_exp_year_info.setStyleSheet("border: 1px solid white; color: white;")
        self.customer_card_exp_year_info.setFont(QFont('SansSerif', 10))
        self.customer_card_exp_year_info.resize(65, 19)
        self.customer_card_exp_year_info.move(150, 340)

        self.customer_cvv_text = QLabel(self)
        self.customer_cvv_text.setText("CVV:")
        self.customer_cvv_text.setFont(QFont('SansSerif', 11))
        self.customer_cvv_text.setStyleSheet("color: white;")
        self.customer_cvv_text.move(20, 370)

        self.customer_cvv_info = QLineEdit(self)
        self.customer_cvv_info.setStyleSheet("color: white;")
        self.customer_cvv_info.setFont(QFont('SansSerif', 11))
        self.customer_cvv_info.move(100, 370)

        self.save_payment_info_button = QPushButton('Save info', self)
        self.save_payment_info_button.setStyleSheet("border: 1px solid white; color: white;")
        self.save_payment_info_button.resize(100, 20)
        self.save_payment_info_button.setFont(QFont('SansSerif', 10))
        self.save_payment_info_button.clicked.connect(self.save_payment_func)
        self.save_payment_info_button.move(20, 400)

        self.payment_exception = QTextBrowser(self)
        self.payment_exception.setFont(QFont('SansSerif', 12))
        self.payment_exception.setStyleSheet("border: 1px solid black; color: red;")
        self.payment_exception.resize(250, 60)
        self.payment_exception.move(20, 430)

        self.product_data_text = QLabel(self)
        self.product_data_text.setText("Product data:")
        self.product_data_text.setFont(QFont('SansSerif', 13))
        self.product_data_text.setStyleSheet("color: white;")
        self.product_data_text.move(300, 20)

        self.category_text = QLabel(self)
        self.category_text.setText("Category:")
        self.category_text.setFont(QFont('SansSerif', 11))
        self.category_text.setStyleSheet("color: white;")
        self.category_text.move(350, 60)

        category = ['Skate', 'Accessories', 'Bags', 'Pants', 'Jackets', 'Sweatshirts',
                    'Shirts', 'Tops/Sweaters', 'Hats', 'Shorts', 'Shoes', 'new']
        self.category_info = QComboBox(self)
        self.category_info.addItems(category)
        self.category_info.setStyleSheet("border: 1px solid white; color: white;")
        self.category_info.setFont(QFont('SansSerif', 10))
        self.category_info.move(420, 60)

        self.product_name_text = QLabel(self)
        self.product_name_text.setText("Key words:")
        self.product_name_text.setFont(QFont('SansSerif', 11))
        self.product_name_text.setStyleSheet("color: white;")
        self.product_name_text.move(340, 90)

        self.product_name_info = QLineEdit(self)
        self.product_name_info.setStyleSheet("color: white;")
        self.product_name_info.setFont(QFont('SansSerif', 11))
        self.product_name_info.move(420, 90)

        self.product_color_text = QLabel(self)
        self.product_color_text.setText("Color:")
        self.product_color_text.setFont(QFont('SansSerif', 11))
        self.product_color_text.setStyleSheet("color: white;")
        self.product_color_text.move(374, 120)

        self.product_color_info = QLineEdit(self)
        self.product_color_info.setStyleSheet("color: white;")
        self.product_color_info.setFont(QFont('SansSerif', 11))
        self.product_color_info.move(420, 120)

        self.product_size_text = QLabel(self)
        self.product_size_text.setText("Size:")
        self.product_size_text.setFont(QFont('SansSerif', 11))
        self.product_size_text.setStyleSheet("color: white;")
        self.product_size_text.move(380, 150)

        size = ['Small', 'Medium', 'Large', 'XLarge', '30', '32', '34', '36', "N/A"]
        self.product_size_info = QComboBox(self)
        self.product_size_info.addItems(size)
        self.product_size_info.setStyleSheet("border: 1px solid white; color: white;")
        self.product_size_info.setFont(QFont('SansSerif', 10))
        self.product_size_info.resize(80, 19)
        self.product_size_info.move(420, 150)

        self.add_cart_button = QPushButton('Add to cart', self)
        self.add_cart_button.setStyleSheet("border: 1px solid white; color: white;")
        self.add_cart_button.resize(100, 20)
        self.add_cart_button.setFont(QFont('SansSerif', 10))
        self.add_cart_button.clicked.connect(self.add_cart_func)
        self.add_cart_button.move(340, 180)

        self.delete_item_button = QPushButton('Delete from cart', self)
        self.delete_item_button.setStyleSheet("border: 1px solid white; color: white;")
        self.delete_item_button.resize(120, 20)
        self.delete_item_button.setFont(QFont('SansSerif', 10))
        self.delete_item_button.clicked.connect(self.delete_item_func)
        self.delete_item_button.move(450, 180)

        self.purchase_date_text = QLabel(self)
        self.purchase_date_text.setText("Date:")
        self.purchase_date_text.setFont(QFont('SansSerif', 11))
        self.purchase_date_text.setStyleSheet("color: white;")
        self.purchase_date_text.move(350, 210)

        day = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
               '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
               '30', '31']
        self.purchase_date_day_info = QComboBox(self)
        self.purchase_date_day_info.addItems(day)
        self.purchase_date_day_info.setStyleSheet("border: 1px solid white; color: white;")
        self.purchase_date_day_info.setFont(QFont('SansSerif', 10))
        self.purchase_date_day_info.resize(40, 19)
        self.purchase_date_day_info.move(400, 210)

        self.purchase_date_month_info = QComboBox(self)
        self.purchase_date_month_info.addItems(month)
        self.purchase_date_month_info.setStyleSheet("border: 1px solid white; color: white;")
        self.purchase_date_month_info.setFont(QFont('SansSerif', 10))
        self.purchase_date_month_info.resize(40, 19)
        self.purchase_date_month_info.move(450, 210)

        self.purchase_date_year_info = QComboBox(self)
        self.purchase_date_year_info.addItems(year)
        self.purchase_date_year_info.setStyleSheet("border: 1px solid white; color: white;")
        self.purchase_date_year_info.setFont(QFont('SansSerif', 10))
        self.purchase_date_year_info.resize(65, 19)
        self.purchase_date_year_info.move(500, 210)

        self.timer_text = QLabel(self)
        self.timer_text.setText("Timer in sec:")
        self.timer_text.setFont(QFont('SansSerif', 11))
        self.timer_text.setStyleSheet("color: white;")
        self.timer_text.move(350, 240)

        timer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        self.timer_info = QComboBox(self)
        self.timer_info.addItems(timer)
        self.timer_info.setStyleSheet("border: 1px solid white; color: white;")
        self.timer_info.setFont(QFont('SansSerif', 10))
        self.timer_info.resize(45, 19)
        self.timer_info.move(450, 240)

        self.cart_text = QLabel(self)
        self.cart_text.setText("Cart:")
        self.cart_text.setFont(QFont('SansSerif', 13))
        self.cart_text.setStyleSheet("color: white")
        self.cart_text.move(300, 270)

        self.cart_info = QListWidget(self)
        self.cart_info.setFont(QFont('SansSerif', 11))
        self.cart_info.setStyleSheet("border: 1px solid red; color: white;")
        self.cart_info.resize(280, 210)
        self.cart_info.move(300, 295)

        self.confirm_button = QPushButton('Start bot', self)
        self.confirm_button.setStyleSheet("border: 1px solid white; color: white;")
        self.confirm_button.resize(135, 20)
        self.confirm_button.setFont(QFont('SansSerif', 10))
        self.confirm_button.clicked.connect(self.confirm_purchase_func)
        self.confirm_button.move(450, 520)

        self.cancel_button = QPushButton('Stop bot', self)
        self.cancel_button.setStyleSheet("border: 1px solid white; color: white;")
        self.cancel_button.resize(135, 20)
        self.cancel_button.setFont(QFont('SansSerif', 10))
        self.cancel_button.clicked.connect(self.cancel_purchase_func)
        self.cancel_button.move(300, 520)

        self.console_info = QTextBrowser(self)
        self.console_info.setFont(QFont('SansSerif', 11))
        self.console_info.setStyleSheet("border: 1px solid red; color: white;")
        self.console_info.resize(320, 520)
        self.console_info.move(610, 60)

        self.open_website = QPushButton('Upcoming drop', self)
        self.open_website.setStyleSheet("border: 1px solid white; color: white;")
        self.open_website.resize(100, 20)
        self.open_website.setFont(QFont('SansSerif', 10))
        self.open_website.move(20, 530)
        self.open_website.clicked.connect(self.open_site)

        self.captcha_label = QLabel(self)
        self.captcha_label.setText("Use without captcha")
        self.captcha_label.setFont(QFont('SansSerif', 11))
        self.captcha_label.setStyleSheet("color: white")
        self.captcha_label.move(610, 20)
        self.captcha_label.resize(140, 20)

        self.captcha_checkbox = QCheckBox('Captcha checkbox', self)
        self.captcha_checkbox.move(750, 23)

        self.captcha_button = QPushButton('Configure captcha', self)
        self.captcha_button.setStyleSheet("border: 1px solid white; color: white;")
        self.captcha_button.resize(120, 20)
        self.captcha_button.setFont(QFont('SansSerif', 10))
        self.captcha_button.move(800, 20)
        self.captcha_button.clicked.connect(self.make_captcha_token)

        info = get_info()

        if info:
            info_countries = {'GB': 'UK', 'NB': 'UK (N. IRELAND)', 'AT': 'AUSTRIA', 'BY': 'BELARUS', 'BE': 'BELGIUM',
                              'BG': 'BULGARIA', 'HR': 'CROATIA', 'CY': 'CYPRUS', 'CZ': 'CZECH REPUBLIC',
                              'DK': 'DENMARK', 'EE': 'ESTONIA', 'FI': 'FINLAND', 'FR': 'FRANCE', 'DE': 'GERMANY',
                              'GR': 'GREECE', 'HU': 'HUNGARY', 'IS': 'ICELAND', 'IE': 'IRELAND', 'IT': 'ITALY',
                              'LV': 'LATVIA', 'LT': 'LITHUANIA', 'LU': 'LUXEMBOURG', 'MT': 'MALTA', 'MC': 'MONACO',
                              'NL': 'NETHERLANDS', 'NO': 'NORWAY', 'PL': 'POLAND', 'PT': 'PORTUGAL', 'RO': 'ROMANIA',
                              'RU': 'RUSSIA', 'SK': 'SLOVAKIA', 'SI': 'SLOVENIA', 'ES': 'SPAIN', 'SE': 'SWEDEN',
                              'CH': 'SWITZERLAND', 'TR': 'TURKEY'}
            self.customer_name_info.setText(info["name"])
            self.customer_mail_info.setText(info['email'])
            self.customer_tel_info.setText(info['tel'])
            self.customer_address1_info.setText(info['address_1'])
            self.customer_address2_info.setText(info['address_2'])
            self.customer_country_info.setCurrentText(info_countries[info['country']])
            self.customer_card_info.setCurrentText(info['card_type'])
            self.customer_city_info.setText(info['city'])
            self.customer_postcode_info.setText(info['zip'])
            self.customer_card_exp_month_info.setCurrentText(info['exp_month'])
            self.customer_card_exp_year_info.setCurrentText(info['exp_year'])
            self.customer_card_number_info.setText(info['card_number'])
            self.customer_cvv_info.setText(info['cvv'])
        self.bot = None
        self.captcha = None
        self.captcha_thread = None

    def make_captcha_token(self):
        '''if self.captcha and self.captcha_thread:
            self.captcha_thread.setTerminationEnabled()
            self.captcha_thread.terminate()
            self.captcha_thread.wait()'''
        if not self.captcha_thread:
            self.captcha_thread = QThread()
            self.captcha = Captcha()
        self.captcha.moveToThread(self.captcha_thread)
        self.captcha.signals.result.connect(self.captcha_output)
        self.captcha_thread.started.connect(self.captcha.run)
        self.captcha_thread.start()

    def captcha_output(self, text):
        self.payment_exception.setText(text)

    def add_to_console(self, text):
        self.console_info.append(text)

    def open_site(self):
        QDesktopServices.openUrl(QUrl('https://supremecommunity.ru/Items/DropListLast'))

    def add_cart_func(self):
        product_data = dict()
        product_data['category'] = str(self.category_info.currentText())
        product_data['product_name'] = self.product_name_info.text()
        product_data['product_color'] = self.product_color_info.text()
        product_data['product_size'] = str(self.product_size_info.currentText())
        self.cart_info.insertItem(0, f'{product_data["category"]}--{product_data["product_name"]}--'
                                     f'{product_data["product_color"]}--{product_data["product_size"]}')
        self.product_name_info.setText('')
        self.product_color_info.setText('')

    def cancel_purchase_func(self):
        if self.bot and self.bot.is_running:
            self.bot.is_running = False
            self.thread.setTerminationEnabled()
            self.thread.terminate()
            self.thread.wait()

    def confirm_purchase_func(self):
        if self.bot and self.thread:
            self.thread.setTerminationEnabled()
            self.thread.terminate()
            self.thread.wait()
        self.console_info.setText('')
        if self.captcha_checkbox.isChecked() or not get_token():
            add_token("")
            self.console_info.setText('Starting without captcha token..')
        items = list()
        drop_date = (int(self.purchase_date_year_info.currentText()),
                     int(self.purchase_date_month_info.currentText()),
                     int(self.purchase_date_day_info.currentText()))
        for product in range(self.cart_info.count()):
            category, name, color, size = self.cart_info.item(product).text().split("--")
            items.append({'name': name, 'size': size, 'color': color, 'category': category})
        add_drop({"drop_date": drop_date, "timer": int(self.timer_info.currentText())})
        if items:
            add_items(items)
            if get_info():

                self.thread = QThread()
                self.bot = Bot(drop_date)
                self.bot.moveToThread(self.thread)
                self.bot.signals.result.connect(self.add_to_console)
                self.bot.signals.finished.connect(self.add_to_console)
                self.thread.started.connect(self.bot.run)
                self.thread.start()
            else:
                self.payment_exception.setText('Fill in payment data')
        else:
            self.payment_exception.setText('No items in cart')

    def delete_item_func(self):
        selected_item = self.cart_info.selectedItems()
        if not selected_item:
            return
        for item in selected_item:
            self.cart_info.takeItem(self.cart_info.row(item))

    def save_payment_func(self):
        countries = {'UK': 'GB', 'UK (N. IRELAND)': 'NB', 'AUSTRIA': 'AT', 'BELARUS': 'BY', 'BELGIUM': 'BE',
                     'BULGARIA': 'BG', 'CROATIA': 'HR', 'CYPRUS': 'CY', 'CZECH REPUBLIC': 'CZ', 'DENMARK': 'DK',
                     'ESTONIA': 'EE', 'FINLAND': 'FI', 'FRANCE': 'FR', 'GERMANY': 'DE', 'GREECE': 'GR', 'HUNGARY': 'HU',
                     'ICELAND': 'IS', 'IRELAND': 'IE', 'ITALY': 'IT', 'LATVIA': 'LV', 'LITHUANIA': 'LT',
                     'LUXEMBOURG': 'LU', 'MALTA': 'MT', 'MONACO': 'MC', 'NETHERLANDS': 'NL', 'NORWAY': 'NO',
                     'POLAND': 'PL', 'PORTUGAL': 'PT', 'ROMANIA': 'RO', 'RUSSIA': 'RU', 'SLOVAKIA': 'SK',
                     'SLOVENIA': 'SI', 'SPAIN': 'ES', 'SWEDEN': 'SE', 'SWITZERLAND': 'CH', 'TURKEY': 'TR'}
        info_data = dict()
        info_data['name'] = self.customer_name_info.text()
        info_data['email'] = self.customer_mail_info.text()
        info_data['tel'] = self.customer_tel_info.text()
        info_data['address_1'] = self.customer_address1_info.text()
        info_data['address_2'] = self.customer_address2_info.text()
        info_data['city'] = self.customer_city_info.text()
        info_data['zip'] = self.customer_postcode_info.text()
        info_data['country'] = countries[str(self.customer_country_info.currentText())]
        info_data['card_type'] = str(self.customer_card_info.currentText())
        info_data['card_number'] = self.customer_card_number_info.text()
        info_data['exp_month'] = str(self.customer_card_exp_month_info.currentText())
        info_data['exp_year'] = str(self.customer_card_exp_year_info.currentText())
        info_data['cvv'] = self.customer_cvv_info.text()

        counter = 9

        if all(info_data.values()):
            # Name exception
            if not all(i.isalpha() for i in info_data['name'].split()):
                self.payment_exception.setText('Mistake in name: has numbers in name')
                counter -= 1
            if len(info_data['name'].split()) < 2:
                self.payment_exception.setText('Mistake in name: need first and second name')
                counter -= 1

            # Mail exception
            if '@' not in info_data['email']:
                self.payment_exception.setText('Mistake in mail: no @ mark')
                counter -= 1
            if '.' not in info_data['email']:
                self.payment_exception.setText('Mistake in mail: no . mark')
                counter -= 1

            # Telephone exception
            if info_data['tel'].isalpha():
                self.payment_exception.setText('Mistake in tel: has letters in telephone')
                counter -= 1

            # City exception
            if info_data['city'].isdigit():
                self.payment_exception.setText('Mistake in city: number in city')
                counter -= 1

            # Card number exception
            if info_data['card_number'].isalpha():
                self.payment_exception.setText('Mistake in card number: letter in card number')
                counter -= 1
            if len(info_data['card_number']) != 16:
                self.payment_exception.setText('Mistake in card number: not enough symbols')
                counter -= 1

            # Cvv exception
            if info_data['cvv'].isalpha():
                self.payment_exception.setText('Mistake in card cvv: letter in card number')
                counter -= 1
            if counter == 9:
                add_info(info_data)
                self.payment_exception.setText('Data saved')

        else:
            self.payment_exception.setText('Not all data inserted')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec_())
