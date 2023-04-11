class CorruptedPublicKeyFile(Exception):
    def __init__(self):
        super().__init__("File key corrupted")
    

class CorruptedPrivateKeyFile(Exception):
    def __init__(self):
        super().__init__("File key corrupted")


class SignatureNotFound(Exception):
    def __init__(self):
        super().__init__("Digital signature tidak ditemukan")


class SignatureCorrupted(Exception):
    def __init__(self):
        super().__init__("Digital signature rusak")


class FileModified(Exception):
    def __init__(self):
        super().__init__("File telah dimodifikasi")