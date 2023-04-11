from PyQt5.QtWidgets import QApplication, QWidget
from lib.rsa import generate_rsa, PublicKey, PrivateKey
from lib.signing import sign_text_file, verify_text_file
from lib.exception import FileModified, SignatureCorrupted, SignatureNotFound
import sys

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

cek_flow_rsa()

app = QApplication(sys.argv)
window = QWidget()
window.show()

app.exec()