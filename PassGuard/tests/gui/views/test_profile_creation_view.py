import unittest
from unittest.mock import patch, MagicMock
from customtkinter import CTk
from gui.views.profile_creation import ProfileCreationView
from utils.hashing_handler import HashingHandler
from gui import FrameManager, Frames
from PIL import Image

class TestProfileCreationView(unittest.TestCase):
    def setUp(self):
        self.root = CTk()
        self.view = ProfileCreationView(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        """Test if the view initializes with correct components"""
        self.assertIsNotNone(self.view.profile_name_entry)
        self.assertIsNotNone(self.view.root_password_entry)
        self.assertIsNotNone(self.view.confirm_password_entry)

    def test_empty_inputs(self):
        """Test validation of empty inputs"""
        # Test with all empty fields
        self.assertTrue(self.view.check_for_empty_inputs())

        # Test with only profile name
        self.view.profile_name_entry.insert(0, "TestProfile")
        self.assertTrue(self.view.check_for_empty_inputs())

        # Test with profile name and root password
        self.view.root_password_entry.insert(0, "password123")
        self.assertTrue(self.view.check_for_empty_inputs())

        # Test with all fields filled
        self.view.confirm_password_entry.insert(0, "password123")
        self.assertFalse(self.view.check_for_empty_inputs())

    def test_password_mismatch(self):
        """Test password mismatch validation"""
        self.view.profile_name_entry.insert(0, "TestProfile")
        self.view.root_password_entry.insert(0, "password123")
        self.view.confirm_password_entry.insert(0, "different_password")

        with patch('gui.views.profile_creation.Toast') as mock_toast:
            self.view.create_profile()
            mock_toast.assert_called_once_with(self.root, "Passwords don't match", 3000)

