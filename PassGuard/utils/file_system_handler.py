from enum import Enum
import os
import shutil

class FileSystemError(Enum):
    """
    Enum for file system errors
    """
    NONE = 0,
    FILE_NOT_FOUND = 1,
    PERMISSION_ERROR = 2,
    TIMEOUT_ERROR = 3,
    IS_A_DIRECTORY = 4,
    OS_ERROR = 5,
    FILE_EXISTS = 6,
    ERROR = 7

class FileSystemHandler:
    @staticmethod
    def read_file(file_path: str) -> tuple[str, FileSystemError]:
        """
        Reads a file based on the provided file_path

        Args:
            file_path (str): The file path

        Returns:
            tuple[str, FileSystemError]: The file content and an error

        Raises:
            FileNotFoundError: The file was not found
            PermissionError: The program does not have permission to read the file
            TimeoutError: The file is took too long to read
            IsADirectoryError: The file path leads to a directory
            OSError: An OS error occured
        """
        try:
            with open(file_path, "r") as file:
                return file.read(), FileSystemError.NONE
        except FileNotFoundError:
            return "", FileSystemError.FILE_NOT_FOUND
        except PermissionError:
            return "", FileSystemError.PERMISSION_ERROR
        except TimeoutError:
            return "", FileSystemError.TIMEOUT_ERROR
        except IsADirectoryError:
            return "", FileSystemError.IS_A_DIRECTORY
        except OSError:
            return "", FileSystemError.OS_ERROR
        except:
            return "", FileSystemError.ERROR

    @staticmethod
    def create_file(file_path: str, file_content: str = "") -> FileSystemError:
        """
        Creates a file based on the provided file_path

        Args:
            file_path (str): The file path
            file_content (str): The file content which is an empty string by default

        Returns:
            FileSystemError: An error based on the success of the operation

        Raises:
            FileExistsError: The file already exists
            PermissionError: The program does not have permission to write to the file
            IsADirectoryError: The file path leads to a directory
            FileNotFoundError: The directory of the file is not created
            OSError: An OS error occured
        """
        try:
            with open(file_path, "x") as file:
                file.write(file_content)
        except FileExistsError:
            return FileSystemError.FILE_EXISTS
        except PermissionError:
            return FileSystemError.PERMISSION_ERROR
        except IsADirectoryError:
            return FileSystemError.IS_A_DIRECTORY
        except FileNotFoundError:
            return FileSystemError.FILE_NOT_FOUND
        except OSError:
            return FileSystemError.OS_ERROR
        except:
            return FileSystemError.ERROR
        return FileSystemError.NONE

    @staticmethod
    def delete_file(file_path: str) -> FileSystemError:
        """
        Deletes a file based on the provided file_path

        Args:
            file_path (str): The file path

        Returns:
            FileSystemError: An error based on the success of the operation

        Raises:
            FileNotFoundError: The file was not found
            PermissionError: The program does not have permission to delete the file
            OSError: An OS error occured
        """
        try:
            os.remove(file_path)
        except FileNotFoundError:
            return FileSystemError.FILE_NOT_FOUND
        except PermissionError:
            return FileSystemError.PERMISSION_ERROR
        except IsADirectoryError:
            return FileSystemError.IS_A_DIRECTORY
        except FileExistsError:
            return FileSystemError.FILE_EXISTS
        except OSError:
            return FileSystemError.OS_ERROR
        except:
            return FileSystemError.ERROR
        return FileSystemError.NONE

    @staticmethod
    def update_file(file_path: str, file_content: str) -> FileSystemError:
        """
        Writes the provided file content into the file

        Args:
            file_path (str): The file path
            file_content (str): The file content

        Returns:
            FileSystemError: An error based on the success of the operation

        Raises:
            FileNotFoundError: The file was not found
            PermissionError: The program does not have permission to read the file
            IsADirectoryError: The file path leads to a directory
            OSError: An OS error occured
        """
        try:
            with open(file_path, "w") as f:
                f.write(file_content)
        except FileNotFoundError:
            return FileSystemError.FILE_NOT_FOUND
        except PermissionError:
            return FileSystemError.PERMISSION_ERROR
        except IsADirectoryError:
            return FileSystemError.IS_A_DIRECTORY
        except OSError:
            return FileSystemError.OS_ERROR
        except:
            return FileSystemError.ERROR
        return FileSystemError.NONE

    @staticmethod
    def append_content_to_file(file_path: str, file_content: str) -> FileSystemError:
        """
        Adds the file content into the file

        Args:
            file_path (str): The file path
            file_content (str): The file content

        Returns:
            FileSystemError: An error based on the success of the operation

        Raises:
            FileNotFoundError: The file was not found
            PermissionError: The program does not have permission to read the file
            IsADirectoryError: The file path leads to a directory
            OSError: An OS error occured
        """
        try:
            with open(file_path, "a") as f:
                f.write(file_content)
        except FileNotFoundError:
            return FileSystemError.FILE_NOT_FOUND
        except PermissionError:
            return FileSystemError.PERMISSION_ERROR
        except IsADirectoryError:
            return FileSystemError.IS_A_DIRECTORY
        except OSError:
            return FileSystemError.OS_ERROR
        except:
            return FileSystemError.ERROR
        return FileSystemError.NONE

    @staticmethod
    def create_directory(directory_path: str) -> FileSystemError:
        """
        Creates a directory based on the provided directory_path

        Args:
            directory_path (str): The directory path

        Returns:
            FileSystemError: An error based on the success of the operation

        Raises:
            FileExistsError: The directory already exists
            FileNotFoundError: The directory is not found
            PermissionError: The program does not have permission to delete the directory
            OSError: An OS error occured
        """
        try:
            os.mkdir(directory_path)
        except FileExistsError:
            return FileSystemError.FILE_EXISTS
        except FileNotFoundError:
            return FileSystemError.FILE_NOT_FOUND
        except PermissionError:
            return FileSystemError.PERMISSION_ERROR
        except OSError:
            return FileSystemError.OS_ERROR
        except:
            return FileSystemError.ERROR
        return FileSystemError.NONE

    @staticmethod
    def delete_directory(directory_path: str) -> FileSystemError:
        """
        Deletes a directory based on the provided directory_path

        Args:
            directory_path (str): The directory path

        Returns:
            FileSystemError: An error based on the success of the operation

        Raises:
            FileNotFoundError: The directory was not found
            PermissionError: The program does not have permission to delete the directory
            OSError: An OS error occured
        """
        try:
            shutil.rmtree(directory_path)
        except FileNotFoundError:
            return FileSystemError.FILE_NOT_FOUND
        except PermissionError:
            return FileSystemError.PERMISSION_ERROR
        except OSError:
            return FileSystemError.OS_ERROR
        except:
            return FileSystemError.ERROR
        return FileSystemError.NONE

    @staticmethod
    def list_files_in_directory(directory_path: str) -> tuple[list[str], FileSystemError]:
        """
        Lists all files in the directory

        Args:
            directory_path (str): The directory path

        Returns:
            FileSystemError: An error based on the success of the operation

        Raises:
            FileNotFoundError: The directory was not found
            PermissionError: The program does not have permission to list the directory
            OSError: An OS error occured
        """
        try:
            files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
            return files, FileSystemError.NONE
        except FileNotFoundError:
            return [], FileSystemError.FILE_NOT_FOUND
        except PermissionError:
            return [], FileSystemError.PERMISSION_ERROR
        except OSError:
            return [], FileSystemError.OS_ERROR



