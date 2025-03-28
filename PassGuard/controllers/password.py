import bcrypt

class Password:
    @staticmethod
    def hash(password: str):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    @staticmethod
    def compare(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
