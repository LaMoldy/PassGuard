import pytest
import os
import shutil

from controllers import ProfileController

from utils import FileSystemError

class TestProfileController:
    directory_path = "PassGuard/tests/profile_controller_tests/"

    @pytest.fixture(scope="class", autouse=True)
    def cleanup_test_folder(self):
        os.mkdir(self.directory_path)
        self.create_test_file("test.profile")
        self.create_test_file("bob_jones.profile")
        yield
        if os.path.exists(self.directory_path):
            shutil.rmtree(self.directory_path)

    def create_test_file(self, file_name: str) -> None:
        with open(self.directory_path + file_name, "w") as file:
            file.write("test\npassword\nimage_path")

    def test_get_profile_names(self):
        names = ProfileController.get_profile_names(self.directory_path)
        assert names == ["bob jones", "test"]

    def test_get_profile_names_error(self):
        names = ProfileController.get_profile_names("test")
        assert names == []

    def test_get_profile_content_by_line_number(self):
        result = ProfileController.get_profile_content_by_line_number(self.directory_path, "test", 0)
        assert result == "test"

    def test_get_profile_content_by_line_number_password(self):
        result = ProfileController.get_profile_content_by_line_number(self.directory_path, "test", 1)
        assert result == "password"

    def test_get_profile_content_by_line_number_image_path(self):
        result = ProfileController.get_profile_content_by_line_number(self.directory_path, "test", 2)
        assert result == "image_path"

    def test_get_profile_content_by_line_number_past_file_length(self):
        result = ProfileController.get_profile_content_by_line_number(self.directory_path, "tests", 3)
        assert result == ""

    def  test_get_profile_content_by_line_number_error(self):
        result = ProfileController.get_profile_content_by_line_number("tests", "test", 0)
        assert result == ""

    def test_create_profile(self):
        result = ProfileController.create_profile(self.directory_path, "test_create", "test\npassword\nimage_path")
        assert result == FileSystemError.NONE

    def test_create_profile_error(self):
        result = ProfileController.create_profile("tests/tests/tests", "test_create", "test\npassword\nimage_path")
        assert result != FileSystemError.NONE

    def test_add_to_profile(self):
        result = ProfileController.add_to_profile(self.directory_path, "test", "\nhello")
        new_line = ProfileController.get_profile_content_by_line_number(self.directory_path, "test", 3)
        assert result == FileSystemError.NONE and new_line == "hello"

    def test_add_to_profile_error(self):
        result = ProfileController.add_to_profile("tests/tests", "test", "\nhello")
        new_line = ProfileController.get_profile_content_by_line_number("tests/tests", "test", 3)
        assert result != FileSystemError.NONE and new_line == ""
