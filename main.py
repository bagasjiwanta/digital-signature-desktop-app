import sys
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from lib.rsa import generate_rsa, PublicKey, PrivateKey
from lib.signing import sign_text_file, verify_text_file, sign_binary_file, verify_binary_file
from lib.signing import sign_text_file, verify_text_file
from lib.exception import *
import time

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
        print(public_key)

        sign_text_file('test/message.txt', 'test/outputtext.txt', public_key)
        is_verified = verify_text_file('test/outputtext.txt', private_key)
        print(is_verified)

        sign_binary_file('test/message.mp4', 'test/outputbinary.txt', public_key)
        is_verified = verify_binary_file('test/message.mp4', 'test/outputbinary.txt', private_key)
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
        self.b_sign.clicked.connect(self.Sign)
        self.b_verif.clicked.connect(self.Verify)
        
    def RSA(self):
            rsa = RSA()
            widget.addWidget(rsa)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def Sign(self):
            sign = Sign()
            widget.addWidget(sign)
            widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def Verify(self):
            verify = Verify()
            widget.addWidget(verify)
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

class Sign (QMainWindow):
    fileLoc = ''
    privKey = ''
    def __init__(self):
        super(Sign, self).__init__()
        loadUi("ui/digital_sign.ui", self)
        self.importFileButton.clicked.connect(self.FileImport)
        self.impPrivKeyButton.clicked.connect(self.PrivKeyImport)
        self.generateSign.clicked.connect(self.GenerateSign)
        self.backButton.clicked.connect(self.Menu)

    def FileImport(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.fileLoc = fname[0]
        self.label_3.setText("File Imported Successfully")

    def PrivKeyImport(self):
        try : 
            fname = QFileDialog.getOpenFileName(self, "Choose File", "")
            self.privKey = PrivateKey.read_from_file(fname[0])
            self.label_3.setText("Private Key Imported Successfully")
        except CorruptedPrivateKeyFile as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Verification")
            msg.setText(str(e))
            x = msg.exec_() 

    def GenerateSign (self):
        loc = self.lineEdit.text()
        if self.radioTxt.isChecked():
            sign_text_file(self.fileLoc, loc +'\output.txt', self.privKey)
        else :
            sign_binary_file(self.fileLoc,loc +'\output.txt', self.privKey )
        self.label_3.setText("Generated Successfully")

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Verify (QMainWindow):
    fileLoc = ''
    orgloc = ''
    pubKey = ''
    is_txt = False
    is_File = False
    def __init__(self):
        super(Verify, self).__init__()
        loadUi("ui/verif.ui", self)
        self.importFileButton.clicked.connect(self.FileImport)
        self.imporOriginalButton.clicked.connect(self.OriginalImport)
        self.impPrivKeyButton.clicked.connect(self.PubKeyImport)
        self.verifButton.clicked.connect(self.Verification)
        self.backButton.clicked.connect(self.Menu)
        self.fileTxtButton.clicked.connect(self.IsTxt)
        self.fileLainButton.clicked.connect(self.IsFile)
        self.label_6.hide()
        self.label_5.hide()
        self.label_4.hide()
        self.imporOriginalButton.hide()
        self.importFileButton.hide()
        self.impPrivKeyButton.hide()

    def FileImport(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.fileLoc = fname[0]
        self.label_3.setText("File Imported Successfully")
    
    def OriginalImport(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "")
        self.orgloc = fname[0]
        self.label_3.setText("Original File Imported Successfully")
    
    def PubKeyImport(self):
        try : 
            fname = QFileDialog.getOpenFileName(self, "Choose File", "")
            self.pubKey = PublicKey.read_from_file(fname[0])
            self.label_3.setText("Public Key Imported Successfully")
        except CorruptedPublicKeyFile as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Verification")
            msg.setText(str(e))
            x = msg.exec_() 

    def IsTxt (self):
        self.importFileButton.show()
        self.impPrivKeyButton.show()
        self.label_5.show()
        self.label_4.show()
        self.is_txt = True
    def IsFile (self):
        self.label_6.hide()
        self.label_5.hide()
        self.label_4.hide()
        self.imporOriginalButton.hide()
        self.importFileButton.hide()
        self.impPrivKeyButton.hide()
        self.is_File = True
        self.label_4.setText("Import Sign File :")

    
    def Verification(self):
        try:
            if self.is_txt:
                is_verified = verify_text_file(self.fileLoc, self.pubKey)
            else :
                is_verified = verify_binary_file(self.orgloc ,self.fileLoc, self.pubKey)
            
            if (is_verified):
                self.label_3.setText('Verified')
        except FileModified as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Verification")
            msg.setText(str(e))
            x = msg.exec_() 

        except SignatureNotFound as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Verification")
            msg.setText(str(e))
            x = msg.exec_() 
        except SignatureCorrupted as e:
            print(e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Verification")
            msg.setText(str(e))
            x = msg.exec_() 

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

