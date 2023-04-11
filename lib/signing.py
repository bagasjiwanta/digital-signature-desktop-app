from Crypto.Hash import SHA3_256
from Crypto.Signature import pkcs1_15
import rsa

def sign_text_file(input_file_name, public_key_file_name):
    with open(input_file_name, "r") as f:
        content = f.read()

    hash = SHA3_256.new(content.encode()).digest()

    public_key = rsa.read_public_key(public_key_file_name)

