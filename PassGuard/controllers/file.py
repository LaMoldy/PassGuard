import os, os.path

class File:
    @staticmethod
    def read(file_path: str) -> tuple[str, bool]:
        try:
            f = open(file_path, "r")
            return f.read(), True
        except Exception as e:
            return str(e), False

    @staticmethod
    def create(file_path: str) -> bool:
        try:
            open(file_path, "x")
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


