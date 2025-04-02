from utils import EncryptionHandler

class TestEncryptionHandler:
    def test_encrypt(self):
        input = "Hello, World"
        password = "secret"
        encrypted = EncryptionHandler.encrypt(input, password)
        assert encrypted != input

    def test_decrypt(self):
        input = "Hello, World"
        password = "secret"
        encrypted = EncryptionHandler.encrypt(input, password)
        decrypted = EncryptionHandler.decrypt(encrypted, password)
        assert decrypted == input
