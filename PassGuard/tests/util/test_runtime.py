import sys

from utils import is_exe
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

