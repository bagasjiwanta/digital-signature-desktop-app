import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from lib.rsa import generate_rsa, PublicKey, PrivateKey
from lib.signing import sign_text_file, verify_text_file
from lib.exception import FileModified, SignatureCorrupted, SignatureNotFound

def cek_flow_rsa():
    try:
        # bikin key
        private_key, public_key = generate_rsa()

        # save key
        private_key.save_to_file('test/private_key.pri')
        public_key.save_to_file('test/public_key.pub')

        # baca key
        private_key = PrivateKey.read_from_file('test/private_key.pri')
        public_key = PublicKey.read_from_file('test/public_key.pub')

        sign_text_file('test/message.txt', 'test/output.txt', public_key)
        is_verified = verify_text_file('test/output.txt', private_key)
        print(is_verified)
        
    except FileModified as e:
        print(e)
    except SignatureNotFound as e:
        print(e)
    except SignatureCorrupted as e:
        print(e)

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("ui/main_menu.ui", self)
        self.b_rsa.clicked.connect(self.RSA)
        # self.DigitalSign.clicked.connect(self.Extended)
        # self.Verif.clicked.connect(self.Playfair)
        
    def RSA(self):
            rsa = RSA()
            widget.addWidget(rsa)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class RSA(QMainWindow):
    def __init__(self):
        super(RSA, self).__init__()
        loadUi("ui/rsa.ui", self)
        self.generateRSA.clicked.connect(self.GenerateRSA)
        self.backButton.clicked.connect(self.Menu)

    def GenerateRSA(self):
        text = self.lineEdit.text()
        private_key, public_key = generate_rsa()
        private_key.save_to_file(text + '\private_key.pri')
        public_key.save_to_file(text + '\public_key.pub')
        self.label_3.setText("Generated Successfully")
    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(900)
widget.show()

app.exec()