from bcrypt import hashpw, gensalt, checkpw

class HashingHandler:
    @staticmethod
    def hash(input: str) -> bytes:
        """
        Hashes the input

        Args:
            input (str): The input to hash

        Returns:
            bytes: The hashed input
        """
        salt = gensalt()
        encoded_input = input.encode("utf-8")
        hashed_input = hashpw(encoded_input, salt)
        return hashed_input

    @staticmethod
    def compare_hash(input: str, hash: bytes) -> bool:
        """
        Compares the hash and the input

        Args:
            input (str): The input to compare
            hash (bytes): The hash to compare

        Returns:
            bool: True if the hash matches the input
        """
        encrypted_input = input.encode("utf-8")
        return checkpw(encrypted_input, hash)
