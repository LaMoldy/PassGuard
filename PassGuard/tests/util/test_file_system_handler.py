import pytest
import os
import shutil

from utils import FileSystemHandler, FileSystemError
from unittest.mock import patch, mock_open

class TestFileSystemHandler:
    file_path = "PassGuard/tests/tests/test.txt"
    directory_path = "PassGuard/tests/tests/"

    @pytest.fixture(scope="class", autouse=True)
    def cleanup_test_folder(self):
        os.mkdir(self.directory_path)
        yield
        if os.path.exists(self.directory_path):
            shutil.rmtree(self.directory_path)

    def test_create_file(self):
        error = FileSystemHandler.create_file(self.file_path, "Test")
        assert error == FileSystemError.NONE

    def test_create_file_file_exists(self):
        error = FileSystemHandler.create_file(self.file_path, "Hello, World")
        assert error == FileSystemError.FILE_EXISTS

    def test_create_file_permission_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = PermissionError("Permission Denied")
            error = FileSystemHandler.create_file("some_file.txt", "Hello, World")
            mock_file.assert_called_once_with("some_file.txt", "x")
        assert error == FileSystemError.PERMISSION_ERROR

    def test_create_file_is_a_directory(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = IsADirectoryError("File path is a directory")
            error = FileSystemHandler.create_file("some_file/", "Hello, World")
            mock_file.assert_called_once_with("some_file/", "x")
        assert error == FileSystemError.IS_A_DIRECTORY

    def test_create_file_os_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = OSError("OS Error")
            error = FileSystemHandler.create_file("some_file.txt", "Hello, World")
            mock_file.assert_called_once_with("some_file.txt", "x")
        assert error == FileSystemError.OS_ERROR

    def test_create_file_file_not_found(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = FileNotFoundError("Directory doesn't exist")
            error = FileSystemHandler.create_file("some_file.txt", "Hello, World")
            mock_file.assert_called_once_with("some_file.txt", "x")
        assert error == FileSystemError.FILE_NOT_FOUND

    def test_read_file(self):
        file_content, error = FileSystemHandler.read_file(self.file_path)
        assert file_content != "" and error == FileSystemError.NONE

    def test_read_file_file_not_found(self):
        file_content, error = FileSystemHandler.read_file("test.txt")
        assert file_content == "" and error == FileSystemError.FILE_NOT_FOUND

    def test_read_file_permission_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = PermissionError("Permission Denied")
            file_content, error = FileSystemHandler.read_file("some_file.txt")
        assert file_content == "" and error == FileSystemError.PERMISSION_ERROR

    def test_read_file_timeout_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = TimeoutError("Operation timed out")
            file_content, error = FileSystemHandler.read_file("some_file.txt")
        assert file_content == "" and error == FileSystemError.TIMEOUT_ERROR

    def test_read_file_is_a_directory(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = IsADirectoryError("File path goes to a directory instead of a file")
            file_content, error = FileSystemHandler.read_file("some_directory/")
        assert file_content == "" and error == FileSystemError.IS_A_DIRECTORY

    def test_read_file_os_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = OSError("OS Error")
            file_content, error = FileSystemHandler.read_file("some_file.txt")
        assert file_content == "" and error == FileSystemError.OS_ERROR

    def test_update_file(self):
        error = FileSystemHandler.update_file(self.file_path, "Hello, World")
        assert error == FileSystemError.NONE

    def test_update_file_file_not_found(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = FileNotFoundError("File not found")
            error = FileSystemHandler.update_file("test.txt", "Hello, World")
        assert error == FileSystemError.FILE_NOT_FOUND

    def test_update_permission_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = PermissionError("Permission Denied")
            error = FileSystemHandler.update_file("test.txt", "Hello, World")
        assert error == FileSystemError.PERMISSION_ERROR

    def test_update_is_a_directory_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = IsADirectoryError("Can't update directory")
            error = FileSystemHandler.update_file("test.txt", "Hello, World")
        assert error == FileSystemError.IS_A_DIRECTORY

    def test_update_file_os_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = OSError("OS Error")
            error = FileSystemHandler.update_file("test.txt", "Hello, World")
        assert error == FileSystemError.OS_ERROR

    def test_append_content_to_file(self):
        error = FileSystemHandler.update_file(self.file_path, "Hello, World")
        assert error == FileSystemError.NONE

    def test_append_content_to_file_file_not_found(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = FileNotFoundError("File not found")
            error = FileSystemHandler.append_content_to_file("test.txt", "Hello, World")
        assert error == FileSystemError.FILE_NOT_FOUND

    def test_append_content_to_file_permission_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = PermissionError("Permission Denied")
            error = FileSystemHandler.append_content_to_file("test.txt", "Hello, World")
        assert error == FileSystemError.PERMISSION_ERROR

    def test_append_content_to_file_is_a_directory_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = IsADirectoryError("Can't update directory")
            error = FileSystemHandler.append_content_to_file("test.txt", "Hello, World")
        assert error == FileSystemError.IS_A_DIRECTORY

    def test_append_content_to_file_os_error(self):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = OSError("OS Error")
            error = FileSystemHandler.append_content_to_file("test.txt", "Hello, World")
        assert error == FileSystemError.OS_ERROR

    def test_delete_file(self):
        error = FileSystemHandler.delete_file(self.file_path)
        assert error == FileSystemError.NONE

    def test_delete_file_file_not_found(self):
        error = FileSystemHandler.delete_file("test.txt")
        assert error == FileSystemError.FILE_NOT_FOUND

    def test_delete_file_permission_error(self):
        with patch("os.remove", side_effect=PermissionError("Permission Denied")):
            error = FileSystemHandler.delete_file("some_file.txt")
            assert error == FileSystemError.PERMISSION_ERROR

    def test_delete_file_is_a_directory(self):
        with patch("os.remove", side_effect=IsADirectoryError("File path goes to a directory instead of a file")):
            error = FileSystemHandler.delete_file("some_file.txt")
            assert error == FileSystemError.IS_A_DIRECTORY

    def test_delete_file_os_error(self):
        with patch("os.remove", side_effect=OSError("OS Error")):
            error = FileSystemHandler.delete_file("some_file.txt")
            assert error == FileSystemError.OS_ERROR

    def test_delete_file_file_exists(self):
        with patch("os.remove", side_effect=FileExistsError("File not in a directory that exists")):
            error = FileSystemHandler.delete_file("some_file.txt")
            assert error == FileSystemError.FILE_EXISTS

    def test_create_directory(self):
        error = FileSystemHandler.create_directory(self.directory_path + "/text/")
        assert error == FileSystemError.NONE

    def test_create_directory_file_exists(self):
        with patch("os.mkdir", side_effect=FileExistsError("Directory already exists")):
            error = FileSystemHandler.create_directory("tests/")
            assert error == FileSystemError.FILE_EXISTS

    def test_create_directory_file_not_found(self):
        with patch("os.mkdir", side_effect=FileNotFoundError("Directory already exists")):
            error = FileSystemHandler.create_directory("tests/")
            assert error == FileSystemError.FILE_NOT_FOUND

    def test_create_directory_permission_error(self):
        with patch("os.mkdir", side_effect=PermissionError("Permission Denied")):
            error = FileSystemHandler.create_directory("tests/")
            assert error == FileSystemError.PERMISSION_ERROR

    def test_create_directory_os_error(self):
        with patch("os.mkdir", side_effect=OSError("OS Error")):
            error = FileSystemHandler.create_directory("tests/")
            assert error == FileSystemError.OS_ERROR

    def test_delete_directory(self):
        error = FileSystemHandler.delete_directory(self.directory_path)
        assert error == FileSystemError.NONE

    def test_delete_directory_file_not_found(self):
        error = FileSystemHandler.delete_directory("unknown_folder/")
        assert error == FileSystemError.FILE_NOT_FOUND

    def test_delete_directory_permission_error(self):
        with patch("shutil.rmtree", side_effect=PermissionError("Permission Denied")):
            error = FileSystemHandler.delete_directory("tests/")
            assert error == FileSystemError.PERMISSION_ERROR

    def test_delete_directory_os_error(self):
        with patch("shutil.rmtree", side_effect=OSError("OS Error")):
            error = FileSystemHandler.delete_directory("tests/")
            assert error == FileSystemError.OS_ERROR

    def test_list_files_in_directory(self):
        FileSystemHandler.create_directory(self.directory_path)
        FileSystemHandler.create_file(self.directory_path + "test.txt")
        files, error = FileSystemHandler.list_files_in_directory(self.directory_path)
        assert files == ["test.txt"] and error == FileSystemError.NONE

    def test_list_files_in_directory_file_not_found(self):
        with patch("os.listdir", side_effect=FileNotFoundError("Directory not found")):
            files, error = FileSystemHandler.list_files_in_directory("tests/")
            assert files == [] and error == FileSystemError.FILE_NOT_FOUND

    def test_list_files_in_directory_permission_error(self):
        with patch("os.listdir", side_effect=PermissionError("Permission Denied")):
            files, error = FileSystemHandler.list_files_in_directory("tests/")
            assert files == [] and error == FileSystemError.PERMISSION_ERROR

    def test_list_files_in_directory_os_error(self):
        with patch("os.listdir", side_effect=OSError("OS Error")):
            files, error = FileSystemHandler.list_files_in_directory("tests/")
            assert files == [] and error == FileSystemError.OS_ERROR
