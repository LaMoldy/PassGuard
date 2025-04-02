import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class EncryptionHandler:
    @staticmethod
    def __setup_kdf() -> PBKDF2HMAC:
        """
        Creates the kdf

        Returns:
            PBKDF2HMAC: The kdf
        """
        return PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=bytes(16),
            iterations=1_000_000
        )

    @staticmethod
    def encrypt(input: str, password: str) -> str:
        """
        Encrypts the input and locks it with the password

        Args:
            input (str): The input to encrypt
            password (str): The password to encrypt with

        Returns:
            str: The encrypted input
        """
        kdf = EncryptionHandler.__setup_kdf()
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        f = Fernet(key)
        return f.encrypt(input.encode()).decode()

    @staticmethod
    def decrypt(input: str, password: str) -> str:
        """
        Decrypts the input with the password

        Args:
            input (str): The input to decrypt
            password (str): The password to decrypt with

        Returns:
            str: The decrypted input
        """
        kdf = EncryptionHandler.__setup_kdf()
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        f = Fernet(key)
        return f.decrypt(input).decode()
