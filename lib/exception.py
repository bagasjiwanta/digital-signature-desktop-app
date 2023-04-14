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


class FileOrKeyModified(Exception):
    def __init__(self):
        super().__init__("File atau key telah dimodifikasi")