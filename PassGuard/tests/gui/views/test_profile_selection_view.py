import pytest
import os
from customtkinter import CTk
from gui.views.profile_selection import ProfileSelectionView

class TestProfileSelectionView:
    @pytest.fixture(scope="class", autouse=True)
    def setup_headless(self):
        # Set environment variable to use headless mode
        os.environ['DISPLAY'] = ':0'
        yield
        # Clean up
        if 'DISPLAY' in os.environ:
            del os.environ['DISPLAY']

    @pytest.fixture(scope="class")
    def root(self):
        root = CTk()
        yield root
        root.destroy()

    def test_initialization(self, root):
        view = ProfileSelectionView(root)
        assert isinstance(view, ProfileSelectionView)
        assert view.master == root

    def test_welcome_message(self, root):
        view = ProfileSelectionView(root)
        assert view.welcome_message is not None
        assert view.welcome_message.cget("text") == "Welcome"
        assert view.welcome_message.cget("font") == ("Segoe UI", 36)
        grid_info = view.welcome_message.grid_info()
        assert grid_info["row"] == 0
        assert grid_info["column"] == 0
        assert grid_info["columnspan"] == 8
        assert grid_info["padx"] == 20
        assert grid_info["pady"] == (30, 0)
