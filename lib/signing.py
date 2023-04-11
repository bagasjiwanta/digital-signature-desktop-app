from Crypto.Hash import SHA3_256
from lib.rsa import PublicKey, PrivateKey
from lib.exception import SignatureNotFound, SignatureCorrupted, FileModified


def sign_text_file(input_file_name:str, output_file_name:str, public_key: PublicKey):
    '''menambahkan digital signature ke file text'''
    with open(input_file_name, "r") as f:
        content = f.read()

    hash = int.from_bytes(SHA3_256.new(content.encode()).digest())
    signature = public_key.encrypt(hash)
    output = "<ds>" + str(signature) + "</ds>\n" + content

    with open(output_file_name, "w") as f:
        f.write(output)
    

def verify_text_file(input_file_name: str, private_key: PrivateKey):
    '''memeriksa keasilan file text dengan menguji digital signaturenya'''
    with open(input_file_name, "r") as f:
        content = f.read()
    
    start_tag = content.find("<ds>")
    if start_tag == -1:
        raise SignatureNotFound
    
    end_ds = content.find("</ds>")
    if end_ds == -1:
        raise SignatureCorrupted
    
    start_ds = start_tag + len("<ds>")
    end_tag = end_ds + len("</ds>\n")

    signature = int(content[start_ds:end_ds])
    real_content = content[end_tag:]
    hash = int.from_bytes(SHA3_256.new(real_content.encode()).digest())
    decrypted = private_key.decrypt(signature)
    if decrypted != hash:
        raise FileModified
    return True

    