import sys
import os

from utils import is_exe, get_profile_directory, get_asset_directory
from unittest.mock import patch

class TestRuntime:
    def test_is_exe_true(self):
        with patch.object(sys, "frozen", True, create=True), \
             patch.object(sys, "_MEIPASS", True, create=True):
            assert is_exe() is True

    def test_is_exe_false_no_frozen(self):
        with patch.object(sys, "frozen", False, create=True), \
             patch.object(sys, "_MEIPASS", True, create=True):
            assert is_exe() is False

    def test_is_exe_false_no_meipass(self):
        with patch.object(sys, "frozen", True, create=True):
            if hasattr(sys, '_MEIPASS'):
                delattr(sys, '_MEIPASS')
            assert is_exe() is False

    def test_is_exe_false_no_attributes(self):
        with patch.object(sys, "frozen", False, create=True):
            if hasattr(sys, '_MEIPASS'):
                delattr(sys, '_MEIPASS')
            assert is_exe() is False

    def test_get_profile_directory_exe(self):
        with patch.object(sys, "frozen", True, create=True), \
             patch.object(sys, "_MEIPASS", "/path/to/meipass", create=True):
            expected = os.path.join("/path/to/meipass", "profiles")
            assert get_profile_directory() == expected

    def test_get_profile_directory_non_exe(self):
        with patch.object(sys, "frozen", False, create=True):
            assert get_profile_directory() == "profiles/"

    def test_get_asset_directory_exe(self):
        with patch.object(sys, "frozen", True, create=True), \
             patch.object(sys, "_MEIPASS", "/path/to/meipass", create=True):
            expected = os.path.join("/path/to/meipass", "assets")
            assert get_asset_directory() == expected

    def test_get_asset_directory_non_exe(self):
        with patch.object(sys, "frozen", False, create=True):
            assert get_asset_directory() == "assets/"

