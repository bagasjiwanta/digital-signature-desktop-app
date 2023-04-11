from PyQt5.QtWidgets import QApplication, QWidget
from lib.rsa import generate_rsa, PublicKey, PrivateKey
import sys

def cek_flow_rsa():
    try:
        # bikin key
        private_key, public_key = generate_rsa()

        # save key
        private_key.save_to_file('test/private_key.pri')
        public_key.save_to_file('test/public_key.pub')

        print("generated_public_key:", public_key.key)
        print("generated_private_key:", private_key.key)

        # baca key
        private_key = PrivateKey.read_from_file('test/private_key.pri')
        public_key = PublicKey.read_from_file('test/public_key.pub')

        print("public_key:", public_key.key)
        print("private_key:", private_key.key)

        # encryption
        message = 69420
        print(message)

        encrypted = public_key.encrypt(message)
        decrypted = private_key.decrypt(encrypted)

        print("message:", message)
        print("encrypted:", encrypted)
        print("decrypted:", decrypted)
        
    except Exception as e:
        print(e)

cek_flow_rsa()

app = QApplication(sys.argv)
window = QWidget()
window.show()

app.exec()