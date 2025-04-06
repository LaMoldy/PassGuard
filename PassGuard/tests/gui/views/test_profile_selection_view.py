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

