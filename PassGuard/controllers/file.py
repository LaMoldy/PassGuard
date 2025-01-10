import os

class File():
    @staticmethod
    def read(file_path: str) -> tuple[str, bool]:
        try:
            f = open(file_path, "r")
            return r.read(), True
        except:
            return "", False

    @staticmethod
    def create(file_name: str) -> bool:
        try:
            f = open(file_path, "x")
            return True
        except:
            return False

    @staticmethod
    def update(file_name: str, updated_content: str) -> bool:
        try:
            f = open(file_name, "a")
            f.write(updated_content)
            return True
        except:
            return False

    @staticmethod
    def delete(file_path: str) -> bool:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
